# Ćwiczenie: wywołanie LLM i parametry (moduł 2)

## Co ćwiczymy
Najprostszy typ aplikacji z LLM: **jeden krok, jedno wywołanie**. Proces biznesowy,
w którym LLM coś nam odpowiada. Plus wpływ **parametrów** (temperature, top_p,
max_tokens) i **promptu systemowego** (roli) na odpowiedź.

## Zakres tego ćwiczenia
- Wywołanie modelu przez OpenRouter (OpenAI SDK + base_url).
- Prompt systemowy nadający rolę.
- Eksperyment z parametrami i porównanie odpowiedzi.

## Poza zakresem (przyjdzie później)
- Narzędzia / function calling — ćwiczenie 02.
- Pętla, w której model sam decyduje o krokach — ćwiczenie 03.
- ADK i cokolwiek z części 2.

## Koncepcja w pigułce
LLM to funkcja: tekst wejściowy -> tekst wyjściowy, niedeterministycznie.
`temperature` steruje losowością (0 = zachowawczo, wyżej = kreatywniej). Rola
(system prompt) ustawia kontekst, w jakim model odpowiada. Tu nie ma jeszcze
żadnej "akcji" — model tylko generuje tekst.

## Twoje zadanie
Patrz `starter.py`: napisz prompt systemowy i porównaj odpowiedzi dla różnych
temperatur.

## "Działa", gdy
Widzisz, że ta sama prośba przy temperature=0 i temperature=1 daje zauważalnie
różne odpowiedzi, a rola zmienia ton/treść.
