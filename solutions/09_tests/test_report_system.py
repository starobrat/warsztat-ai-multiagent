"""Rozwiązanie ćwiczenia 12 - test systemu raportowego.

Zakłada nagrany wcześniej test set 06_evaluation/report_system.evalset.json
(nagrywasz go w `adk web 08_report_system`, zakładka Eval).
"""

from pathlib import Path

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

REPO = Path(__file__).resolve().parents[2]
EVALSET = REPO / "06_evaluation" / "report_system.evalset.json"


@pytest.mark.asyncio
async def test_report_system_evalset():
    await AgentEvaluator.evaluate(
        agent_module="08_report_system",
        eval_dataset_file_path_or_dir=str(EVALSET),
    )
