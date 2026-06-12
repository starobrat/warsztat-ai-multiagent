"""Agent referencyjny - moduł 5. GOTOWY, do podejrzenia.

Pierwszy agent w ADK: to samo, co robiłeś ręcznie w części 1, ale pętlę, sesje,
UI i ewaluację masz gotowe.

Uruchom: uv run adk web 04_hello (UI) albo uv run adk run 04_hello (terminal).
"""

from common.model import get_model

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="hello",
    model=get_model(),
    description="Prosty agent powitalny do pierwszego kontaktu z ADK.",
    instruction=(
        "Jesteś pomocnym asystentem sklepu z muzyką. Odpowiadasz krótko i po polsku. "
        "Jeszcze nie masz żadnych narzędzi - po prostu rozmawiasz."
    ),
)
