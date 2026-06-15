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


# --- Dedykowane narzędzia czytające konkret (bez pisania SQL przez agenta) ----
# Każde zwraca wąski, konkretny wynik. Agent je KOMPONUJE; SQL siedzi w środku.


def get_genres() -> list[str]:
    """Zwraca listę wszystkich gatunków muzycznych w bazie Chinook."""
    with _connect() as conn:
        rows = conn.execute("SELECT Name FROM Genre ORDER BY Name").fetchall()
    return [r["Name"] for r in rows]


def get_artists() -> list[str]:
    """Zwraca listę wszystkich wykonawców w bazie Chinook."""
    with _connect() as conn:
        rows = conn.execute("SELECT Name FROM Artist ORDER BY Name").fetchall()
    return [r["Name"] for r in rows]


def get_albums_for_artist(artist: str) -> list[str]:
    """Zwraca tytuły albumów danego wykonawcy.

    Args:
        artist: Dokładna nazwa wykonawcy (np. "AC/DC").

    Returns:
        Lista tytułów albumów. Pusta, jeśli wykonawca nie istnieje.
    """
    with _connect() as conn:
        rows = conn.execute(
            "SELECT al.Title FROM Album al "
            "JOIN Artist ar ON ar.ArtistId = al.ArtistId "
            "WHERE ar.Name = ? ORDER BY al.Title",
            (artist,),
        ).fetchall()
    return [r["Title"] for r in rows]


def get_sold_count_for_artist(artist: str) -> int:
    """Zwraca liczbę sprzedanych utworów danego wykonawcy (suma ze wszystkich faktur).

    Args:
        artist: Dokładna nazwa wykonawcy (np. "AC/DC").

    Returns:
        Liczba sprzedanych sztuk. 0, jeśli brak sprzedaży lub wykonawcy.
    """
    with _connect() as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(il.Quantity), 0) AS n FROM InvoiceLine il "
            "JOIN Track t ON t.TrackId = il.TrackId "
            "JOIN Album al ON al.AlbumId = t.AlbumId "
            "JOIN Artist ar ON ar.ArtistId = al.ArtistId "
            "WHERE ar.Name = ?",
            (artist,),
        ).fetchone()
    return int(row["n"])


def get_sold_count_for_genre(genre: str, year: int | None = None) -> int:
    """Zwraca liczbę sprzedanych utworów danego gatunku, opcjonalnie w danym roku.

    Args:
        genre: Dokładna nazwa gatunku (np. "Rock").
        year: Rok sprzedaży (np. 2025). Pominięty -> cała historia (2021-2025).

    Returns:
        Liczba sprzedanych sztuk. 0, jeśli brak sprzedaży lub gatunku.
    """
    sql = (
        "SELECT COALESCE(SUM(il.Quantity), 0) AS n FROM InvoiceLine il "
        "JOIN Track t ON t.TrackId = il.TrackId "
        "JOIN Genre g ON g.GenreId = t.GenreId "
    )
    params: tuple = (genre,)
    if year is not None:
        sql += "JOIN Invoice i ON i.InvoiceId = il.InvoiceId WHERE g.Name = ? AND strftime('%Y', i.InvoiceDate) = ?"
        params = (genre, str(year))
    else:
        sql += "WHERE g.Name = ?"
    with _connect() as conn:
        row = conn.execute(sql, params).fetchone()
    return int(row["n"])
