"""Agent referencyjny - moduł 5. GOTOWY, do podejrzenia.

Pierwszy agent w ADK. To samo, co robiłeś ręcznie w części 1, tylko że ADK
ogarnia za Ciebie pętlę, sesje, interfejs webowy i ewaluację.

Uruchom interfejs webowy z katalogu repo:
    uv run adk web part2_adk/agents

albo CLI:
    uv run adk run part2_adk/agents/hello
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402


root_agent = LlmAgent(
    name="hello",
    model=get_model(),
    description="Prosty agent powitalny do pierwszego kontaktu z ADK.",
    instruction=(
        "Jesteś pomocnym asystentem sklepu z muzyką. Odpowiadasz krótko i po polsku. "
        "Jeszcze nie masz żadnych narzędzi - po prostu rozmawiasz."
    ),
)
