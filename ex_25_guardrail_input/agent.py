"""Ćwiczenie ex_27: guardrail na WEJŚCIU (before_model_callback). STARTER.

ex_26 pilnował narzędzia. Tutaj pilnujemy WEJŚCIA - sprawdzamy wiadomość
użytkownika ZANIM w ogóle dotrze do modelu. Jeśli wykryjemy próbę wstrzyknięcia
instrukcji ("zignoruj instrukcje", "ujawnij system prompt") albo polecenie
modyfikacji bazy, zwracamy gotową odmowę i model w ogóle się nie odpala.

Zasada ADK: jeśli before_model_callback ZWRÓCI LlmResponse, ADK użyje go zamiast
wołać model (krótkie spięcie). Zwrócenie None = lecimy normalnie do modelu.

Uruchom: uv run adk web ex_25_guardrail_input (albo adk run ex_25_guardrail_input).
"""

from typing import Optional

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse

import google.genai.types as gt

# Wzorce, które traktujemy jako próbę wstrzyknięcia / wyjścia poza zakres agenta.
_INJECTION_PATTERNS = (
    "ignore",
    "zignoruj",
    "pomiń instrukcje",
    "system prompt",
    "drop",
    "delete",
    "ujawnij instrukcje",
)


def block_injection_input(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """Callback przed wywołaniem modelu.

    Zwróć LlmResponse = odmowa (model się nie odpala), None = puść do modelu.
    """
    # TODO(you): wyciągnij tekst OSTATNIEJ wiadomości użytkownika z
    # llm_request.contents (lista gt.Content; każdy ma .role i .parts, a part ma
    # .text). Jeśli zawiera któryś z _INJECTION_PATTERNS (case-insensitive),
    # zwróć LlmResponse z gotową odmową po polsku. W innym wypadku None.
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
