"""Rozwiązanie: agent SQL (sql_agent) - wypełniona instrukcja i narzędzia.

Skopiuj zawartość do ex_05_sql_agent/agent.py, jeśli utkniesz.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.model import get_model  # noqa: E402
from common.tools.db import get_schema, run_query  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane sklepu Chinook na podstawie SQL.",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką. Pracujesz na bazie Chinook (SQLite). "
        "Aby odpowiedzieć na pytanie o dane:\n"
        "1. NAJPIERW wywołaj get_schema, żeby poznać tabele i kolumny.\n"
        "2. Następnie napisz zapytanie SELECT i wykonaj je przez run_query.\n"
        "Nie zgaduj nazw tabel ani kolumn - zawsze opieraj się na schemacie. "
        "Odpowiadaj po polsku, zwięźle, wyłącznie na podstawie danych z bazy. "
        "Jeśli zapytanie zwróci błąd, popraw je i spróbuj ponownie."
    ),
    tools=[get_schema, run_query],
)
