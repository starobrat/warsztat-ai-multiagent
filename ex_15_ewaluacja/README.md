# Ćwiczenie ex_15: ewaluacja (moduł 7)

<!-- [TODO Piotr - ŁUK: agent SQL (ex_14) działa, ale skąd wiesz, że DOBRZE? Tu
budujesz test set i puszczasz eval - jeden flow od "co znaczy dobra odpowiedź" po
liczby. Twój głos.] -->

## Co ćwiczymy
**Pełny flow ewaluacji w `adk web`** (zakładka **Eval**): zbuduj test set, uruchom eval,
przeczytaj metryki. To sedno szkolenia - jakość agenta to PROCES, nie "chyba lepiej".

## Co jest w katalogu (do podejrzenia)
- `przyklad.evalset.json`, `_szablony/wlasny.evalset.json` - wzory formatu test setu.
- Wzorcowy (gotowy) test set + kryteria leżą w `solutions/ex_15_ewaluacja/`
  (`sql_agent.evalset.json`, `test_config.json`) - tu budujesz WŁASNY.

## Twoje zadanie (w `adk web`, zakładka Eval)
1. **Zbuduj własny test set** dla agenta `ex_14_text_to_sql`:
   - uruchom `uv run adk web ex_14_text_to_sql`, wejdź w zakładkę **Eval**,
   - nagraj kilka rozmów jako przypadki ewaluacyjne (pytanie + trajektoria + odpowiedź),
   - **oczekiwane liczby SPRAWDŹ na bazie**, nie zgaduj (`run_query`).
2. **Uruchom eval** w zakładce Eval (Run) i obejrzyj wynik per przypadek.
3. **Przeczytaj metryki**: co znaczy trajektoria (0.0 = nie wymagamy identycznej),
   co znaczy `response_match_score` (≥ 0.5).

> CLI (`adk eval`) i pytest poznasz w demie prowadzącego i w module 12 - tu zostajemy w GUI.

## "Działa", gdy
Masz własny, zweryfikowany na bazie test set; w zakładce Eval na poprawnym agencie eval jest
zielony, na starterze - czerwony; umiesz wyjaśnić, które kryterium zadecydowało.

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do modułu 8: zielono na mocnym modelu, a na słabszym?
Tam prompt naprawdę zaczyna mieć znaczenie. Twój głos.] -->
