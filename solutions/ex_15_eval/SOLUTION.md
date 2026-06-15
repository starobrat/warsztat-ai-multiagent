# Rozwiązanie: ex_15_eval (ćwiczenie NIEKODOWE - ewaluacja, moduł 7)

To ćwiczenie nie ma `agent.py` z TODO - jego "rozwiązaniem" jest **nagrany test set**
i umiejętność puszczenia ewaluacji. W repo jest gotowy wzór: `ex_15_eval/sql_agent.evalset.json`
(2 przypadki, oczekiwane odpowiedzi zweryfikowane na realnej bazie Chinook).

## Jak wygląda test set
Każdy `eval_case` to: pytanie użytkownika (`user_content`), oczekiwana odpowiedź
(`final_response`) i oczekiwana trajektoria narzędzi (`intermediate_data.tool_uses` -
np. `get_schema` potem `run_query`).

## Kryteria (ex_15_eval/test_config.json)
```json
{ "tool_trajectory_avg_score": 0.0, "response_match_score": 0.5 }
```
- `tool_trajectory_avg_score: 0.0` - nie wymagamy identycznej trajektorii (różne, ale
  poprawne SQL-e przechodzą).
- `response_match_score: 0.5` - odpowiedź musi pokryć się z oczekiwaną w ~50% (ROUGE).

`AgentEvaluator` automatycznie bierze `test_config.json` leżący OBOK pliku evalset.

## Jak nagrać własne case'y (kanonicznie)
1. `uv run adk web ex_16_text_to_sql` -> zakładka **Eval** -> nagraj sesję (zadaj pytanie,
   sprawdź odpowiedź), zapisz jako case do evalsetu.
2. Liczby w oczekiwanej odpowiedzi ZWERYFIKUJ na bazie (`run_query`), zanim je wpiszesz.
3. Szablon do podejrzenia: `ex_15_eval/_szablony/wlasny.evalset.json`.

## Jak uruchomić ewaluację
```bash
# CLI:
uv run adk eval ex_16_text_to_sql ex_15_eval/sql_agent.evalset.json \
    --config_file_path ex_15_eval/test_config.json
# Web: adk web ex_16_text_to_sql -> zakładka Eval
# pytest (moduł 12): uv run pytest ex_19_tests/test_sql_agent.py
```

## Zweryfikowane
Eval `sql_agent.evalset.json` uruchomiony przeciw POPRAWNIE rozwiązanemu agentowi SQL
(`solutions/ex_16_text_to_sql`, a także `solutions/ex_17_modele_i_diagnostyka` na słabym
modelu): **Tests passed: 2, Tests failed: 0**. Na starterze (placeholder) eval jest
czerwony - to oczekiwane, bo agent nie sięga po dane.

## Friction
Brak. Ćwiczenie wymaga tylko nagrania case'ów w adk web + uruchomienia eval - zgodnie z README.
