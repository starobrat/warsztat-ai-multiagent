"""DEMO (moduł 3): function calling napisany ręcznie - wersja kompletna.

To samo, co uczestnicy piszą w ex_02 - ale gotowe, do pokazania na żywo.
Kluczowa idea: model NIE wykonuje funkcji. Zwraca DECYZJĘ (JSON), a nasz kod ją
wykonuje. Na "ile to 17+25" model zleca add(17,25); na pytanie ogólne odpowiada sam.

Uruchom: uv run demo_02_function_calling/run.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402


def add(a: float, b: float) -> float:
    return a + b


TOOLS = {
    "add": {
        "fn": add,
        "description": "Dodaje dwie liczby. Argumenty: a (number), b (number).",
    },
}

SYSTEM = (
    "Masz do dyspozycji narzędzia:\n"
    + "\n".join(f"- {n}: {m['description']}" for n, m in TOOLS.items())
    + "\n\nOdpowiadasz WYŁĄCZNIE poprawnym JSON-em, bez komentarza:\n"
    '  {"tool": "<nazwa>", "args": {...}}      gdy potrzebujesz narzędzia\n'
    '  {"tool": null, "answer": "<odpowiedź>"} gdy odpowiadasz sam'
)


def run(pytanie: str) -> None:
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": pytanie},
        ],
    )
    decision = json.loads(resp.choices[0].message.content)
    print("PYTANIE:", pytanie)
    if decision.get("tool"):
        result = TOOLS[decision["tool"]]["fn"](**decision["args"])
        print(f"  model ZLECIŁ: {decision['tool']}({decision['args']})")
        print(f"  nasz KOD wykonał -> {result}\n")
    else:
        print(f"  model odpowiedział sam: {decision['answer']}\n")


if __name__ == "__main__":
    for p in ["Ile to 17 + 25?", "Jaka jest stolica Polski?"]:
        run(p)
