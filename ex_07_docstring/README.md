# Ćwiczenie ex_07: docstring narzędzia (moduł 6)

<!-- [TODO Piotr - ŁUK: w ex_06 agent miał jedno narzędzie. Teraz dokładamy
drugie - i pojawia się pytanie: skąd model wie, KTÓRE wywołać? Z docstringa.] -->

## Co ćwiczymy
**Docstring to kontrakt, który czyta model.** To on decyduje, czy i kiedy model
sięgnie po narzędzie. Piszesz docstring dla `get_genres` i sprawdzasz efekt.

## Które narzędzia podpinamy
- `get_schema` (gotowe) - struktura bazy.
- `get_genres` (lokalne, w `agent.py`) - z PUSTYM docstringiem do napisania.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Napisz docstring funkcji `get_genres` (co zwraca, kiedy ją wołać).
2. Podłącz `get_schema` i `get_genres` do `tools`.
3. Eksperyment: wpisz CELOWO mylący docstring i zobacz, że model przestaje
   trafiać w narzędzie.

## Jak sprawdzić, że działa
- Zapytaj "jakie są gatunki?" -> w Events widać `functionCall` z `get_genres`.
- Po zepsuciu docstringa -> model go nie woła (albo woła zły). To jest lekcja.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, jak ADK buduje
opis narzędzia z funkcji - nie o gotowy docstring.

## "Działa", gdy
Z dobrym docstringiem model trafnie woła `get_genres`; ze złym - nie.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_08: narzędzia bez argumentów
są proste; co, gdy narzędzie potrzebuje parametru z pytania użytkownika?] -->
