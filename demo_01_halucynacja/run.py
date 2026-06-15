"""DEMO (moduł 1): halucynacja na żywo.

Pytamy model o funkcję, która NIE istnieje. Model pewnym tonem zmyśli opis -
brzmi wiarygodnie, a jest wymyślone. To pokazuje, czemu nie można ślepo ufać LLM.

Uruchom: uv run demo_01_halucynacja/run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import MODEL, client  # noqa: E402

PYTANIE = (
    "Opisz dokładnie funkcję `chinook_quantum_join()` z biblioteki sqlite3 "
    "w Pythonie: jakie ma argumenty i co zwraca."
)


def main() -> None:
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.7,
        messages=[
            {"role": "system", "content": "Jesteś pomocnym ekspertem od Pythona."},
            {"role": "user", "content": PYTANIE},
        ],
    )
    print("PYTANIE:\n ", PYTANIE)
    print("\nODPOWIEDŹ MODELU (zmyślona, choć brzmi pewnie):\n")
    print(resp.choices[0].message.content)
    print("\n--- Taka funkcja nie istnieje. Model zmyślił pewnym tonem. ---")


if __name__ == "__main__":
    main()
