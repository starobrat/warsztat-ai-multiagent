"""ROZWIĄZANIE ex_21: ParallelAgent - równoległe odpytanie bazy.

Wzorzec fan-out/gather: ParallelAgent(branch_klienci, branch_faktury) -> synteza,
całość owinięta w SequentialAgent. Gałęzie i synteza były gotowe.

Uruchom: uv run adk run solutions/ex_21_rownoleglosc "..." (albo adk web).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent


branch_klienci = LlmAgent(
    name="branch_klienci",
    model=get_model(),
    description="Liczy łączną liczbę klientów w bazie Chinook.",
    instruction=(
        "Policz, ilu jest klientów w bazie Chinook. Najpierw get_schema, potem "
        "SELECT przez run_query. Zwróć samą liczbę z krótkim opisem."
    ),
    tools=[get_schema, run_query],
    output_key="wynik_klienci",
)

branch_faktury = LlmAgent(
    name="branch_faktury",
    model=get_model(),
    description="Liczy łączną liczbę faktur w bazie Chinook.",
    instruction=(
        "Policz, ile jest faktur w bazie Chinook. Najpierw get_schema, potem "
        "SELECT przez run_query. Zwróć samą liczbę z krótkim opisem."
    ),
    tools=[get_schema, run_query],
    output_key="wynik_faktury",
)

synteza = LlmAgent(
    name="synteza",
    model=get_model(),
    description="Składa wyniki obu gałęzi w jedną odpowiedź.",
    instruction=(
        "Masz dwa policzone wyniki:\n"
        "- klienci: {wynik_klienci}\n"
        "- faktury: {wynik_faktury}\n"
        "Złóż je w jedno krótkie podsumowanie po polsku."
    ),
)

rownolegle = ParallelAgent(
    name="rownolegle",
    description="Uruchamia oba zapytania do bazy równolegle.",
    sub_agents=[branch_klienci, branch_faktury],
)

root_agent = SequentialAgent(
    name="rownoleglosc",
    description="Równoległe odpytanie bazy, a potem synteza wyników.",
    sub_agents=[rownolegle, synteza],
)
