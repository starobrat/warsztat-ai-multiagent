# Ćwiczenie: wywołanie LLM i parametry (moduł 2)

## Co ćwiczymy
Najprostszy typ aplikacji z LLM: **jeden krok, jedno wywołanie**. Proces biznesowy,
w którym LLM coś nam odpowiada. Plus wpływ **parametrów** (temperature, top_p,
max_tokens) i **promptu systemowego** (roli) na odpowiedź.

## Zakres tego ćwiczenia
- Wywołanie modelu bezpośrednio przez OpenAI SDK.
- Prompt systemowy nadający rolę.
- Eksperyment z parametrami i porównanie odpowiedzi.

## Poza zakresem (przyjdzie później)
- Narzędzia / function calling - ćwiczenie 02.
- Pętla, w której model sam decyduje o krokach - ćwiczenie 03.
- ADK i cokolwiek z części 2.

## Koncepcja w pigułce
LLM to funkcja: tekst wejściowy -> tekst wyjściowy, niedeterministycznie.
`temperature` steruje losowością (0 = zachowawczo, wyżej = kreatywniej). Rola
(system prompt) ustawia kontekst, w jakim model odpowiada. Tu nie ma jeszcze
żadnej "akcji" - model tylko generuje tekst.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`): **napisz własny prompt systemowy (rolę), poproś
model o krótki wiersz o tym szkoleniu (aplikacje wieloagentowe) i uruchom raz przy
temperaturze 0.2, a potem przy 0.8.** Skrypt wykonuje jedno wywołanie na uruchomienie.

## "Działa", gdy
Ten sam wiersz przy temperaturze 0.2 i 0.8 daje zauważalnie różne odpowiedzi,
a zmiana roli w prompcie zmienia ton i treść.

## Pójdź dalej
- Pozmieniaj inne parametry (`top_p`, `max_tokens`, `presence_penalty`) i opisz wpływ.
- Ta sama treść, różne role (analityk vs sprzedawca vs sceptyk) - jak zmienia się odpowiedź?
- Znajdź pytanie, gdzie temperatura prawie nic nie zmienia, i takie, gdzie zmienia wszystko. Dlaczego?
