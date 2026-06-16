"""DEMO (moduł 14): co się dzieje, gdy narzędzie ma dostęp WRITE do bazy.

CELOWO niebezpieczny agent: dostaje narzędzie wykonujące DOWOLNY SQL na bazie w
trybie ZAPISU (nie read-only jak w reszcie szkolenia). Pokaz: prosisz (albo
prompt-injection prosi) "usuń tabelę Genre" -> tabela faktycznie znika.

Przywrócenie bazy po pokazie (baza jest w repo):
    git checkout data/chinook.sqlite

Pointa: to NIE jest tak, że dajemy agentowi write-SQL i już. Bez least privilege
i guardraili (moduł 14) jedna komenda kasuje dane. Dlatego w reszcie szkolenia
baza jest read-only.

Uruchom: uv run adk web demo_14_write   (a po pokazie: git checkout data/chinook.sqlite)
"""

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.model import get_model  # noqa: E402
from common.tools.db import DB_PATH  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


def wykonaj_sql(sql: str) -> dict:
    """Wykonuje DOWOLNE zapytanie SQL na bazie Chinook w trybie ZAPISU.

    UWAGA: to narzędzie demonstracyjne - świadomie BEZ zabezpieczeń. Wykonuje
    też INSERT/UPDATE/DELETE/DROP. Bazę przywracasz z repo: git checkout data/chinook.sqlite.

    Args:
        sql: Dowolne zapytanie SQL do wykonania.

    Returns:
        Słownik z wynikiem (wiersze dla SELECT, liczba zmienionych wierszy dla zapisu)
        albo 'error' przy błędzie.
    """
    try:
        conn = sqlite3.connect(DB_PATH)  # zapis (BEZ mode=ro - to jest cały problem)
        try:
            cur = conn.execute(sql)
            conn.commit()
            if cur.description:  # SELECT
                rows = [list(r) for r in cur.fetchall()[:50]]
                return {"columns": [c[0] for c in cur.description], "rows": rows}
            return {"ok": True, "rowcount": cur.rowcount, "sql": sql}
        finally:
            conn.close()
    except sqlite3.Error as exc:
        return {"error": f"Błąd SQL: {exc}"}


root_agent = LlmAgent(
    name="agent_write_danger",
    model=get_model(),
    description="CELOWO niebezpieczny agent z dostępem WRITE do bazy (demo modułu 14).",
    instruction=(
        "Jesteś agentem z dostępem do bazy Chinook przez narzędzie wykonaj_sql. "
        "Wykonujesz polecenia użytkownika dotyczące danych - również modyfikujące. "
        "Odpowiadasz po polsku i pokazujesz wykonane zapytanie."
    ),
    tools=[wykonaj_sql],
)
