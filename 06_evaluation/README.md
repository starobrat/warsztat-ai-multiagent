# Ewaluacja agentów (moduły 7 i 12)

Główny takeaway szkolenia: **prompt to nie strzał z głowy. Prompt się testuje.**

## Dwa sposoby uruchomienia tego samego test setu

**1. CLI** (moduł 7):
```bash
uv run adk eval 05_sql_agent 06_evaluation/sql_agent.evalset.json \
    --config_file_path 06_evaluation/test_config.json --print_detailed_results
```

**2. Interfejs webowy** (moduł 7): `adk web 05_sql_agent` -> zakładka **Eval**.
Tu też NAGRYWASZ nowe przypadki: prowadzisz rozmowę, zapisujesz ją jako eval case.
To jest kanoniczny sposób tworzenia test setów - plik `.evalset.json` powstaje sam.

**3. pytest** (moduł 12): `uv run pytest 09_tests`

## Metryki ADK

- `tool_trajectory_avg_score` - czy agent użył właściwych narzędzi we właściwej kolejności
- `response_match_score` - czy finalna odpowiedź zgadza się z oczekiwaną

Progi w `test_config.json`.

## Ważne (uczciwie)

Plik `sql_agent.evalset.json` napisaliśmy ręcznie wg udokumentowanego schematu ADK,
a oczekiwane liczby zweryfikowaliśmy na realnej bazie (Niemcy = 4 klientów, Rock = 1297 utworów).
Dopasowanie `tool_uses` po dokładnym SQL bywa kruche (model może napisać równoważny,
ale inny SELECT) - dlatego w praktyce nagrywaj przypadki przez `adk web` i opieraj się
głównie na `response_match_score`.
