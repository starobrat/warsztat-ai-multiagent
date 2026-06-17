# Rozwiązanie: ex_23_tests (testy automatyczne agentów, moduł 12)

Cel: ta sama ewaluacja co w module 7, ale uruchamiana jak zwykły test (`pytest`) -
czyli ewaluacja agenta wchodzi do CI. Dwa gotowe przykłady: pojedynczy agent (SQL)
i system wieloagentowy (raportowy).

## Co jest gotowe w repo
- `test_sql_agent.py` - odpala `AgentEvaluator.evaluate(agent_module="ex_14_text_to_sql",
  eval_dataset_file_path_or_dir=solutions/ex_15_ewaluacja/sql_agent.evalset.json)`.
  Progi z `solutions/ex_15_ewaluacja/test_config.json` (trajektoria 0.0, response 0.5).
- `test_report_system.py` - odpala `AgentEvaluator.evaluate(agent_module="ex_22_report_writer",
  eval_dataset_file_path_or_dir=solutions/ex_23_tests/report_system.evalset.json)`.
  Progi z `solutions/ex_23_tests/test_config.json` (trajektoria 0.0, response 0.0 - smoke test).
- `report_system.evalset.json` + `test_config.json` w tym katalogu - gotowy, samowystarczalny
  bundla (evalset + progi obok siebie, bo `AgentEvaluator` czyta `test_config.json`
  z katalogu evalsetu).

## Jak działa wybór progów (ważne)
`AgentEvaluator` szuka `test_config.json` w **katalogu evalsetu** (nie testu). Dlatego
każdy test wskazuje evalset leżący obok własnego `test_config.json`:
- SQL -> `solutions/ex_15_ewaluacja/` (response 0.5, bo odpowiedź jest deterministyczna),
- system raportowy -> `solutions/ex_23_tests/` (response 0.0, bo nie jest).

## Jak uruchomić / weryfikacja
```bash
uv run pytest ex_23_tests                          # oba testy
uv run pytest ex_23_tests/test_report_system.py    # tylko system raportowy
```
Zweryfikowane: `test_report_system.py` -> **1 passed** (realnie uruchamia
`ex_22_report_writer` end-to-end). `test_sql_agent.py` -> zielony po rozwiązaniu ex_14
(na starterze czerwony - agent nie sięga po dane; to oczekiwane).

## Dlaczego łagodne progi dla systemu wieloagentowego
Trajektoria w `report_system` (planner -> data_agent -> report_writer) jest dłuższa i
mniej deterministyczna niż u pojedynczego agenta. Dlatego trajektorię trzymamy na `0.0`,
a w odpowiedzi nie celujemy w dokładny tekst - sprawdzamy, że system przeszedł end-to-end
i zwrócił raport (smoke test eval w CI). System raportowy zweryfikowany ręcznie:
`solutions/ex_22_report_writer` produkuje plik HTML + wykres PNG w `out/`.

## Wariant dla uczestnika (pójdź dalej)
Nagraj własną sesję w `adk web ex_22_report_writer` (zakładka Eval) i dorzuć ją jako
nowy case do evalsetu - albo dopisz case ręcznie wg wzoru istniejącego.
