# Bonus B5: Ewaluacja - przypadki brzegowe

## Zadanie
Dorzuć do test setu przypadki, na których agenci zwykle zawodzą:
- pytanie o dane, których NIE MA w bazie (agent powinien przyznać, że nie wie),
- pytanie wieloznaczne ("najlepszy artysta" - wg czego?),
- pytanie podchwytliwe z błędnym założeniem.

## Kroki
1. Nagraj te przypadki w `adk web` (zakładka Eval) albo dopisz do evalset ręcznie.
2. Uruchom eval i zobacz, które agent oblewa.
3. Popraw instrukcję tak, żeby agent radził sobie z brzegami (np. przyznawał niewiedzę).

## Czego się uczysz
Dobry test set to nie tylko "happy path". Brzegi pokazują prawdziwą jakość agenta.
