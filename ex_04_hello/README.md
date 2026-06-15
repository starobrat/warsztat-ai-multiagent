# Ćwiczenie: pierwszy agent w ADK (moduł 5)

## Co ćwiczymy
**Wejście w Google ADK 2.0.** Ten sam pomysł co Twoja ręczna pętla z części 1,
ale teraz pętlę, sesje, interfejs webowy i ewaluację robi za Ciebie ADK.
Skupiamy się na: czym jest `LlmAgent` i jak go uruchomić.

## Zakres tego ćwiczenia
- Minimalny `LlmAgent` (name, model, instruction).
- Uruchomienie w `adk web ex_04_hello` i w `adk run ex_04_hello`.
- Obserwacja, jak zmiana `instruction` zmienia zachowanie.

## Poza zakresem (przyjdzie później)
- Narzędzia (FunctionTool) - `ex_16_text_to_sql` (moduł 6).
- Pamięć i sesje - `ex_16_text_to_sql` (moduł 6).
- Wieloagentowość - `ex_18_report_system` (moduły 9-11).
- Ewaluacja - `ex_15_eval/` (moduł 7).
- Bezpieczeństwo / guardraile - `ex_20_guardrails` (moduł 14).

## Koncepcja w pigułce
`LlmAgent` to deklaratywny agent: opisujesz rolę (`instruction`) i - później -
narzędzia. ADK uruchamia pętlę i daje interfejs. To "to samo, co pisałeś ręcznie",
tylko że pętlę i I/O masz gotowe.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz `instruction` swojego pierwszego agenta
(`name`, `model` i `description` masz już dane). Uruchom w `adk web`, porozmawiaj,
a potem podmień instrukcję i zobacz, jak zmienia się zachowanie.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `instruction` to zwykły string z rolą i zasadami odpowiadania - nic więcej tu nie trzeba.

## "Działa", gdy
W przeglądarce rozmawiasz z agentem `hello`, a zmiana instrukcji widocznie zmienia
jego odpowiedzi.

## Pójdź dalej
- Daj agentowi wyrazistą osobowość (zabawny sprzedawca, oschły ekspert) - jak zmienia się ton?
- Każ mu instrukcją podać liczbę z bazy (nie ma narzędzi) - zmyśli czy przyzna, że nie wie?
- Co odróżnia ten `LlmAgent` od Twojej ręcznej pętli z części 1? Wypisz 3 rzeczy.
