"""Ćwiczenie ex_28: guardrail na WYJŚCIU (after_tool_callback). ROZWIĄZANIE.

Po tym jak run_query zwróci wiersze, a ZANIM trafią do modelu, maskujemy komórki
wyglądające na e-mail/telefon. Zwrócenie dict = podmiana wyniku narzędzia.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import re
from typing import Any, Optional

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

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
    if tool.name == "run_query" and isinstance(tool_response, dict):
        rows = tool_response.get("rows")
        if isinstance(rows, list):
            tool_response["rows"] = [
                [_mask(cell) for cell in row] if isinstance(row, list) else row
                for row in rows
            ]
            return tool_response
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
