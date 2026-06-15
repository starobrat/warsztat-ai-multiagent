# Ćwiczenie ex_14: text-to-SQL (moduł 7)

<!-- [TODO Piotr - ŁUK: dotąd agent miał gotowe, wąskie narzędzia. Co, gdy
pytanie wykracza poza nie? Dajemy mu ogólne narzędzie - sam pisze SQL.] -->

## Co ćwiczymy
**Agent sam pisze SQL, gdy nie ma gotowca.** `get_schema` (poznaj strukturę) ->
`run_query` (wykonaj SELECT). Potężne i elastyczne - ale niebezpieczne.

## Które narzędzia podpinamy
- `get_schema` - struktura bazy.
- `run_query(sql)` - wykonuje dowolny SELECT (baza read-only).

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz `get_schema` i `run_query`.
2. Napisz instrukcję: NAJPIERW `get_schema`, potem `SELECT`, bez zgadywania
   nazw tabel i kolumn.
3. Zadaj pytania, na które NIE ma gotowego narzędzia.

## Dlaczego to niebezpieczne (dyskusja)
<!-- [TODO Piotr: postmortem/produkcyjny - czemu LLM piszący dowolny SQL na
produkcyjnej bazie to ryzyko (uprawnienia, koszty, błędne joiny, dane wrażliwe).
Kontrast z wąskimi narzędziami z ex_06-11.] -->

## Jak sprawdzić, że działa
- W Traces widać `get_schema`, a potem `run_query` z wygenerowanym SELECT-em.
- Wynik zgadza się z bazą.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił różnicę między
wąskim a ogólnym narzędziem - nie o gotową instrukcję.

## "Działa", gdy
Agent najpierw czyta schemat, potem pisze poprawny SELECT i odpowiada z danych.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_15: skoro agent pisze SQL,
to jak RÓŻNE modele radzą sobie z tym samym zadaniem? Czas na diagnostykę.] -->
