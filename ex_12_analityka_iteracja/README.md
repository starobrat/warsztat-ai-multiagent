# Ćwiczenie ex_13: analityka przez iterację (moduł 6)

<!-- [TODO Piotr - ŁUK: w ex_12 agent zrobił dwa wywołania. Teraz robi ich
WIELE - pętla po gatunkach. To pierwsza prawdziwa analityka.] -->

## Co ćwiczymy
**Analityka przez wielokrotne wywołania.** Agent pobiera gatunki (`get_genres`),
a potem dla każdego liczy sprzedaż w roku (`get_sold_count_for_genre`) i porównuje.

## Które narzędzia podpinamy
- `get_genres` - lista gatunków.
- `get_sold_count_for_genre(genre, year)` - sprzedaż gatunku w danym roku.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz oba narzędzia.
2. Napisz instrukcję: zbierz gatunki, policz sprzedaż każdego w zadanym roku,
   porównaj i podaj wynik.
3. Zapytaj "który gatunek sprzedał się najlepiej w 2025?".

## Jak sprawdzić, że działa
- W Traces widać wiele wywołań `get_sold_count_for_genre` (po jednym na gatunek).
- Wynik zgadza się z bazą (np. Rock 2025 = 176).

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, czemu model
sam decyduje o liczbie iteracji - nie o gotową instrukcję.

## "Działa", gdy
Agent iteruje po gatunkach, liczy sprzedaż każdego i poprawnie wskazuje najlepszy.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_14: masz liczby; czas zrobić
z nich coś, co widać - wykres. To payoff całego bloku narzędziowego.] -->
