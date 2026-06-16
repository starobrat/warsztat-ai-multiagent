"""Klocek: wykresy PNG (matplotlib) + zapis jako artefakt ADK."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # bez GUI - tylko zapis do pliku
import matplotlib.pyplot as plt  # noqa: E402

import google.genai.types as types  # noqa: E402
from google.adk.tools.tool_context import ToolContext  # noqa: E402

OUT_DIR = Path(__file__).resolve().parents[2] / "out"


def bar_chart(labels: list[str], values: list[float], title: str, filename: str) -> str:
    """Tworzy wykres słupkowy i zapisuje go jako PNG.

    Args:
        labels: Etykiety osi X.
        values: Wartości słupków.
        title: Tytuł wykresu.
        filename: Nazwa pliku PNG (np. 'sprzedaz.png').

    Returns:
        Ścieżka do zapisanego pliku PNG.
    """
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / filename

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(labels, values, color="#2563EB")
    ax.set_title(title)
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return str(path)


async def bar_chart_artifact(
    labels: list[str],
    values: list[float],
    title: str,
    filename: str,
    tool_context: ToolContext,
) -> str:
    """Tworzy wykres słupkowy PNG i zapisuje go jako ARTEFAKT agenta.

    W odróżnieniu od bar_chart (zwykły plik na dysku), ten klocek dodatkowo zapisuje
    PNG przez ArtifactService - dzięki temu pojawia się w zakładce Artifacts w adk web.

    Args:
        labels: Etykiety osi X.
        values: Wartości słupków.
        title: Tytuł wykresu.
        filename: Nazwa pliku PNG (np. 'sprzedaz.png').

    Returns:
        Ścieżka do zapisanego pliku PNG (ten sam plik jest też artefaktem agenta).
    """
    path = bar_chart(labels, values, title, filename)
    data = Path(path).read_bytes()
    await tool_context.save_artifact(
        filename, types.Part.from_bytes(data=data, mime_type="image/png")
    )
    return path
