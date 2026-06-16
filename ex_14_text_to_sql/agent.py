"""Ćwiczenie ex_14: text-to-SQL - moduł 7. STARTER.

Do tej pory agent miał gotowe, wąskie narzędzia. Tu dostaje OGÓLNE: gdy nie
ma gotowca, sam pisze SQL. `get_schema` (poznaj strukturę) -> `run_query`
(wykonaj SELECT). To potężne, ale i NIEBEZPIECZNE - dlaczego, jest w README.

Uruchom: uv run adk web ex_14_text_to_sql
"""

import sys
from pathlib import Path

# To ćwiczenie uruchamiamy też przez `adk eval` (moduł 7) - a `adk eval` ładuje
# agenta po ścieżce pliku i NIE dokłada korzenia repo do sys.path. Dokładamy go
# sami, żeby `from common...` działało i pod `adk web`, i pod `adk eval`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.exercise import placeholder  # noqa: E402
from common.model import get_model  # noqa: E402
from common.tools.db import get_schema, run_query  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane Chinook na podstawie SQL.",
    # TODO(you): podmień placeholder na instrukcję dyscyplinującą pisanie SQL.
    instruction=placeholder(
        "podłącz get_schema i run_query; napisz instrukcję: NAJPIERW get_schema, "
        "potem SELECT, bez zgadywania nazw tabel i kolumn",
        readme="README ex_14_text_to_sql",
    ),
    # TODO(you): podłącz get_schema oraz run_query.
    tools=[],
)
