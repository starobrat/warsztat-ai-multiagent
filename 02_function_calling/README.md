# Ćwiczenie: function calling napisany samodzielnie (moduł 3)

## Co ćwiczymy
**Mechanikę function callingu** - najważniejszy model myślowy całego szkolenia:
LLM **nie wykonuje** akcji. LLM **decyduje** (generuje tekst/JSON: które narzędzie
i z jakimi argumentami), a **Twój kod** to narzędzie wywołuje.

## Zakres tego ćwiczenia
- Prompt, który każe modelowi zwrócić decyzję jako JSON (`tool` + `args`).
- Parsowanie tej decyzji.
- Wywołanie wskazanej funkcji po stronie Pythona i pokazanie wyniku.

## Poza zakresem (przyjdzie później)
- Powtarzanie w pętli aż do odpowiedzi - ćwiczenie 03 (pętla agentyczna).
- Prawdziwa baza danych - ćwiczenie 03.
- Automatyczny function calling robiony przez ADK - część 2 (tu robimy go RĘCZNIE celowo).

## Koncepcja w pigułce
Pętla decyzji: model dostaje opis narzędzi -> zwraca `{"tool": "...", "args": {...}}`
albo `{"tool": null, "answer": "..."}`. Twój kod sprawdza, co model wybrał, i jeśli
wskazał narzędzie - sam je uruchamia. To wszystko. Cała "magia" agentów to ta jedna
mechanika powtórzona w pętli.

Typowy błąd do sprostowania: "model wykona funkcję". Nie - model tylko generuje
tekst, a wywołanie wykonuje Twój kod.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`): dokończ prompt systemowy, sparsuj decyzję modelu,
wywołaj narzędzie z `tools.py`.

## "Działa", gdy
Na pytanie "ile to 17 + 25" kod wywołuje `add(17, 25)` i pokazuje 42; na pytanie
o coś ogólnego model odpowiada sam (`tool: null`).
