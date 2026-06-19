"""Custom metric ex_16: czy odpowiedź agenta jest GRZECZNA (sędzia-LLM w ADK).

Poprzednia metryka (`answer_correct_score`) była deterministyczna - sprawdzała
wartość z bazy. Grzeczność to ocena miękka: nie da się jej policzyć regexem,
więc wołamy **sędziego-LLM**. Sędzia to osobny agent ADK (`LlmAgent`) na
mocniejszym modelu - ten sam mechanizm, który oceniamy, służy do oceny.

Jak liczy grzeczność:
1. Dla każdej odpowiedzi agenta odpala agenta-sędziego przez `Runner`.
2. Sędzia zwraca samą liczbę 0.0-1.0 (1.0 = uprzejma/neutralnie rzeczowa,
   niżej = szorstka/lekceważąca, 0.0 = niegrzeczna).
3. Wynik metryki = średnia ocen; próg ustawiamy w `test_config.json`.

Uwaga: ton rzeczowy i neutralny liczymy jako grzeczny - karzemy dopiero
szorstkość/lekceważenie, nie brak grzecznościowych zwrotów.

Podpięcie w test_config.json (`custom_metrics` -> `code_config.name`):
    solutions.ex_16_modele_i_diagnostyka.politeness_metric.answer_polite_score
"""

from __future__ import annotations

import re
from typing import Optional

from google.genai import types as genai_types

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from google.adk.evaluation.eval_case import ConversationScenario, Invocation
from google.adk.evaluation.eval_metrics import EvalMetric
from google.adk.evaluation.evaluator import (
    EvaluationResult,
    EvalStatus,
    PerInvocationResult,
)

from common.model import get_model  # sędzia chodzi na MOCNIEJSZYM modelu

_JUDGE_APP = "ex16_judge"
_JUDGE_USER = "ewaluator"

_JUDGE_INSTRUCTION = (
    "Jesteś sędzią oceniającym GRZECZNOŚĆ (uprzejmość) odpowiedzi agenta dla "
    "klienta sklepu. Zwróć WYŁĄCZNIE jedną liczbę od 0.0 do 1.0 - bez słów, bez "
    "wyjaśnień. 1.0 = uprzejma albo neutralnie rzeczowa; 0.5 = lekko szorstka; "
    "0.0 = niegrzeczna, lekceważąca lub obraźliwa. Sam rzeczowy, neutralny ton "
    "(bez 'proszę'/'dziękuję') to nadal grzeczna odpowiedź - oceń 1.0."
)


def _text(content: Optional[genai_types.Content]) -> str:
    if content and content.parts:
        return "\n".join(p.text for p in content.parts if p.text)
    return ""


def _parse_score(verdict: str) -> float:
    """Wyłuskuje liczbę 0.0-1.0 z odpowiedzi sędziego; przycina do zakresu."""
    match = re.search(r"\d+(?:[.,]\d+)?", verdict)
    if not match:
        return 0.0
    value = float(match.group().replace(",", "."))
    return max(0.0, min(1.0, value))


async def _judge(runner: Runner, session_service: InMemorySessionService, answer: str) -> float:
    """Świeża sesja na odpowiedź; zwraca ocenę grzeczności od sędziego-LLM."""
    session_id = f"s-{abs(hash(answer))}"
    await session_service.create_session(
        app_name=_JUDGE_APP, user_id=_JUDGE_USER, session_id=session_id
    )
    msg = genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text=f"Odpowiedź do oceny:\n{answer}")],
    )
    verdict = ""
    async for ev in runner.run_async(
        user_id=_JUDGE_USER, session_id=session_id, new_message=msg
    ):
        if ev.is_final_response() and ev.content and ev.content.parts:
            verdict = "".join(p.text or "" for p in ev.content.parts)
    return _parse_score(verdict)


async def answer_polite_score(
    eval_metric: EvalMetric,
    actual_invocations: list[Invocation],
    expected_invocations: Optional[list[Invocation]],
    conversation_scenario: Optional[ConversationScenario] = None,
) -> EvaluationResult:
    """Ocenia grzeczność każdej odpowiedzi agenta przy pomocy sędziego-LLM (ADK)."""
    threshold = eval_metric.threshold if eval_metric.threshold is not None else 0.6

    judge = LlmAgent(
        name="sedzia_grzecznosci",
        model=get_model(),
        instruction=_JUDGE_INSTRUCTION,
    )
    session_service = InMemorySessionService()
    runner = Runner(
        app_name=_JUDGE_APP, agent=judge, session_service=session_service
    )

    per_invocation: list[PerInvocationResult] = []
    total = 0.0
    for actual in actual_invocations:
        answer = _text(actual.final_response)
        score = await _judge(runner, session_service, answer) if answer else 0.0
        status = EvalStatus.PASSED if score >= threshold else EvalStatus.FAILED
        per_invocation.append(
            PerInvocationResult(
                actual_invocation=actual,
                score=score,
                eval_status=status,
            )
        )
        total += score

    if not per_invocation:
        return EvaluationResult()

    overall = total / len(per_invocation)
    return EvaluationResult(
        overall_score=overall,
        overall_eval_status=(
            EvalStatus.PASSED if overall >= threshold else EvalStatus.FAILED
        ),
        per_invocation_results=per_invocation,
    )
