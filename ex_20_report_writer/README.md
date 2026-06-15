# Ćwiczenie ex_22: pipeline raportu - report_writer (moduł 11)

<!-- [TODO Piotr - ŁUK: w ex_21 napisaliśmy mózg (plannera). Dane już płyną.
Teraz domykamy pipeline: report_writer bierze plan + dane i SKŁADA z nich gotowy
artefakt - wykres i raport HTML. Pierwszy raz agent woła narzędzia, które
produkują plik na dysku.] -->

## Co ćwiczymy
**Rolę report_writera - składanie artefaktu z klocków.** Ten sam pipeline
(planner -> data_agent -> report_writer), tylko teraz writer jest do napisania.
Bierze `{report_plan}` i `{report_data}` i woła narzędzia raportowe, by zbudować
plik.

## Które narzędzia podpinamy
- `planner` (GOTOWY) - `output_key="report_plan"`.
- `data_agent` (GOTOWY) - `get_schema`, `run_query`, `output_key="report_data"`.
- `report_writer` - `bar_chart`, `make_html_report` (TWOJE zadanie podłączyć i opisać).

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz `tools=[bar_chart, make_html_report]`.
2. Napisz instrukcję: z `{report_plan}` i `{report_data}` (opcjonalnie zrób
   `bar_chart`) zbuduj raport `make_html_report(title, sections, filename)`.
   `sections` to lista `{"heading", "body", "image": ścieżka_PNG lub pomiń}`.
3. Każ podać na końcu ścieżkę wygenerowanego pliku; zabroń zmyślania danych.

## Jak sprawdzić, że działa
- `uv run adk run ex_20_report_writer "raport o sprzedaży gatunków"` lub `adk web`.
- Po przejściu pipeline w katalogu `out/` pojawia się plik `.html` (i ewentualnie `.png`).

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś, by asystent wyjaśnił, skąd writer bierze
dane (`{report_data}`) i czym jest `sections` w `make_html_report`. Bez gotowej instrukcji.

## "Działa", gdy
W `out/` powstaje raport HTML zbudowany z realnych danych z bazy (nie zmyślony),
a w Traces widać wywołania `bar_chart` / `make_html_report`.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_23: pipeline jest liniowy -
krok po kroku. A gdyby dwa zapytania do bazy mogły lecieć RÓWNOLEGLE i skrócić
czas? To ParallelAgent - ex_23.] -->
