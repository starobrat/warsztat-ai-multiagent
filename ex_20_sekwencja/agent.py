"""Ćwiczenie ex_20: SequentialAgent - sztywna kolejność i output_key. STARTER.

Transfer (ex_19) zostawiał wybór modelowi. Tu kolejność jest GWARANTOWANA:
`SequentialAgent` uruchamia sub-agentów po kolei. Agent A zapisuje swój wynik pod
`output_key`, a agent B czyta go w instrukcji przez `{klucz}`.

Minimalny przykład (bez bazy, bez raportów): agent_pomyslodawca wymyśla temat,
agent_rozwijacz rozwija ten sam temat w 3 punktach.

Uruchom: uv run adk web ex_20_sekwencja (albo adk run ex_20_sekwencja).
"""

from common.exercise import placeholder
from common.model import get_model

from google.adk.agents import LlmAgent, SequentialAgent


# Agent A - produkuje wynik i zapisuje go pod output_key.
agent_pomyslodawca = LlmAgent(
    name="agent_pomyslodawca",
    model=get_model(),
    description="Wymyśla jeden konkretny temat na krótki wpis.",
    instruction=(
        "Wymyśl JEDEN konkretny temat na krótki wpis blogowy o programowaniu. "
        "Zwróć sam temat, jedno zdanie, po polsku."
    ),
    # TODO(you): pod jakim kluczem zapisać wynik, żeby agent B mógł go odczytać?
    output_key="",
)

# Agent B - konsumuje wynik agenta A przez {klucz} w instrukcji.
agent_rozwijacz = LlmAgent(
    name="agent_rozwijacz",
    model=get_model(),
    description="Rozwija podany temat w 3 punktach.",
    # TODO(you): w instrukcji odwołaj się do wyniku agenta A przez {klucz}
    # (ten sam, który ustawisz w output_key powyżej).
    instruction=placeholder(
        "ustaw output_key w agent_pomyslodawca i odwołaj się do niego przez {klucz} "
        "w tej instrukcji; potem złóż obu w SequentialAgent",
        readme="README ex_20_sekwencja",
    ),
)

# Master = sztywna sekwencja kroków A -> B.
root_agent = SequentialAgent(
    name="sekwencja",
    description="Dwa kroki po kolei: wymyśl temat, potem go rozwiń.",
    # TODO(you): podłącz oba agenty we właściwej kolejności.
    sub_agents=[],
)
