# Ćwiczenie ex_11: raport z wykresem (moduł 6)

<!-- [TODO Piotr - ŁUK: w ex_10 agent policzył sprzedaż gatunków. Teraz robi
z tego ARTEFAKT - wykres. To payoff całego bloku narzędziowego.] -->

## Co ćwiczymy
**Agent produkuje artefakt.** Łączysz analitykę (gatunki + sprzedaż) z narzędziem
rysującym wykres słupkowy. Pytanie -> dane -> plik PNG.

## Które narzędzia podpinamy
- `get_genres`, `get_sold_count_for_genre` - dane (jak w ex_10).
- `narysuj_wykres_slupkowy(labels, values, title)` - rysuje wykres (PNG).

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz trzy narzędzia.
2. Napisz instrukcję: zbierz dane sprzedaży gatunków, a potem przekaż je do
   narzędzia wykresu.
3. Zapytaj "zrób wykres sprzedaży wg gatunku za 2025".

## Jak sprawdzić, że działa
- W Traces widać dane z `get_sold_count_for_genre`, a na końcu wywołanie
  `narysuj_wykres_slupkowy`.
- Powstaje plik `raport.png` z poprawnymi słupkami.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, jak agent
przekazuje wynik jednego narzędzia na wejście kolejnego - nie o gotową instrukcję.

## "Działa", gdy
Agent zbiera dane i generuje wykres PNG odpowiadający liczbom z bazy.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_12: jak UPEWNIĆ się, że agent
odpowiada dobrze za każdym razem? Czas na ewaluację.] -->
