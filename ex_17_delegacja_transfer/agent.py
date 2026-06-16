"""Ćwiczenie ex_17: delegacja przez transfer (moduł 9). STARTER.

Master (`LlmAgent` z `sub_agents`) NIE robi roboty sam - na podstawie `description`
swoich specjalistów decyduje, KOMU przekazać zadanie (transfer sterowania). Model
sam wybiera sub-agenta. W `adk web` (zakładka Traces) widać, kto przejął zadanie.

Dwaj specjaliści są gotowi. Twoje zadanie: napisać instrukcję mastera i podłączyć
ich jako `sub_agents`.

Uruchom: uv run adk web ex_17_delegacja_transfer
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent


# Specjalista 1 - powitania i luźna rozmowa. GOTOWY.
agent_powitan = LlmAgent(
    name="agent_powitan",
    model=get_model(),
    description="Obsługuje powitania, podziękowania i luźną rozmowę (small talk).",
    instruction="Jesteś uprzejmym gospodarzem. Witaj się i prowadź lekką rozmowę po polsku.",
)

# Specjalista 2 - dane sklepu Chinook. GOTOWY.
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

# MASTER - koordynator. Sam nie liczy ani nie wita - DELEGUJE.
root_agent = LlmAgent(
    name="koordynator",
    model=get_model(),
    description="Koordynator - deleguje zadanie właściwemu specjaliście.",
    # TODO(you): napisz instrukcję, która opisuje, KIEDY przekazać zadanie któremu
    # sub-agentowi (powitania -> agent_powitan, dane sklepu -> analityk_chinook).
    instruction=placeholder(
        "napisz instrukcję mastera (kiedy delegować do agent_powitan, a kiedy do "
        "analityk_chinook) i podłącz obu jako sub_agents",
        readme="README ex_17_delegacja_transfer",
    ),
    # TODO(you): podłącz obu specjalistów jako sub_agents.
    sub_agents=[],
)
