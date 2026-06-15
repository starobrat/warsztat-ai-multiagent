"""ROZWIĄZANIE ex_24: LoopAgent - pętla z warunkiem stopu.

Wypełnione: LoopAgent z agenta skracacz + max_iterations jako twardy limit.
Pętla kończy się przez exit_loop (gdy hasło dość krótkie) albo po max_iterations.

Uruchom: uv run adk run solutions/ex_22_petla_agentow "..." (albo adk web).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model

from google.adk.agents import LoopAgent, LlmAgent
from google.adk.tools import exit_loop


skracacz = LlmAgent(
    name="skracacz",
    model=get_model(),
    description="Iteracyjnie skraca hasło reklamowe, aż będzie krótkie i mocne.",
    instruction=(
        "Skracasz hasło reklamowe w pętli, jedna iteracja = jedno skrócenie.\n"
        "Dotychczasowa najlepsza wersja: {haslo_robocze?}\n"
        "Jeśli powyżej jest już jakaś wersja, skróć JĄ; jeśli puste, skróć hasło "
        "z prośby użytkownika.\n"
        "ZAWSZE napisz w odpowiedzi nową, krótszą wersję hasła (mniej słów, "
        "mocniej) - to jest wynik tej iteracji.\n"
        "Dopiero gdy hasło ma maksymalnie 4 słowa i nie da się go sensownie "
        "skrócić, na końcu tej samej odpowiedzi wywołaj narzędzie exit_loop, żeby "
        "zakończyć pętlę."
    ),
    tools=[exit_loop],
    output_key="haslo_robocze",
)

root_agent = LoopAgent(
    name="petla_skracania",
    description="Powtarza skracanie hasła, aż będzie krótkie (lub do limitu iteracji).",
    sub_agents=[skracacz],
    max_iterations=5,
)
