# Ćwiczenie ex_15: ewaluacja (moduł 7)

<!-- [TODO Piotr - ŁUK: agent SQL (ex_14) działa, ale skąd wiesz, że DOBRZE? Tu
budujesz test set i puszczasz eval - jeden flow od "co znaczy dobra odpowiedź" po
liczby. Twój głos.] -->

## Co ćwiczymy
**Pełny flow ewaluacji** w jednym ćwiczeniu: zbuduj test set, uruchom eval, przeczytaj
metryki. To sedno szkolenia - jakość agenta to PROCES, nie "chyba lepiej".

## Co jest w katalogu (gotowe)
- `sql_agent.evalset.json` - wzorcowy test set (2 przypadki, odpowiedzi sprawdzone na bazie).
- `test_config.json` - kryteria: `tool_trajectory_avg_score`, `response_match_score` (próg 0.5).
- `przyklad.evalset.json`, `_szablony/wlasny.evalset.json` - wzory do podejrzenia.

## Twoje zadanie
1. **Zbuduj własny test set** dla agenta `ex_14_text_to_sql` - dwie drogi:
   - ręcznie w JSON (zobacz format: `user_content`, `intermediate_data.tool_uses`,
     `final_response`), albo
   - wygodniej: nagraj rozmowę w `adk web ex_14_text_to_sql` -> zakładka **Eval**.
   - **Oczekiwane liczby SPRAWDŹ na bazie**, nie zgaduj (`run_query`).
2. **Uruchom eval** z CLI:
   ```bash
   uv run adk eval ex_14_text_to_sql ex_15_ewaluacja/sql_agent.evalset.json \
       --config_file_path ex_15_ewaluacja/test_config.json
   ```
3. **Przeczytaj metryki**: co znaczy trajektoria (0.0 = nie wymagamy identycznej),
   co znaczy `response_match_score` (≥ 0.5).

## "Działa", gdy
Masz własny, zweryfikowany na bazie test set; na poprawnym agencie eval jest zielony,
na starterze - czerwony; umiesz wyjaśnić, które kryterium zadecydowało.

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do modułu 8: zielono na mocnym modelu, a na słabszym?
Tam prompt naprawdę zaczyna mieć znaczenie. Twój głos.] -->
