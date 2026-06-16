"""ROZWIĄZANIE ćwiczenia 1 - wywołanie LLM i parametry (moduł 2).

Jedno wywołanie, jedna odpowiedź. Bez pętli, bez narzędzi.
W starterze TODO to: rola (system prompt), pytanie i temperatura. Tu pokazujemy
TĘ SAMĄ prośbę (krótki wiersz o tym szkoleniu) przy temperaturze 0.2 i 0.8 w
jednym uruchomieniu, żeby od razu było widać różnicę - tak jak na slajdzie i w
README (to jest kryterium "Działa, gdy").

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
    # Rola (system prompt): poeta-asystent, zwięźle, po polsku.
    system_prompt = (
        "Jesteś asystentem, który pisze krótkie, zgrabne wiersze po polsku."
    )

    # Pytanie celowo "kreatywne" - przy wyższej temperaturze odpowiedzi się rozjadą.
    user_prompt = (
        "Napisz krótki wiersz o tym szkoleniu - o budowaniu aplikacji "
        "wieloagentowych w Google ADK."
    )

    # Ta sama prośba przy dwóch temperaturach - widać wpływ parametru.
    # (W starterze robisz to przez dwa osobne uruchomienia; tu dla wygody w jednym.)
    for temperature in (0.2, 0.8):
        print(f"\n=== temperature={temperature} ===")
        print(ask(system_prompt, user_prompt, temperature))


if __name__ == "__main__":
    main()
