"""Ćwiczenie ex_27: guardrail na BŁĄD narzędzia (on_tool_error_callback). ROZWIĄZANIE.

Gdy run_query_raw rzuci wyjątek (np. zła nazwa kolumny), callback łapie go i oddaje
modelowi czysty dict z błędem zamiast pozwolić przerwać całą turę agenta.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import Any, Optional

from common.model import get_model
from common.tools.db import _connect, get_schema

from google.adk.agents import LlmAgent
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext


def run_query_raw(sql: str) -> dict:
    """Wykonuje zapytanie SELECT na bazie Chinook BEZ łapania błędów.

    W odróżnieniu od run_query, ta wersja NIE przechwytuje wyjątków SQL - błędne
    zapytanie (np. zła nazwa kolumny) rzuci wyjątek. Obsłużysz go w guardrailu.

    Args:
        sql: Zapytanie SELECT do wykonania.

    Returns:
        Słownik z kluczami 'columns', 'rows', 'row_count'.
    """
    # DEMO ex_27: wymuszamy błąd na KAŻDYM zapytaniu, żeby on_tool_error_callback
    # zawsze miał co łapać. Zamiast wykonać przekazane `sql`, odpalamy celowo błędne
    # zapytanie -> realny sqlite3.OperationalError (jak literówka w nazwie kolumny).
    with _connect() as conn:
        result = conn.execute("SELECT Naem FROM Artist").fetchall()
    rows = [list(tuple(r)) for r in result]
    columns = list(result[0].keys()) if result else []
    return {"columns": columns, "rows": rows, "row_count": len(result)}


def handle_tool_error(
    tool: BaseTool,
    args: dict[str, Any],
    tool_context: ToolContext,
    error: Exception,
) -> Optional[dict]:
    """Callback wywoływany, gdy narzędzie rzuci wyjątek.

    Zwróć dict = czysta odpowiedź dla modelu (tura żyje dalej), None = błąd leci
    dalej i tura się przerywa.
    """
    return {
        "error": (
            f"Narzędzie {tool.name} nie powiodło się: {error}. "
            "Sprawdź schemat przez get_schema i popraw zapytanie SELECT."
        )
    }


root_agent = LlmAgent(
    name="sql_agent_error_guarded",
    model=get_model(),
    description="Agent SQL z guardrailem na błędy narzędzi (graceful degradation).",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Pisz SELECT i wykonuj je przez run_query_raw. "
        "Jeśli narzędzie zwróci błąd, NIE ponawiaj zapytania w kółko - przekaż "
        "użytkownikowi krótką, czytelną informację, że zapytanie się nie powiodło "
        "(wraz z powodem). Odpowiadaj po polsku."
    ),
    tools=[get_schema, run_query_raw],
    on_tool_error_callback=handle_tool_error,
)
