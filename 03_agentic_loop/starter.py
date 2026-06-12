"""Ćwiczenie 3 - pętla agentyczna (moduł 4). KONIEC części 1.

Składasz wszystko z modułów 2-3 w jedno: AGENTA.

Różnica, którą tu zobaczysz na własnej skórze:
  - wywołanie LLM      = jeden krok, jedna odpowiedź
  - pipeline           = z góry ustalona sekwencja kroków
  - agent (pętla)      = LLM SAM decyduje, ile kroków i jakich narzędzi użyć,
                         aż uzna, że ma odpowiedź

Agent odpowiada na pytania o bazę Chinook (sklep z muzyką). Ma dwa narzędzia:
get_schema() i run_query(sql). Twoim zadaniem jest napisać pętlę.

Uruchom:
    uv run 03_agentic_loop/starter.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402

from db_tools import get_schema, run_query  # noqa: E402

TOOLS = {
    "get_schema": get_schema,
    "run_query": run_query,
}

SYSTEM_PROMPT = """Jesteś agentem analitycznym sklepu z muzyką (baza Chinook, SQLite).
Masz narzędzia:
- get_schema: zwraca schemat bazy (bez argumentów)
- run_query: wykonuje zapytanie SELECT (argument: sql)

W każdej turze odpowiadasz WYŁĄCZNIE JSON-em w jednym z formatów:
  {"tool": "get_schema", "args": {}}
  {"tool": "run_query", "args": {"sql": "SELECT ..."}}
  {"tool": null, "answer": "<finalna odpowiedź po polsku>"}

Najpierw sprawdź schemat, dopiero potem pisz zapytania. Nie zgaduj nazw tabel."""

MAX_STEPS = 8


def agent_step(messages: list[dict]) -> dict:
    """Jedno wywołanie LLM -> decyzja (dict)."""
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=messages,
    )
    raw = response.choices[0].message.content
    return json.loads(raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```"))


def run_agent(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    # TODO(you): napisz pętlę agentyczną.
    # Powtarzaj maksymalnie MAX_STEPS razy:
    #   1. decision = agent_step(messages)
    #   2. jeśli decision["tool"] is None -> zwróć decision["answer"]
    #   3. w przeciwnym razie: wywołaj narzędzie TOOLS[decision["tool"]] z args,
    #      dołóż wynik do messages (jako rola "user" lub "assistant"+"user")
    #      i kontynuuj pętlę.
    # Pamiętaj o bezpieczniku: po MAX_STEPS przerwij i zwróć komunikat.
    raise NotImplementedError("Napisz pętlę agentyczną")


def main() -> None:
    for question in (
        "Ilu mamy klientów z Niemiec?",
        "Podaj 5 gatunków z największą liczbą utworów.",
    ):
        print(f"\n### Pytanie: {question}")
        print(run_agent(question))


if __name__ == "__main__":
    main()
