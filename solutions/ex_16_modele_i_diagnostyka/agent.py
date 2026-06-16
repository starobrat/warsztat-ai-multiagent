"""ROZWIĄZANIE ex_16: modele i diagnostyka - moduł 8.

Diagnoza: opisy narzędzi (docstringi) były mylące - 'sales_by_artist' twierdził,
że zwraca albumy, a 'albums_by_artist', że liczy sprzedaż. Słaby model słuchał
opisów dosłownie i wybierał ZŁE narzędzie -> zła trajektoria -> eval czerwony.
Naprawa: poprawne, konkretne docstringi (kontrakt dla LLM) + instrukcja mówiąca,
kiedy którego narzędzia użyć. Nazwy i środek funkcji bez zmian.

Pointa modułu: dla słabszego modelu liczy się każda warstwa - model, OPIS
narzędzia i instrukcja. Mocniejszy model wybacza złe opisy; słabszy nie - dlatego
diagnozujemy warstwę, zanim coś naprawimy.

Uruchom eval:
  uv run adk eval solutions/ex_16_modele_i_diagnostyka \\
      ex_16_modele_i_diagnostyka/diagnostyka.evalset.json \\
      --config_file_path ex_16_modele_i_diagnostyka/test_config.json
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_weak_model
from common.tools import db

from google.adk.agents import LlmAgent


def sales_by_artist(artist: str) -> int:
    """Zwraca liczbę sprzedanych utworów danego wykonawcy (suma ze wszystkich faktur).

    Użyj, gdy klient pyta, ILE utworów/sztuk danego wykonawcy sprzedano.

    Args:
        artist: Dokładna nazwa wykonawcy, np. "AC/DC".
    """
    return db.get_sold_count_for_artist(artist)


def albums_by_artist(artist: str) -> list[str]:
    """Zwraca tytuły albumów danego wykonawcy.

    Użyj, gdy klient pyta, JAKIE albumy nagrał dany wykonawca.

    Args:
        artist: Dokładna nazwa wykonawcy, np. "AC/DC".
    """
    return db.get_albums_for_artist(artist)


def sales_by_genre(genre: str) -> int:
    """Zwraca liczbę sprzedanych utworów danego gatunku muzycznego.

    Użyj, gdy klient pyta o sprzedaż w obrębie gatunku.

    Args:
        genre: Dokładna nazwa gatunku, np. "Rock".
    """
    return db.get_sold_count_for_genre(genre)


def list_genres() -> list[str]:
    """Zwraca listę wszystkich gatunków muzycznych dostępnych w sklepie."""
    return db.get_genres()


root_agent = LlmAgent(
    name="music_shop_agent",
    model=get_weak_model(),  # słaby model bez zmian - naprawiamy OPISY i instrukcję
    description="Agent sklepu muzycznego z poprawnymi opisami narzędzi - przechodzi eval.",
    instruction=(
        "Jesteś analitykiem sklepu muzycznego. Na pytania klientów odpowiadasz "
        "WYŁĄCZNIE na podstawie wyniku narzędzia, nigdy z pamięci. Dobierz narzędzie "
        "po jego opisie: liczba sprzedanych utworów wykonawcy -> sales_by_artist; "
        "albumy wykonawcy -> albums_by_artist; sprzedaż gatunku -> sales_by_genre; "
        "lista gatunków -> list_genres. Podaj zwięzłą odpowiedź po polsku opartą na "
        "liczbie/danych z wyniku."
    ),
    tools=[sales_by_artist, albums_by_artist, sales_by_genre, list_genres],
)
