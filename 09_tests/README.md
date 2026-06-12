# Ćwiczenie: testy automatyczne agentów (moduł 12)

## Co ćwiczymy
**Ewaluacja agenta jako test w CI.** Ten sam test set co w module 7, tylko
uruchamiany przez `pytest` (`AgentEvaluator`). Pokazuje, jak jakość agenta pilnuje
się automatycznie, a nie "na oko".

## Zakres tego ćwiczenia
- Uruchomienie gotowego testu agenta SQL (`test_sql_agent.py`).
- Dorobienie test setu dla systemu wieloagentowego (`test_report_system.py` -> `# TODO(you)`).
- Zrozumienie, że `agent_module` wskazuje katalog agenta (np. `05_sql_agent`).

## Poza zakresem (gdzie indziej)
- Tworzenie/nagrywanie evalsetów i metryki — moduł 7 (`06_evaluation/`).
- Budowa samych agentów — `05_sql_agent`, `08_report_system`.

## Koncepcja w pigułce
`AgentEvaluator.evaluate(agent_module="05_sql_agent", eval_dataset_file_path_or_dir=...)`
ładuje agenta po nazwie jego katalogu i odpala na nim evalset. Próg zaliczenia bierze
z `06_evaluation/test_config.json`. To most między "ręcznym" evalem a CI.

## Twoje zadanie
Najpierw nagraj test set systemu raportowego w `adk web 08_report_system` (zakładka
Eval), zapisz go do `06_evaluation/report_system.evalset.json`, a potem odkomentuj
i uruchom `test_report_system.py`.

## "Działa", gdy
`uv run pytest 09_tests` przechodzi (lub świadomie pomija test, którego evalsetu
jeszcze nie nagrałeś).
