"""DEMO (moduł 13): podpięcie serwera MCP do agenta ADK.

Agent dostaje narzędzia z gotowego serwera MCP (filesystem) - bez pisania własnych
funkcji. Wymaga Node/npx (serwer MCP startuje przez npx).

UWAGA: ADK 2.0 to wersja wczesna. Jeśli import/API MCPToolset się różni, sprawdź
dokumentację ADK - agent załaduje się bez narzędzi MCP (lista pusta) i wtedy
pokazujesz koncepcję na kodzie zamiast na żywo.

Uruchom: uv run adk web demo_13_mcp
"""

from common.model import get_model

from google.adk.agents import LlmAgent

# Tu, w katalogu repo, serwer filesystem MCP wystawi narzędzia do plików.
_FS_ROOT = "."

try:
    from google.adk.tools.mcp_tool import MCPToolset, StdioServerParameters

    _tools = [
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem", _FS_ROOT],
            )
        )
    ]
except Exception:  # noqa: BLE001 - API MCP w alpha może się różnić; degraduj łagodnie
    _tools = []

root_agent = LlmAgent(
    name="agent_z_mcp",
    model=get_model(),
    description="Agent korzystający z narzędzi serwera MCP (filesystem).",
    instruction=(
        "Korzystaj z narzędzi plikowych udostępnionych przez serwer MCP. "
        "Odpowiadaj po polsku. Jeśli nie masz narzędzi, powiedz to wprost."
    ),
    tools=_tools,
)
