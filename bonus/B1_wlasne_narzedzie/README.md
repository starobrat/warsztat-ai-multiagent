# Bonus B1: Własne narzędzie od zera

**Kiedy:** dla osób, które skończyły szybciej, albo jako praca własna.

## Zadanie
Dodaj agentowi narzędzie, którego nie ma w `tools/`: pobranie kursu waluty z
publicznego API (np. NBP: `https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json`)
i przeliczenie sprzedaży z bazy na PLN.

## Kroki
1. Napisz funkcję `eur_to_pln(amount: float) -> dict` z docstringiem (to będzie FunctionTool).
2. Podłącz ją do `sql_agent` obok `get_schema`, `run_query`.
3. Zapytaj: "Jaka jest łączna sprzedaż w przeliczeniu na PLN?"

## Czego się uczysz
Integracja z zewnętrznym API jako narzędzie agenta - to samo, co robi każde
realne narzędzie produkcyjne (pogoda, kursy, CRM).
