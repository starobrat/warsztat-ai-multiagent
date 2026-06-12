"""Agent referencyjny - moduł 5. GOTOWY, do podejrzenia.

Pierwszy agent w ADK. To samo, co robiłeś ręcznie w części 1, tylko że ADK
ogarnia za Ciebie pętlę, sesje, interfejs webowy i ewaluację.

Uruchom interfejs webowy z katalogu repo:
    uv run adk web 04_hello

albo CLI:
    uv run adk run 04_hello
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
