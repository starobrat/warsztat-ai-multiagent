"""Testy systemu raportowego (wieloagentowego) - moduł 12. GOTOWY przykład.

Odpowiednik test_sql_agent.py, ale dla systemu wieloagentowego (ex_22_report_writer:
planner -> data_agent -> report_writer). Trajektoria w systemie wieloagentowym jest
niedeterministyczna (kolejność i liczba wywołań narzędzi bywa różna), więc progi
w solutions/ex_23_tests/test_config.json są łagodne - sprawdzamy głównie, że system
przechodzi end-to-end i zwraca odpowiedź (smoke test eval w CI).

Uruchom:
    uv run pytest ex_23_tests/test_report_system.py
"""

from pathlib import Path

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

REPO = Path(__file__).resolve().parents[1]
# Gotowy test set systemu raportowego. Obok leży test_config.json (łagodne progi),
# który AgentEvaluator dobiera automatycznie z katalogu evalsetu.
EVALSET = REPO / "ex_23_tests" / "report_system.evalset.json"


@pytest.mark.asyncio
async def test_report_system_evalset():
    """System raportowy przechodzi swój test set (eval w CI, łagodne progi)."""
    await AgentEvaluator.evaluate(
        agent_module="ex_22_report_writer",
        eval_dataset_file_path_or_dir=str(EVALSET),
    )
