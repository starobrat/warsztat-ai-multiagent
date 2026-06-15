# Ćwiczenie ex_07: instrukcja-grounding (moduł 6)

<!-- [TODO Piotr - ŁUK: w ex_06 agent dostał narzędzie i woła get_schema, ale gdy
spytasz o coś spoza danych - nadal potrafi zmyślić. Teraz go dyscyplinujemy.] -->

## Co ćwiczymy
**Grounding: agent odpowiada wyłącznie na podstawie narzędzi, a bez danych -
odmawia.** Jeden koncept: instrukcja jako bezpiecznik przeciw halucynacji.

## Które narzędzia podpinamy
- `get_schema` (już podłączone) - tu nie dokładamy narzędzi, pracujemy nad instrukcją.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): podmień placeholder na instrukcję, która:
- każe odpowiadać TYLKO na podstawie danych z narzędzi,
- każe ODMÓWIĆ ("nie mam danych"), gdy narzędzie nie daje odpowiedzi.
<!-- [TODO Piotr: ewentualny gotowiec/wskazówka brzmienia instrukcji] -->

## Jak sprawdzić, że działa
- Zapytaj o strukturę -> agent woła `get_schema` i odpowiada z danych.
- Zapytaj o coś spoza bazy ("kto wygrał mecz?") -> agent ODMAWIA, nie zmyśla.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, żeby wytłumaczył, czemu sama
instrukcja nie jest twardą gwarancją - nie o gotową instrukcję.

## "Działa", gdy
Pytanie z danych -> odpowiedź z narzędzia; pytanie spoza danych -> odmowa.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_08: agent ma jedno narzędzie;
gdy dołożymy drugie, skąd model wie, którego użyć? Od docstringa.] -->
