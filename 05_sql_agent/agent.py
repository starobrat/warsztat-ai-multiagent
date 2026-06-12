"""Agent SQL - moduły 6-7. STARTER.

Ten sam agent co w części 1, ale w ADK. Funkcje z common/tools/db.py mają docstringi
i type hinty, więc po podaniu w tools=[...] ADK sam zrobi z nich FunctionTool.
Zadanie: napisz instruction i podłącz get_schema oraz run_query.

Uruchom: uv run adk web 05_sql_agent (albo adk run 05_sql_agent).
"""

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane sklepu Chinook na podstawie SQL.",
    # TODO(you): instruction - rola analityka (Chinook/SQLite), NAJPIERW get_schema,
    # potem SELECT, bez zgadywania nazw, odpowiedź po polsku tylko na podstawie danych.
    instruction="",
    # TODO(you): podłącz narzędzia (get_schema, run_query).
    tools=[],
)
