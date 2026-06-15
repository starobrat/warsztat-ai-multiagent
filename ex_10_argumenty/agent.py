"""Ćwiczenie ex_11: narzędzie z argumentem - moduł 6. STARTER.

Narzędzie `get_sold_count_for_artist(artist)` bierze ARGUMENT. Model musi
wyłuskać go z pytania ("ile sprzedał AC/DC?") i podać narzędziu. Tu ćwiczysz
przepływ argumentu z języka naturalnego do wywołania narzędzia.

Uruchom: uv run adk web ex_10_argumenty
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_sold_count_for_artist

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent liczący sprzedaż wykonawców w bazie Chinook.",
    # TODO(you): podmień placeholder na instrukcję (grounding + użycie narzędzia).
    instruction=placeholder(
        "podłącz get_sold_count_for_artist i napisz instrukcję, by agent pytał "
        "narzędzie o liczbę sprzedanych utworów danego wykonawcy",
        readme="README ex_10_argumenty",
    ),
    # TODO(you): podłącz get_sold_count_for_artist.
    tools=[],
)
