# Bonus B3: Audyt zapytań SQL

## Zadanie
Rozszerz guardrail z modułu 14 (`sql_agent_guarded`): zamiast tylko blokować,
LOGUJ każde zapytanie SQL, które agent próbuje wykonać, do pliku `out/audit.log`.

## Kroki
1. W `before_tool_callback` dopisz zapis do pliku: timestamp + nazwa narzędzia + argumenty.
2. Zostaw blokadę groźnych wzorców.
3. Zadaj kilka pytań i obejrzyj `out/audit.log`.

## Czego się uczysz
Observability agenta - w produkcji musisz wiedzieć, co agent naprawdę zrobił.
