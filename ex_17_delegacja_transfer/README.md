# Ćwiczenie ex_19: delegacja przez transfer (moduł 9)

<!-- [TODO Piotr - ŁUK: do tej pory budowaliśmy JEDNEGO agenta z narzędziami.
Tu pierwszy raz agent przekazuje sterowanie INNEMU agentowi - to wejście w
wieloagentowość.] -->

## Co ćwiczymy
**Delegację sterowaną przez LLM (transfer).** Master `LlmAgent` ma `sub_agents`,
ale sam nie wykonuje zadania - na podstawie `description` każdego specjalisty
model decyduje, KOMU przekazać pytanie. Routing robi LLM, nie sztywny kod.

## Które narzędzia podpinamy
- `agent_powitan` (sub-agent, GOTOWY) - powitania, small talk, bez narzędzi.
- `analityk_chinook` (sub-agent, GOTOWY) - dane sklepu Chinook, `get_schema` + `run_query`.
- Master nie dostaje własnych narzędzi - jego "narzędziem" są sub-agenci.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. Podłącz obu specjalistów jako `sub_agents=[agent_powitan, analityk_chinook]`.
2. Napisz instrukcję mastera: kiedy delegować do kogo (powitania -> `agent_powitan`,
   pytania o dane sklepu -> `analityk_chinook`).
3. Zadaj jedno pytanie "danych" i jedno "powitalne" - prześledź transfer w Traces.

## Jak sprawdzić, że działa
- `uv run adk web ex_17_delegacja_transfer`, potem zakładka Traces.
- Pytanie o dane ("ilu mamy klientów z Niemiec?") -> transfer do `analityk_chinook`.
- Powitanie ("cześć, co słychać?") -> transfer do `agent_powitan`.

## Praca z agentem AI
Bramka sokratejska (`CLAUDE.md`): poproś asystenta, by wyjaśnił, na podstawie
CZEGO master wybiera sub-agenta (rola `description`) - nie o gotową instrukcję.

## "Działa", gdy
W Traces widać, że master przekazał zadanie właściwemu sub-agentowi, a odpowiedź
przychodzi od niego (analityk sięga po `get_schema`/`run_query`).

## Pójdź dalej
<!-- [TODO Piotr - rozszerzenie + CLIFFHANGER do ex_20: transfer to swoboda -
model SAM decyduje. A jeśli kolejność kroków ma być sztywna, gwarantowana? Wtedy
SequentialAgent - następne ćwiczenie.] -->
