"""Ćwiczenie ex_27: guardrail na WEJŚCIU (before_model_callback). ROZWIĄZANIE.

Sprawdzamy ostatnią wiadomość użytkownika ZANIM dotrze do modelu. Jeśli wykryjemy
próbę wstrzyknięcia instrukcji, zwracamy gotowy LlmResponse z odmową - ADK użyje
go zamiast wołać model (krótkie spięcie), więc nie palimy tokenów ani narzędzi.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import Optional

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse

import google.genai.types as gt

_INJECTION_PATTERNS = (
    "ignore",
    "zignoruj",
    "pomiń instrukcje",
    "system prompt",
    "drop",
    "delete",
    "ujawnij instrukcje",
)


def _last_user_text(llm_request: LlmRequest) -> str:
    """Skleja tekst z ostatniej wiadomości użytkownika w llm_request.contents."""
    for content in reversed(llm_request.contents or []):
        if content.role == "user" and content.parts:
            return " ".join(p.text or "" for p in content.parts)
    return ""


def block_injection_input(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """Callback przed wywołaniem modelu.

    Zwróć LlmResponse = odmowa (model się nie odpala), None = puść do modelu.
    """
    text = _last_user_text(llm_request).lower()
    if any(pattern in text for pattern in _INJECTION_PATTERNS):
        return LlmResponse(
            content=gt.Content(
                role="model",
                parts=[
                    gt.Part(
                        text=(
                            "Odmawiam: wykryto próbę wstrzyknięcia instrukcji lub "
                            "modyfikacji bazy. Zadaj pytanie analityczne o dane sklepu."
                        )
                    )
                ],
            )
        )
    return None


root_agent = LlmAgent(
    name="sql_agent_input_guarded",
    model=get_model(),
    description="Agent SQL z guardrailem na wejściu (blokuje wstrzykiwanie instrukcji).",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Najpierw sprawdź schemat (get_schema), potem pisz SELECT (run_query). "
        "Nie zgaduj nazw tabel. Odpowiadaj po polsku, na podstawie danych z bazy."
    ),
    tools=[get_schema, run_query],
    before_model_callback=block_injection_input,
)
