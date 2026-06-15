"""Ćwiczenie ex_08: pierwsze narzędzie - moduł 6. STARTER.

Twój agent dostaje PIERWSZE narzędzie: `get_schema` (czyta strukturę bazy
Chinook). Tu chodzi o jedno: podłączyć narzędzie i zobaczyć jego wywołanie
w adk web (zakładki Events / Traces).

Uruchom: uv run adk web ex_08_pierwsze_narzedzie
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
    description="Agent odpowiadający o strukturze bazy Chinook.",
    instruction=(
        "Jesteś analitykiem bazy Chinook. Rozmawiasz po polsku, krótko i "
        "rzeczowo.\n\n"
        "Gdy użytkownik pyta o strukturę bazy (jakie są tabele, kolumny, "
        "relacje), wywołaj narzędzie `get_schema`, żeby poznać schemat, i "
        "odpowiedz na podstawie tego, co zwróci. Nie zgaduj nazw tabel ani "
        "kolumn - opieraj się wyłącznie na schemacie z narzędzia."
    ),
    tools=[get_schema],
)
