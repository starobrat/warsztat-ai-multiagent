# Ćwiczenie: pierwszy agent w ADK (moduł 5)

## Co ćwiczymy
**Wejście w Google ADK 2.0.** Ten sam pomysł co Twoja ręczna pętla z części 1,
ale teraz ADK ogarnia za Ciebie pętlę, sesje, interfejs webowy i ewaluację.
Skupiamy się na: czym jest `LlmAgent` i jak go uruchomić.

## Zakres tego ćwiczenia
- Minimalny `LlmAgent` (name, model, instruction).
- Uruchomienie w `adk web 04_hello` i w `adk run 04_hello`.
- Obserwacja, jak zmiana `instruction` zmienia zachowanie.

## Poza zakresem (przyjdzie później)
- Narzędzia (FunctionTool) - `05_sql_agent` (moduł 6).
- Pamięć i sesje - `05_sql_agent` (moduł 6).
- Wieloagentowość - `08_report_system` (moduły 9-11).
- Ewaluacja - `06_evaluation/` (moduł 7).
- Bezpieczeństwo / guardraile - `10_guardrails` (moduł 14).

## Koncepcja w pigułce
`LlmAgent` to deklaratywny agent: opisujesz rolę (`instruction`) i - później -
narzędzia. ADK uruchamia pętlę i daje interfejs. To "to samo, co pisałeś ręcznie",
tylko że pętlę i I/O masz gotowe.

## Twoje zadanie
`agent.py` jest tu **gotowy** jako referencja. Uruchom go w `adk web`, porozmawiaj
z nim, podmień `instruction` i zobacz różnicę. Następne ćwiczenia będą już z `# TODO(you)`.

## "Działa", gdy
W przeglądarce rozmawiasz z agentem `hello`, a zmiana instrukcji widocznie zmienia
jego odpowiedzi.
