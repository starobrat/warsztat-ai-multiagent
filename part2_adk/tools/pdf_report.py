"""Klocek: raport PDF (fpdf2).

Używamy czcionki Unicode DejaVu (dostarcza ją matplotlib), żeby polskie znaki
(ł, ą, ę, ...) renderowały się poprawnie - rdzeniowy Helvetica w fpdf2 ich nie obsługuje.
"""

from pathlib import Path

import matplotlib
from fpdf import FPDF

OUT_DIR = Path(__file__).resolve().parents[1] / "out"

_FONT_DIR = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
_FONT_REGULAR = _FONT_DIR / "DejaVuSans.ttf"
_FONT_BOLD = _FONT_DIR / "DejaVuSans-Bold.ttf"


def _new_pdf() -> FPDF:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", str(_FONT_REGULAR))
    pdf.add_font("DejaVu", "B", str(_FONT_BOLD))
    pdf.add_page()
    return pdf


def make_pdf_report(title: str, sections: list[dict], filename: str) -> str:
    """Generuje prosty raport PDF z sekcji tekstowych i opcjonalnych wykresów.

    Args:
        title: Tytuł raportu na pierwszej stronie.
        sections: Lista sekcji. Każda to słownik:
            {"heading": str, "body": str, "image": str | None}
            gdzie image to ścieżka do PNG (np. z bar_chart) albo None.
        filename: Nazwa pliku PDF (np. 'raport.pdf').

    Returns:
        Ścieżka do zapisanego pliku PDF.
    """
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / filename

    pdf = _new_pdf()
    width = pdf.epw  # efektywna szerokość strony (między marginesami)

    pdf.set_font("DejaVu", "B", 20)
    pdf.multi_cell(width, 12, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    for section in sections:
        pdf.set_font("DejaVu", "B", 14)
        pdf.multi_cell(width, 9, section.get("heading", ""), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("DejaVu", "", 11)
        pdf.multi_cell(width, 7, section.get("body", ""), new_x="LMARGIN", new_y="NEXT")
        image = section.get("image")
        if image and Path(image).exists():
            pdf.image(image, w=170)
        pdf.ln(4)

    pdf.output(str(path))
    return str(path)
