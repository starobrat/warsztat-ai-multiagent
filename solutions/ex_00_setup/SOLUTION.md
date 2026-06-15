# Rozwiązanie: ex_00_setup

To ćwiczenie nie ma `# TODO(you)` - to smoke test setupu. "Rozwiązaniem" jest po
prostu poprawnie skonfigurowane środowisko.

## Jak uruchomić
```bash
uv sync
cp .env.example .env        # wklej OPENAI_API_KEY
uv run python ex_00_setup/smoke_test.py
```

## Sukces (potwierdzony)
Skrypt wypisuje odpowiedź modelu, np.:
```
Odpowiedź modelu:
  Cześć, jestem gotowy do pracy.
Setup działa. Jesteś gotowy na szkolenie.
```
`ex_00_setup/schema.py` dodatkowo wypisuje schemat bazy Chinook (11 tabel).

## Friction
Brak. Wymaga tylko kroków z README (uv sync, klucz w .env).
