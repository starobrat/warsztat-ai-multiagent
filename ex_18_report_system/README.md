# Ćwiczenie: system wieloagentowy - raportowanie (moduły 9-11)

## Co ćwiczymy
**Wieloagentowość**: hierarchię agentów i delegację. Agent = instrukcja + narzędzia;
system = kilku agentów, którzy przekazują sobie pracę. Budujesz pipeline:
**planner -> data_agent -> report_writer**.

## Zakres tego ćwiczenia
- Rozumienie `sub_agents` i `SequentialAgent` (kolejność, przekazywanie przez `output_key`).
- Napisanie instrukcji plannera (co ma być w raporcie, zanim ktoś odpyta bazę).
- Złożenie report_writera z gotowych klocków raportowych (PDF/Excel/HTML z `common/tools/`).

## Poza zakresem (przyjdzie później)
- **Testowanie systemu wieloagentowego - moduł 12 (`ex_19_tests/`).**
- Bezpieczeństwo / guardraile - `ex_20_guardrails` (moduł 14).
- MCP i A2A - moduł 13.
- Interfejs webowy masz gotowy (`adk web`) - nie budujemy własnego UI.

## Koncepcja w pigułce
- **SequentialAgent** = sztywna kolejność kroków, dane płyną przez `output_key`.
- **sub_agents + delegacja przez LLM** = master decyduje, komu przekazać (routing
  po `description`).
Planner planuje raport (sekcje, jakie dane, jakie wykresy), data_agent realizuje plan
na bazie, report_writer składa artefakt. Każdy agent ma wąską odpowiedzialność.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz instrukcję plannera, a w module 11 podłącz
report_writerowi narzędzia raportowe. Klocki gotowe w `common/tools/`.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `report_writer`: `tools=[bar_chart, make_pdf_report, make_html_report]`.
- W instrukcjach odwołuj się do wyników poprzednich agentów przez templating:
  `{report_plan}`, `{report_data}` (to klucze z `output_key`).

## "Działa", gdy
W `adk web` system `report_system` przechodzi planner -> dane -> raport i generuje
plik w `out/`, a w trace widać przekazania między agentami.

## Pójdź dalej
- Dodaj 4. agenta - krytyka, który sprawdza raport, zanim trafi do użytkownika.
- Zrównoleglij pobieranie danych (`ParallelAgent`, patrz bonus B7) - porównaj czas i trace.
- Co, gdy `data_agent` zwróci błędne dane - czy `report_writer` to wyłapie? Dodaj walidację.
