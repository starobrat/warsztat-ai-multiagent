"""ROZWIĄZANIE ćwiczenia ex_13: analityka przez iterację - moduł 6.

Pierwsza prawdziwa ANALITYKA: agent pobiera listę gatunków (`get_genres`),
a potem dla każdego liczy sprzedaż w danym roku (`get_sold_count_for_genre`)
i porównuje. Wynik to wielokrotne wywołania narzędzi w pętli - widać je w Traces.

Uruchom: uv run adk web solutions/ex_13_analityka_iteracja
"""

import sys
from pathlib import Path

# Solution leży o poziom głębiej (solutions/<ex>/) - dokładamy korzeń repo do
# sys.path, żeby `from common...` działało niezależnie od sposobu startu adk.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_genres, get_sold_count_for_genre

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent analizujący sprzedaż gatunków w bazie Chinook.",
    instruction=(
        "Jesteś analitykiem sprzedaży sklepu Chinook. Odpowiadasz po polsku, "
        "krótko i rzeczowo, wyłącznie na podstawie danych z narzędzi - nie zmyślasz liczb.\n\n"
        "Gdy użytkownik pyta, który gatunek sprzedał się najlepiej (lub najgorzej) "
        "w danym roku, postępuj tak:\n"
        "1. Wywołaj get_genres, żeby pobrać pełną listę gatunków.\n"
        "2. Dla KAŻDEGO gatunku z listy wywołaj get_sold_count_for_genre(genre, year) "
        "z rokiem podanym przez użytkownika. To wiele wywołań - po jednym na gatunek.\n"
        "3. Porównaj wszystkie wyniki i wskaż gatunek z najwyższą (lub najniższą) sprzedażą.\n\n"
        "W odpowiedzi podaj zwycięski gatunek i jego liczbę sprzedanych utworów. "
        "Nie pomijaj żadnego gatunku - musisz sprawdzić każdy, zanim wyciągniesz wniosek."
    ),
    tools=[get_genres, get_sold_count_for_genre],
)
