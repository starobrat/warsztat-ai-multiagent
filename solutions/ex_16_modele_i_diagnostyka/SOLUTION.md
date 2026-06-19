# Rozwiązanie ex_16: modele i diagnostyka

## Diagnoza
Eval był czerwony, bo agent wybierał **złe narzędzie**. W raporcie widać: na pytanie
o sprzedaż AC/DC padało `albums_by_artist` zamiast `sales_by_artist` (zła trajektoria).
Przyczyna nie leżała w modelu ani w samej instrukcji, tylko w **opisach narzędzi** -
docstringi kłamały:
- `sales_by_artist` (zwraca sprzedaż) miał opis "Zwraca albumy wykonawcy",
- `albums_by_artist` (zwraca albumy) miał opis "Liczy, ile sztuk sprzedano",
- `sales_by_genre` i `list_genres` miały opisy bezużyteczne ("Coś o gatunku", "Lista").

Słaby model dobiera narzędzie **po docstringu** - skoro opis kłamie, wybór jest zły.

## Naprawa
Tylko **opisy** (docstringi) i **instrukcja** - nazwy funkcji i ich środek bez zmian:
- każdy docstring mówi prawdę i wprost ("Użyj, gdy klient pyta...") + udokumentowany `Args`,
- instrukcja mapuje typ pytania na narzędzie (sprzedaż wykonawcy -> `sales_by_artist`,
  albumy -> `albums_by_artist`, sprzedaż gatunku -> `sales_by_genre`, lista -> `list_genres`)
  i zakazuje odpowiadania z pamięci.

Po poprawie eval przechodzi (zielony) mimo słabszego modelu.

## Uruchomienie
```bash
uv run adk eval solutions/ex_16_modele_i_diagnostyka \
    ex_16_modele_i_diagnostyka/diagnostyka.evalset.json \
    --config_file_path solutions/ex_16_modele_i_diagnostyka/test_config.json
```
Rozwiązanie używa własnego `test_config.json` (config ćwiczenia zostaje nietknięty) -
dokłada dwie własne metryki poza dwiema wbudowanymi: deterministyczną
`answer_correct_score` i sędziego-LLM `answer_polite_score`.

## Custom metric: `answer_correct_score`
Wbudowane metryki sprawdzają trajektorię (które narzędzie) i pokrycie tekstu (ROUGE).
Żadna nie mówi wprost: czy w odpowiedzi padła **właściwa wartość z bazy**. Dokładamy
więc własną metrykę (`correctness_metric.py`), podpiętą w `test_config.json` przez
`custom_metrics` -> `code_config.name`.

Jak liczy poprawność:
1. Z wzorcowego przypadku bierze, które narzędzie i z jakim argumentem POWINNO paść.
2. Wykonuje to narzędzie na realnej bazie -> ground truth (16, 835, lista albumów).
3. Sprawdza, czy odpowiedź agenta zawiera każdą z tych wartości. Wynik = ułamek
   trafionych wartości; próg `1.0` = wszystkie muszą paść.

Dlaczego ground truth z wzorcowego wywołania, a nie z tego, co zrobił agent: dzięki
temu metryka jest niezależnym sprawdzianem obok trajektorii - łapie też złą odpowiedź
udzieloną mimo właściwego narzędzia. Liczy się deterministycznie, bez sędziego-LLM.

Uwaga na przypadek "albumy": agent zwykle nie powtarza liczby "2", za to wymienia oba
tytuły - dlatego metryka sprawdza wartości zwrócone przez narzędzie (tytuły), a nie
liczby wyłuskane z wzorcowego zdania. Naiwny test "czy liczba się zgadza" by tu oblał.

## Custom metric: `answer_polite_score` (sędzia-LLM)
Grzeczność to ocena miękka - nie policzysz jej regexem ani porównaniem z bazą. Dlatego
druga własna metryka (`politeness_metric.py`) woła **sędziego-LLM**: osobnego agenta
ADK (`LlmAgent` na mocniejszym modelu), odpalanego przez `Runner` per odpowiedź.

Jak liczy grzeczność:
1. Dla każdej odpowiedzi agenta odpala agenta-sędziego (świeża sesja w `Runner`).
2. Sędzia zwraca samą liczbę 0.0-1.0 (1.0 = uprzejma/neutralnie rzeczowa,
   0.0 = niegrzeczna/lekceważąca). Ton rzeczowy bez "proszę/dziękuję" = nadal grzeczny.
3. Wynik metryki = średnia ocen; próg `0.6` w `test_config.json`.

Dwie nauki z tej metryki:
- **kiedy sędzia-LLM, a kiedy kod**: poprawność (wartość z bazy) liczymy
  deterministycznie; grzeczność - tylko LLM. Custom metric obejmuje oba przypadki.
- **ten sam mechanizm ocenia mechanizm**: sędzia to zwykły agent ADK. Sprawdzony
  ręcznie - odpowiedź szorstka ("sam się doczytaj, nie zawracaj mi głowy") dostaje
  0.0 i oblewa próg; odpowiedzi rzeczowe z evalsetu dostają 1.0.

Koszt/wada: każda ocena to wywołanie modelu (wolniej, niedeterministycznie) -
dlatego sędziego-LLM dokładamy świadomie tam, gdzie kod nie wystarcza.

## Pointa
Zanim coś naprawisz - **zdiagnozuj warstwę**. Eval pokazuje nie tylko "źle", ale i
GDZIE: zła trajektoria narzędzi -> opis narzędzia; brak wywołania narzędzia -> instrukcja;
błąd mimo dobrego opisu -> model. Mocniejszy model maskuje złe opisy; na słabszym każda
warstwa ma znaczenie.
