"""Ćwiczenie ex_21: system raportowy - PLANNER (moduł 10). STARTER.

Tu budujesz TYLKO planner. Jego zadanie: na podstawie prośby ułożyć ZWIĘZŁY plan
raportu (sekcje, jakich danych potrzeba, gdzie wykres) - i NIC poza tym. Pobieranie
danych i składanie raportu dokładamy dopiero w ex_22.

Uruchom: uv run adk web ex_21_planner (albo adk run ex_21_planner).
"""

from common.exercise import placeholder
from common.model import get_model

from google.adk.agents import LlmAgent


# PLANNER - planuje raport: jakie sekcje, jakie dane, jakie wykresy. TWOJE ZADANIE.
# Zwraca SAM PLAN (output_key="report_plan"); danych jeszcze nie pobiera.
root_agent = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    # TODO(you): napisz instrukcję plannera. Ma wypisać ZWIĘZŁY plan raportu:
    # 2-4 sekcje, dla każdej jaką liczbę/dane trzeba pobrać i czy dodać wykres.
    # NIE pisze SQL i NIE pobiera danych - od tego jest data_agent (ex_22).
    # Jeśli użytkownik tylko się wita lub nie podał, o jaki raport chodzi - krótko
    # przedstaw się (planista raportów Chinook) i zapytaj, jaki raport przygotować.
    instruction=placeholder(
        "napisz instrukcję plannera: ma ułożyć zwięzły plan raportu (sekcje, jakich "
        "danych potrzeba, gdzie wykres), bez pisania SQL; na powitanie - przedstaw się i zapytaj",
        readme="README ex_21_planner",
    ),
    output_key="report_plan",
)
