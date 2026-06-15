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
uv run python solutions/_verify.py solutions/ex_08_pierwsze_narzedzie "Jakie tabele są w bazie?"
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
| ex_08_pierwsze_narzedzie | adk | functionCall get_schema |
| ex_09_instrukcja_grounding | adk | pytanie spoza bazy -> odmowa |
| ex_10_docstring | adk | functionCall get_genres |
| ex_11_argumenty | adk | get_sold_count_for_artist(AC/DC) = 16 |
| ex_12_lancuch_narzedzi | adk | get_artists -> get_albums_for_artist (2) |
| ex_13_analityka_iteracja | adk | iteracja; Rock 2025 = 176 |
| ex_14_raport_wykres | adk | narysuj_wykres_slupkowy -> PNG w out/ |
| ex_15_eval | niekodowe | SOLUTION.md; eval 2/2 na rozwiązanym SQL |
| ex_16_text_to_sql | adk | get_schema -> run_query; Niemcy = 4 |
| ex_17_modele_i_diagnostyka | adk | eval RED->GREEN na słabym modelu |
| ex_18_report_system | adk | planner->data->writer; HTML+PNG w out/ |
| ex_19_tests | niekodowe+kod | SOLUTION.md + szablon evalsetu |
| ex_20_guardrails | adk | DROP zablokowane, SELECT działa |

Pełne wyniki weryfikacji i notatki o friction: `FRICTION.md`.
