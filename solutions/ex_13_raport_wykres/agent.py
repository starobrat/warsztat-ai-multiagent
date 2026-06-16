"""ROZWIĄZANIE ćwiczenia ex_13: raport z wykresem - moduł 6.

Payoff bloku narzędziowego: agent nie tylko liczy, ale ROBI ARTEFAKT. Łączysz
analitykę (gatunki + sprzedaż) z narzędziem rysującym wykres słupkowy. Pytasz
"zrób wykres sprzedaży wg gatunku za 2025" - agent generuje plik PNG.

Uruchom: uv run adk web solutions/ex_13_raport_wykres
"""

import sys
from pathlib import Path

# Solution leży o poziom głębiej (solutions/<ex>/) - dokładamy korzeń repo do
# sys.path, żeby `from common...` działało niezależnie od sposobu startu adk.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

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
    instruction=(
        "Jesteś analitykiem sprzedaży sklepu Chinook, który tworzy raporty wizualne. "
        "Odpowiadasz po polsku, opierasz się wyłącznie na danych z narzędzi - nie zmyślasz liczb.\n\n"
        "Gdy użytkownik prosi o wykres sprzedaży gatunków za dany rok, postępuj tak:\n"
        "1. Wywołaj get_genres, żeby pobrać pełną listę gatunków.\n"
        "2. Dla KAŻDEGO gatunku wywołaj get_sold_count_for_genre(genre, year) "
        "z rokiem podanym przez użytkownika - po jednym wywołaniu na gatunek.\n"
        "3. Gdy masz już komplet danych, OBOWIĄZKOWO wywołaj narysuj_wykres_slupkowy: "
        "labels to lista nazw gatunków, values to odpowiadające im liczby sprzedaży, "
        "a title opisuje raport (np. 'Sprzedaż wg gatunku 2025').\n"
        "4. W odpowiedzi podaj ścieżkę zwróconą przez narzędzie i zaznacz, że wykres "
        "jest też zapisany jako artefakt (widoczny w zakładce Artifacts).\n\n"
        "Nie kończ, dopóki nie wywołasz narzędzia rysującego wykres - sama tabela liczb to za mało."
    ),
    tools=[get_genres, get_sold_count_for_genre, narysuj_wykres_slupkowy],
)
