# Ćwiczenie: narzędzia, sesje i pamięć w ADK (moduły 6-7)

## Co ćwiczymy
**Podpinanie narzędzi do agenta ADK** i pisanie dobrej **instrukcji**. Funkcja
Pythona z docstringiem i type hintami staje się narzędziem (FunctionTool) - to samo,
co robiłeś ręcznie w części 1, tylko że ADK robi function calling automatycznie.

## Zakres tego ćwiczenia
- Napisanie `instruction` dla agenta SQL (rola + zasady użycia narzędzi).
- Podpięcie `get_schema` i `run_query` jako narzędzi.
- Obserwacja sesji/stanu w `adk web` (co agent pamięta w ramach rozmowy).

## Poza zakresem (przyjdzie później)
- **Ewaluacja tego agenta - moduł 7, katalog `ex_06_evaluation/`.** Jeśli chcesz
  "dodać test"/eval: spokojnie, to następny krok, nie tutaj.
- Tuning promptu na evalu - `ex_07_sql_agent_tuning` (moduł 8).
- Wieloagentowość - `ex_08_report_system` (moduły 9-11).
- Guardraile / bezpieczeństwo - `ex_10_guardrails` (moduł 14).
- Interfejs webowy masz już gotowy (`adk web`) - nie budujemy własnego.

## Koncepcja w pigułce
Agent = instrukcja + narzędzia. Dobra instrukcja dla agenta SQL: nadaj rolę, każ
NAJPIERW sprawdzić schemat (`get_schema`), potem pisać `SELECT` (`run_query`),
zabroń zgadywania nazw tabel. Sesja trzyma historię jednej rozmowy - to jeszcze nie
pamięć długoterminowa.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz `instruction` i podłącz narzędzia.

## Wskazówki (jeśli pracujesz bez agenta AI)
- Narzędzia podajesz jako listę funkcji: `tools=[get_schema, run_query]` - ADK sam
  zrobi z nich `FunctionTool` (po docstringach i type hintach).
- `instruction` to zwykły string z rolą i zasadami korzystania z narzędzi.

## "Działa", gdy
W `adk web` agent `sql_agent` odpowiada na pytania o dane, faktycznie wołając
`get_schema` i `run_query` (widać to w trace), i nie zmyśla nazw tabel.

## Pójdź dalej
- Zadaj pytanie wymagające złączenia 3 tabel - czy agent poradzi sobie ze schematem sam?
- Zapytaj o dane, których NIE MA - zmyśla czy przyznaje niewiedzę? Popraw instrukcję, żeby przyznawał.
- Następny krok: napisz dla niego eval (moduł 6/7) - dopiero wtedy wiesz, że instrukcja jest dobra.
