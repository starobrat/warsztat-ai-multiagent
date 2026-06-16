"""Ćwiczenie 3 - pętla agentyczna (moduł 4). Koniec części 1.

Łączysz moduły 2-3 w agenta: w pętli LLM SAM decyduje, ile kroków i jakich narzędzi
użyć, aż ma odpowiedź (inaczej niż pojedyncze wywołanie czy sztywny pipeline).
Agent odpowiada na pytania o bazę Chinook; ma get_schema() i run_query(). Napisz pętlę.

Uruchom: uv run python solutions/ex_03_agentic_loop/solution.py
"""

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT))
# Narzędzia bazodanowe bierzemy z oryginalnego katalogu ćwiczenia (ten sam kod,
# który ma uczestnik) - bez duplikowania klocków w solutions/.
sys.path.insert(0, str(_ROOT / "ex_03_agentic_loop"))
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

Wykonujesz JEDEN krok na turę. Odpowiadasz WYŁĄCZNIE jednym obiektem JSON
w jednym z formatów (nic przed ani po obiekcie):
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
        response_format={"type": "json_object"},
        messages=messages,
    )
    raw = response.choices[0].message.content
    cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    # Bierzemy PIERWSZY obiekt JSON (jedna akcja na turę). Niektóre modele lubią
    # od razu wypluć całą trajektorię - raw_decode ignoruje to, co po pierwszym.
    decision, _ = json.JSONDecoder().raw_decode(cleaned)
    return decision


def run_agent(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    # Pętla agentyczna: model SAM decyduje o kolejnym kroku, aż zwróci tool=null.
    for _ in range(MAX_STEPS):
        decision = agent_step(messages)

        # Decyzja modelu wraca do historii (rola assistant) - inaczej model jej "nie pamięta".
        messages.append({"role": "assistant", "content": json.dumps(decision, ensure_ascii=False)})

        if decision.get("tool") is None:
            return decision.get("answer", "(brak odpowiedzi)")

        tool_name = decision["tool"]
        if tool_name not in TOOLS:
            messages.append({"role": "user", "content": f"BŁĄD: nie ma narzędzia {tool_name!r}."})
            continue

        result = TOOLS[tool_name](**decision.get("args", {}))
        # Wynik narzędzia wraca do modelu jako kolejna wiadomość - to "obserwacja".
        messages.append({"role": "user", "content": f"Wynik {tool_name}:\n{result}"})

    # Bezpiecznik: agent nie domknął zadania w limicie kroków.
    return f"Przekroczono limit {MAX_STEPS} kroków bez finalnej odpowiedzi."


def main() -> None:
    for question in (
        "Ilu mamy klientów z Niemiec?",
        "Podaj 5 gatunków z największą liczbą utworów.",
    ):
        print(f"\n### Pytanie: {question}")
        print(run_agent(question))


if __name__ == "__main__":
    main()
