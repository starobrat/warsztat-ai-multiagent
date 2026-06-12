"""Klocek: dostęp do bazy Chinook (read-only).

Te funkcje są gotowymi NARZĘDZIAMI dla agenta ADK - mają docstringi i type
hinty, więc ADK zrobi z nich FunctionTool automatycznie. Składasz z nich agenta,
nie dotykasz ich środka.
"""

import sqlite3
from pathlib import Path

# data/chinook.sqlite w korzeniu repo
DB_PATH = Path(__file__).resolve().parents[2] / "data" / "chinook.sqlite"

MAX_ROWS = 50


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def get_schema() -> dict:
    """Zwraca schemat bazy Chinook: tabele i ich kolumny.

    Wywołaj to ZANIM napiszesz zapytanie SQL, żeby poznać nazwy tabel i kolumn.

    Returns:
        Słownik {nazwa_tabeli: ["kolumna typ", ...]}.
    """
    with _connect() as conn:
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        schema: dict[str, list[str]] = {}
        for (table,) in (tuple(r) for r in tables):
            cols = conn.execute(f"PRAGMA table_info('{table}')").fetchall()
            schema[table] = [f"{c['name']} {c['type']}" for c in cols]
    return schema


def run_query(sql: str) -> dict:
    """Wykonuje zapytanie SELECT na bazie Chinook i zwraca wynik.

    Dozwolone są wyłącznie zapytania SELECT (baza jest tylko do odczytu).

    Args:
        sql: Zapytanie SELECT do wykonania.

    Returns:
        Słownik z kluczami 'columns', 'rows' i 'row_count', albo 'error' przy błędzie.
    """
    if not sql.strip().lower().startswith("select"):
        return {"error": "Dozwolone są tylko zapytania SELECT."}
    try:
        with _connect() as conn:
            result = conn.execute(sql).fetchall()
    except sqlite3.Error as exc:
        return {"error": f"Błąd SQL: {exc}"}

    rows = [list(tuple(r)) for r in result[:MAX_ROWS]]
    columns = list(result[0].keys()) if result else []
    return {
        "columns": columns,
        "rows": rows,
        "row_count": len(result),
        "truncated": len(result) > MAX_ROWS,
    }
