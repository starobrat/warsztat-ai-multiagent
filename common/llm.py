"""Wspólny klient LLM dla części 1 (ćwiczenia 01-03).

Część 1 świadomie NIE używa ADK - budujemy pętlę agentyczną ręcznie, żeby
zrozumieć, co ADK robi za nas. Wołamy model bezpośrednio przez OpenAI SDK.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

# Domyślny base_url SDK to api.openai.com - klucz bierzemy z OPENAI_API_KEY.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
