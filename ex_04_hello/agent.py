"""Ćwiczenie: pierwszy agent w ADK - moduł 5. STARTER.

Twój pierwszy LlmAgent. Napisz instruction (rolę), uruchom i porozmawiaj.

Uruchom: uv run adk web ex_04_hello (UI) albo uv run adk run ex_04_hello (terminal).
"""

from common.model import get_model

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="hello",
    model=get_model(),
    description="Prosty agent powitalny do pierwszego kontaktu z ADK.",
    # TODO(you): napisz instruction - rolę agenta (np. asystent sklepu z muzyką,
    # odpowiada krótko i po polsku; narzędzi jeszcze nie ma, po prostu rozmawia).
    instruction="",
)
