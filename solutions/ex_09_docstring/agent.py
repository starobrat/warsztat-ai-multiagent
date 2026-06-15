"""ROZWIĄZANIE ćwiczenia ex_10: docstring narzędzia - moduł 6.

Docstring to KONTRAKT, który czyta model, żeby zdecydować, KIEDY wywołać
narzędzie. `get_genres` dostaje opisowy docstring, a agent - instrukcję
grounding. Sprawdź w Traces, czy model trafnie sięga po narzędzia.

Uruchom: uv run adk web solutions/ex_09_docstring
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema
from common.tools.db import get_genres as _dane_gatunkow

from google.adk.agents import LlmAgent


def get_genres() -> list[str]:
    """Zwraca listę nazw gatunków muzycznych dostępnych w sklepie Chinook.

    Wywołaj to narzędzie, gdy użytkownik pyta o gatunki muzyczne - jakie
    gatunki są w ofercie lub jaką muzykę można znaleźć w sklepie.
    """
    return _dane_gatunkow()


root_agent = LlmAgent(
    name="analityk_chinook",
    model=get_model(),
    description="Agent o danych Chinook (struktura + gatunki).",
    instruction=(
        "Jesteś analitykiem danych sklepu muzycznego Chinook. Odpowiadaj po "
        "polsku, krótko i rzeczowo. Korzystaj WYŁĄCZNIE z danych zwróconych "
        "przez narzędzia: użyj `get_genres`, gdy ktoś pyta o gatunki muzyczne, "
        "a `get_schema`, gdy pyta o strukturę bazy. Nie zmyślaj - jeśli "
        "narzędzia nie zwracają odpowiedzi, powiedz, że nie masz tych danych."
    ),
    tools=[get_schema, get_genres],
)
