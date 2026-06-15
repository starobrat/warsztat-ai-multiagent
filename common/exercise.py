"""Wspólne klocki dydaktyczne ćwiczeń.

Stan "niezaimplementowane" ma PROWADZIĆ: zamiast gołego traceback uczestnik
dostaje wskazówkę, co zrobić i gdzie szukać.

- `todo(...)`        - dla ćwiczeń-skryptów (Python): w miejscu `# TODO(you)`.
- `placeholder(...)` - dla ćwiczeń-agentów (adk web): instrukcja-zaślepka.
"""

from __future__ import annotations


class TodoError(NotImplementedError):
    """Ćwiczenie niezrobione - czytelny komunikat zamiast gołego traceback."""


def todo(co: str, gdzie: str = "README.md w tym katalogu") -> None:
    """Zatrzymuje ćwiczenie-skrypt z czytelną wskazówką, co zaimplementować.

    Użyj zamiast `raise NotImplementedError(...)` tam, gdzie jest `# TODO(you)`.

    Args:
        co: jedno zdanie - co uczestnik ma zaimplementować.
        gdzie: gdzie szukać kontekstu (np. "krok 2 w README").
    """
    raise TodoError(
        "\n\n"
        "  TO ĆWICZENIE CZEKA NA CIEBIE.\n"
        f"  Do zrobienia: {co}\n"
        f"  Szczegóły: {gdzie}\n"
    )


def placeholder(zadanie: str, readme: str = "README w tym katalogu") -> str:
    """Instrukcja-zaślepka dla ćwiczeń-agentów (adk web).

    Niezaimplementowany agent na KAŻDE pytanie odpowiada wskazówką, co trzeba
    zrobić, zamiast udawać, że działa. Uczestnik podmienia ją na właściwą
    instrukcję w ramach ćwiczenia.

    Args:
        zadanie: co uczestnik ma zrobić w tym ćwiczeniu.
        readme: gdzie szukać szczegółów.
    """
    return (
        "Bez względu na pytanie użytkownika odpowiedz DOKŁADNIE tym i niczym więcej:\n"
        f'"To ćwiczenie nie jest jeszcze gotowe. Twoje zadanie: {zadanie}. '
        f'Szczegóły: {readme}."'
    )
