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

Uwaga: w tym ćwiczeniu `run_query_raw` jest celowo podrasowane - na KAŻDE zapytanie
odpala błędny SELECT (realny `sqlite3.OperationalError`), żeby guardrail odpalał się
za każdym razem (nie zależymy od tego, czy model sam popełni błąd). To jedyne
narzędzie zapytań - bezpieczne `run_query` usunęliśmy, żeby model nie miał drogi
ucieczki. `run_query_raw` NIE łapie błędu w środku, dlatego wyjątek dociera do
callbacku.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `error` to obiekt wyjątku (np. `sqlite3.OperationalError`). `str(error)` da treść.
- Zwróć `dict`, np. `{"error": "..."}`. Zwrócenie `None` = wyjątek leci dalej.

## Jak sprawdzić
```
uv run adk web ex_27_guardrail_blad
```
Zadaj DOWOLNE pytanie - narzędzie zawsze rzuci błąd. Bez guardrailu (starter)
tura się przerywa; po napisaniu `handle_tool_error` agent dostaje czysty `{"error": ...}`
i przekazuje użytkownikowi czytelny komunikat.

## "Działa", gdy
Błąd narzędzia (a tu pada na KAŻDE zapytanie) NIE przerywa tury - w `ODPOWIEDZI
NARZĘDZI` widać kontrolowany `{"error": ...}`, a agent przekazuje użytkownikowi
czytelną informację o błędzie zamiast się zatrzymać na wyjątku.

## Pójdź dalej
- Zaloguj błąd (observability) zanim zwrócisz czysty komunikat modelowi.
- Dodaj limit prób, żeby agent nie kręcił się w kółko na tym samym błędzie.
- Co z błędami spoza SQL (timeout, brak pliku bazy)? Czy łapać wszystko jednakowo?

<!-- [TODO Piotr: narracja - moment "narzędzie wybucha, a agent musi to przeżyć"; analogia do try/except na granicy systemu, nie tłumienia błędów] -->
