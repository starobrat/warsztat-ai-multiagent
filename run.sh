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
  "03  agentic loop  -  petla na bazie Chinook"
  "04  hello  -  pierwszy agent ADK (adk web)"
  "05  pamiec i sesje  -  stan sesji, co agent pamieta (adk web)"
  "06  pamiec dlugoterminowa  -  Memory ponad rozmowy (skrypt)"
  "07  kompaktowanie  -  rolling window + streszczanie kontekstu (skrypt)"
  "08  pierwsze narzedzie  -  podlacz get_schema (adk web)"
  "09  instrukcja grounding  -  agent odmawia bez danych (adk web)"
  "10  docstring  -  kontrakt narzedzia (adk web)"
  "11  argumenty  -  narzedzie z parametrem (adk web)"
  "12  lancuch narzedzi  -  sekwencja wywolan (adk web)"
  "13  analityka iteracja  -  petla po gatunkach (adk web)"
  "14  raport wykres  -  artefakt PNG (adk web)"
  "15  ewaluacja  -  adk eval"
  "16  text-to-sql  -  agent pisze SQL (adk web)"
  "17  modele i diagnostyka  -  porownanie modeli (adk web)"
  "18  report_system  -  system wieloagentowy (adk web)"
  "19  testy  -  pytest"
  "20  guardrails  -  bezpieczenstwo (adk web)"
  "---  DEMA prowadzacego (do pokazania na zywo)  ---"
  "demo 01  halucynacja  -  model zmysla pewnym tonem"
  "demo 02  function calling  -  model zwraca decyzje, kod wykonuje"
  "demo 09  transfer  -  delegacja master -> specjalisci (adk web)"
  "demo 13  mcp  -  podpiecie serwera MCP (adk web)"
  "demo 14  injection  -  prompt injection bez guardraila (adk web)"
  "---  ROZWIAZANIA (dla prowadzacego)  ---"
  "sol 01  simple call"
  "sol 02  function calling"
  "sol 03  agentic loop"
  "sol 04  hello"
  "sol 05  pamiec i sesje"
  "sol 06  pamiec dlugoterminowa"
  "sol 07  kompaktowanie"
  "sol 08  pierwsze narzedzie"
  "sol 09  instrukcja grounding"
  "sol 10  docstring"
  "sol 11  argumenty"
  "sol 12  lancuch narzedzi"
  "sol 13  analityka iteracja"
  "sol 14  raport wykres"
  "sol 15  eval  -  zielony na rozwiazanym SQL (adk eval)"
  "sol 16  text-to-sql"
  "sol 17  diagnostyka  -  eval zielony na slabym modelu"
  "sol 18  report_system"
  "sol 19  testy  -  SOLUTION.md"
  "sol 20  guardrails"
  "Wyjscie"
)
cmds=(
  "uv sync"
  "uv run python ex_00_setup/smoke_test.py"
  "uv run python ex_01_simple_call/starter.py"
  "uv run python ex_02_function_calling/starter.py"
  "uv run python ex_03_agentic_loop/starter.py"
  "uv run adk web ex_04_hello"
  "uv run adk web ex_05_pamiec_i_sesje"
  "uv run python ex_06_pamiec_dlugoterminowa/starter.py"
  "uv run python ex_07_kompaktowanie/starter.py"
  "uv run adk web ex_08_pierwsze_narzedzie"
  "uv run adk web ex_09_instrukcja_grounding"
  "uv run adk web ex_10_docstring"
  "uv run adk web ex_11_argumenty"
  "uv run adk web ex_12_lancuch_narzedzi"
  "uv run adk web ex_13_analityka_iteracja"
  "uv run adk web ex_14_raport_wykres"
  "uv run adk eval ex_16_text_to_sql ex_15_eval/sql_agent.evalset.json --config_file_path ex_15_eval/test_config.json"
  "uv run adk web ex_16_text_to_sql"
  "uv run adk web ex_17_modele_i_diagnostyka"
  "uv run adk web ex_18_report_system"
  "uv run pytest ex_19_tests"
  "uv run adk web ex_20_guardrails"
  ":"
  "uv run python demo_01_halucynacja/run.py"
  "uv run python demo_02_function_calling/run.py"
  "uv run adk web demo_09_transfer"
  "uv run adk web demo_13_mcp"
  "uv run adk web demo_14_injection"
  ":"
  "uv run python solutions/ex_01_simple_call/solution.py"
  "uv run python solutions/ex_02_function_calling/solution.py"
  "uv run python solutions/ex_03_agentic_loop/solution.py"
  "uv run adk web solutions/ex_04_hello"
  "uv run adk web solutions/ex_05_pamiec_i_sesje"
  "uv run python solutions/ex_06_pamiec_dlugoterminowa/solution.py"
  "uv run python solutions/ex_07_kompaktowanie/solution.py"
  "uv run adk web solutions/ex_08_pierwsze_narzedzie"
  "uv run adk web solutions/ex_09_instrukcja_grounding"
  "uv run adk web solutions/ex_10_docstring"
  "uv run adk web solutions/ex_11_argumenty"
  "uv run adk web solutions/ex_12_lancuch_narzedzi"
  "uv run adk web solutions/ex_13_analityka_iteracja"
  "uv run adk web solutions/ex_14_raport_wykres"
  "uv run adk eval solutions/ex_16_text_to_sql ex_15_eval/sql_agent.evalset.json --config_file_path ex_15_eval/test_config.json"
  "uv run adk web solutions/ex_16_text_to_sql"
  "uv run adk eval solutions/ex_17_modele_i_diagnostyka ex_15_eval/sql_agent.evalset.json --config_file_path ex_15_eval/test_config.json"
  "uv run adk web solutions/ex_18_report_system"
  "cat solutions/ex_19_tests/SOLUTION.md"
  "uv run adk web solutions/ex_20_guardrails"
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
