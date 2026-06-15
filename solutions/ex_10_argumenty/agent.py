"""ROZWIĄZANIE ćwiczenia ex_10: narzędzie z argumentem - moduł 6.

Narzędzie `get_sold_count_for_artist(artist)` bierze ARGUMENT. Model musi
wyłuskać go z pytania ("ile sprzedał AC/DC?") i podać narzędziu. Tu widać
przepływ argumentu z języka naturalnego do wywołania narzędzia.

Uruchom: uv run adk web solutions/ex_10_argumenty
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_sold_count_for_artist

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent liczący sprzedaż wykonawców w bazie Chinook.",
    instruction=(
        "Jesteś analitykiem sprzedaży sklepu muzycznego Chinook. Odpowiadaj "
        "po polsku, krótko i rzeczowo. Gdy użytkownik pyta, ile utworów "
        "sprzedał dany wykonawca, wyłuskaj nazwę wykonawcy z pytania i wywołaj "
        "narzędzie `get_sold_count_for_artist`, podając tę nazwę jako argument "
        "`artist` (np. dla pytania o AC/DC -> artist='AC/DC'). Odpowiadaj "
        "WYŁĄCZNIE liczbą zwróconą przez narzędzie - nie zmyślaj. Jeśli "
        "narzędzie nie zwróci wyniku, powiedz, że nie masz tych danych."
    ),
    tools=[get_sold_count_for_artist],
)
