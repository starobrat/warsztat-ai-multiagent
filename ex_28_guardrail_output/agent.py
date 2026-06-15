"""Ćwiczenie ex_28: guardrail na WYJŚCIU (after_tool_callback). STARTER.

ex_26 pilnował wywołania narzędzia, ex_27 pilnował wejścia. Tutaj pilnujemy
WYJŚCIA - po tym jak run_query zwróci wiersze, a ZANIM trafią do modelu i
użytkownika, maskujemy dane wrażliwe (e-maile, telefony klientów).

Zasada ADK: after_tool_callback dostaje (tool, args, tool_context, tool_response)
i jeśli ZWRÓCI dict, ADK użyje go zamiast oryginalnej odpowiedzi narzędzia.
Zwrócenie None = oryginalna odpowiedź leci dalej bez zmian.

Uruchom: uv run adk web ex_28_guardrail_output (albo adk run ex_28_guardrail_output).
"""

import re
from typing import Any, Optional

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

# Prosty wykrywacz e-maila i telefonu w pojedynczej komórce wyniku.
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_PHONE_RE = re.compile(r"[+()\d][\d\s().+-]{6,}\d")


def _mask(value: Any) -> Any:
    """Zwraca zamaskowaną wersję komórki, jeśli wygląda na e-mail/telefon."""
    if not isinstance(value, str):
        return value
    if _EMAIL_RE.fullmatch(value):
        return "***@***"
    if _PHONE_RE.fullmatch(value):
        return "***"
    return value


def redact_sensitive_output(
    tool: BaseTool,
    args: dict[str, Any],
    tool_context: ToolContext,
    tool_response: dict,
) -> Optional[dict]:
    """Callback po wykonaniu narzędzia. Zwróć dict = podmiana wyniku, None = bez zmian."""
    # TODO(you): jeśli to run_query i tool_response ma klucz "rows" (lista list),
    # przepuść każdą komórkę przez _mask i zwróć ZMODYFIKOWANY tool_response.
    # W innym wypadku zwróć None (nic nie maskujemy).
    return None


root_agent = LlmAgent(
    name="sql_agent_output_guarded",
    model=get_model(),
    description="Agent SQL z guardrailem na wyjściu (maskuje dane wrażliwe).",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Najpierw sprawdź schemat (get_schema), potem pisz SELECT (run_query). "
        "Nie zgaduj nazw tabel. Odpowiadaj po polsku, na podstawie danych z bazy. "
        "Jeśli dane są zamaskowane (***), pokaż je tak jak są - nie próbuj ich odtwarzać."
    ),
    tools=[get_schema, run_query],
    after_tool_callback=redact_sensitive_output,
)
