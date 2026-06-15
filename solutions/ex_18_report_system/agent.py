"""ROZWIĄZANIE: system wieloagentowy raportowania - moduły 9-11.

Pipeline trzech agentów (SequentialAgent, dane płyną przez output_key):
    planner -> data_agent -> report_writer
Wypełnione: instruction plannera, instruction report_writera + narzędzia raportowe.
data_agent był gotowy.

Uruchom: uv run adk run solutions/ex_18_report_system "..." (albo adk web).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema, run_query
from common.tools.charts import bar_chart
from common.tools.pdf_report import make_pdf_report
from common.tools.html_report import make_html_report

from google.adk.agents import LlmAgent, SequentialAgent


# 1) PLANNER - planuje raport: jakie sekcje, jakie dane, jakie wykresy.
planner = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    instruction=(
        "Jesteś planistą raportu o sklepie z muzyką Chinook. Na podstawie prośby "
        "użytkownika wypisz ZWIĘZŁY plan raportu: 2-4 sekcje, a dla każdej sekcji "
        "podaj, jakiej liczby/danych potrzebujesz i czy warto dodać wykres. "
        "NIE pisz SQL - od pobierania danych jest osobny agent. Zwróć sam plan, "
        "po polsku, w punktach."
    ),
    output_key="report_plan",
)

# 2) DATA AGENT - realizuje plan: odpytuje bazę Chinook.
data_agent = LlmAgent(
    name="data_agent",
    model=get_model(),
    description="Pobiera dane z bazy zgodnie z planem raportu.",
    instruction=(
        "Masz plan raportu: {report_plan}\n"
        "Dla każdej potrzebnej liczby NAJPIERW sprawdź schemat (get_schema), "
        "potem napisz SELECT (run_query). Nie zgaduj nazw tabel. "
        "Zbierz wyniki i przekaż je dalej w czytelnej formie."
    ),
    tools=[get_schema, run_query],
    output_key="report_data",
)

# 3) REPORT WRITER - składa artefakt z gotowych klocków.
report_writer = LlmAgent(
    name="report_writer",
    model=get_model(),
    description="Składa finalny raport (PDF / HTML) z danych.",
    instruction=(
        "Składasz finalny raport ze sklepu Chinook. Masz plan: {report_plan}\n"
        "oraz zebrane dane: {report_data}\n"
        "Krok 1 (opcjonalnie): jeśli dane mają się do tego, zrób wykres słupkowy "
        "narzędziem bar_chart (labels, values, tytuł, nazwa pliku PNG).\n"
        "Krok 2: zbuduj raport narzędziem make_html_report(title, sections, filename), "
        "gdzie sections to lista słowników {\"heading\": ..., \"body\": ..., "
        "\"image\": ścieżka_do_PNG lub pomiń}. Użyj danych z {report_data}, nie zmyślaj. "
        "Na końcu podaj ścieżkę do wygenerowanego pliku."
    ),
    tools=[bar_chart, make_html_report, make_pdf_report],
    output_key="report_path",
)

# Master = pipeline trzech kroków.
root_agent = SequentialAgent(
    name="report_system",
    description="System wieloagentowy generujący raport z danych sklepu Chinook.",
    sub_agents=[planner, data_agent, report_writer],
)
