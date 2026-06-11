"""Rozwiązanie: system raportowy (report_system) - wypełniony planner i report_writer.

Skopiuj do part2_adk/agents/report_system/agent.py, jeśli utkniesz.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[4] / "part2_adk"))
from model import get_model  # noqa: E402
from tools.db import get_schema, run_query  # noqa: E402
from tools.charts import bar_chart  # noqa: E402
from tools.pdf_report import make_pdf_report  # noqa: E402
from tools.html_report import make_html_report  # noqa: E402

from google.adk.agents import LlmAgent, SequentialAgent  # noqa: E402


planner = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    instruction=(
        "Jesteś analitykiem planującym raport ze sklepu z muzyką (baza Chinook). "
        "Na podstawie prośby użytkownika zaproponuj zwięzły plan raportu:\n"
        "- 2-4 sekcje (tytuł + co ma pokazać),\n"
        "- dla każdej sekcji: jakie pytanie do danych trzeba zadać,\n"
        "- które dane warto pokazać na wykresie słupkowym.\n"
        "Nie pisz SQL - od tego jest kolejny agent. Wypisz sam plan."
    ),
    output_key="report_plan",
)

data_agent = LlmAgent(
    name="data_agent",
    model=get_model(),
    description="Pobiera dane z bazy zgodnie z planem raportu.",
    instruction=(
        "Masz plan raportu: {report_plan}\n"
        "Dla każdej potrzebnej liczby NAJPIERW sprawdź schemat (get_schema), "
        "potem napisz SELECT (run_query). Nie zgaduj nazw tabel. "
        "Zbierz wyniki i przekaż je dalej w czytelnej formie (etykiety + wartości)."
    ),
    tools=[get_schema, run_query],
    output_key="report_data",
)

report_writer = LlmAgent(
    name="report_writer",
    model=get_model(),
    description="Składa finalny raport (PDF) z danych.",
    instruction=(
        "Masz plan: {report_plan}\noraz dane: {report_data}\n"
        "Zbuduj raport:\n"
        "1. Jeśli masz serię etykieta+wartość, zrób wykres przez bar_chart "
        "(labels, values, title, filename='wykres.png').\n"
        "2. Złóż sekcje raportu i wywołaj make_pdf_report(title, sections, filename='raport.pdf'), "
        "gdzie sections to lista {{'heading','body','image'}} (image = ścieżka z bar_chart albo None).\n"
        "Na końcu podaj użytkownikowi ścieżkę do wygenerowanego pliku."
    ),
    tools=[bar_chart, make_pdf_report, make_html_report],
    output_key="report_path",
)

root_agent = SequentialAgent(
    name="report_system",
    description="System wieloagentowy generujący raport z danych sklepu Chinook.",
    sub_agents=[planner, data_agent, report_writer],
)
