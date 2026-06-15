"""Ćwiczenie ex_29: guardrail na BŁĄD narzędzia (on_tool_error_callback). STARTER.

Czwarty guardrail. ex_26 pilnował akcji, ex_27 wejścia, ex_28 wyjścia. Tutaj
pilnujemy BŁĘDU: gdy narzędzie rzuci wyjątek, łapiemy go i oddajemy modelowi
czysty komunikat zamiast pozwolić, by cała tura agenta się wywaliła.

Po co osobne narzędzie `run_query_raw`? Zwykłe run_query łapie błędy SQL w środku
i nigdy nie rzuca - więc nie da się na nim pokazać on_tool_error. `run_query_raw`
celowo NIE łapie wyjątku (np. zła nazwa kolumny -> sqlite3.OperationalError),
żebyś mógł obsłużyć go w callbacku.

Zasada ADK: on_tool_error_callback dostaje (tool, args, tool_context, error) i
jeśli ZWRÓCI dict, ADK użyje go jako odpowiedzi narzędzia (zamiast propagować
wyjątek). Zwrócenie None = błąd leci dalej (tura się wywala).

Uruchom: uv run adk web ex_27_guardrail_blad (albo adk run ex_27_guardrail_blad).
"""

import sqlite3
from typing import Any, Optional

from common.model import get_model
from common.tools.db import _connect, get_schema, run_query

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
    with _connect() as conn:
        result = conn.execute(sql).fetchall()
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
    dalej i tura się wywala.
    """
    # TODO(you): zamień wyjątek `error` w czytelny dict z kluczem "error", żeby
    # model dostał kontrolowany komunikat ("zapytanie się nie powiodło: ...")
    # zamiast crashu. Możesz dołożyć podpowiedź, by sprawdził schemat (get_schema).
    return None


root_agent = LlmAgent(
    name="sql_agent_error_guarded",
    model=get_model(),
    description="Agent SQL z guardrailem na błędy narzędzi (graceful degradation).",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Najpierw sprawdź schemat (get_schema), potem pisz SELECT przez run_query_raw. "
        "Jeśli narzędzie zwróci błąd, sprawdź schemat i popraw zapytanie. "
        "Odpowiadaj po polsku, na podstawie danych z bazy."
    ),
    tools=[get_schema, run_query, run_query_raw],
    on_tool_error_callback=handle_tool_error,
)
