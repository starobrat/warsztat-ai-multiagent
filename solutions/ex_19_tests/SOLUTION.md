# Rozwiązanie: ex_19_tests (ćwiczenie NIEKODOWE + kod - testy, moduł 12)

Cel: ta sama ewaluacja co w module 7, ale uruchamiana jak zwykły test (`pytest`) -
czyli ewaluacja agenta wchodzi do CI.

## Co jest gotowe w repo
- `test_sql_agent.py` - GOTOWY przykład. Odpala `AgentEvaluator.evaluate(agent_module=
  "ex_16_text_to_sql", eval_dataset=ex_15_eval/sql_agent.evalset.json)`. `AgentEvaluator`
  sam dobiera `ex_15_eval/test_config.json` (kryteria łagodne: trajektoria 0.0, response 0.5).
- `test_report_system.py` - ĆWICZENIE. Test jest, ale `@pytest.mark.skipif` pomija go,
  dopóki nie ma pliku `ex_15_eval/report_system.evalset.json`.

## Zadanie (i rozwiązanie)
1. **test_sql_agent** przechodzi, gdy agent SQL (ex_16) jest rozwiązany.
   Zweryfikowane: eval przeciw `solutions/ex_16_text_to_sql` -> **2 passed, 0 failed**.
   (Na starterze ex_16 test jest czerwony - agent nie sięga po dane. To oczekiwane.)
2. **test_report_system**: nagraj test set systemu wieloagentowego i zapisz jako
   `ex_15_eval/report_system.evalset.json`. Wtedy `skipif` przepuszcza test.
   - Szablon takiego evalsetu: `report_system.evalset.json` w tym katalogu (skopiuj do
     `ex_15_eval/`).
   - Kanonicznie: `uv run adk web ex_18_report_system` -> zakładka **Eval** -> nagraj sesję.

## Jak uruchomić
```bash
uv run pytest ex_19_tests                      # oba testy
uv run pytest ex_19_tests/test_sql_agent.py    # tylko SQL (przechodzi po rozwiązaniu ex_16)
```

## Uwaga o ewaluacji systemu wieloagentowego
Trajektoria w `report_system` obejmuje wywołania narzędzi przez `data_agent` i
`report_writer` - jest dłuższa i mniej deterministyczna niż u pojedynczego agenta SQL.
Dlatego kryterium trajektorii trzymamy na `0.0` (z `ex_15_eval/test_config.json`), a w
oczekiwanej odpowiedzi celujemy w fakt, że RAPORT POWSTAŁ, nie w dokładny tekst/ścieżkę.
System raportowy zweryfikowany ręcznie: `solutions/ex_18_report_system` produkuje plik
HTML + wykres PNG w `out/` (planner -> data_agent -> report_writer).

## Friction
Drobne: README startera mówi "odkomentuj test", a w obecnej wersji test nie jest
zakomentowany - jest pomijany przez `skipif`, dopóki nie ma evalsetu. Rozwiązaniem jest
dostarczenie `report_system.evalset.json`, nie odkomentowanie. (Do poprawy w README.)
