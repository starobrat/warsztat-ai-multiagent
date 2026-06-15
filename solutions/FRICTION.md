# Friction log - budowa solutions

Cel: dla każdego ćwiczenia potwierdzić, że rozwiązanie wymaga TYLKO kroków z
`# TODO(you)` / README. Friction = cokolwiek poza tym (brakujący import, zła
ścieżka, ukryta zależność). Uwaga: problemy wynikające z UMIESZCZENIA solutions
o poziom głębiej (ścieżki sys.path/DB w kopiach klocków) to artefakt struktury
solutions/, NIE friction samego ćwiczenia - rozwiązane przez import klocków z
oryginalnego katalogu ćwiczenia.

## Część 1 (ex_00-03)
- ex_00_setup: brak friction. `uv sync` + klucz w .env + smoke test - działa.
- ex_01_simple_call: brak friction. Trzy TODO (rola, pytanie, temperatura) wystarczają.
- ex_02_function_calling: brak friction. TODO (reguła JSON, parsowanie, wywołanie) wystarczają.
- ex_03_agentic_loop: brak friction. TODO (pętla while + bezpiecznik) wystarcza.
  Zweryfikowane: klienci z Niemiec = 4 (zgodne z bazą).

## Część 2 - ADK
- ex_04_hello: brak friction. TODO (instruction). Zweryfikowane: agent rozmawia, odmawia zmyślania.
- ex_05_pamiec_i_sesje: brak friction. TODO (tools + instrukcja). Zweryfikowane: zapamietaj/przypomnij, stan sesji.
- ex_06_pamiec_dlugoterminowa (NOWE): brak friction. 3 TODO (instrukcja, load_memory,
  add_session_to_memory). Zweryfikowane: sesja 2 odzyskuje fakt przez load_memory.
- ex_07_kompaktowanie (NOWE): brak friction. TODO (events_compaction_config).
  Zweryfikowane: pojawiają się zwinięcia, agent pamięta wczesny fakt mimo kompaktowania.
- ex_08_pierwsze_narzedzie: brak friction. Zweryfikowane: functionCall get_schema.
- ex_09_instrukcja_grounding: brak friction. Zweryfikowane: pytanie spoza bazy -> odmowa bez zmyślania.
- ex_10_docstring: brak friction. Zweryfikowane: get_genres (z dopisanym docstringiem) wołane.
- ex_11_argumenty: brak friction. Zweryfikowane: get_sold_count_for_artist(artist="AC/DC") = 16.
- ex_12_lancuch_narzedzi: brak friction. Zweryfikowane: get_artists -> get_albums_for_artist (2 albumy).
- ex_13_analityka_iteracja: brak friction. Zweryfikowane: iteracja po gatunkach, Rock 2025 = 176.
- ex_14_raport_wykres: brak friction. Zweryfikowane: narysuj_wykres_slupkowy -> PNG w out/.
- ex_15_eval (NIEKODOWE): brak friction. SOLUTION.md + wzorcowy evalset. Eval przeciw
  rozwiązanemu agentowi SQL: 2 passed, 0 failed.
- ex_16_text_to_sql: brak friction. Zweryfikowane: get_schema -> run_query, klienci z Niemiec = 4.
- ex_17_modele_i_diagnostyka: brak friction. Naprawa WYŁĄCZNIE instruction na słabym modelu;
  eval RED->GREEN (2 passed). Diagnoza w nagłówku solution.
- ex_18_report_system: brak friction. Zweryfikowane: planner -> data_agent -> report_writer;
  powstaje HTML + wykres PNG w out/.
- ex_19_tests (NIEKODOWE+kod): SOLUTION.md + szablon report_system.evalset.json.
  Friction (drobne, POPRAWIONE w starterze): README/docstring mówiły "odkomentuj test",
  a test jest pomijany przez `@pytest.mark.skipif` do czasu pojawienia się evalsetu -
  poprawiono opis w `ex_19_tests/README.md` i `test_report_system.py`.
- ex_20_guardrails: brak friction. Zweryfikowane: callback blokuje DROP/INSERT itd.,
  przepuszcza SELECT (dodatkowo test jednostkowy callbacku - bo model często odmawia
  groźnego zapytania już na poziomie instrukcji, zanim guard zdąży zadziałać).

## Podsumowanie friction
Same ćwiczenia są czyste - każde rozwiązuje się WYŁĄCZNIE krokami z `# TODO(you)`.
Jedyna realna poprawka startera: opis "odkomentuj" w ex_19_tests (powyżej). Reszta
to artefakty struktury `solutions/` (shim sys.path o poziom głębiej), nie friction ćwiczeń.

## Narzędzie weryfikacyjne
`solutions/_verify.py <katalog_agenta> "<wiadomość>"` - uruchamia agenta ADK
programowo (InMemoryRunner) i wypisuje wywołania narzędzi + finalny tekst. Pozwala
potwierdzić sekcję "Działa, gdy" bez interaktywnego `adk web`.
