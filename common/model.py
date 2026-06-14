"""Wspólna konfiguracja modelu dla agentów ADK (część 2).

ADK natywnie woła Gemini, więc do OpenAI używamy wrappera LiteLlm - dlatego
model owijamy w LiteLlm(model="openai/<id>"). LiteLLM sam czyta OPENAI_API_KEY
ze środowiska. Całe szkolenie chodzi na jednym kluczu OpenAI.
"""

import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm, LiteLLMClient
from pydantic import Field

load_dotenv()


class _SerializableLiteLlm(LiteLlm):
    """LiteLlm bezpieczny dla panelu struktury agenta w `adk web`.

    ADK 2.2 przy renderowaniu `/build_graph` robi model_dump() modelu i probuje
    zserializowac go do JSON. Zwykly LiteLlm wpycha tam pole `llm_client`
    (obiekt LiteLLMClient), ktorego nie da sie zserializowac -> 500 w UI.
    Oznaczamy to pole `exclude=True`: nadal dziala w runtime (wola OpenAI),
    ale wypada z serializacji, wiec panel sie renderuje.
    """

    llm_client: LiteLLMClient = Field(default_factory=LiteLLMClient, exclude=True)

# id modelu OpenAI, np. "gpt-5.4-mini"
_OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

# Słabszy model - używany WYŁĄCZNIE w ćwiczeniu 8 (tuning promptu / TDD).
# Mocny model maskuje słaby prompt (i tak sięgnie po narzędzia i odpowie dobrze),
# więc nie da się na nim pokazać pętli czerwony->zielony. Słabszy model jest
# wrażliwy na jakość instrukcji - dlatego prompt naprawdę ma znaczenie.
_OPENAI_MODEL_WEAK = os.getenv("OPENAI_MODEL_WEAK", "gpt-4o-mini")


def get_model() -> LiteLlm:
    """Zwraca model gotowy do podstawienia w LlmAgent(model=...)."""
    return _SerializableLiteLlm(model=f"openai/{_OPENAI_MODEL}")


def get_weak_model() -> LiteLlm:
    """Słabszy model - tylko do ćwiczenia 8 (tuning promptu na test secie)."""
    return _SerializableLiteLlm(model=f"openai/{_OPENAI_MODEL_WEAK}")
