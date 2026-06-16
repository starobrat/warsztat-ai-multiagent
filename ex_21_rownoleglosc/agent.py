"""Ćwiczenie ex_21: ParallelAgent - równoległe odpytanie bazy (moduł 11). STARTER.

Do tej pory agenty szły po kolei (SequentialAgent). Tu DWA niezależne zapytania
do bazy lecą RÓWNOLEGLE (ParallelAgent) - każde zapisuje wynik pod swój output_key.
Na końcu agent-syntezator czyta oba wyniki i składa odpowiedź.

Wzorzec fan-out/gather:
    SequentialAgent( ParallelAgent(branch_a, branch_b) -> synteza )

branch_a, branch_b i synteza są gotowe. Twoje zadanie: złożyć ParallelAgent z gałęzi
i wpiąć go w sekwencję z syntezatorem.

Uruchom: uv run adk web ex_21_rownoleglosc (albo adk run ex_21_rownoleglosc).
"""

from common.exercise import placeholder
from common.model import get_model
from common.tools.db import get_schema, run_query

from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent


# Gałąź A - liczy klientów. GOTOWA. Wynik -> output_key="wynik_klienci".
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

# Gałąź B - liczy faktury. GOTOWA. Wynik -> output_key="wynik_faktury".
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

# Syntezator - czyta oba wyniki przez templating. GOTOWY.
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

# TODO(you): złóż gałęzie w ParallelAgent (uruchamia je równolegle).
rownolegle = None  # ParallelAgent(name=..., sub_agents=[branch_klienci, branch_faktury])

# TODO(you): wpnij ParallelAgent + synteza w SequentialAgent w tej kolejności.
root_agent = LlmAgent(
    name="placeholder",
    model=get_model(),
    description="STARTER - jeszcze niezłożony.",
    instruction=placeholder(
        "złóż branch_klienci i branch_faktury w ParallelAgent, a potem [rownolegle, "
        "synteza] w SequentialAgent jako root_agent",
        readme="README ex_21_rownoleglosc",
    ),
)
