"""ROZWIĄZANIE ex_20: SequentialAgent - sztywna kolejność i output_key.

Agent A zapisuje temat pod output_key="temat", agent B czyta go przez {temat}.
SequentialAgent gwarantuje kolejność A -> B.

Uruchom: uv run adk run solutions/ex_20_sekwencja "..." (albo adk web).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model

from google.adk.agents import LlmAgent, SequentialAgent


agent_pomyslodawca = LlmAgent(
    name="agent_pomyslodawca",
    model=get_model(),
    description="Wymyśla jeden konkretny temat na krótki wpis.",
    instruction=(
        "Wymyśl JEDEN konkretny temat na krótki wpis blogowy o programowaniu. "
        "Zwróć sam temat, jedno zdanie, po polsku."
    ),
    output_key="temat",
)

agent_rozwijacz = LlmAgent(
    name="agent_rozwijacz",
    model=get_model(),
    description="Rozwija podany temat w 3 punktach.",
    instruction=(
        "Masz temat wpisu: {temat}\n"
        "Rozwiń go w 3 zwięzłych punktach (po polsku). Trzymaj się dokładnie tego "
        "tematu - nie zmieniaj go."
    ),
)

root_agent = SequentialAgent(
    name="sekwencja",
    description="Dwa kroki po kolei: wymyśl temat, potem go rozwiń.",
    sub_agents=[agent_pomyslodawca, agent_rozwijacz],
)
