"""Ćwiczenie 2 - function calling napisany samodzielnie (moduł 3).

Kluczowa idea: LLM nie wykonuje akcji - DECYDUJE, co wykonać, a wywołuje to Twój kod.
Robimy to ręcznie: model zwraca JSON {"tool", "args"} albo {"tool": null, "answer"},
my go parsujemy i sami wołamy narzędzie.

Uruchom: uv run 02_function_calling/starter.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402

from tools import TOOLS  # noqa: E402


def build_system_prompt() -> str:
    tool_list = "\n".join(
        f"- {name}: {meta['description']}" for name, meta in TOOLS.items()
    )
    # TODO(you): dopisz do promptu zasadę, że model odpowiada WYŁĄCZNIE JSON-em:
    #   {"tool": "<nazwa>", "args": {...}}      -> gdy potrzebuje narzędzia
    #   {"tool": null, "answer": "<odpowiedź>"} -> gdy odpowiada sam
    return f"Masz do dyspozycji narzędzia:\n{tool_list}\n"


def call_model(user_prompt: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_prompt},
        ],
    )
    raw = response.choices[0].message.content
    # TODO(you): sparsuj `raw` na dict przez json.loads.
    # Wskazówka: model czasem owija JSON w ```...``` - oczyść string przed parsowaniem.
    raise NotImplementedError("Sparsuj odpowiedź modelu na dict")


def run(user_prompt: str) -> None:
    print(f"\nUżytkownik: {user_prompt}")
    decision = call_model(user_prompt)

    tool_name = decision.get("tool")
    if tool_name is None:
        print(f"Model odpowiada sam: {decision.get('answer')}")
        return

    # TODO(you): wywołaj wskazane narzędzie z TOOLS z argumentami decision["args"]
    # i wypisz wynik. Obsłuż przypadek, gdy model wskaże nieistniejące narzędzie.
    raise NotImplementedError("Wywołaj narzędzie wskazane przez model")


def main() -> None:
    run("Ile to jest 17 plus 25?")
    run("Jaka jest cena utworu 'Smells Like Teen Spirit'?")
    run("Kim był Mozart?")  # tu model powinien odpowiedzieć sam, bez narzędzia


if __name__ == "__main__":
    main()
