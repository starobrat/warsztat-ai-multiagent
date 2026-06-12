"""Pytest: dołóż korzeń repo do sys.path.

Dzięki temu testy (09_tests) mogą zaimportować agentów po numerowanej nazwie
katalogu (np. "05_sql_agent") i pakiet `common`, niezależnie od trybu importu
pytest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
