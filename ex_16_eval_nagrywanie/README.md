# Ćwiczenie ex_16: nagraj test set w adk web (moduł 7)

<!-- [TODO Piotr - ŁUK: pisanie evalsetu w JSON (ex_15) jest żmudne. ADK ma na to
wygodniejszą drogę - nagrywanie w przeglądarce. Twój głos.] -->

## Co ćwiczymy
**Nagrywanie test case'ów w GUI.** Zamiast pisać JSON ręcznie, prowadzisz rozmowę
w `adk web` i zapisujesz ją jako przypadek ewaluacyjny jednym kliknięciem.

## Twoje zadanie
1. `uv run adk web ex_14_text_to_sql` (Twój rozwiązany agent SQL).
2. Zakładka **Eval** -> nowa rozmowa -> zadaj 2-3 pytania, sprawdź odpowiedzi.
3. Zapisz je jako eval case'y do `ex_14_text_to_sql/` (ADK utworzy plik `.evalset.json`).
4. **Sprawdź oczekiwane liczby na bazie** - ADK zapisuje to, co odpowiedział agent;
   jeśli agent się pomylił, popraw oczekiwaną odpowiedź ręcznie.

## Jak sprawdzić, że działa
W zakładce Eval widać Twoje nagrane przypadki; możesz je odtworzyć i zobaczyć
metryki (trajektoria + dopasowanie odpowiedzi).

## "Działa", gdy
Masz nagrane 2-3 przypadki bez pisania JSON-a ręcznie, a oczekiwane odpowiedzi są
zweryfikowane na bazie (nie "co akurat powiedział agent").

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do ex_17: masz test set - jak uruchomić go hurtem
z terminala i odczytać metryki? Twój głos.] -->
