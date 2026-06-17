# Ćwiczenie: testy automatyczne agentów (moduł 12)

## Co ćwiczymy
**Ewaluacja agenta jako test w CI.** Ten sam test set co w module 7, tylko
uruchamiany przez `pytest` (`AgentEvaluator`). Pokazuje, jak jakość agenta pilnuje
się automatycznie, a nie "na oko".

## Zakres tego ćwiczenia
- Uruchomienie gotowego testu agenta SQL (`test_sql_agent.py`).
- Uruchomienie gotowego testu systemu wieloagentowego (`test_report_system.py`).
- Zrozumienie, że `agent_module` wskazuje katalog agenta (np. `ex_14_text_to_sql`).

## Poza zakresem (gdzie indziej)
- Tworzenie/nagrywanie evalsetów i metryki - moduł 7 (`ex_15_ewaluacja/`).
- Budowa samych agentów - `ex_14_text_to_sql`, `ex_22_report_writer`.

## Koncepcja w pigułce
`AgentEvaluator.evaluate(agent_module="ex_14_text_to_sql", eval_dataset_file_path_or_dir=...)`
ładuje agenta po nazwie jego katalogu i uruchamia na nim evalset. Próg zaliczenia
`AgentEvaluator` bierze z `test_config.json` leżącego w katalogu evalsetu. To most
między "ręcznym" evalem a CI.

## Twoje zadanie
Uruchom oba testy: `uv run pytest ex_23_tests`. Zobacz, jak ewaluacja agenta wchodzi
do CI jako zwykły pytest - dla pojedynczego agenta (SQL) i dla systemu wieloagentowego
(raportowy).

Dlaczego dwa różne progi? System wieloagentowy (planner -> data_agent -> report_writer)
ma niedeterministyczną trajektorię, dlatego jego test ma łagodne progi
(`solutions/ex_23_tests/test_config.json`): to smoke test, że system przechodzi
end-to-end i zwraca raport - nie sprawdzamy dokładnej trajektorii ani tekstu.

## "Działa", gdy
`uv run pytest ex_23_tests` przechodzi - oba testy zielone. Uwaga: test SQL celuje
w Twojego agenta z `ex_14_text_to_sql`, więc zazieleni się dopiero, gdy rozwiążesz ex_14.
Test systemu raportowego wymaga działającego `ex_22_report_writer`.

## Pójdź dalej
- Nagraj własną sesję w `adk web ex_22_report_writer` (zakładka Eval) i dorzuć ją
  jako nowy case do evalsetu (albo dopisz ręcznie wg wzoru istniejącego case'a).
- Dodaj case, który celowo łamie system (pytanie poza zakresem raportu).
- Porównaj, ile testów przechodzi na słabym vs mocnym modelu.
- Jak podłączyłbyś te testy do CI (GitHub Actions)? Naszkicuj workflow.
