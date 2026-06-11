"""Gotowe narzędzia bazodanowe do ćwiczenia 3.

Read-only dostęp do bazy Chinook. To są "klocki" - nie musisz ich dotykać,
masz złożyć z nich pętlę agentyczną w starter.py.
"""

import sqlite3
from pathlib import Path

# data/chinook.sqlite w korzeniu repo
DB_PATH = Path(__file__).resolve().parents[2] / "data" / "chinook.sqlite"

MAX_ROWS = 50


def _connect() -> sqlite3.Connection:
    # tryb read-only - agent nie zmodyfikuje bazy, nawet gdyby spróbował
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def get_schema() -> str:
    """Zwraca schemat bazy (nazwy tabel i kolumn)."""
    with _connect() as conn:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        lines = []
        for (table,) in (tuple(r) for r in rows):
            cols = conn.execute(f"PRAGMA table_info('{table}')").fetchall()
            col_desc = ", ".join(f"{c['name']} {c['type']}" for c in cols)
            lines.append(f"{table}({col_desc})")
        return "\n".join(lines)


def run_query(sql: str) -> str:
    """Wykonuje zapytanie SELECT i zwraca wynik jako tekst.

    Tylko SELECT - inne zapytania są odrzucane.
    """
    if not sql.strip().lower().startswith("select"):
        return "BŁĄD: dozwolone są tylko zapytania SELECT."
    try:
        with _connect() as conn:
            rows = conn.execute(sql).fetchall()
    except sqlite3.Error as exc:
        return f"BŁĄD SQL: {exc}"

    if not rows:
        return "Brak wyników."
    header = " | ".join(rows[0].keys())
    body = "\n".join(" | ".join(str(v) for v in tuple(r)) for r in rows[:MAX_ROWS])
    suffix = f"\n... (obcięto do {MAX_ROWS} wierszy)" if len(rows) > MAX_ROWS else ""
    return f"{header}\n{body}{suffix}"
