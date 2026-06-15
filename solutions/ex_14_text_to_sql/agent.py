"""ROZWIĄZANIE ćwiczenia ex_14: text-to-SQL - moduł 7.

Agent dostaje OGÓLNE narzędzia: gdy nie ma gotowca, sam pisze SQL. `get_schema`
(poznaj strukturę) -> `run_query` (wykonaj SELECT). Instrukcja dyscyplinuje:
najpierw poznaj schemat, dopiero potem pisz SELECT - bez zgadywania nazw.

Uruchom: uv run adk web solutions/ex_14_text_to_sql
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane Chinook na podstawie SQL.",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Gdy użytkownik pyta o dane, postępuj dyscyplinująco:\n"
        "1. NAJPIERW wywołaj get_schema, aby poznać tabele i kolumny.\n"
        "2. POTEM napisz zapytanie SELECT i wykonaj je przez run_query.\n"
        "Nigdy nie zgaduj nazw tabel ani kolumn - opieraj się wyłącznie na tym, "
        "co zwróciło get_schema. Odpowiadaj po polsku, na podstawie wyników zapytania."
    ),
    tools=[get_schema, run_query],
)
