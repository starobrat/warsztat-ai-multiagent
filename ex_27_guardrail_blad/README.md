# Ćwiczenie ex_27: guardrail na błąd narzędzia (on_tool_error)

## Co ćwiczymy
**Guardrail na błędy**: gdy narzędzie rzuci wyjątek, łapiemy go i oddajemy modelowi
czysty komunikat, zamiast pozwolić, by tura agenta się przerwała. `on_tool_error_callback`
dostaje `(tool, args, tool_context, error)` i jeśli zwróci `dict`, ADK użyje go jako
odpowiedzi narzędzia (graceful degradation - agent może spróbować ponownie).

Czwarty i ostatni guardrail. ex_24 akcja, ex_25 wejście, ex_26 wyjście, ex_27 błąd.
Razem: defense in depth na każdym etapie pracy agenta.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz ciało `handle_tool_error`. Zamień wyjątek
`error` w czytelny `dict` z kluczem `error`, żeby model dostał kontrolowany komunikat
zamiast crashu. Możesz dołożyć podpowiedź, by sprawdził schemat (`get_schema`).

Uwaga: agent woła `run_query_raw` (NIE łapie błędów w środku - dlatego wyjątek w
ogóle dociera do callbacku). Zwykłe `run_query` łapie błędy samo, więc nie nadaje
się do pokazania on_tool_error.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `error` to obiekt wyjątku (np. `sqlite3.OperationalError`). `str(error)` da treść.
- Zwróć `dict`, np. `{"error": "..."}`. Zwrócenie `None` = wyjątek leci dalej.

## Jak sprawdzić
```
uv run python solutions/_verify.py solutions/ex_27_guardrail_blad "Policz wiersze: SELECT TotallyWrongColumn FROM Customer"
```
(zła nazwa kolumny -> run_query_raw rzuci -> callback łapie -> agent dostaje błąd
i może poprawić zapytanie)

## "Działa", gdy
Błędne zapytanie NIE przerywa tury - w `ODPOWIEDZI NARZĘDZI` widać kontrolowany
`{"error": ...}`, a agent reaguje na komunikat (sprawdza schemat / poprawia SQL),
zamiast się zatrzymać na wyjątku.

## Pójdź dalej
- Zaloguj błąd (observability) zanim zwrócisz czysty komunikat modelowi.
- Dodaj limit prób, żeby agent nie kręcił się w kółko na tym samym błędzie.
- Co z błędami spoza SQL (timeout, brak pliku bazy)? Czy łapać wszystko jednakowo?

<!-- [TODO Piotr: narracja - moment "narzędzie wybucha, a agent musi to przeżyć"; analogia do try/except na granicy systemu, nie tłumienia błędów] -->
