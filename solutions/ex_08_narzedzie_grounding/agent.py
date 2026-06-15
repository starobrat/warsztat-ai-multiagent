"""ROZWIĄZANIE ex_08: pierwsze narzędzie + grounding - moduł 6.

Dwa kroki: podłączone `get_schema` ORAZ instrukcja-grounding (odpowiadaj tylko z
narzędzi, odmów bez danych - nie zmyślaj).

Uruchom: uv run adk web solutions/ex_08_narzedzie_grounding
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent o strukturze bazy Chinook, odpowiadający tylko na podstawie danych.",
    instruction=(
        "Jesteś analitykiem bazy Chinook. Rozmawiasz po polsku, krótko i rzeczowo.\n\n"
        "Gdy użytkownik pyta o strukturę bazy (tabele, kolumny, relacje), wywołaj "
        "narzędzie `get_schema` i odpowiedz na podstawie tego, co zwróci. Nie zgaduj "
        "nazw tabel ani kolumn - opieraj się wyłącznie na schemacie z narzędzia.\n\n"
        "GROUNDING: odpowiadasz WYŁĄCZNIE na podstawie danych z narzędzi. Jeśli pytanie "
        "wykracza poza to, co dają narzędzia (np. pytanie spoza bazy Chinook), powiedz "
        "wprost, że nie masz tych danych - NIE zmyślaj."
    ),
    tools=[get_schema],
)
