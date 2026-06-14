"""Ćwiczenie 1 - wywołanie LLM i parametry (moduł 2).

Jedno wywołanie, jedna odpowiedź. Bez pętli, bez narzędzi.
Zadanie: napisz własny prompt i pytanie, uruchom raz, a potem pozmieniaj
temperaturę i uruchom ponownie - zobacz, jak zmienia się odpowiedź.

Uruchom: uv run ex_01_simple_call/starter.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402


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

    # TODO(you): napisz pytanie do modelu.
    user_prompt = ""

    # TODO(you): ustaw temperaturę (0.0 = zachowawczo, ~1.0 = kreatywnie).
    # Uruchom raz, potem zmień tę wartość i uruchom ponownie, żeby porównać.
    temperature = 0.0

    print(f"=== temperature={temperature} ===")
    print(ask(system_prompt, user_prompt, temperature))


if __name__ == "__main__":
    main()
