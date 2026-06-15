# Ćwiczenie ex_08: pierwsze narzędzie + grounding (moduł 6)

<!-- [TODO Piotr - ŁUK / "gdzie jesteśmy": w ex_04 agent miał tylko instrukcję i
pewnie zmyślał liczby z bazy. Teraz dajemy mu PIERWSZE narzędzie - i od razu uczymy
dyscypliny, żeby nie zmyślał, gdy danych brak. Twój głos.] -->

## Co ćwiczymy
Dwa sklejone koncepty (były osobno jako ex_08 i ex_09, teraz razem):
1. **Pierwszy kontakt agenta z narzędziem** - podłączasz `get_schema` i widzisz
   wywołanie w Events / Traces.
2. **Grounding** - instrukcja jako bezpiecznik: agent odpowiada WYŁĄCZNIE z danych
   narzędzi, a bez danych ODMAWIA (zamiast halucynować).

## Które narzędzia podpinamy
- `get_schema` (gotowe, `common/tools/db.py`) - zwraca strukturę bazy Chinook.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. **Podłącz `get_schema`** do `tools` (import już jest).
2. **Napisz instrukcję-grounding**: odpowiadaj tylko na podstawie narzędzi; gdy
   narzędzie nie daje odpowiedzi (pytanie spoza bazy) - powiedz, że nie wiesz.
   <!-- [TODO Piotr: gotowiec/wskazówka brzmienia instrukcji - Twój głos] -->
3. Uruchom `uv run adk web ex_08_narzedzie_grounding`.

## Jak sprawdzić, że działa
- **Events**: `functionCall get_schema` (nie sam tekst) przy pytaniu o strukturę.
- Pytanie spoza bazy ("kto wygrał mecz?") -> agent ODMAWIA, nie zmyśla.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, żeby przeprowadził Cię przez to,
**czym jest narzędzie w ADK**, **jak agent decyduje, że je wywołać** i **czemu sama
instrukcja nie jest twardą gwarancją** - nie o gotowy kod.

## "Działa", gdy
W Events widać `get_schema`, odpowiedź o strukturze pochodzi z narzędzia, a pytanie
spoza danych kończy się odmową, nie zmyśloną odpowiedzią.

## Pójdź dalej
<!-- [TODO Piotr - CLIFFHANGER do ex_09 (docstring): dołożymy drugie narzędzie -
skąd model wie, KTÓRE wybrać? Od docstringa. Twój głos.] -->
