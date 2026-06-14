"""Gotowe narzędzia do ćwiczenia 2.

Dwie proste funkcje. W ćwiczeniu LLM ma ZDECYDOWAĆ, którą wywołać i z jakimi
argumentami - ale wywołanie wykonuje Twój kod, nie model.
"""


def add(a: float, b: float) -> float:
    """Dodaje dwie liczby."""
    return a + b


def get_price(track_name: str) -> float:
    """Zwraca cenę utworu (uproszczone - w sklepie wszystko po tej samej cenie)."""
    return 0.99


# Rejestr narzędzi: nazwa -> (funkcja, opis dla modelu).
TOOLS = {
    "add": {
        "fn": add,
        "description": "Dodaje dwie liczby. Argumenty: a (number), b (number).",
    },
    "get_price": {
        "fn": get_price,
        "description": "Zwraca cenę utworu. Argumenty: track_name (string).",
    },
}
