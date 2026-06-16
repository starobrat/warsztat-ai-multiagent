"""Ćwiczenie ex_11: łańcuch narzędzi - moduł 6. STARTER.

Czasem jedno pytanie wymaga DWÓCH narzędzi po kolei: najpierw rozwiąż
wykonawcę (`get_artists`), potem pobierz jego albumy (`get_albums_for_artist`).
Tu ćwiczysz sekwencjonowanie - widać je jako łańcuch w zakładce Traces.

Uruchom: uv run adk web ex_11_lancuch_narzedzi
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_artists, get_albums_for_artist

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent dobierający albumy wykonawcy z bazy Chinook.",
    # TODO(you): podmień placeholder na instrukcję prowadzącą agenta przez łańcuch.
    instruction=placeholder(
        "podłącz get_artists i get_albums_for_artist; napisz instrukcję, by agent "
        "NAJPIERW znalazł właściwego wykonawcę, a POTEM pobrał jego albumy",
        readme="README ex_11_lancuch_narzedzi",
    ),
    # TODO(you): podłącz get_artists oraz get_albums_for_artist.
    tools=[],
)
