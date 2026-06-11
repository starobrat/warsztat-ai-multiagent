"""Testy automatyczne agenta SQL - moduł 12. GOTOWY przykład.

Ten sam test set co w CLI/GUI, tylko uruchamiany jak zwykły test (pytest).
To pokazuje, jak ewaluacja agenta wchodzi do CI.

Uruchom:
    uv run pytest part2_adk/tests/test_sql_agent.py
"""

from pathlib import Path

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

REPO = Path(__file__).resolve().parents[2]
EVALSET = REPO / "part2_adk" / "evals" / "sql_agent.evalset.json"


@pytest.mark.asyncio
async def test_sql_agent_evalset():
    """Agent SQL przechodzi swój test set (trajektoria narzędzi + odpowiedź)."""
    await AgentEvaluator.evaluate(
        agent_module="part2_adk.agents.sql_agent",
        eval_dataset_file_path_or_dir=str(EVALSET),
    )
