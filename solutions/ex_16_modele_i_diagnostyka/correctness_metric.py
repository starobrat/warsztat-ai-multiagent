"""Custom metric ex_16: czy odpowiedź agenta jest POPRAWNA (oparta na danych).

Wbudowane metryki ADK sprawdzają trajektorię (które narzędzie) i pokrycie tekstu
(ROUGE). Żadna nie mówi wprost: "czy w odpowiedzi padła właściwa liczba/tytuł z
bazy". Tę lukę zamyka ta metryka.

Jak liczy poprawność:
1. Z WZORCOWEGO przypadku (`expected`) bierze, które narzędzie i z jakim argumentem
   POWINNO paść (`intermediate_data.tool_uses`).
2. Wykonuje to narzędzie na realnej bazie -> ground truth (np. 16, 835, lista albumów).
3. Sprawdza, czy odpowiedź agenta zawiera każdą z tych wartości (case-insensitive).

Wynik = ułamek wymaganych wartości obecnych w odpowiedzi. Próg 1.0 = wszystkie muszą paść.

Uwaga dydaktyczna: liczymy ground truth z WZORCOWEGO wywołania, nie z tego, co
faktycznie zrobił agent. Dzięki temu metryka łapie też złą odpowiedź na dobre
narzędzie - jest niezależnym sprawdzianem obok trajektorii.

Custom metric podpinamy w test_config.json (`custom_metrics` -> `code_config.name`):
    solutions.ex_16_modele_i_diagnostyka.correctness_metric.answer_correct_score
"""

from __future__ import annotations

from typing import Optional

from google.genai import types as genai_types

from google.adk.evaluation.eval_case import ConversationScenario, Invocation
from google.adk.evaluation.eval_metrics import EvalMetric
from google.adk.evaluation.evaluator import (
    EvaluationResult,
    EvalStatus,
    PerInvocationResult,
)

# Te same narzędzia, które ma agent - wołamy je, by policzyć wartość wzorcową.
from .agent import albums_by_artist, list_genres, sales_by_artist, sales_by_genre

_TOOLS = {
    fn.__name__: fn
    for fn in (sales_by_artist, albums_by_artist, sales_by_genre, list_genres)
}


def _text(content: Optional[genai_types.Content]) -> str:
    """Skleja tekst z części odpowiedzi (tak samo jak robią to metryki ADK)."""
    if content and content.parts:
        return "\n".join(p.text for p in content.parts if p.text)
    return ""


def _expected_facts(expected: Invocation) -> list[str]:
    """Wartości, które MUSZĄ paść w odpowiedzi - z wykonania wzorcowych narzędzi."""
    facts: list[str] = []
    data = expected.intermediate_data
    if not data:
        return facts
    for call in data.tool_uses:
        tool = _TOOLS.get(call.name)
        if tool is None:
            continue
        result = tool(**(call.args or {}))
        # int -> jedna wartość; lista (np. albumy/gatunki) -> każdy element osobno.
        if isinstance(result, list):
            facts.extend(str(item) for item in result)
        else:
            facts.append(str(result))
    return facts


def answer_correct_score(
    eval_metric: EvalMetric,
    actual_invocations: list[Invocation],
    expected_invocations: Optional[list[Invocation]],
    conversation_scenario: Optional[ConversationScenario] = None,
) -> EvaluationResult:
    """Zwraca ułamek wzorcowych wartości obecnych w odpowiedzi agenta."""
    if expected_invocations is None:
        raise ValueError("answer_correct_score wymaga wzorcowych przypadków (expected).")

    threshold = eval_metric.threshold if eval_metric.threshold is not None else 1.0
    per_invocation: list[PerInvocationResult] = []
    total = 0.0

    for actual, expected in zip(actual_invocations, expected_invocations):
        answer = _text(actual.final_response).lower()
        facts = _expected_facts(expected)
        if facts:
            hits = sum(1 for fact in facts if fact.lower() in answer)
            score = hits / len(facts)
        else:
            score = 1.0  # brak wartości do sprawdzenia - nie ma czego oblać
        status = EvalStatus.PASSED if score >= threshold else EvalStatus.FAILED
        per_invocation.append(
            PerInvocationResult(
                actual_invocation=actual,
                expected_invocation=expected,
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
