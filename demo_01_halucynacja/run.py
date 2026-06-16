"""DEMO (moduł 1): halucynacja na żywo.

Pytamy model o rzeczy, do których NIE ma dostępu albo które są po jego punkcie
odcięcia (cut-off). Część model pewnie ZMYŚLI, część UCZCIWIE ODMÓWI - i to też
jest lekcja: czasem zna swoje granice, czasem nie, a brzmi tak samo pewnie.

Uruchom: uv run demo_01_halucynacja/run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402

PYTANIA = [
    "Kim jest Piotr Starobrat?",
    "Która jest teraz godzina?",
    "Jaki jest najnowszy model z rodziny Anthropic Claude?",
    "Jaka jest w tej chwili pogoda w Poznaniu?",
]


def zapytaj(pytanie: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.7,
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem. Odpowiadaj po polsku."},
            {"role": "user", "content": pytanie},
        ],
    )
    return resp.choices[0].message.content


def main() -> None:
    for pytanie in PYTANIA:
        print("=" * 70)
        print("PYTANIE:", pytanie)
        print("-" * 70)
        print(zapytaj(pytanie))
        print()
    print("=" * 70)
    print("Zwróć uwagę: część odpowiedzi to pewna siebie ZMYŚLONA treść,")
    print("a część - uczciwe 'nie mam dostępu'. Model nie zawsze zna swoje granice.")


if __name__ == "__main__":
    main()
