# Ćwiczenie ex_17: uruchom eval i czytaj metryki (moduł 7)

<!-- [TODO Piotr - ŁUK: masz test set (ręcznie z ex_15, nagrany z ex_16). Teraz
uruchamiasz go hurtem i uczysz się czytać metryki. Twój głos.] -->

## Co ćwiczymy
**Uruchamianie ewaluacji z CLI i czytanie metryk.** Jednym poleceniem puszczasz cały
test set na agencie i dostajesz liczby - koniec z "chyba lepiej".

## Co jest w katalogu (gotowe)
- `sql_agent.evalset.json` - wzorcowy test set (2 przypadki, odpowiedzi sprawdzone na bazie).
- `test_config.json` - kryteria: `tool_trajectory_avg_score` (trajektoria narzędzi),
  `response_match_score` (dopasowanie odpowiedzi, próg 0.5).
- `_szablony/wlasny.evalset.json` - wzór do własnych przypadków.

## Twoje zadanie
Uruchom eval na rozwiązanym agencie SQL i odczytaj wynik:
```bash
uv run adk eval ex_14_text_to_sql ex_17_eval_uruchom/sql_agent.evalset.json \
    --config_file_path ex_17_eval_uruchom/test_config.json
```
Następnie odpowiedz sobie:
- ile przypadków przeszło / oblało?
- co znaczy `tool_trajectory_avg_score` = 0.0 w configu (nie wymagamy identycznej trajektorii)?
- co znaczy `response_match_score` = 0.5 (odpowiedź musi pokryć się w ~50%)?

## Jak sprawdzić, że działa
Widzisz `Tests passed / Tests failed` i rozumiesz, które kryterium zadecydowało.

## "Działa", gdy
Na poprawnym agencie eval jest zielony (2/2); na starterze (placeholder) - czerwony.
Umiesz wyjaśnić DLACZEGO (agent nie sięga po dane = pusta trajektoria + zła odpowiedź).

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do modułu 8: zielono na mocnym modelu, a na słabszym?
Tam prompt naprawdę zaczyna mieć znaczenie. Twój głos.] -->
