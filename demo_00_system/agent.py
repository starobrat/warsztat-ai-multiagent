"""DEMO 00 (moduł 1): system, który zbudujemy przez dwa dni - teaser dla prowadzącego.

To NIE jest ćwiczenie - to demo "co tu zbudujemy", odpalane na slajdzie 11.
Łączy w jednym agencie trzy rzeczy, które uczestnicy złożą sami warstwa po warstwie:
  - poznanie struktury bazy (get_schema)            -> moduł 5/7
  - pisanie i wykonywanie SQL na żywo (run_query)    -> ćwiczenie ex_14 (text-to-SQL)
  - artefakt: wykres słupkowy PNG (bar_chart)        -> ćwiczenie ex_13 (raport z wykresem)

Pomysł na pokaz:
  1. "Jak wygląda struktura tej bazy?"  -> agent woła get_schema i opisuje tabele.
  2. Dowolne pytanie analityczne, np.
     "Którzy wykonawcy sprzedali się najlepiej? Zrób wykres top 10."
     -> agent pisze SELECT, wykonuje go, rysuje wykres (zakładka Artifacts).
  3. Pointa: tego NIE zaprogramowaliśmy pod konkretne pytanie - agent sam dobiera
     SQL i narzędzia. Przez dwa dni rozbierzemy to na części i złożymy od zera.

Uruchom: uv run adk web demo_00_system
"""

import sys
from pathlib import Path

# adk ładuje agenta po ścieżce pliku - dokładamy korzeń repo, żeby `from common`
# działało zarówno pod `adk web`, jak i `adk eval`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.model import get_model  # noqa: E402
from common.tools.charts import bar_chart_artifact  # noqa: E402
from common.tools.db import get_schema, run_query  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.tools.tool_context import ToolContext  # noqa: E402


async def narysuj_wykres_slupkowy(
    labels: list[str], values: list[float], title: str, tool_context: ToolContext
) -> str:
    """Rysuje wykres słupkowy i zapisuje go jako ARTEFAKT agenta (zakładka Artifacts).

    Args:
        labels: etykiety słupków (np. nazwy wykonawców albo gatunków).
        values: wartości słupków (np. liczby sprzedanych utworów).
        title: tytuł wykresu.
    """
    return await bar_chart_artifact(labels, values, title, "demo.png", tool_context)


root_agent = LlmAgent(
    name="demo_system_chinook",
    model=get_model(),
    description="Analityk sklepu Chinook: poznaje schemat, pisze SQL, robi wykresy.",
    instruction=(
        "Jesteś analitykiem danych sklepu muzycznego Chinook. Odpowiadasz po polsku, "
        "zwięźle, i opierasz się WYŁĄCZNIE na danych z narzędzi - nie zmyślasz liczb.\n\n"
        "Masz trzy narzędzia:\n"
        "- get_schema: zwraca strukturę bazy (tabele i kolumny). Użyj go, gdy nie znasz "
        "nazw tabel/kolumn albo gdy ktoś pyta, jak wygląda baza.\n"
        "- run_query: wykonuje zapytanie SELECT (tylko do odczytu) i zwraca wiersze.\n"
        "- narysuj_wykres_slupkowy: tworzy wykres słupkowy jako artefakt.\n\n"
        "Zasady:\n"
        "1. Gdy potrzebujesz danych, NAJPIERW poznaj schemat (get_schema), potem pisz SELECT - "
        "nie zgaduj nazw tabel ani kolumn.\n"
        "2. Gdy użytkownik prosi o wykres / ranking / 'pokaż', po zebraniu danych OBOWIĄZKOWO "
        "wywołaj narysuj_wykres_slupkowy (labels = etykiety, values = liczby).\n"
        "3. W odpowiedzi krótko podsumuj wynik i - jeśli był wykres - zaznacz, że jest w "
        "zakładce Artifacts.\n"
        "4. To baza tylko do odczytu - generuj wyłącznie zapytania SELECT."
    ),
    tools=[get_schema, run_query, narysuj_wykres_slupkowy],
)
