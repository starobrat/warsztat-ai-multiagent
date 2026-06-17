"""ROZWIĄZANIE ex_17: delegacja przez transfer (moduł 9).

Master deleguje do jednego z dwóch specjalistów na podstawie ich `description`.
Wypełnione: instrukcja mastera + podpięcie sub_agents.

Uruchom: uv run adk run solutions/ex_17_delegacja_transfer "..." (albo adk web).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


agent_powitan = LlmAgent(
    name="agent_powitan",
    model=get_model(),
    description="Obsługuje powitania, podziękowania i luźną rozmowę (small talk).",
    instruction="Jesteś uprzejmym gospodarzem. Witaj się i prowadź lekką rozmowę po polsku.",
)

analityk_chinook = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Odpowiada na pytania o dane sklepu z muzyką (baza Chinook).",
    instruction=(
        "Najpierw sprawdź schemat (get_schema), potem napisz SELECT (run_query). "
        "Nie zgaduj nazw tabel. Odpowiadaj po polsku na podstawie danych z bazy."
    ),
    tools=[get_schema, run_query],
)

root_agent = LlmAgent(
    name="master",
    model=get_model(),
    description="Master - deleguje zadanie właściwemu specjaliście.",
    instruction=(
        "Jesteś masterem. Sam nie odpowiadasz merytorycznie - rozpoznaj "
        "intencję użytkownika i PRZEKAŻ zadanie właściwemu sub-agentowi.\n"
        "- Powitania, podziękowania, luźna rozmowa -> agent_powitan.\n"
        "- Pytania o dane sklepu z muzyką (klienci, sprzedaż, gatunki, faktury) "
        "-> analityk_chinook."
    ),
    sub_agents=[agent_powitan, analityk_chinook],
)
