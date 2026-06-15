# Ćwiczenie ex_08: pierwsze narzędzie (moduł 6)

<!-- [TODO Piotr - ŁUK / "gdzie jesteśmy": 1-2 zdania kontynuacji z ex_04.
Np.: w ex_04 agent miał tylko instrukcję i pewnie zmyślał liczby z bazy.
Teraz dajemy mu PIERWSZE narzędzie, żeby przestał zgadywać. Twój głos.] -->

## Co ćwiczymy
**Pierwszy kontakt agenta z narzędziem.** Podłączasz jedno gotowe narzędzie
(`get_schema`) i widzisz, jak agent je wywołuje - w zakładce Events i Traces.
Jeden koncept: pętla tool-callingu w praktyce.

## Które narzędzia podpinamy
- `get_schema` (gotowe, w `common/tools/db.py`) - zwraca strukturę bazy Chinook
  jako `{tabela: ["kolumna typ", ...]}`.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. **Podłącz `get_schema`** do `tools` (import już jest).
2. **Podmień instrukcję-placeholder** na prostą instrukcję. Gotowiec:
   <!-- [TODO Piotr: wklej tu prostą, gotową instrukcję dla uczestnika -
   np. rola: asystent od struktury bazy Chinook, odpowiada po polsku,
   przy pytaniu o strukturę woła get_schema]. -->
3. Uruchom `uv run adk web ex_08_pierwsze_narzedzie` i zapytaj o strukturę bazy.

## Jak sprawdzić, że działa
- Zakładka **Events**: pojawia się `functionCall` z `get_schema` (a nie sam tekst).
- Zakładka **Traces**: span wywołania narzędzia.
- Zanim podłączysz narzędzie, agent na każde pytanie odpowiada tylko wskazówką
  (to ta instrukcja-placeholder) - czyli "uruchom -> dostań info, co zrobić".

## Praca z agentem AI
To repo ma bramkę sokratejską (patrz `CLAUDE.md`): asystent nie wklei Ci
rozwiązania, dopóki nie pokażesz, że rozumiesz. Poproś go, żeby przeprowadził Cię
przez to, **czym jest narzędzie w ADK** i **jak agent decyduje, że je wywołać** -
nie o gotowy kod.

## "Działa", gdy
W Events widać wywołanie `get_schema`, a odpowiedź agenta o strukturze bazy
pochodzi z narzędzia, nie ze zgadywania.

## Pójdź dalej
<!-- [TODO Piotr - otwarte rozszerzenie + CLIFFHANGER do ex_09. Np.: agent woła
narzędzie, ale gdy spytasz o coś spoza schematu - nadal potrafi zmyślić.
W ex_09 ujarzmisz to instrukcją-grounding (agent odmawia bez danych). Twój głos.] -->
