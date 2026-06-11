# Ćwiczenie: pierwszy agent w ADK (moduł 5)

## Co ćwiczymy
**Wejście w Google ADK 2.0.** Ten sam pomysł co Twoja ręczna pętla z części 1,
ale teraz ADK ogarnia za Ciebie pętlę, sesje, interfejs webowy i ewaluację.
Skupiamy się na: czym jest `LlmAgent` i jak go uruchomić.

## Zakres tego ćwiczenia
- Minimalny `LlmAgent` (name, model, instruction).
- Uruchomienie w `adk web part2_adk/agents` i w `adk run`.
- Obserwacja, jak zmiana `instruction` zmienia zachowanie.

## Poza zakresem (przyjdzie później)
- Narzędzia (FunctionTool) — `agents/sql_agent` (moduł 6).
- Pamięć i sesje — `agents/sql_agent` (moduł 6).
- Wieloagentowość — `agents/report_system` (moduły 9-11).
- Ewaluacja — `part2_adk/evals/` (moduł 7).
- Bezpieczeństwo / guardraile — `agents/sql_agent_guarded` (moduł 14).

## Koncepcja w pigułce
`LlmAgent` to deklaratywny agent: opisujesz rolę (`instruction`) i — później —
narzędzia. ADK uruchamia pętlę i daje interfejs. To "to samo, co pisałeś ręcznie",
tylko że pętlę i I/O dostajesz z pudełka.

## Twoje zadanie
`agent.py` jest tu **gotowy** jako referencja. Uruchom go w `adk web`, pogadaj,
podmień `instruction` i zobacz różnicę. Następne ćwiczenia będą już z `# TODO(you)`.

## "Działa", gdy
W przeglądarce rozmawiasz z agentem `hello`, a zmiana instrukcji widocznie zmienia
jego odpowiedzi.
