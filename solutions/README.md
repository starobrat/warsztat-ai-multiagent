# Rozwiązania (solutions)

Referencyjne rozwiązania wszystkich ćwiczeń. Zaglądaj tu, **gdy utkniesz** - najpierw
spróbuj sam (ćwiczenia mają bramkę sokratejską i `# TODO(you)`), a rozwiązanie potraktuj
jako sprawdzenie, nie skrót.

> Same ćwiczenia (`ex_*/`) zostają z placeholderami i TODO - rozwiązania żyją TYLKO tutaj,
> żeby przez przypadek nie zacommitować rozwiązanego ćwiczenia.

## Jak uruchomić rozwiązanie

- **Skrypty** (część 1 + pamięć): `uv run python solutions/<ćwiczenie>/solution.py`
- **Agenci ADK** (`adk web`/`adk run`): `uv run adk run solutions/<ćwiczenie> "pytanie"`
  albo `uv run adk web solutions/<ćwiczenie>`
- **Ćwiczenia niekodowe** (ewaluacja/testy): patrz `SOLUTION.md` w katalogu

## Narzędzie weryfikacyjne

`solutions/_verify.py` uruchamia agenta ADK programowo (InMemoryRunner) i wypisuje
wywołania narzędzi + finalną odpowiedź - tak potwierdzamy sekcję "Działa, gdy" bez
klikania w `adk web`:

```bash
uv run python solutions/_verify.py solutions/ex_08_narzedzie_grounding "Jakie tabele są w bazie?"
```

## Mapa rozwiązań

| ćwiczenie | typ | jak sprawdzić "Działa" |
|-----------|-----|------------------------|
| ex_00_setup | n/d | smoke test zwraca odpowiedź modelu |
| ex_01_simple_call | skrypt | różne temperatury = różne odpowiedzi |
| ex_02_function_calling | skrypt | "17+25" -> add=42; ogólne -> model sam |
| ex_03_agentic_loop | skrypt | klienci z Niemiec = 4 |
| ex_04_hello | adk | rozmawia, nie zmyśla danych |
| ex_05_pamiec_i_sesje | adk | zapamietaj/przypomnij; stan w sesji |
| ex_06_pamiec_dlugoterminowa | skrypt | sesja 2 odzyskuje fakt przez load_memory |
| ex_07_kompaktowanie | skrypt | zwinięcia kontekstu, wczesny fakt przeżywa |
| ex_08_narzedzie_grounding | adk | functionCall get_schema |
| ex_08_narzedzie_grounding | adk | pytanie spoza bazy -> odmowa |
| ex_09_docstring | adk | functionCall get_genres |
| ex_10_argumenty | adk | get_sold_count_for_artist(AC/DC) = 16 |
| ex_11_lancuch_narzedzi | adk | get_artists -> get_albums_for_artist (2) |
| ex_12_analityka_iteracja | adk | iteracja; Rock 2025 = 176 |
| ex_13_raport_wykres | adk | narysuj_wykres_slupkowy -> PNG w out/ |
| ex_17_eval_uruchom | niekodowe | SOLUTION.md; eval 2/2 na rozwiązanym SQL |
| ex_14_text_to_sql | adk | get_schema -> run_query; Niemcy = 4 |
| ex_18_modele_i_diagnostyka | adk | eval RED->GREEN na słabym modelu |
| ex_22_report_writer | adk | planner->data->writer; HTML+PNG w out/ |
| ex_25_tests | niekodowe+kod | SOLUTION.md + szablon evalsetu |
| ex_26_guardrail_tool | adk | DROP zablokowane, SELECT działa |

Pełne wyniki weryfikacji i notatki o friction: `FRICTION.md`.
