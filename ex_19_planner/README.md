# Ćwiczenie ex_21: pipeline raportu - planner (moduł 10)

<!-- [TODO Piotr - ŁUK: minimalną sekwencję mamy z ex_20. Teraz prawdziwy pipeline
trzech ról: planista, ten-co-pobiera-dane, ten-co-składa-raport. W tym ćwiczeniu
piszemy MÓZG całości - plannera, który decyduje, co w ogóle ma się znaleźć w raporcie.] -->

## Co ćwiczymy
**Rolę plannera w pipelinie wieloagentowym.** Trzy agenty w `SequentialAgent`:
planner -> data_agent -> report_writer. Planner NIE dotyka bazy - układa plan
(sekcje, jakich danych trzeba, gdzie wykres). Plan płynie dalej przez `output_key`.

## Które narzędzia podpinamy
- `planner` - bez narzędzi (sama instrukcja, `output_key="report_plan"`). TWOJE zadanie.
- `data_agent` (GOTOWY) - `get_schema`, `run_query`, czyta `{report_plan}`.
- `report_writer` (GOTOWY) - `bar_chart`, `make_html_report`, czyta `{report_data}`.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz instrukcję plannera. Ma wypisać zwięzły
plan raportu (2-4 sekcje; dla każdej: jakiej liczby/danych potrzeba, czy dodać
wykres). Bez pisania SQL - od tego jest `data_agent`.

## Jak sprawdzić, że działa
- `uv run adk run ex_19_planner "raport o sprzedaży gatunków"` lub `adk web`.
- W Traces: planner zwraca plan -> data_agent go realizuje -> report_writer składa plik.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś, by asystent wyjaśnił, DLACZEGO planner
nie pisze SQL i jak `{report_plan}` trafia do następnego agenta. Bez gotowej instrukcji.

## "Działa", gdy
Planner produkuje czytelny plan, a dalsze agenty go realizują - cały pipeline
przechodzi i powstaje plik w `out/`.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_22: planner zaplanował, dane
są zebrane. Ale kto z tego zlepia gotowy artefakt? W ex_22 bierzemy na warsztat
report_writera - wykres + HTML.] -->
