"""Agent do tuningu promptu - moduł 8. TDD dla promptu.

Prompt SIĘ TESTUJE jak kod. Test (ex_17_eval_uruchom) już jest, a agent startuje z laicką
instrukcją i OBLEWA eval (czerwony). Iteruj WYŁĄCZNIE instruction, aż przejdzie
(zielony) - porównaj z ex_14_text_to_sql. Nie ruszaj narzędzi ani modelu.

Chodzi celowo na słabszym modelu (get_weak_model): mocny zamaskowałby słaby prompt.
Pełne uzasadnienie i komendy: README tego katalogu.

Uruchom eval: uv run adk eval ex_18_modele_i_diagnostyka ex_17_eval_uruchom/sql_agent.evalset.json \\
    --config_file_path ex_17_eval_uruchom/test_config.json
"""

from common.model import get_weak_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent_to_tune",
    model=get_weak_model(),
    description="Agent SQL ze słabą, laicką instrukcją - do poprawienia w module 8.",
    # Instrukcja napisana przez laika: nie wie, że jest baza, schemat ani SQL.
    # Każe odpowiadać "z głowy" - agent nie sięga po dane i oblewa eval.
    instruction=(
        "Jesteś sympatycznym sprzedawcą w sklepie z muzyką. Odpowiadasz klientom "
        "na pytania o nasz sklep z głowy, na podstawie tego, co wiesz o muzyce. "
        "Pisz miło i krótko. Nie znasz się na bazach danych ani na SQL."
    ),
    tools=[get_schema, run_query],
)
