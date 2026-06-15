"""Ćwiczenie ex_07: docstring narzędzia - moduł 6. STARTER.

Docstring to KONTRAKT, który czyta model, żeby zdecydować, KIEDY wywołać
narzędzie. Dokładasz narzędzie `get_genres` z PUSTYM docstringiem, sam piszesz
jego opis - a potem sprawdzasz w Traces, czy model trafnie po nie sięga.

Uruchom: uv run adk web ex_07_docstring
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema
from common.tools.db import get_genres as _dane_gatunkow

from google.adk.agents import LlmAgent


def get_genres() -> list[str]:
    # TODO(you): napisz docstring tego narzędzia (1-2 zdania: co zwraca i kiedy
    # je wywołać). To właśnie on decyduje, czy model w ogóle po nie sięgnie.
    return _dane_gatunkow()


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent o danych Chinook (struktura + gatunki).",
    # TODO(you): podmień placeholder na instrukcję-grounding (jak w ex_06).
    instruction=placeholder(
        "napisz docstring narzędzia get_genres (niżej) i podłącz get_schema oraz get_genres",
        readme="README ex_07_docstring",
    ),
    # TODO(you): podłącz get_schema oraz lokalne get_genres.
    tools=[],
)
