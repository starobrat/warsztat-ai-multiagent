# Ćwiczenie ex_09: łańcuch narzędzi (moduł 6)

<!-- [TODO Piotr - ŁUK: w ex_08 wystarczyło jedno narzędzie. Teraz jedno pytanie
wymaga DWÓCH po kolei - to pierwsza prawdziwa orkiestracja.] -->

## Co ćwiczymy
**Sekwencjonowanie narzędzi.** Agent najpierw rozwiązuje wykonawcę
(`get_artists`), potem pobiera jego albumy (`get_albums_for_artist`). Łańcuch
widać w Traces.

## Które narzędzia podpinamy
- `get_artists` - lista wykonawców.
- `get_albums_for_artist(artist)` - albumy danego wykonawcy.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz oba narzędzia.
2. Napisz instrukcję: NAJPIERW znajdź właściwego wykonawcę, POTEM jego albumy.
3. Zapytaj "jakie albumy ma zespół AC/DC?" i prześledź łańcuch w Traces.

## Jak sprawdzić, że działa
- W Traces widać sekwencję: `get_artists` -> `get_albums_for_artist` -> odpowiedź.
- Albumy zgadzają się z bazą (AC/DC: 2 albumy).

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, jak model
decyduje o KOLEJNOŚCI wywołań - nie o gotową instrukcję.

## "Działa", gdy
Agent wykonuje dwa wywołania we właściwej kolejności i podaje albumy z bazy.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_10: dwa wywołania to mało;
co, gdy trzeba przejść w pętli przez wszystkie gatunki i policzyć sprzedaż?] -->
