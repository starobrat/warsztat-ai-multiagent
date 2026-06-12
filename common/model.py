"""Wspólna konfiguracja modelu dla agentów ADK (część 2).

ADK natywnie woła Gemini, więc do OpenAI używamy wrappera LiteLlm - dlatego
model owijamy w LiteLlm(model="openai/<id>"). LiteLLM sam czyta OPENAI_API_KEY
ze środowiska. Całe szkolenie chodzi na jednym kluczu OpenAI.
"""

import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

# id modelu OpenAI, np. "gpt-5.4-mini"
_OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

# Słabszy model - używany WYŁĄCZNIE w ćwiczeniu 8 (tuning promptu / TDD).
# Mocny model maskuje słaby prompt (i tak sięgnie po narzędzia i odpowie dobrze),
# więc nie da się na nim pokazać pętli czerwony->zielony. Słabszy model jest
# wrażliwy na jakość instrukcji - dlatego prompt naprawdę ma znaczenie.
_OPENAI_MODEL_WEAK = os.getenv("OPENAI_MODEL_WEAK", "gpt-4o-mini")


def get_model() -> LiteLlm:
    """Zwraca model gotowy do podstawienia w LlmAgent(model=...)."""
    return LiteLlm(model=f"openai/{_OPENAI_MODEL}")


def get_weak_model() -> LiteLlm:
    """Słabszy model - tylko do ćwiczenia 8 (tuning promptu na test secie)."""
    return LiteLlm(model=f"openai/{_OPENAI_MODEL_WEAK}")
