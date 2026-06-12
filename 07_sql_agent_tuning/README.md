# Ćwiczenie: tuning promptu na test secie (moduł 8)

## Co ćwiczymy
**Pętlę jakości promptu.** Główny takeaway szkolenia: prompt to nie strzał z głowy.
Ten agent ma celowo słabą instrukcję i **oblewa ewaluację**. Twoje zadanie: poprawiać
`instruction`, aż eval przejdzie — w pętli zmiana -> eval -> porównanie.

## Zakres tego ćwiczenia
- Uruchomienie evalu i odczytanie, dlaczego jest czerwony.
- Iteracyjna poprawa **wyłącznie instrukcji**.
- Ponowny eval i porównanie.

## Poza zakresem (świadomie zabronione lub później)
- **Zmiana narzędzi albo modelu** — tego NIE ruszamy, w tym ćwiczeniu zmieniasz
  tylko `instruction` (o to chodzi).
- Dodawanie nowych funkcji/możliwości agentowi — to nie tutaj.
- Tworzenie nowych test case'ów — moduł 7 (`06_evaluation/`).
- Testy automatyczne / pytest — moduł 12 (`09_tests/`).

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

## "Działa", gdy
Eval świeci na zielono, a Ty potrafisz powiedzieć, której części instrukcji
brakowało i dlaczego.
