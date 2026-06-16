"""Ćwiczenie ex_21: pipeline raportu - PLANNER (moduł 10). STARTER.

Pełny pipeline raportu (SequentialAgent): planner -> data_agent -> report_writer.
data_agent i report_writer są GOTOWE. Twoje zadanie: napisać instrukcję plannera,
który układa plan raportu (sekcje, jakich danych potrzeba, gdzie wykres) i zapisuje
go pod output_key="report_plan". data_agent czyta ten plan przez {report_plan}.

Uruchom: uv run adk web ex_21_planner (albo adk run ex_21_planner).
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema, run_query
from common.tools.charts import bar_chart_artifact
from common.tools.html_report import make_html_report

from google.adk.agents import LlmAgent, SequentialAgent


# 1) PLANNER - planuje raport: jakie sekcje, jakie dane, jakie wykresy. TWOJE ZADANIE.
planner = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    # TODO(you): napisz instrukcję plannera. Ma wypisać ZWIĘZŁY plan raportu:
    # 2-4 sekcje, dla każdej jaką liczbę/dane trzeba pobrać i czy dodać wykres.
    # NIE pisze SQL - od tego jest data_agent. Plan wędruje dalej przez output_key.
    instruction=placeholder(
        "napisz instrukcję plannera: ma ułożyć zwięzły plan raportu (sekcje, jakich "
        "danych potrzeba, gdzie wykres), bez pisania SQL",
        readme="README ex_21_planner",
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

# 3) REPORT WRITER - składa artefakt z gotowych klocków. GOTOWY.
report_writer = LlmAgent(
    name="report_writer",
    model=get_model(),
    description="Składa finalny raport (HTML) z danych.",
    instruction=(
        "Składasz finalny raport ze sklepu Chinook. Masz plan: {report_plan}\n"
        "oraz zebrane dane: {report_data}\n"
        "Krok 1 (opcjonalnie): jeśli dane się do tego nadają, zrób wykres słupkowy "
        "narzędziem bar_chart_artifact (labels, values, tytuł, nazwa pliku PNG) - "
        "zwróci ścieżkę PNG i zapisze wykres jako artefakt.\n"
        "Krok 2: zbuduj raport make_html_report(title, sections, filename), gdzie "
        "sections to lista {\"heading\": ..., \"body\": ..., \"image\": ścieżka_PNG "
        "lub pomiń}. Używaj danych z {report_data}, nie zmyślaj. Na końcu podaj "
        "ścieżkę do wygenerowanego pliku."
    ),
    tools=[bar_chart_artifact, make_html_report],
    output_key="report_path",
)

# Master = pipeline trzech kroków.
root_agent = SequentialAgent(
    name="report_system",
    description="System wieloagentowy generujący raport z danych sklepu Chinook.",
    sub_agents=[planner, data_agent, report_writer],
)
