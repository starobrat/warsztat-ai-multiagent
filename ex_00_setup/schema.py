"""Pokaż schemat bazy Chinook - zanim agent zacznie ją odpytywać (przed ćw. 03).

Chinook to przykładowa baza sklepu z muzyką: artyści, albumy, utwory, klienci,
faktury. Licencja MIT.

Uruchom: uv run python ex_00_setup/schema.py
"""

import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "data" / "chinook.sqlite"


def main() -> None:
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )]
    print(f"Baza Chinook (sklep z muzyką) - {len(tables)} tabel:\n")
    for t in tables:
        rows = conn.execute(f"SELECT COUNT(*) FROM '{t}'").fetchone()[0]
        cols = ", ".join(c[1] for c in conn.execute(f"PRAGMA table_info('{t}')"))
        print(f"  {t}  ({rows} wierszy)")
        print(f"      {cols}\n")
    print("Pełny schemat z typami zwraca narzędzie get_schema() (ćwiczenie 05).")


if __name__ == "__main__":
    main()
