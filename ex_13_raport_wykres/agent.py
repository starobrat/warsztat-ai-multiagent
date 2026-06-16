"""Ćwiczenie ex_13: raport z wykresem - moduł 6. STARTER.

Payoff bloku narzędziowego: agent nie tylko liczy, ale ROBI ARTEFAKT. Łączysz
analitykę (gatunki + sprzedaż) z narzędziem rysującym wykres słupkowy. Pytasz
"zrób wykres sprzedaży wg gatunku za 2025" - agent generuje PNG i zapisuje go
jako ARTEFAKT (widoczny w zakładce Artifacts w adk web).

Uruchom: uv run adk web ex_13_raport_wykres
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.charts import bar_chart_artifact
from common.tools.db import get_genres, get_sold_count_for_genre

from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


async def narysuj_wykres_slupkowy(
    labels: list[str], values: list[float], title: str, tool_context: ToolContext
) -> str:
    """Rysuje wykres słupkowy i zapisuje go jako ARTEFAKT agenta (zakładka Artifacts).

    Args:
        labels: etykiety słupków (np. nazwy gatunków).
        values: wartości słupków (np. liczby sprzedanych utworów).
        title: tytuł wykresu.
    """
    return await bar_chart_artifact(labels, values, title, "raport.png", tool_context)


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent budujący raporty sprzedaży z bazy Chinook.",
    # TODO(you): podmień placeholder na instrukcję prowadzącą zebranie danych i wykres.
    instruction=placeholder(
        "podłącz get_genres, get_sold_count_for_genre i narysuj_wykres_slupkowy; "
        "napisz instrukcję, by agent zebrał dane i zrobił z nich wykres",
        readme="README ex_13_raport_wykres",
    ),
    # TODO(you): podłącz get_genres, get_sold_count_for_genre i narysuj_wykres_slupkowy.
    tools=[],
)
