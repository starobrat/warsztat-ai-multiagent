"""Agent SQL - moduły 6-7. STARTER.

Ten sam agent co w części 1 (odpytuje Chinook), ale teraz w ADK. Zauważ:
funkcje z common/tools/db.py mają docstringi i type hinty, więc wystarczy podać
je w tools=[...] - ADK sam zrobi z nich FunctionTool.

Zadanie:
  1. Napisz instruction dla agenta (rola + zasady korzystania z narzędzi).
  2. Podłącz narzędzia get_schema i run_query.

Uruchom:
    uv run adk web 05_sql_agent
"""

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent",
    model=get_model(),
    description="Agent odpowiadający na pytania o dane sklepu Chinook na podstawie SQL.",
    # TODO(you): napisz instruction. Dobra instrukcja powinna:
    #   - nadać rolę (analityk sklepu z muzyką, baza Chinook/SQLite),
    #   - kazać NAJPIERW sprawdzić schemat (get_schema), potem pisać SELECT,
    #   - zabronić zgadywania nazw tabel/kolumn,
    #   - kazać odpowiadać po polsku, zwięźle, na podstawie danych z bazy.
    instruction="",
    # TODO(you): podłącz narzędzia.
    tools=[],
)
