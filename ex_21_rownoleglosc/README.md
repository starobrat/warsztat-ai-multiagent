# Ćwiczenie ex_21: ParallelAgent (moduł 11)

<!-- [TODO Piotr - ŁUK: cały pipeline raportu szedł liniowo - krok po kroku. Ale
nie wszystko MUSI być po kolei. Dwa niezależne zapytania do bazy nie czekają na
siebie - mogą lecieć równolegle. To pierwsze zrównoleglenie pracy agentów.] -->

## Co ćwiczymy
**`ParallelAgent` - równoległe uruchomienie niezależnych gałęzi.** Dwie gałęzie
odpytują bazę jednocześnie, każda pod swój `output_key`. Potem agent-syntezator
zbiera oba wyniki. Wzorzec: `Sequential( Parallel(a, b) -> synteza )`.

## Które narzędzia podpinamy
- `branch_klienci`, `branch_faktury` (GOTOWE) - `get_schema`, `run_query`,
  każda z własnym `output_key`.
- `synteza` (GOTOWY) - bez narzędzi, czyta `{wynik_klienci}` i `{wynik_faktury}`.
- Klocki orkiestracji: `ParallelAgent` + `SequentialAgent`.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Złóż obie gałęzie w `ParallelAgent(sub_agents=[branch_klienci, branch_faktury])`.
2. Wpnij `[rownolegle, synteza]` w `SequentialAgent` i przypisz do `root_agent`.

## Jak sprawdzić, że działa
- `uv run adk run ex_21_rownoleglosc "podsumuj bazę"` lub `adk web`.
- W Traces widać DWIE gałęzie uruchomione równolegle, potem syntezę.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś, by asystent wyjaśnił, KIEDY wolno
zrównoleglić agentów (kiedy gałęzie są niezależne) i dlaczego po Parallel
potrzebny jest krok zbierający. Bez gotowego kodu.

## "Działa", gdy
Obie gałęzie policzyły swoją liczbę (klienci ORAZ faktury), a syntezator zwrócił
podsumowanie z obiema wartościami.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_22: Sequential = po kolei,
Parallel = naraz. Brakuje jeszcze jednego kształtu: powtarzaj, AŻ będzie dobrze.
To LoopAgent - ex_22.] -->
