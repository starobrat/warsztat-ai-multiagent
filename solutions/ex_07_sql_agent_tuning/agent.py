"""Rozwiązanie ćwiczenia 8 - poprawiona instrukcja (eval przechodzi na zielono).

Zmieniona jest TYLKO instrukcja. Model (słaby) i narzędzia bez zmian.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.model import get_weak_model  # noqa: E402
from common.tools.db import get_schema, run_query  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


root_agent = LlmAgent(
    name="sql_agent_to_tune",
    model=get_weak_model(),
    description="Agent SQL z poprawioną instrukcją.",
    instruction=(
        "Jesteś analitykiem sklepu z muzyką (baza Chinook, SQLite). "
        "Najpierw wywołaj get_schema, potem napisz SELECT i wykonaj run_query. "
        "Nie zgaduj nazw tabel ani kolumn. Odpowiadaj po polsku, zwięźle, "
        "wyłącznie na podstawie danych z bazy."
    ),
    tools=[get_schema, run_query],
)
