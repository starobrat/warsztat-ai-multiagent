"""ROZWIĄZANIE ćwiczenia ex_11: łańcuch narzędzi - moduł 6.

Czasem jedno pytanie wymaga DWÓCH narzędzi po kolei: najpierw rozwiąż
wykonawcę (`get_artists`), potem pobierz jego albumy (`get_albums_for_artist`).
Sekwencję widać jako łańcuch w zakładce Traces.

Uruchom: uv run adk web solutions/ex_11_lancuch_narzedzi
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_artists, get_albums_for_artist

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent dobierający albumy wykonawcy z bazy Chinook.",
    instruction=(
        "Jesteś analitykiem katalogu sklepu muzycznego Chinook. Odpowiadaj po "
        "polsku, krótko i rzeczowo. Gdy użytkownik pyta o albumy danego "
        "wykonawcy, działaj w dwóch krokach: NAJPIERW wywołaj `get_artists`, "
        "żeby znaleźć właściwego wykonawcę, a POTEM "
        "wywołaj `get_albums_for_artist` dla tego wykonawcy, by pobrać jego "
        "albumy. Korzystaj WYŁĄCZNIE z danych zwróconych przez narzędzia - "
        "nie zmyślaj. Jeśli wykonawcy nie ma w bazie, powiedz to wprost."
    ),
    tools=[get_artists, get_albums_for_artist],
)
