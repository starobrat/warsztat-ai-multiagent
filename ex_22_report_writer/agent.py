"""Ćwiczenie ex_22: pipeline raportu - REPORT WRITER (moduł 11). STARTER.

Ten sam pipeline co ex_21 (planner -> data_agent -> report_writer), ale tym razem
planner i data_agent są GOTOWE. Twoje zadanie: złożyć report_writera - podłączyć
narzędzia raportowe (bar_chart_artifact, make_html_report) i napisać instrukcję, która z
{report_plan} i {report_data} buduje gotowy artefakt (wykres PNG + raport HTML).

Uruchom: uv run adk web ex_22_report_writer (albo adk run ex_22_report_writer).
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema, run_query
from common.tools.charts import bar_chart_artifact
from common.tools.html_report import make_html_report

from google.adk.agents import LlmAgent, SequentialAgent


# 1) PLANNER - planuje raport. GOTOWY.
planner = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    instruction=(
        "Jesteś planistą raportu o sklepie z muzyką Chinook. Na podstawie prośby "
        "użytkownika wypisz ZWIĘZŁY plan raportu: 2-4 sekcje, a dla każdej sekcji "
        "podaj, jakiej liczby/danych potrzeba i czy warto dodać wykres. "
        "NIE pisz SQL - od pobierania danych jest osobny agent. Zwróć sam plan, "
        "po polsku, w punktach.\n"
        "Jeśli użytkownik tylko się wita lub nie napisał, o jaki raport chodzi - "
        "krótko przedstaw się (system raportowy Chinook) i zapytaj, jaki raport przygotować."
    ),
    output_key="report_plan",
)

# 2) DATA AGENT - realizuje plan: odpytuje bazę Chinook. GOTOWY.
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

# 3) REPORT WRITER - składa artefakt z gotowych klocków. TWOJE ZADANIE.
report_writer = LlmAgent(
    name="report_writer",
    model=get_model(),
    description="Składa finalny raport (HTML) z danych.",
    # TODO(you): napisz instrukcję. Na podstawie {report_plan} i {report_data} ma
    # (opcjonalnie) zrobić wykres bar_chart_artifact, a potem złożyć make_html_report.
    # Ma używać danych z {report_data}, nie zmyślać, i na końcu podać ścieżkę pliku.
    instruction=placeholder(
        "podłącz narzędzia raportowe (bar_chart_artifact, make_html_report) i napisz "
        "instrukcję budującą artefakt z {report_plan} i {report_data}",
        readme="README ex_22_report_writer",
    ),
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
