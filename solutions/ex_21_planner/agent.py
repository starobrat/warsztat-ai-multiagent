"""ROZWIĄZANIE ex_21: system raportowy - PLANNER.

Tu budujemy TYLKO planner: na podstawie prośby układa zwięzły plan raportu i zwraca
go (output_key="report_plan"). Danych jeszcze nie pobiera, raportu nie składa - to
dokładamy w ex_22 (data_agent + report_writer w pełnym pipeline).

Uruchom: uv run adk web solutions/ex_21_planner (albo adk run).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model

from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="planner",
    model=get_model(),
    description="Planuje strukturę raportu, zanim ktokolwiek odpyta bazę.",
    instruction=(
        "Jesteś planistą raportu o sklepie z muzyką Chinook. Na podstawie prośby "
        "użytkownika wypisz ZWIĘZŁY plan raportu: 2-4 sekcje, a dla każdej sekcji "
        "podaj, jakiej liczby/danych potrzeba i czy warto dodać wykres. "
        "NIE pisz SQL i NIE pobieraj danych - od tego jest osobny agent (ex_22). "
        "Zwróć sam plan, po polsku, w punktach.\n"
        "Jeśli użytkownik tylko się wita lub nie napisał, o jaki raport chodzi - "
        "krótko przedstaw się (planista raportów Chinook) i zapytaj, jaki raport przygotować."
    ),
    output_key="report_plan",
)
