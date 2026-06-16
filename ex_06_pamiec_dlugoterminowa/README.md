# Ćwiczenie: pamięć faktów o użytkowniku - ponad sesjami (moduł 6)

## Co ćwiczymy
Różnicę między **stanem sesji** (ex_05) a **stanem użytkownika**. State bez prefiksu
ginie razem z rozmową; stan z zasięgiem `user:` jest przypisany do użytkownika i
**przeżywa kolejne sesje**. To najprostszy sposób, by agent pamiętał trwałe fakty
o rozmówcy (np. ulubione gatunki, z kim współpracuje) między rozmowami.

## Zakres tego ćwiczenia
- Dwa gotowe narzędzia: `zapamietaj_fakt(kategoria, wartosc)` i `przypomnij_fakty()`.
- Zapis do stanu z zasięgiem `user:` (`tool_context.state["user:fakty"]`).
- Dowód na żywo: nowa sesja tego samego użytkownika odzyskuje fakty bez dopytywania.

## Poza zakresem (przyjdzie później)
- Kompaktowanie / rolling window rosnącego kontekstu - ex_07.
- Pamięć typu RAG nad CAŁYMI rozmowami (`MemoryService` + `load_memory`,
  produkcyjnie VertexAiMemoryBank) - omawiamy na slajdzie jako koncept, bez ćwiczenia.
- Narzędzia bazodanowe i agenci `adk web` - od ex_08.

## Koncepcja w pigułce
Model jest bezstanowy. "Pamięć" to ktoś, kto dokłada potrzebne fragmenty do okna
kontekstu. W ex_05 tym kimś był stan sesji - ginął z rozmową. Tu używamy stanu z
zasięgiem `user:`: cokolwiek zapiszesz pod kluczem `user:...`, ADK wiąże z
użytkownikiem, nie z pojedynczą sesją. Dzięki temu w NOWEJ rozmowie tego samego
użytkownika te fakty nadal są dostępne - agent je odczytuje i odpowiada na nich.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`):
1. **Napisz `INSTRUKCJA`** - kiedy agent ma wołać `zapamietaj_fakt` (gdy user podaje
   trwały fakt o sobie), a kiedy `przypomnij_fakty` (gdy pyta, co o nim wiesz).
   Bez faktu - niech powie, że nie wie, a nie zmyśla.
2. **Podłącz narzędzia**: `tools=[zapamietaj_fakt, przypomnij_fakty]`.

## Wskazówki (jeśli pracujesz bez agenta AI)
- Narzędzia są gotowe - tylko wkładasz je do `tools` i opisujesz w instrukcji, kiedy ich użyć.
- Zasięg `user:` działa, bo klucz ma prefiks `user:` - ADK trzyma go per użytkownik, nie per sesja.
- Nie musisz nic "zapisywać po rozmowie" - stan `user:` utrzymuje się sam.

## "Działa", gdy
W sesji 2 (NOWEJ rozmowie) agent odpowiada poprawnie "interesują Cię Rock i Jazz,
współpracujesz z Jane Peacock", woła `przypomnij_fakty`, a w sesji 1 widać wywołania
`zapamietaj_fakt`. Gdyby klucz nie miał prefiksu `user:` (zwykły stan sesji), sesja 2
nic by nie wiedziała - tak jak w ex_05.

## Pójdź dalej
- Zmień klucz z `user:fakty` na `fakty` (bez prefiksu) i zobacz, że sesja 2 znów
  "zapomina" - to dowód, że to zasięg `user:` daje trwałość ponad sesjami.
- Zadaj w sesji 2 pytanie o fakt, którego NIE podałeś w sesji 1 - czy agent zmyśla,
  czy mówi, że nie wie? Dostrój instrukcję.
- Dla zaawansowanych: porównaj to z `MemoryService` + `load_memory` (RAG nad całymi
  rozmowami) - kiedy proste fakty `user:` wystarczą, a kiedy potrzebujesz wyszukiwania?
