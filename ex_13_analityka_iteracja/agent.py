"""Ćwiczenie ex_13: analityka przez iterację - moduł 6. STARTER.

Pierwsza prawdziwa ANALITYKA: agent pobiera listę gatunków (`get_genres`),
a potem dla każdego liczy sprzedaż w danym roku (`get_sold_count_for_genre`)
i porównuje. Wynik to wielokrotne wywołania narzędzi w pętli - widać je w Traces.

Uruchom: uv run adk web ex_13_analityka_iteracja
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_genres, get_sold_count_for_genre

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent analizujący sprzedaż gatunków w bazie Chinook.",
    # TODO(you): podmień placeholder na instrukcję prowadzącą iterację po gatunkach.
    instruction=placeholder(
        "podłącz get_genres i get_sold_count_for_genre; napisz instrukcję, by agent "
        "zebrał gatunki i porównał ich sprzedaż w zadanym roku",
        readme="README ex_13_analityka_iteracja",
    ),
    # TODO(you): podłącz get_genres oraz get_sold_count_for_genre.
    tools=[],
)
