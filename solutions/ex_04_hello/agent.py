"""Rozwiązanie: pierwszy agent w ADK (hello)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.model import get_model  # noqa: E402

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
