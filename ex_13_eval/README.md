<!-- [TODO Piotr - REFRAME do tool-first]: to ćwiczenie przyszło ze starej struktury
(eval agenta SQL). W nowym układzie ex_13 ma ewaluować AGENTA NARZĘDZIOWEGO
(deterministyczne narzędzia = łatwiejsze ground-truth). Evalset SQL (sql_agent.evalset.json)
pasuje raczej do ex_14/ex_15. Do przepisania: evalset + framing pod agenta narzędziowego. -->

# Ewaluacja agentów (moduły 7 i 12)

Główny wniosek szkolenia: **prompt to nie strzał z głowy. Prompt się testuje.**

## Dwa sposoby uruchomienia tego samego test setu

**1. CLI** (moduł 7):
```bash
uv run adk eval ex_14_text_to_sql ex_13_eval/sql_agent.evalset.json \
    --config_file_path ex_13_eval/test_config.json --print_detailed_results
```

**2. Interfejs webowy** (moduł 7): `adk web ex_14_text_to_sql` -> zakładka **Eval**.
Tu też NAGRYWASZ nowe przypadki: prowadzisz rozmowę, zapisujesz ją jako eval case.
To jest kanoniczny sposób tworzenia test setów - plik `.evalset.json` powstaje sam.

**3. pytest** (moduł 12): `uv run pytest ex_17_tests`

## Twoje zadanie
Nagraj **2-3 własne case'y eval** dla `ex_14_text_to_sql`: w `adk web ex_14_text_to_sql`,
zakładka **Eval**, poprowadź rozmowę i zapisz ją jako eval case. Wykorzystaj pusty
szablon z `ex_13_eval/_szablony/`. Potem uruchom eval i sprawdź, czy agent je
przechodzi. To jest kanoniczny sposób budowania test setów - kod piszesz minimalnie,
case'y nagrywasz.

## Metryki ADK

- `tool_trajectory_avg_score` - czy agent użył właściwych narzędzi we właściwej kolejności
- `response_match_score` - czy finalna odpowiedź zgadza się z oczekiwaną (ROUGE)

Progi w `test_config.json`. **Bramką jest `response_match_score` (0.5).**
`tool_trajectory_avg_score` ma próg `0.0` (informacyjnie) - ADK porównuje też dokładne
argumenty narzędzi, więc równoważny, ale inaczej zapisany SELECT (inne aliasy, inna
kolejność JOIN) daje 0, mimo że agent odpowiada poprawnie. Potwierdzone na ADK 2.2.

## Ważne (uczciwie)

Plik `sql_agent.evalset.json` napisaliśmy ręcznie wg udokumentowanego schematu ADK,
a oczekiwane liczby zweryfikowaliśmy na realnej bazie (Niemcy = 4 klientów, Rock = 1297 utworów).
Dopasowanie `tool_uses` po dokładnym SQL bywa kruche (model może napisać równoważny,
ale inny SELECT) - dlatego w praktyce nagrywaj przypadki przez `adk web` i opieraj się
głównie na `response_match_score`.

## "Działa", gdy
Twój nagrany case przechodzi (`response_match` powyżej progu) na dobrym agencie,
a oblewa, gdy celowo zepsujesz mu instrukcję - czyli eval naprawdę coś mierzy.

## Pójdź dalej
- Dodaj case brzegowy (pytanie bez odpowiedzi w bazie) - czy agent go przechodzi?
- Porównaj `response_match` i `tool_trajectory` na tym samym case - czemu się różnią?
- Zbuduj test set, który złapie regresję niewidoczną "na oko".
