"""Ćwiczenie ex_16: modele i diagnostyka - moduł 8.

Agent sklepu muzycznego ma KILKA narzędzi, ale ich OPISY (docstringi) wprowadzają
w błąd - słabszy model wybiera złe narzędzie i OBLEWA eval (czerwony). Znasz test
(diagnostyka.evalset.json) i wiesz, czego oczekuje. Twoje zadanie: zdiagnozować,
GDZIE jest problem (model / docstring / instrukcja) i zazielenić test.

Chodzi celowo na słabszym modelu (get_weak_model): mocny zamaskowałby złe opisy,
bo i tak trafi w intencję. Słabszy słucha docstringów dosłownie - dlatego opis
narzędzia naprawdę ma znaczenie. Pełny opis i komendy: README tego katalogu.

Uruchom eval:
  uv run adk eval ex_16_modele_i_diagnostyka \\
      ex_16_modele_i_diagnostyka/diagnostyka.evalset.json \\
      --config_file_path ex_16_modele_i_diagnostyka/test_config.json
"""

from common.model import get_weak_model
from common.tools import db

from google.adk.agents import LlmAgent


# --- Narzędzia z CELOWO mylącymi opisami (docstring = kontrakt dla LLM) --------
# TODO(you): NIE zmieniaj nazw funkcji ani ich środka. Popraw OPISY (docstringi),
# żeby model trafnie wybierał narzędzie. (Możesz też dopracować instruction niżej
# i poeksperymentować z modelem - patrz README.)


def sales_by_artist(artist: str) -> int:
    """Zwraca albumy wykonawcy."""  # opis kłamie: to jest SPRZEDAŻ, nie albumy
    return db.get_sold_count_for_artist(artist)


def albums_by_artist(artist: str) -> list[str]:
    """Liczy, ile sztuk sprzedano."""  # opis kłamie: to są ALBUMY, nie sprzedaż
    return db.get_albums_for_artist(artist)


def sales_by_genre(genre: str) -> int:
    """Coś o gatunku."""  # opis za ogólny - nie wiadomo, co zwraca ani po co
    return db.get_sold_count_for_genre(genre)


def list_genres() -> list[str]:
    """Lista."""  # opis bezużyteczny
    return db.get_genres()


root_agent = LlmAgent(
    name="music_shop_agent",
    model=get_weak_model(),
    description="Agent sklepu muzycznego z mylącymi opisami narzędzi - do diagnozy w module 8.",
    # Instrukcja laika: ogólnik, nie mówi, kiedy którego narzędzia użyć.
    instruction="Jesteś miłym sprzedawcą w sklepie muzycznym. Pomóż klientowi.",
    tools=[sales_by_artist, albums_by_artist, sales_by_genre, list_genres],
)
