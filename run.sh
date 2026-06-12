#!/usr/bin/env bash
# Proste menu wyboru: strzalki gora/dol, Enter uruchamia, q konczy.
# Dziala bez zaleznosci, zgodne z bash 3.2 (domyslny na macOS).
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

labels=(
  "uv sync  -  instalacja zaleznosci"
  "00  smoke test  -  sprawdz setup (klucz + model)"
  "01  simple call  -  wywolanie LLM + parametry"
  "02  function calling  -  recznie"
  "Chinook  -  pokaz schemat bazy (przed cw. 03)"
  "03  agentic loop  -  petla na bazie Chinook"
  "04  hello  -  pierwszy agent ADK (adk web)"
  "05  sql_agent  -  agent SQL (adk web)"
  "06  ewaluacja  -  adk eval na 05_sql_agent"
  "07  tuning promptu  -  adk eval (TDD: czerwony -> zielony)"
  "07  tuning promptu  -  adk web"
  "08  report_system  -  system wieloagentowy (adk web)"
  "09  testy  -  pytest"
  "10  guardrails  -  bezpieczenstwo (adk web)"
  "Wyjscie"
)
cmds=(
  "uv sync"
  "uv run python 00_setup/smoke_test.py"
  "uv run python 01_simple_call/starter.py"
  "uv run python 02_function_calling/starter.py"
  "uv run python 00_setup/schema.py"
  "uv run python 03_agentic_loop/starter.py"
  "uv run adk web 04_hello"
  "uv run adk web 05_sql_agent"
  "uv run adk eval 05_sql_agent 06_evaluation/sql_agent.evalset.json --config_file_path 06_evaluation/test_config.json"
  "uv run adk eval 07_sql_agent_tuning 06_evaluation/sql_agent.evalset.json --config_file_path 06_evaluation/test_config.json"
  "uv run adk web 07_sql_agent_tuning"
  "uv run adk web 08_report_system"
  "uv run pytest 09_tests"
  "uv run adk web 10_guardrails"
  "__EXIT__"
)

sel=0
n=${#labels[@]}

draw() {
  clear
  printf "  Warsztat AI Multi-Agentic  -  co odpalic?\n"
  printf "  strzalki gora/dol, Enter = uruchom, q = wyjscie\n\n"
  local i
  for ((i = 0; i < n; i++)); do
    if [ "$i" -eq "$sel" ]; then
      printf "  \033[7m > %s \033[0m\n" "${labels[$i]}"
    else
      printf "    %s\n" "${labels[$i]}"
    fi
  done
}

run_selected() {
  local cmd="${cmds[$sel]}"
  [ "$cmd" = "__EXIT__" ] && { clear; exit 0; }
  clear
  printf "> %s\n\n" "$cmd"
  eval "$cmd"
  printf "\n--- gotowe. Nacisnij Enter, aby wrocic do menu ---"
  read -r _
}

while true; do
  draw
  IFS= read -rsn1 key || true
  case "$key" in
    $'\x1b')
      # sekwencja strzalki: ESC [ A/B (przychodzi w jednym pakiecie)
      read -rsn2 rest || true
      case "$rest" in
        '[A') sel=$(((sel - 1 + n) % n)) ;;
        '[B') sel=$(((sel + 1) % n)) ;;
      esac
      ;;
    "" | $'\n' | $'\r') run_selected ;;   # Enter
    k | K) sel=$(((sel - 1 + n) % n)) ;;   # vim w gore
    j | J) sel=$(((sel + 1) % n)) ;;       # vim w dol
    q | Q) clear; exit 0 ;;
  esac
done
