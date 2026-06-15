"""ROZWIĄZANIE ćwiczenia: pierwszy agent w ADK - moduł 5.

Twój pierwszy LlmAgent. Jedyne TODO to instruction (rola). Reszta gotowa.

Uruchom: uv run adk web solutions/ex_04_hello (UI)
         uv run adk run solutions/ex_04_hello "Cześć" (terminal, jeden krok).
"""

import sys
from pathlib import Path

# Solution leży o poziom głębiej (solutions/<ex>/) - dokładamy korzeń repo do
# sys.path, żeby `from common...` działało niezależnie od sposobu startu adk.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="hello",
    model=get_model(),
    description="Prosty agent powitalny do pierwszego kontaktu z ADK.",
    instruction=(
        "Jesteś przyjaznym asystentem sklepu z muzyką Chinook. "
        "Rozmawiasz po polsku, odpowiadasz krótko i rzeczowo. "
        "Nie masz jeszcze żadnych narzędzi ani dostępu do bazy - po prostu "
        "rozmawiasz. Jeśli ktoś pyta o konkretne dane (liczby, ceny, statystyki), "
        "uczciwie mówisz, że na razie nie masz do nich dostępu, i nie zmyślasz."
    ),
)
