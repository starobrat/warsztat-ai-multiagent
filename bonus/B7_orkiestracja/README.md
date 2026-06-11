# Bonus B7: Inne wzorce orkiestracji

## Zadanie
Poznałeś `SequentialAgent` (kolejność) i delegację przez `sub_agents`. ADK ma więcej:
- `ParallelAgent` - kilku agentów naraz (np. równoległe odpytanie 3 obszarów danych),
- `LoopAgent` - powtarzanie, aż warunek spełniony (np. iteracyjne dopracowanie raportu).

## Kroki
1. Przerób fragment systemu raportowego tak, żeby dane dla 3 sekcji pobierały się
   równolegle (`ParallelAgent`).
2. Porównaj czas i strukturę trace w `adk web`.

## Czego się uczysz
Dobór wzorca orkiestracji do problemu: sekwencja vs równoległość vs pętla.
