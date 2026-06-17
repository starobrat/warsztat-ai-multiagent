"""DEMO (moduł 9): transfer sterowania w systemie wieloagentowym.

Master deleguje zadanie do jednego z dwóch specjalistów na podstawie
ich `description`. W adk web (zakładka Traces) widać, KTO przejął zadanie.

Spróbuj: "cześć, co słychać?" (-> agent_powitan) oraz "ilu mamy klientów z Niemiec?"
(-> analityk_chinook).

Uruchom: uv run adk web demo_09_transfer
"""

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
        "Rozpoznaj intencję użytkownika i przekaż zadanie właściwemu sub-agentowi. "
        "Powitania i luźna rozmowa -> agent_powitan. "
        "Pytania o dane sklepu -> analityk_chinook."
    ),
    sub_agents=[agent_powitan, analityk_chinook],
)
