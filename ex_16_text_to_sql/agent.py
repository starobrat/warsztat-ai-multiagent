"""Ćwiczenie ex_16: text-to-SQL - moduł 7. STARTER.

Do tej pory agent miał gotowe, wąskie narzędzia. Tu dostaje OGÓLNE: gdy nie
ma gotowca, sam pisze SQL. `get_schema` (poznaj strukturę) -> `run_query`
(wykonaj SELECT). To potężne, ale i NIEBEZPIECZNE - dlaczego, jest w README.

Uruchom: uv run adk web ex_16_text_to_sql
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane Chinook na podstawie SQL.",
    # TODO(you): podmień placeholder na instrukcję dyscyplinującą pisanie SQL.
    instruction=placeholder(
        "podłącz get_schema i run_query; napisz instrukcję: NAJPIERW get_schema, "
        "potem SELECT, bez zgadywania nazw tabel i kolumn",
        readme="README ex_16_text_to_sql",
    ),
    # TODO(you): podłącz get_schema oraz run_query.
    tools=[],
)
