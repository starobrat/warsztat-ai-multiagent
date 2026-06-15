# Ćwiczenie: testy automatyczne agentów (moduł 12)

## Co ćwiczymy
**Ewaluacja agenta jako test w CI.** Ten sam test set co w module 7, tylko
uruchamiany przez `pytest` (`AgentEvaluator`). Pokazuje, jak jakość agenta pilnuje
się automatycznie, a nie "na oko".

## Zakres tego ćwiczenia
- Uruchomienie gotowego testu agenta SQL (`test_sql_agent.py`).
- Dorobienie test setu dla systemu wieloagentowego (`test_report_system.py` -> `# TODO(you)`).
- Zrozumienie, że `agent_module` wskazuje katalog agenta (np. `ex_16_text_to_sql`).

## Poza zakresem (gdzie indziej)
- Tworzenie/nagrywanie evalsetów i metryki - moduł 7 (`ex_15_eval/`).
- Budowa samych agentów - `ex_16_text_to_sql`, `ex_18_report_system`.

## Koncepcja w pigułce
`AgentEvaluator.evaluate(agent_module="ex_16_text_to_sql", eval_dataset_file_path_or_dir=...)`
ładuje agenta po nazwie jego katalogu i uruchamia na nim evalset. Próg zaliczenia bierze
z `ex_15_eval/test_config.json`. To most między "ręcznym" evalem a CI.

## Twoje zadanie
Najpierw nagraj test set systemu raportowego w `adk web ex_18_report_system` (zakładka
Eval), zapisz go do `ex_15_eval/report_system.evalset.json`. Gdy plik już istnieje,
`test_report_system.py` przestaje być pomijany (`skipif`) i odpala się sam.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `AgentEvaluator.evaluate(agent_module="ex_18_report_system", eval_dataset_file_path_or_dir=...)`.
- Evalset nagraj w `adk web ex_18_report_system` (zakładka Eval) albo dopisz ręcznie
  wg wzoru `ex_15_eval/sql_agent.evalset.json`.

## "Działa", gdy
`uv run pytest ex_19_tests` przechodzi (lub świadomie pomija test, którego evalsetu
jeszcze nie nagrałeś).

## Pójdź dalej
- Dodaj case, który celowo łamie system (pytanie poza zakresem raportu).
- Porównaj, ile testów przechodzi na słabym vs mocnym modelu.
- Jak podłączyłbyś te testy do CI (GitHub Actions)? Naszkicuj workflow.
