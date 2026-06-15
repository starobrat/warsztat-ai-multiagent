"""Ćwiczenie 2 - function calling napisany samodzielnie (moduł 3).

Kluczowa idea: LLM nie wykonuje akcji - DECYDUJE, co wykonać, a wywołuje to Twój kod.
Robimy to ręcznie: model zwraca JSON {"tool", "args"} albo {"tool": null, "answer"},
my go parsujemy i sami wołamy narzędzie.

Uruchom: uv run python solutions/ex_02_function_calling/solution.py
"""

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT))
# Rejestr narzędzi bierzemy z oryginalnego katalogu ćwiczenia (ten sam kod,
# który ma uczestnik) - bez duplikowania klocków w solutions/.
sys.path.insert(0, str(_ROOT / "ex_02_function_calling"))
from common.llm import MODEL, client  # noqa: E402

from tools import TOOLS  # noqa: E402


def build_system_prompt() -> str:
    tool_list = "\n".join(
        f"- {name}: {meta['description']}" for name, meta in TOOLS.items()
    )
    # Reguła: model zwraca WYŁĄCZNIE JSON z decyzją - albo narzędzie, albo odpowiedź.
    return (
        f"Masz do dyspozycji narzędzia:\n{tool_list}\n\n"
        "Odpowiadasz WYŁĄCZNIE poprawnym JSON-em, bez komentarza i bez tekstu wokół:\n"
        '  {"tool": "<nazwa>", "args": {...}}      gdy potrzebujesz narzędzia\n'
        '  {"tool": null, "answer": "<odpowiedź>"} gdy odpowiadasz sam'
    )


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
    # Model czasem owija JSON w ```...``` - oczyść string, zanim sparsujesz.
    cleaned = (
        raw.strip()
        .removeprefix("```json")
        .removeprefix("```")
        .removesuffix("```")
        .strip()
    )
    return json.loads(cleaned)


def run(user_prompt: str) -> None:
    print(f"\nUżytkownik: {user_prompt}")
    decision = call_model(user_prompt)

    tool_name = decision.get("tool")
    if tool_name is None:
        print(f"Model odpowiada sam: {decision.get('answer')}")
        return

    # Model tylko ZADECYDOWAŁ - to nasz kod faktycznie wywołuje narzędzie.
    if tool_name not in TOOLS:
        print(f"Model wskazał nieistniejące narzędzie: {tool_name!r}")
        return

    args = decision.get("args", {})
    result = TOOLS[tool_name]["fn"](**args)
    print(f"  model ZLECIŁ: {tool_name}({args})")
    print(f"  nasz KOD wykonał -> {result}")


def main() -> None:
    run("Ile to jest 17 plus 25?")
    run("Jaka jest cena utworu 'Smells Like Teen Spirit'?")
    run("Kim był Mozart?")  # tu model powinien odpowiedzieć sam, bez narzędzia


if __name__ == "__main__":
    main()
