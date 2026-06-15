"""Ćwiczenie ex_05: pamięć i sesje - moduł 6. STARTER.

Pierwsze spotkanie z PAMIĘCIĄ agenta w ADK. Agent dostaje dwa gotowe narzędzia,
które zapisują i czytają STAN sesji (`tool_context.state`). W obrębie jednej
rozmowy agent pamięta; po otwarciu nowej sesji - zaczyna od zera (to różnica
między stanem sesji a pamięcią długoterminową).

Twoje zadanie: podłącz narzędzia i napisz instrukcję, kiedy ich używać.

Uruchom: uv run adk web ex_05_pamiec_i_sesje
"""

from common.exercise import placeholder
from common.model import get_model

from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


def zapamietaj(fakt: str, tool_context: ToolContext) -> str:
    """Zapisuje fakt o użytkowniku w pamięci tej sesji.

    Wołaj, gdy użytkownik podaje coś o sobie, co warto zapamiętać na później
    w rozmowie (np. imię, rola, preferencje).
    """
    notatki = tool_context.state.get("notatki", [])
    notatki.append(fakt)
    tool_context.state["notatki"] = notatki
    return f"Zapamiętane: {fakt}"


def przypomnij(tool_context: ToolContext) -> list[str]:
    """Zwraca wszystkie fakty zapamiętane w tej sesji."""
    return tool_context.state.get("notatki", [])


root_agent = LlmAgent(
    name="agent_z_pamiecia",
    model=get_model(),
    description="Agent, który pamięta fakty o użytkowniku w obrębie sesji.",
    # TODO(you) [krok 2]: podmień placeholder na instrukcję pamięci. Kiedy wołać
    # `zapamietaj` (gdy user podaje fakt o sobie), kiedy `przypomnij` (gdy pyta,
    # co o nim wiesz). Gotowiec w README.
    instruction=placeholder(
        "podłącz narzędzia zapamietaj i przypomnij oraz napisz instrukcję pamięci",
        readme="README ex_05_pamiec_i_sesje",
    ),
    # TODO(you) [krok 1]: podłącz narzędzia zapamietaj i przypomnij.
    tools=[],
)
