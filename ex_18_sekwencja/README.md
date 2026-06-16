# Ćwiczenie ex_18: SequentialAgent (moduł 9/10)

<!-- [TODO Piotr - ŁUK: w ex_17 to MODEL wybierał, komu przekazać. Tu kolejność
jest narzucona z góry - pierwszy krok, potem drugi, zawsze tak samo. I pokazujemy,
jak dane przepływają z agenta do agenta przez output_key.] -->

## Co ćwiczymy
**`SequentialAgent` i przepływ danych przez `output_key`.** Sekwencja uruchamia
sub-agentów po kolei (gwarantowana kolejność, bez decyzji modelu). Agent A zapisuje
wynik pod `output_key`, agent B czyta go w instrukcji przez `{klucz}`.

## Które narzędzia podpinamy
- Brak narzędzi - to ćwiczenie jest o ORKIESTRACJI, nie o tools.
- Klocek przepływu: `output_key` (agent A) + templating `{klucz}` (agent B).

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Ustaw `output_key` w `agent_pomyslodawca` (np. `"temat"`).
2. W instrukcji `agent_rozwijacz` odwołaj się do tego wyniku przez `{temat}`.
3. Złóż obu w `SequentialAgent(sub_agents=[agent_pomyslodawca, agent_rozwijacz])`.

## Jak sprawdzić, że działa
- `uv run adk run ex_18_sekwencja "zacznij"` lub `adk web ex_18_sekwencja`.
- W Traces widać dwa kroki po kolei; drugi agent operuje na temacie z pierwszego.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś, by asystent wyjaśnił RÓŻNICĘ między
transferem (ex_17) a sekwencją - kto tu decyduje o kolejności. Bez gotowej instrukcji.

## "Działa", gdy
Drugi agent rozwija DOKŁADNIE ten temat, który wymyślił pierwszy - czyli dane
przepłynęły przez `output_key` (`{temat}` nie zostało puste).

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_19: dwa kroki to rozgrzewka.
Prawdziwy pipeline ma trzy: planista -> dane -> raport. W ex_19 piszemy mózg
całego raportu - plannera.] -->
