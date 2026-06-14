# Bonus B4: Trwałe sesje

## Zadanie
Domyślnie sesje ADK żyją w pamięci i znikają po restarcie. Włącz trwałe sesje
w SQLite, żeby rozmowa przeżyła restart serwera.

## Kroki
```bash
uv run adk web ex_05_sql_agent --session_service_uri "sqlite:///sessions.db"
```
1. Porozmawiaj z agentem, podaj mu jakąś informację.
2. Zatrzymaj serwer (Ctrl+C) i uruchom ponownie z tym samym `--session_service_uri`.
3. Sprawdź, czy wcześniejsza rozmowa jest dostępna.

## Czego się uczysz
Różnica sesja-w-pamięci vs sesja-trwała i jak ADK zarządza stanem rozmowy.
