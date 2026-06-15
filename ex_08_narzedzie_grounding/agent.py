"""Ćwiczenie ex_08: pierwsze narzędzie + grounding - moduł 6. STARTER.

Dwa kroki w jednym ćwiczeniu:
1. Agent dostaje PIERWSZE narzędzie `get_schema` (czyta strukturę bazy Chinook) -
   podłączasz je i widzisz wywołanie w adk web (Events / Traces).
2. GROUNDING: piszesz instrukcję, która każe odpowiadać WYŁĄCZNIE na podstawie
   narzędzi, a bez danych - ODMÓWIĆ (zamiast zmyślać).

Uruchom: uv run adk web ex_08_narzedzie_grounding
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent o strukturze bazy Chinook, odpowiadający tylko na podstawie danych.",
    # TODO(you) [krok 2]: podmień placeholder na instrukcję-grounding - odpowiadaj
    # tylko z narzędzi, odmów gdy brak danych (gotowiec/wskazówka w README).
    instruction=placeholder(
        "podłącz get_schema oraz napisz instrukcję-grounding (tylko z danych, "
        "odmowa bez danych)",
        readme="README ex_08_narzedzie_grounding",
    ),
    # TODO(you) [krok 1]: podłącz narzędzie get_schema (zaimportowane wyżej).
    tools=[],
)
