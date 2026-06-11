# Ćwiczenie: narzędzia, sesje i pamięć w ADK (moduły 6-7)

## Co ćwiczymy
**Podpinanie narzędzi do agenta ADK** i pisanie dobrej **instrukcji**. Funkcja
Pythona z docstringiem i type hintami staje się narzędziem (FunctionTool) — to samo,
co robiłeś ręcznie w części 1, tylko że ADK robi function calling automatycznie.

## Zakres tego ćwiczenia
- Napisanie `instruction` dla agenta SQL (rola + zasady użycia narzędzi).
- Podpięcie `get_schema` i `run_query` jako narzędzi.
- Obserwacja sesji/stanu w `adk web` (co agent pamięta w ramach rozmowy).

## Poza zakresem (przyjdzie później)
- **Ewaluacja tego agenta — moduł 7, katalog `part2_adk/evals/`.** Jeśli chcesz
  "dodać test"/eval: spokojnie, to następny krok, nie tutaj.
- Tuning promptu na evalu — `agents/sql_agent_to_tune` (moduł 8).
- Wieloagentowość — `agents/report_system` (moduły 9-11).
- Guardraile / bezpieczeństwo — `agents/sql_agent_guarded` (moduł 14).
- Interfejs webowy masz już gotowy (`adk web`) — nie budujemy własnego.

## Koncepcja w pigułce
Agent = instrukcja + narzędzia. Dobra instrukcja dla agenta SQL: nadaj rolę, każ
NAJPIERW sprawdzić schemat (`get_schema`), potem pisać `SELECT` (`run_query`),
zabroń zgadywania nazw tabel. Sesja trzyma historię jednej rozmowy — to jeszcze nie
pamięć długoterminowa.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz `instruction` i podłącz narzędzia.

## "Działa", gdy
W `adk web` agent `sql_agent` odpowiada na pytania o dane, faktycznie wołając
`get_schema` i `run_query` (widać to w trace), i nie zmyśla nazw tabel.
