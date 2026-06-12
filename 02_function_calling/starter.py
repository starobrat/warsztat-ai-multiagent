"""Ćwiczenie 2 - function calling napisany samodzielnie (moduł 3).

Najważniejsza idea całego szkolenia:
    LLM NIE wykonuje akcji. LLM DECYDUJE, co wykonać. Wykonuje Twój kod.

Tu symulujemy function calling ręcznie - bez gotowego mechanizmu z SDK -
żeby zobaczyć, jak to naprawdę działa pod spodem.

Plan:
  1. Prosimy model, żeby ZAMIAST odpowiadać tekstem, zwrócił JSON:
     {"tool": "<nazwa>", "args": {...}}  albo  {"tool": null, "answer": "..."}
  2. Parsujemy JSON.
  3. Jeśli model wskazał narzędzie - MY je wywołujemy i pokazujemy wynik.

Uruchom:
    uv run 02_function_calling/starter.py
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
    # TODO(you): dokończ prompt systemowy. Model MA zwracać wyłącznie JSON:
    #   {"tool": "<nazwa>", "args": {...}}        -> gdy potrzebuje narzędzia
    #   {"tool": null, "answer": "<odpowiedź>"}   -> gdy umie odpowiedzieć sam
    return f"""Masz do dyspozycji narzędzia:
{tool_list}

# TODO(you): dopisz instrukcję, że model odpowiada WYŁĄCZNIE JSON-em
# w jednym z dwóch formatów powyżej.
"""


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
    # TODO(you): sparsuj JSON z odpowiedzi modelu i zwróć jako dict.
    # Uwaga: model bywa kapryśny i czasem owija JSON w ```...```. Pomyśl o tym.
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
