# Ćwiczenie: pętla agentyczna (moduł 4)

## Co ćwiczymy
**Pętlę agentyczną** - różnicę między: wywołaniem LLM, pipeline'em i agentem.
Agent to LLM w **pętli**, który **sam decyduje**, ilu kroków i jakich narzędzi
użyć, aż uzna, że ma odpowiedź. To domknięcie części 1.

## Zakres tego ćwiczenia
- Pętla `while`: decyzja modelu -> wywołanie narzędzia -> wynik wraca do modelu -> powtórz.
- Dwa narzędzia na bazie Chinook: `get_schema`, `run_query` (gotowe, read-only).
- Bezpiecznik: limit kroków (`MAX_STEPS`).

## Poza zakresem (przyjdzie później)
- Pamięć / sesje - część 2 (ADK).
- Abstrakcja ADK (LlmAgent, adk web) - część 2, zaczyna się od `ex_04_hello`.
- Ewaluacja - część 2, moduł 7 (`ex_06_evaluation/`).
- Wieloagentowość - część 2, `ex_08_report_system`.

## Koncepcja w pigułce
- **Wywołanie** = jeden krok, jedna odpowiedź.
- **Pipeline** = z góry ustalona sekwencja kroków.
- **Agent** = pętla, w której model decyduje o następnym kroku.

Składasz tu function calling z ćwiczenia 02 z pętlą. Najpierw model patrzy w schemat,
potem pisze SELECT, potem na podstawie wyniku formułuje odpowiedź - wszystko sam,
w pętli, dopóki nie zwróci `tool: null`.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`): napisz pętlę w `run_agent`. Narzędzia masz gotowe
w `db_tools.py`.

## Wskazówki (jeśli pracujesz bez agenta AI)
- Pętla: `for _ in range(MAX_STEPS)`, `agent_step(messages)`, `decision.get("tool")`.
- Wywołanie narzędzia: `TOOLS[nazwa](**args)`.
- Dołóż decyzję i wynik do historii: `messages.append({"role": ..., "content": ...})`,
  `json.dumps(...)`.

## "Działa", gdy
Na "ilu mamy klientów z Niemiec?" agent sam wywołuje `get_schema`, potem `run_query`
z sensownym SELECT-em i zwraca poprawną liczbę - bez Twojej ingerencji w pętli.

## Pójdź dalej
- Zadaj pytanie wymagające kilku zapytań SQL (porównanie dwóch gatunków) - ile kroków zrobi agent?
- Znajdź pytanie, które ciągnie pętlę aż do `MAX_STEPS`. Czemu nie kończy?
- Dołóż logowanie każdego kroku (jakie SQL, jaki wynik) - pierwszy krok ku observability.
