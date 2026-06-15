# Ćwiczenie: pamięć długoterminowa - Memory ponad rozmowy (moduł 6)

## Co ćwiczymy
Różnicę między **stanem sesji** (ex_05) a **pamięcią długoterminową**. State ginie
razem z rozmową; Memory przeżywa wiele rozmów. W ADK pamięć długoterminowa to
osobny `MemoryService` plus narzędzie `load_memory`, którym agent SAM przeszukuje
przeszłe rozmowy, gdy bieżąca rozmowa nie wystarcza.

## Zakres tego ćwiczenia
- `InMemoryMemoryService` podpięty do `Runner(memory_service=...)`.
- Narzędzie `load_memory` w agencie.
- `add_session_to_memory(...)` - zapis zakończonej rozmowy do pamięci.
- Dowód na żywo: nowa sesja odzyskuje fakt z poprzedniej.

## Poza zakresem (przyjdzie później)
- Kompaktowanie / rolling window rosnącego kontekstu - ex_07.
- Produkcyjna pamięć (VertexAiMemoryBank, RAG) - tu używamy wersji InMemory.
- Narzędzia bazodanowe i agenci `adk web` - od ex_08.

## Koncepcja w pigułce
Model jest bezstanowy. "Pamięć" to ktoś, kto dokłada potrzebne fragmenty do okna
kontekstu. W ex_05 tym kimś był stan sesji (ginął z rozmową). Tu pamięć żyje w
osobnym serwisie: po rozmowie robisz `add_session_to_memory(session)`, a w kolejnej
rozmowie agent woła `load_memory`, dostaje znalezione fragmenty i na nich odpowiada.
To jest dokładnie wzorzec RAG: wyszukaj -> doklej -> odpowiedz.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`):
1. Napisz `INSTRUKCJA` - kiedy agent ma sięgać do `load_memory` (gdy nie wie z
   bieżącej rozmowy), a nie zmyślać.
2. Podłącz narzędzie: `tools=[load_memory]`.
3. W `main` zapisz zakończoną sesję 1 do pamięci (`zapisz_sesje_do_pamieci("s1")`).

## Wskazówki (jeśli pracujesz bez agenta AI)
- `load_memory` importujesz gotowe z `google.adk.tools` - tylko wkładasz do `tools`.
- Pamięć działa, bo `Runner` dostał `memory_service` (już podłączone w klockach).
- `add_session_to_memory` potrzebuje obiektu sesji - masz na to helper.

## "Działa", gdy
W sesji 2 (NOWEJ rozmowie) agent odpowiada poprawnie "masz na imię Piotr, pracujesz
nad raportem sprzedaży Rocka", a na liście narzędzi widać `load_memory`. Bez kroku 3
(zapis do pamięci) sesja 2 nie wie nic - tak jak w ex_05.

## Pójdź dalej
- Usuń krok 3 (zapis do pamięci) i zobacz, że agent znów "zapomina" - to różnica
  między State a Memory.
- Zadaj w sesji 2 pytanie, którego NIE było w sesji 1 - czy agent zmyśla, czy mówi,
  że nie wie? Dostrój instrukcję.
- Dołóż drugą sesję z innym faktem i sprawdź, czy `load_memory` wyciąga właściwy.
