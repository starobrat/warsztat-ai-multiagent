"""Ćwiczenie 1 - wywołanie LLM i parametry (moduł 2).

Typ 1 aplikacji: proces biznesowy z JEDNYM krokiem LLM.
Tu nie ma jeszcze żadnej pętli ani narzędzi - po prostu pytamy i dostajemy odpowiedź.

Cel:
  1. Napisz własny prompt systemowy, który nada modelowi rolę.
  2. Zobacz na żywo, jak temperature zmienia odpowiedź.

Uruchom:
    uv run part1_loop/01_simple_call/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from llm import MODEL, client  # noqa: E402


def ask(system_prompt: str, user_prompt: str, temperature: float) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


def main() -> None:
    # TODO(you): napisz prompt systemowy nadający modelowi rolę
    # (np. "Jesteś analitykiem sprzedaży sklepu muzycznego...").
    system_prompt = ""

    user_prompt = "Wymień 3 metryki, które warto śledzić w sklepie z muzyką."

    # TODO(you): uruchom to samo pytanie z różnymi temperaturami i porównaj.
    for temperature in (0.0, 1.0):
        print(f"\n=== temperature={temperature} ===")
        print(ask(system_prompt, user_prompt, temperature))


if __name__ == "__main__":
    main()
