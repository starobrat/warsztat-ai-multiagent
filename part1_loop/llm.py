"""Wspólny klient LLM dla części 1.

Część 1 świadomie NIE używa ADK - budujemy pętlę agentyczną ręcznie, żeby
zrozumieć, co ADK robi za nas. Wołamy LLM przez OpenRouter, korzystając z
OpenAI SDK z podmienionym base_url (OpenRouter jest kompatybilny z API OpenAI).
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)
