"""Klocek: raport Excel z wykresem (openpyxl)."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

OUT_DIR = Path(__file__).resolve().parents[1] / "out"


def make_excel_report(
    title: str, columns: list[str], rows: list[list], filename: str
) -> str:
    """Zapisuje dane do arkusza Excel i dorzuca wykres słupkowy.

    Zakłada, że pierwsza kolumna to etykiety, a druga to wartości liczbowe
    (na nich budowany jest wykres).

    Args:
        title: Tytuł arkusza.
        columns: Nazwy kolumn (nagłówek).
        rows: Wiersze danych.
        filename: Nazwa pliku XLSX (np. 'raport.xlsx').

    Returns:
        Ścieżka do zapisanego pliku XLSX.
    """
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / filename

    wb = Workbook()
    ws = wb.active
    ws.title = title[:31] or "Raport"
    ws.append(columns)
    for row in rows:
        ws.append(row)

    if len(rows) >= 1 and len(columns) >= 2:
        chart = BarChart()
        chart.title = title
        data = Reference(ws, min_col=2, min_row=1, max_row=len(rows) + 1)
        cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows) + 1)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        ws.add_chart(chart, "E2")

    wb.save(path)
    return str(path)
