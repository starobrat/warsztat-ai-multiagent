"""Rozwiązanie ćwiczenia 2 - function calling napisany samodzielnie."""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "02_function_calling"))
sys.path.insert(0, str(REPO))
from common.llm import MODEL, client  # noqa: E402
from tools import TOOLS  # noqa: E402


def build_system_prompt() -> str:
    tool_list = "\n".join(
        f"- {name}: {meta['description']}" for name, meta in TOOLS.items()
    )
    return f"""Masz do dyspozycji narzędzia:
{tool_list}

Odpowiadasz WYŁĄCZNIE JSON-em, w jednym z dwóch formatów:
  {{"tool": "<nazwa>", "args": {{...}}}}      - gdy potrzebujesz narzędzia
  {{"tool": null, "answer": "<odpowiedź>"}}  - gdy umiesz odpowiedzieć sam
Nie dodawaj nic poza JSON-em."""


def _parse(raw: str) -> dict:
    cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(cleaned)


def call_model(user_prompt: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_prompt},
        ],
    )
    return _parse(response.choices[0].message.content)


def run(user_prompt: str) -> None:
    print(f"\nUżytkownik: {user_prompt}")
    decision = call_model(user_prompt)

    tool_name = decision.get("tool")
    if tool_name is None:
        print(f"Model odpowiada sam: {decision.get('answer')}")
        return

    if tool_name not in TOOLS:
        print(f"Model wskazał nieistniejące narzędzie: {tool_name}")
        return

    result = TOOLS[tool_name]["fn"](**decision.get("args", {}))
    print(f"Wywołano {tool_name}({decision.get('args', {})}) -> {result}")


def main() -> None:
    run("Ile to jest 17 plus 25?")
    run("Jaka jest cena utworu 'Smells Like Teen Spirit'?")
    run("Kim był Mozart?")


if __name__ == "__main__":
    main()
