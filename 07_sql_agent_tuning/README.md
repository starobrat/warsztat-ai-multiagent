# Ćwiczenie: tuning promptu na test secie - TDD dla promptu (moduł 8)

## Co ćwiczymy
**TDD na prompcie.** Główny wniosek szkolenia: prompt to nie strzał z głowy -
prompt SIĘ TESTUJE, jak kod. Najpierw masz test (evalset z modułu 7), potem piszesz
prompt pod ten test. Agent startuje z instrukcją napisaną przez **laika**, który nie
wie, co jest w bazie ani jak ją odpytać - i **oblewa ewaluację (czerwony)**. Twoje
zadanie: iterować `instruction`, aż eval przejdzie (zielony). Pętla: zmiana -> eval
-> porównanie.

## Dlaczego ten agent chodzi na słabszym modelu
Ten jeden agent używa celowo słabszego modelu (`gpt-4o-mini`, przez `get_weak_model`).
Mocny model (gpt-5.4-mini) **maskuje** słaby prompt: i tak sięgnie po narzędzia,
sprawdzi schemat i odpowie dobrze - więc nigdy nie zobaczyłbyś czerwonego i nie dało
by się pokazać pętli TDD. Słabszy model słucha instrukcji dosłownie: zła instrukcja =
zły agent. To samo w sobie jest lekcją - **im słabszy model, tym bardziej liczy się
prompt** (i tym ważniejszy eval).

## Zakres tego ćwiczenia
- Uruchomienie evalu i odczytanie, dlaczego jest czerwony (agent nie zna danych).
- Iteracyjna poprawa **wyłącznie instrukcji**.
- Ponowny eval i porównanie.

## Poza zakresem (świadomie zabronione lub później)
- **Zmiana narzędzi albo modelu** - tego NIE ruszamy (zostaje słabszy model, bo to
  on robi z promptu test). W tym ćwiczeniu zmieniasz tylko `instruction` (o to chodzi).
- Dodawanie nowych funkcji/możliwości agentowi - to nie tutaj.
- Tworzenie nowych test case'ów - moduł 7 (`06_evaluation/`).
- Testy automatyczne / pytest - moduł 12 (`09_tests/`).

## Koncepcja w pigułce
Proces dbania o jakość: masz test set (oczekiwana trajektoria narzędzi + oczekiwana
odpowiedź), zmieniasz prompt, uruchamiasz eval, patrzysz na metryki
(`tool_trajectory_avg_score`, `response_match_score`), powtarzasz. Prompt "rośnie"
w oparciu o przypadki testowe, a nie o przeczucie.

## Twoje zadanie
Uruchom:
```bash
uv run adk eval 07_sql_agent_tuning 06_evaluation/sql_agent.evalset.json \
    --config_file_path 06_evaluation/test_config.json
```
Potem poprawiaj `instruction` w `agent.py`, aż eval przejdzie.

## Wskazówki (jeśli pracujesz bez agenta AI)
- To samo pole `instruction` co w `05_sql_agent` - tam masz wzór dobrej instrukcji.
- Klucz: każ NAJPIERW wywołać `get_schema`, potem `run_query`; zabroń zgadywania
  i każ odpowiadać tylko na podstawie danych z bazy.

## "Działa", gdy
Eval świeci na zielono, a Ty potrafisz powiedzieć, której części instrukcji
brakowało i dlaczego.
