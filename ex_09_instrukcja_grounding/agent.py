"""Ćwiczenie ex_09: instrukcja-grounding - moduł 6. STARTER.

Agent ma już narzędzie (`get_schema`), ale wciąż potrafi zmyślać, gdy pytasz
o coś spoza danych. Tu uczysz go DYSCYPLINY: odpowiadać wyłącznie na podstawie
narzędzi, a bez danych - odmówić.

Uruchom: uv run adk web ex_09_instrukcja_grounding
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent o strukturze bazy Chinook, odpowiadający tylko na podstawie danych.",
    # TODO(you): podmień placeholder na instrukcję-grounding (patrz README).
    instruction=placeholder(
        "napisz instrukcję, która każe odpowiadać WYŁĄCZNIE na podstawie narzędzi "
        "i ODMÓWIĆ, gdy nie ma danych",
        readme="README ex_09_instrukcja_grounding",
    ),
    tools=[get_schema],
)
