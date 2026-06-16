# Rozwiązanie: ex_15 - uruchom eval i czytaj metryki (NIEKODOWE)

Ćwiczenie robi się w adk web (zakładka Eval). Tu leży WZORCOWY test set
(sql_agent.evalset.json) + kryteria (test_config.json) - gold do porównania.

Komenda CLI (demo prowadzącego, na rozwiązanym agencie SQL):
  uv run adk eval solutions/ex_14_text_to_sql solutions/ex_15_ewaluacja/sql_agent.evalset.json --config_file_path solutions/ex_15_ewaluacja/test_config.json
Wynik zweryfikowany: na solutions/ex_14_text_to_sql -> Tests passed: 2, Tests failed: 0.
Metryki: tool_trajectory_avg_score=0.0 (trajektoria nie wymagana identyczna), response_match_score=0.5 (ROUGE >= 0.5).
Friction: brak.
