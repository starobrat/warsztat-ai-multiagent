# Ćwiczenie ex_15: pierwszy test case ręcznie (moduł 7)

<!-- [TODO Piotr - ŁUK: agent SQL (ex_14) już działa. Zanim go zautomatyzujemy,
musimy umieć POWIEDZIEĆ, co znaczy "dobra odpowiedź". Stąd test case. Twój głos.] -->

## Co ćwiczymy
**Format test setu od podszewki.** Zanim nagramy przypadki w GUI, piszemy JEDEN
ręcznie - żeby zrozumieć, z czego składa się eval case: pytanie, oczekiwana
TRAJEKTORIA narzędzi i oczekiwana ODPOWIEDŹ.

## Twoje zadanie
W pliku `starter.evalset.json` (`# TODO`) uzupełnij jeden `eval_case` dla agenta SQL
(`ex_14_text_to_sql`):
- `user_content` - pytanie (np. "Ilu mamy klientów z Niemiec?")
- `intermediate_data.tool_uses` - oczekiwane wywołania (`get_schema`, potem `run_query`)
- `final_response` - oczekiwana odpowiedź; **liczbę sprawdź na bazie**, nie zgaduj
  (`uv run python -c "..."` albo `run_query`)

Wzór do podejrzenia: `ex_17_eval_uruchom/sql_agent.evalset.json`.

## Jak sprawdzić, że działa
Uruchom eval swojego case'a na rozwiązanym agencie:
```bash
uv run adk eval ex_14_text_to_sql ex_15_eval_pierwszy_case/starter.evalset.json \
    --config_file_path ex_17_eval_uruchom/test_config.json
```
Jeśli oczekiwana odpowiedź jest poprawna (sprawdzona na bazie), case przechodzi.

## "Działa", gdy
Twój ręcznie napisany case przechodzi na poprawnym agencie, a Ty rozumiesz każde
pole: pytanie, trajektorię, oczekiwaną odpowiedź.

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do ex_16: pisanie JSON-a ręcznie jest żmudne; w adk web
nagrasz przypadek klikając. Twój głos.] -->
