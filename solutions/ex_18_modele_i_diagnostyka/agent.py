"""ROZWIĄZANIE: agent do tuningu promptu - moduł 8. TDD dla promptu.

Diagnoza: laicka instrukcja kazała odpowiadać "z głowy" - słaby model jej słuchał,
NIE wołał narzędzi i oblewał eval (czerwony). Naprawa: TYLKO instruction - dyscyplina
SQL (najpierw schemat, potem SELECT, bez zgadywania). Model i narzędzia bez zmian.
Po poprawie eval przechodzi (zielony). To jest pointa: prompt = kod, testuje się go.

Uruchom eval:
  uv run adk eval solutions/ex_16_modele_i_diagnostyka \\
      ex_15_ewaluacja/sql_agent.evalset.json --config_file_path ex_15_ewaluacja/test_config.json
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_weak_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="sql_agent_to_tune",
    model=get_weak_model(),  # SŁABY model bez zmian - naprawiamy WYŁĄCZNIE prompt
    description="Agent SQL z naprawioną instrukcją - przechodzi eval mimo słabego modelu.",
    instruction=(
        "Jesteś analitykiem danych sklepu z muzyką (baza Chinook, SQLite). "
        "Odpowiadasz WYŁĄCZNIE na podstawie danych z bazy, nigdy z pamięci. "
        "Zawsze pracuj w dwóch krokach: 1) wywołaj get_schema, żeby poznać tabele i "
        "kolumny; 2) napisz zapytanie SELECT i wykonaj je przez run_query. "
        "Nie zgaduj nazw tabel ani kolumn - bierz je ze schematu. "
        "Gdy masz wynik zapytania, podaj zwięzłą odpowiedź po polsku opartą na liczbach "
        "z bazy. Jeśli pytanie nie dotyczy danych w bazie - powiedz, że nie wiesz."
    ),
    tools=[get_schema, run_query],
)
