"""Ćwiczenie ex_14: raport z wykresem - moduł 6. STARTER.

Payoff bloku narzędziowego: agent nie tylko liczy, ale ROBI ARTEFAKT. Łączysz
analitykę (gatunki + sprzedaż) z narzędziem rysującym wykres słupkowy. Pytasz
"zrób wykres sprzedaży wg gatunku za 2025" - agent generuje plik PNG.

Uruchom: uv run adk web ex_14_raport_wykres
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.charts import bar_chart
from common.tools.db import get_genres, get_sold_count_for_genre

from google.adk.agents import LlmAgent


def narysuj_wykres_slupkowy(labels: list[str], values: list[float], title: str) -> str:
    """Rysuje wykres słupkowy z podanych etykiet i wartości; zwraca ścieżkę do PNG.

    Args:
        labels: etykiety słupków (np. nazwy gatunków).
        values: wartości słupków (np. liczby sprzedanych utworów).
        title: tytuł wykresu.
    """
    return bar_chart(labels, values, title, "raport.png")


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent budujący raporty sprzedaży z bazy Chinook.",
    # TODO(you): podmień placeholder na instrukcję prowadzącą zebranie danych i wykres.
    instruction=placeholder(
        "podłącz get_genres, get_sold_count_for_genre i narysuj_wykres_slupkowy; "
        "napisz instrukcję, by agent zebrał dane i zrobił z nich wykres",
        readme="README ex_14_raport_wykres",
    ),
    # TODO(you): podłącz get_genres, get_sold_count_for_genre i narysuj_wykres_slupkowy.
    tools=[],
)
