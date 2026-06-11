"""Agent do tuningu - moduł 8. Instrukcja jest CELOWO słaba.

To jest serce szkolenia: prompt to nie strzał z głowy. Ten agent ma celowo
kiepską instrukcję i nie przechodzi ewaluacji (part2_adk/evals/sql_agent.evalset.json).

Zadanie:
  1. Uruchom eval i zobacz, że jest czerwony:
        uv run adk eval part2_adk/agents/sql_agent_to_tune part2_adk/evals/sql_agent.evalset.json
  2. Popraw instruction (NIE narzędzia, NIE model) tak, żeby eval przeszedł.
  3. Powtarzaj: zmiana instrukcji -> eval -> porównanie. To jest pętla jakości.

Wskazówka: porównaj z tym, co napisałeś w sql_agent. Czego brakuje tej instrukcji,
żeby agent najpierw patrzył w schemat i nie zgadywał nazw tabel?
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from model import get_model  # noqa: E402
from tools.db import get_schema, run_query  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


root_agent = LlmAgent(
    name="sql_agent_to_tune",
    model=get_model(),
    description="Agent SQL z celowo słabą instrukcją - do poprawienia w module 8.",
    # Celowo zła instrukcja: zbyt ogólna, nie mówi o schemacie ani o zakazie zgadywania.
    instruction="Odpowiadaj na pytania o sklep.",
    tools=[get_schema, run_query],
)
