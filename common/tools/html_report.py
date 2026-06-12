"""Klocek: raport HTML (jinja2)."""

from pathlib import Path

from jinja2 import Template

OUT_DIR = Path(__file__).resolve().parents[2] / "out"

_TEMPLATE = Template(
    """<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 760px; margin: 40px auto; color: #1a1a1a; }
    h1 { border-bottom: 3px solid #2563EB; padding-bottom: 8px; }
    h2 { color: #2563EB; margin-top: 32px; }
    img { max-width: 100%; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: left; }
    th { background: #f3f4f6; }
  </style>
</head>
<body>
  <h1>{{ title }}</h1>
  {% for s in sections %}
    <h2>{{ s.heading }}</h2>
    <p>{{ s.body }}</p>
    {% if s.image %}<img src="{{ s.image }}" alt="{{ s.heading }}">{% endif %}
  {% endfor %}
</body>
</html>"""
)


def make_html_report(title: str, sections: list[dict], filename: str) -> str:
    """Generuje raport jako stronę HTML.

    Args:
        title: Tytuł strony.
        sections: Lista sekcji {"heading": str, "body": str, "image": str | None}.
        filename: Nazwa pliku HTML (np. 'raport.html').

    Returns:
        Ścieżka do zapisanego pliku HTML.
    """
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / filename
    path.write_text(_TEMPLATE.render(title=title, sections=sections), encoding="utf-8")
    return str(path)
