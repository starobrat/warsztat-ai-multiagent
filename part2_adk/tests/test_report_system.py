"""Testy systemu raportowego - moduł 12. ĆWICZENIE.

Po zbudowaniu systemu raportowego (moduły 9-11) dorób mu test set.
W systemie wieloagentowym trajektoria obejmuje też transfery między agentami.

Zadanie:
  1. Nagraj 1-2 sesje w `adk web` (wybierz report_system) i zapisz jako eval case
     do part2_adk/evals/report_system.evalset.json
  2. Odkomentuj test poniżej i uzupełnij ścieżkę.
  3. Pamiętaj o jakości oczekiwanych zapytań SQL (zweryfikuj liczby na bazie!).

Uruchom:
    uv run pytest part2_adk/tests/test_report_system.py
"""

from pathlib import Path

import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

REPO = Path(__file__).resolve().parents[2]

# TODO(you): wskaż swój evalset po nagraniu sesji w adk web.
EVALSET = REPO / "part2_adk" / "evals" / "report_system.evalset.json"


@pytest.mark.skipif(not EVALSET.exists(), reason="Najpierw nagraj test set (moduł 12)")
@pytest.mark.asyncio
async def test_report_system_evalset():
    await AgentEvaluator.evaluate(
        agent_module="part2_adk.agents.report_system",
        eval_dataset_file_path_or_dir=str(EVALSET),
    )
