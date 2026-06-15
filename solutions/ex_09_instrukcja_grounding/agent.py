"""Ćwiczenie ex_09: instrukcja-grounding - moduł 6. STARTER.

Agent ma już narzędzie (`get_schema`), ale wciąż potrafi zmyślać, gdy pytasz
o coś spoza danych. Tu uczysz go DYSCYPLINY: odpowiadać wyłącznie na podstawie
narzędzi, a bez danych - odmówić.

Uruchom: uv run adk web ex_09_instrukcja_grounding
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
        "Jesteś analitykiem bazy Chinook. Rozmawiasz po polsku, krótko i "
        "rzeczowo.\n\n"
        "Twoja jedyna wiedza pochodzi z narzędzia `get_schema`, które zwraca "
        "strukturę bazy Chinook. Zasady:\n"
        "- Gdy użytkownik pyta o strukturę bazy (tabele, kolumny, relacje), "
        "wywołaj `get_schema` i odpowiedz WYŁĄCZNIE na podstawie tego, co "
        "zwróci.\n"
        "- Niczego nie zmyślaj. Nie podawaj nazw tabel ani kolumn, których nie "
        "ma w schemacie.\n"
        "- Gdy użytkownik pyta o coś spoza danych bazy Chinook (np. wiedza "
        "ogólna, fakty ze świata, stolice państw), grzecznie odmów i wyjaśnij, "
        "że odpowiadasz tylko na pytania o strukturę bazy Chinook na podstawie "
        "dostępnych danych. Nie próbuj zgadywać odpowiedzi."
    ),
    tools=[get_schema],
)
