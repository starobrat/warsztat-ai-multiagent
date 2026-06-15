"""Pytest: dołóż korzeń repo do sys.path.

Dzięki temu testy (ex_23_tests) mogą zaimportować agentów po numerowanej nazwie
katalogu (np. "ex_14_text_to_sql") i pakiet `common`, niezależnie od trybu importu
pytest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
