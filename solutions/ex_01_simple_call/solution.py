"""ROZWIĄZANIE ćwiczenia 1 - wywołanie LLM i parametry (moduł 2).

Jedno wywołanie, jedna odpowiedź. Bez pętli, bez narzędzi.
W starterze TODO to: rola (system prompt), pytanie i temperatura. Tu pokazujemy
TĘ SAMĄ prośbę przy temperaturze 0.0 i 1.0 w jednym uruchomieniu, żeby od razu
było widać różnicę (to jest kryterium "Działa, gdy" z README).

Uruchom: uv run python solutions/ex_01_simple_call/solution.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
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
    # Rola (system prompt): analityk sprzedaży sklepu z muzyką, zwięźle, po polsku.
    system_prompt = (
        "Jesteś analitykiem sprzedaży w sklepie z muzyką. "
        "Odpowiadasz po polsku, zwięźle i konkretnie."
    )

    # Pytanie celowo "kreatywne" - przy wyższej temperaturze odpowiedzi się rozjadą.
    user_prompt = "Zaproponuj trzy pomysły na promocję, która zwiększy sprzedaż gatunku Rock."

    # Ta sama prośba przy dwóch temperaturach - widać wpływ parametru.
    # (W starterze robisz to przez dwa osobne uruchomienia; tu dla wygody w jednym.)
    for temperature in (0.0, 1.0):
        print(f"\n=== temperature={temperature} ===")
        print(ask(system_prompt, user_prompt, temperature))


if __name__ == "__main__":
    main()
