"""Ćwiczenie ex_08: pierwsze narzędzie - moduł 6. STARTER.

Twój agent dostaje PIERWSZE narzędzie: `get_schema` (czyta strukturę bazy
Chinook). Tu chodzi o jedno: podłączyć narzędzie i zobaczyć jego wywołanie
w adk web (zakładki Events / Traces).

Uruchom: uv run adk web ex_08_pierwsze_narzedzie
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent odpowiadający o strukturze bazy Chinook.",
    # TODO(you) [krok 2]: podmień placeholder na prostą instrukcję (gotowiec w README).
    instruction=placeholder(
        "podłącz narzędzie get_schema i podmień tę instrukcję",
        readme="README ex_08_pierwsze_narzedzie",
    ),
    # TODO(you) [krok 1]: podłącz narzędzie get_schema (zaimportowane wyżej).
    tools=[],
)
