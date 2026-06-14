"""Rozwiązanie ćwiczenia 1 - wywołanie LLM i parametry."""

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
    system_prompt = (
        "Jesteś analitykiem sprzedaży w sklepie z muzyką. "
        "Odpowiadasz zwięźle i konkretnie, po polsku."
    )
    user_prompt = "Wymień 3 metryki, które warto śledzić w sklepie z muzyką."
    temperature = 0.0

    print(f"=== temperature={temperature} ===")
    print(ask(system_prompt, user_prompt, temperature))


if __name__ == "__main__":
    main()
