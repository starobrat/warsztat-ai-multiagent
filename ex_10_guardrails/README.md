# Ćwiczenie: bezpieczeństwo - guardrail (moduł 14)

## Co ćwiczymy
**Bezpieczeństwo agentów**: ryzyka (prompt injection, nadmierne uprawnienia narzędzi,
wyciek danych) i obronę **w głąb** (defense in depth) przez `before_tool_callback` -
callback sprawdzający argumenty narzędzia ZANIM się wykona.

## Zakres tego ćwiczenia
- Napisanie `before_tool_callback`, który przechwytuje wywołanie narzędzia.
- Demo prompt injection na agencie SQL i sprawdzenie, że Twój guardrail je blokuje.
- Warstwa 1 (narzędzie puszcza tylko SELECT) + warstwa 2 (callback) = obrona w głąb.

## Poza zakresem (gdzie indziej)
- Budowanie nowych narzędzi / funkcji - `ex_05_sql_agent`, `bonus/`.
- Audyt/logowanie zapytań - bonus `B3_audyt_sql`.
- Ewaluacja i testy - moduły 7 i 12.

## Koncepcja w pigułce
Callback zwracający `dict` = blokada (narzędzie się nie wykona). Nie ufaj jednej
warstwie: nawet jeśli narzędzie samo ogranicza zapytania, callback to druga linia
obrony. Złota zasada: least privilege (baza read-only), walidacja wejść, human in
the loop dla groźnych akcji.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz ciało `block_dangerous_sql` - dla wywołania
`run_query` z groźnym wzorcem zwróć blokadę, w innym wypadku przepuść. Potem uruchom
w `adk web`, spróbuj wymusić `DROP TABLE` przez prompt injection i sprawdź, że Twój
guard trzyma. Rozszerzenie (logowanie) zrobisz w bonusie `B3_audyt_sql`.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `tool.name == "run_query"`, `args.get("sql")`, `str.lower()`,
  `any(word in sql for word in _FORBIDDEN)`.
- Zwróć `dict` (np. `{"error": "..."}`) żeby zablokować, `None` żeby przepuścić.

## "Działa", gdy
Próba nakłonienia agenta do zapytania modyfikującego bazę zostaje zablokowana przez
callback, a normalne pytania analityczne działają - i nie umiesz go obejść w 2 minuty.

## Pójdź dalej
- Spróbuj OBEJŚĆ własny guard (komentarze w SQL, wielkość liter, spacje) - trzyma?
- Dołóż logowanie zablokowanych prób (bonus B3) - observability bezpieczeństwa.
- Wypisz inne ryzyka (nadmiarowe uprawnienia, wyciek danych w odpowiedzi) i jak byś je załatał.
