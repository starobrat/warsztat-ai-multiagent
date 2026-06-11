# Ćwiczenie: system wieloagentowy - raportowanie (moduły 9-11)

## Co ćwiczymy
**Wieloagentowość**: hierarchię agentów i delegację. Agent = instrukcja + narzędzia;
system = kilku agentów, którzy przekazują sobie pracę. Budujesz pipeline:
**planner -> data_agent -> report_writer**.

## Zakres tego ćwiczenia
- Rozumienie `sub_agents` i `SequentialAgent` (kolejność, przekazywanie przez `output_key`).
- Napisanie instrukcji plannera (co ma być w raporcie, zanim ktoś odpyta bazę).
- Złożenie report_writera z gotowych klocków raportowych (PDF/Excel/HTML z `tools/`).

## Poza zakresem (przyjdzie później)
- **Testowanie systemu wieloagentowego — moduł 12 (`part2_adk/tests/`).**
- Bezpieczeństwo / guardraile — `agents/sql_agent_guarded` (moduł 14).
- MCP i A2A — moduł 13.
- Interfejs webowy masz gotowy (`adk web`) — nie budujemy własnego UI.

## Koncepcja w pigułce
- **SequentialAgent** = sztywna kolejność kroków, dane płyną przez `output_key`.
- **sub_agents + delegacja przez LLM** = master decyduje, komu przekazać (routing
  po `description`).
Planner planuje raport (sekcje, jakie dane, jakie wykresy), data_agent realizuje plan
na bazie, report_writer składa artefakt. Każdy agent ma wąską odpowiedzialność.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz instrukcję plannera, a w module 11 podłącz
report_writerowi narzędzia raportowe. Klocki gotowe w `part2_adk/tools/`.

## "Działa", gdy
W `adk web` system `report_system` przechodzi planner -> dane -> raport i generuje
plik w `part2_adk/out/`, a w trace widać przekazania między agentami.
