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
    --config_file_path ex_16_modele_i_diagnostyka/test_config.json
```

## Pointa
Zanim coś naprawisz - **zdiagnozuj warstwę**. Eval pokazuje nie tylko "źle", ale i
GDZIE: zła trajektoria narzędzi -> opis narzędzia; brak wywołania narzędzia -> instrukcja;
błąd mimo dobrego opisu -> model. Mocniejszy model maskuje złe opisy; na słabszym każda
warstwa ma znaczenie.
