"""DEMO (moduł 13): agent steruje lokalną przeglądarką przez MCP (Playwright).

Najprostszy lokalny setup: agent dostaje narzędzia z serwera Playwright MCP, który
odpala i steruje PRAWDZIWĄ przeglądarką na Twoim komputerze. Rozmawiasz z agentem
po polsku, a on klika, wpisuje i nawiguje za Ciebie.

Pomysł na pokaz:
  "Wejdź na allegro.pl i poszukaj karmy dla psa."
  -> agent otwiera stronę, wpisuje frazę w wyszukiwarkę, pokazuje wyniki.

Wymaga: Node/npx (serwer Playwright MCP startuje przez npx; pierwsze uruchomienie
pobierze przeglądarkę). Serwer: https://github.com/microsoft/playwright-mcp

Uruchom: uv run adk web demo_mcp_playwright
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams  # noqa: E402
from mcp import StdioServerParameters  # noqa: E402


# Playwright MCP - lokalny serwer sterujący przeglądarką (npx odpala go przez stdio).
_tools = [
    McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@playwright/mcp@latest"],
            )
        )
    )
]

root_agent = LlmAgent(
    name="agent_przegladarka",
    model=get_model(),
    description="Agent sterujący lokalną przeglądarką przez serwer Playwright MCP.",
    instruction=(
        "Sterujesz przeglądarką za pomocą narzędzi z serwera Playwright MCP. "
        "Wykonujesz polecenia użytkownika krok po kroku: nawigacja, wpisywanie tekstu, "
        "klikanie, czytanie zawartości strony. Odpowiadasz po polsku, krótko opisując, "
        "co właśnie zrobiłeś i co widzisz. Jeśli czegoś nie da się zrobić, powiedz wprost."
    ),
    tools=_tools,
)
