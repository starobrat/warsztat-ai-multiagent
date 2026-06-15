# Rozwiązanie: ex_15 - pierwszy test case ręcznie (NIEKODOWE)

Uzupełniony `starter.evalset.json`: 1 case dla agenta SQL. Przykład (Niemcy=4, zweryfikowane na bazie):
- user_content: "Ilu mamy klientów z Niemiec?"
- tool_uses: get_schema, run_query (SELECT COUNT(*) FROM Customer WHERE Country='Germany')
- final_response: "Mamy 4 klientów z Niemiec."

Sprawdzenie: `uv run adk eval ex_14_text_to_sql ex_15_eval_pierwszy_case/<plik> --config_file_path ex_17_eval_uruchom/test_config.json` -> case przechodzi na rozwiązanym agencie.
Friction: brak. Wzór: ex_17_eval_uruchom/sql_agent.evalset.json.
