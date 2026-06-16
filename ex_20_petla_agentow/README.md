# Ćwiczenie ex_20: LoopAgent (moduł 11)

<!-- [TODO Piotr - ŁUK: mamy już trzy kształty orkiestracji - po kolei
(Sequential), naraz (Parallel), a teraz trzeci: powtarzaj, AŻ będzie dobrze.
To zamyka komplet wzorców wieloagentowych. I pierwszy raz agent SAM decyduje,
kiedy skończyć - przez narzędzie.] -->

## Co ćwiczymy
**`LoopAgent` i warunek stopu.** Pętla powtarza ten sam krok. Zatrzymuje się na
DWA sposoby: twardy limit `max_iterations` ORAZ miękki - agent sam woła `exit_loop`
(ustawia `escalate`), gdy uzna, że gotowe.

## Które narzędzia podpinamy
- `skracacz` (GOTOWY) - `LlmAgent` z narzędziem `exit_loop`, w pętli skraca hasło.
- `exit_loop` (z `google.adk.tools`) - kończy pętlę od środka.
- Klocek orkiestracji: `LoopAgent` z `max_iterations`.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz `sub_agents=[skracacz]` do `LoopAgent`.
2. Ustaw `max_iterations` (np. 5) jako twardy limit bezpieczeństwa.

## Jak sprawdzić, że działa
- `uv run adk run ex_20_petla_agentow "Skróć hasło: Najlepsze buty do biegania w mieście dla każdego"`
- W Traces widać kilka iteracji skracacza, a na końcu wywołanie `exit_loop`
  (lub zatrzymanie po `max_iterations`).

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś, by asystent wyjaśnił RÓŻNICĘ między
`max_iterations` a `exit_loop` - po co oba naraz. Bez gotowego kodu.

## "Działa", gdy
Agent powtarza skracanie kilka razy, a pętla kończy się przez `exit_loop` albo
po osiągnięciu `max_iterations` - nie kręci się w nieskończoność.

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie: dodaj drugiego agenta-krytyka w pętli (writer ->
critic), który ocenia hasło i decyduje, czy wołać exit_loop. Klasyczna pętla
generator-krytyk.] -->
