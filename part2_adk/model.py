"""Wspólna konfiguracja modelu dla agentów ADK.

Całe szkolenie chodzi na jednym kluczu OpenRouter. ADK woła OpenRouter przez
LiteLLM - dlatego model owijamy w LiteLlm(model="openrouter/<id>").
LiteLLM sam czyta OPENROUTER_API_KEY ze środowiska.
"""

import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

# id modelu w OpenRouter, np. "openai/gpt-4o-mini"
_OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")


def get_model() -> LiteLlm:
    """Zwraca model gotowy do podstawienia w LlmAgent(model=...)."""
    return LiteLlm(model=f"openrouter/{_OPENROUTER_MODEL}")
