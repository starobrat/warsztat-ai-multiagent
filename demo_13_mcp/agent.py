"""DEMO (moduł 13): podpięcie serwera MCP do agenta ADK.

Agent dostaje narzędzia z gotowego serwera MCP (filesystem) - bez pisania własnych
funkcji. Wymaga Node/npx (serwer MCP startuje przez npx) oraz pakietu `mcp`
(jest w zależnościach repo - instaluje się przez `uv sync`).

Uruchom: uv run adk web demo_13_mcp
"""

from common.model import get_model

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters

# Tu, w katalogu repo, serwer filesystem MCP wystawi narzędzia do plików.
_FS_ROOT = "."

_tools = [
    McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem", _FS_ROOT],
            )
        )
    )
]

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
