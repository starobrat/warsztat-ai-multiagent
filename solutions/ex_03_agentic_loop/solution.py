"""Rozwiązanie ćwiczenia 3 - pętla agentyczna."""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "ex_03_agentic_loop"))
sys.path.insert(0, str(REPO))
from common.llm import MODEL, client  # noqa: E402
from db_tools import get_schema, run_query  # noqa: E402

TOOLS = {"get_schema": get_schema, "run_query": run_query}

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
    response = client.chat.completions.create(
        model=MODEL, temperature=0, response_format={"type": "json_object"}, messages=messages
    )
    raw = response.choices[0].message.content
    cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    # Pierwszy obiekt JSON = jedna akcja na turę (model bywa zachłanny i wypluwa
    # od razu całą trajektorię; raw_decode ignoruje to, co po pierwszym obiekcie).
    decision, _ = json.JSONDecoder().raw_decode(cleaned)
    return decision


def run_agent(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    for _ in range(MAX_STEPS):
        decision = agent_step(messages)

        if decision.get("tool") is None:
            return decision.get("answer", "(brak odpowiedzi)")

        tool_name = decision["tool"]
        args = decision.get("args", {})
        if tool_name not in TOOLS:
            return f"Model wskazał nieistniejące narzędzie: {tool_name}"

        result = TOOLS[tool_name](**args)
        print(f"  -> {tool_name}({args})")
        # dokładamy decyzję modelu i wynik narzędzia do historii
        messages.append({"role": "assistant", "content": json.dumps(decision, ensure_ascii=False)})
        messages.append({"role": "user", "content": f"Wynik narzędzia {tool_name}:\n{result}"})

    return "Przekroczono limit kroków agenta."


def main() -> None:
    for question in (
        "Ilu mamy klientów z Niemiec?",
        "Podaj 5 gatunków z największą liczbą utworów.",
    ):
        print(f"\n### Pytanie: {question}")
        print(run_agent(question))


if __name__ == "__main__":
    main()
