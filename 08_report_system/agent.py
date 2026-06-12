"""System wieloagentowy: raportowanie - moduły 9-11. STARTER.

Architektura docelowa (rysunek z modułu 10):

    planner  ->  data_agent  ->  report_writer
   (co i jak)    (SQL z bazy)    (składa artefakt)

To pipeline: każdy agent oddaje wynik kolejnemu przez output_key. SequentialAgent
wykonuje je po kolei. Planner planuje, zanim ktokolwiek dotknie bazy.

Zadanie (rośnie przez moduły 9-11):
  - moduł 9/10: napisz instruction plannera i podłącz data_agent.
  - moduł 11: dołóż report_writer z narzędziami raportowymi (PDF/Excel/HTML).

Uruchom:
    uv run adk web 08_report_system
"""

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
    # TODO(you): instruction plannera. Ma wypisać plan raportu: jakie sekcje,
    # jakie pytania do danych, jakie wykresy. Bez pisania SQL - to robi data_agent.
    instruction="",
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
    # TODO(you): instruction. Na podstawie {report_plan} i {report_data} ma
    # wywołać narzędzia raportowe i zbudować artefakt. Możesz najpierw zrobić
    # wykres (bar_chart), potem make_pdf_report lub make_html_report.
    instruction="",
    # TODO(you): podłącz narzędzia raportowe.
    tools=[],
    output_key="report_path",
)

# Master = pipeline trzech kroków.
root_agent = SequentialAgent(
    name="report_system",
    description="System wieloagentowy generujący raport z danych sklepu Chinook.",
    sub_agents=[planner, data_agent, report_writer],
)
