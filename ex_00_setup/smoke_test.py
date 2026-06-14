"""Smoke test setupu - moduł 1.

Cel: jeśli zobaczysz odpowiedź modelu, Twój setup działa i jesteś gotowy.

Uruchom:
    uv run ex_00_setup/smoke_test.py
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()


def main() -> int:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    if not api_key:
        print("BŁĄD: brak OPENAI_API_KEY.")
        print("Skopiuj .env.example do .env i wklej klucz z https://platform.openai.com/api-keys")
        return 1

    try:
        from openai import OpenAI
    except ImportError:
        print("BŁĄD: brak pakietu 'openai'. Uruchom: uv sync")
        return 1

    client = OpenAI(api_key=api_key)

    print(f"Pytam model '{model}' przez OpenAI...\n")
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": "Przywitaj się jednym krótkim zdaniem i potwierdź, że jesteś gotowy do pracy."}
        ],
    )
    print("Odpowiedź modelu:")
    print(" ", response.choices[0].message.content)
    print("\nSetup działa. Jesteś gotowy na szkolenie.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
