# Ćwiczenie ex_10: narzędzie z argumentem (moduł 6)

<!-- [TODO Piotr - ŁUK: dotąd narzędzia nie brały argumentów. Teraz model musi
wyłuskać argument z pytania ("ile sprzedał AC/DC?") i podać go narzędziu.] -->

## Co ćwiczymy
**Przepływ argumentu z języka naturalnego do narzędzia.** Model rozpoznaje, że
"AC/DC" to argument `artist`, i wywołuje `get_sold_count_for_artist("AC/DC")`.

## Które narzędzia podpinamy
- `get_sold_count_for_artist(artist)` - liczba sprzedanych utworów wykonawcy.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz `get_sold_count_for_artist`.
2. Napisz instrukcję (grounding + użycie narzędzia do liczby sprzedaży).
3. Zapytaj o kilku wykonawców i sprawdź argument w Traces.

## Jak sprawdzić, że działa
- "Ile sprzedał AC/DC?" -> w Events `functionCall` z `args: {"artist": "AC/DC"}`.
- Wynik zgadza się z bazą (AC/DC = 16).

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, skąd ADK wie,
jakiego typu jest argument `artist` - nie o gotową instrukcję.

## "Działa", gdy
Model poprawnie przekazuje nazwę wykonawcy jako argument i podaje liczbę z bazy.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_11: jedno narzędzie wystarcza
na proste pytanie; co, gdy odpowiedź wymaga DWÓCH narzędzi po kolei?] -->
