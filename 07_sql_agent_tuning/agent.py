"""Agent do tuningu promptu - moduł 8. TDD dla promptu.

Serce szkolenia: prompt to nie strzał z głowy - prompt SIĘ TESTUJE, jak kod.

To jest TDD na prompcie:
  1. Test (evalset) już jest - 06_evaluation/sql_agent.evalset.json.
  2. Agent startuje z instrukcją napisaną przez LAIKA, który nie wie, co jest
     w bazie ani jak ją odpytać. Eval jest CZERWONY (agent nie zna danych).
  3. Twoje zadanie: iterować WYŁĄCZNIE instruction, aż eval przejdzie na zielono.
     Nie ruszaj narzędzi ani modelu.

Zadanie:
  1. Uruchom eval i zobacz czerwony:
        uv run adk eval 07_sql_agent_tuning 06_evaluation/sql_agent.evalset.json \\
            --config_file_path 06_evaluation/test_config.json
  2. Popraw instruction (porównaj z 05_sql_agent): nadaj rolę analityka, każ
     NAJPIERW sprawdzić schemat (get_schema), potem pisać SELECT (run_query),
     zabroń zgadywania, każ odpowiadać po polsku tylko na podstawie danych.
  3. Powtarzaj: zmiana instrukcji -> eval -> porównanie. To jest pętla jakości.

Dlaczego słabszy model? Ten agent chodzi celowo na słabszym modelu
(get_weak_model, domyślnie gpt-4o-mini). Mocny model maskuje słaby prompt -
i tak sięgnie po narzędzia i odpowie dobrze, więc nie zobaczyłbyś czerwonego.
Słabszy model słucha instrukcji dosłownie: zła instrukcja = zły agent. To samo
w sobie jest lekcją - im słabszy model, tym bardziej liczy się prompt.
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
