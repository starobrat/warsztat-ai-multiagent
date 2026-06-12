# Ćwiczenie: bezpieczeństwo - guardrail (moduł 14)

## Co ćwiczymy
**Bezpieczeństwo agentów**: ryzyka (prompt injection, nadmierne uprawnienia narzędzi,
wyciek danych) i obronę **w głąb** (defense in depth) przez `before_tool_callback` -
callback sprawdzający argumenty narzędzia ZANIM się wykona.

## Zakres tego ćwiczenia
- Zrozumienie, jak `before_tool_callback` przechwytuje wywołanie narzędzia.
- Demo prompt injection na agencie SQL i obserwacja, że guardrail je blokuje.
- Warstwa 1 (narzędzie puszcza tylko SELECT) + warstwa 2 (callback) = obrona w głąb.

## Poza zakresem (gdzie indziej)
- Budowanie nowych narzędzi / funkcji - `05_sql_agent`, `bonus/`.
- Audyt/logowanie zapytań - bonus `B3_audyt_sql`.
- Ewaluacja i testy - moduły 7 i 12.

## Koncepcja w pigułce
Callback zwracający `dict` = blokada (narzędzie się nie wykona). Nie ufaj jednej
warstwie: nawet jeśli narzędzie samo ogranicza zapytania, callback to druga linia
obrony. Złota zasada: least privilege (baza read-only), walidacja wejść, human in
the loop dla groźnych akcji.

## Twoje zadanie
`agent.py` jest tu **gotowy** jako referencja do modułu 14. Uruchom w `adk web`,
spróbuj wymusić `DROP TABLE` przez prompt injection i zobacz, że guardrail blokuje.
Rozszerzenie (logowanie) zrobisz w bonusie `B3_audyt_sql`.

## "Działa", gdy
Próba nakłonienia agenta do zapytania modyfikującego bazę zostaje zablokowana przez
callback, a normalne pytania analityczne działają.
