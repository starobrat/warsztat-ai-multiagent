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
  "06  pierwsze narzedzie  -  podlacz get_schema (adk web)"
  "07  instrukcja grounding  -  agent odmawia bez danych (adk web)"
  "08  docstring  -  kontrakt narzedzia (adk web)"
  "09  argumenty  -  narzedzie z parametrem (adk web)"
  "10  lancuch narzedzi  -  sekwencja wywolan (adk web)"
  "11  analityka iteracja  -  petla po gatunkach (adk web)"
  "12  raport wykres  -  artefakt PNG (adk web)"
  "13  ewaluacja  -  adk eval"
  "14  text-to-sql  -  agent pisze SQL (adk web)"
  "15  modele i diagnostyka  -  porownanie modeli (adk web)"
  "16  report_system  -  system wieloagentowy (adk web)"
  "17  testy  -  pytest"
  "18  guardrails  -  bezpieczenstwo (adk web)"
  "---  DEMA prowadzacego (do pokazania na zywo)  ---"
  "demo 01  halucynacja  -  model zmysla pewnym tonem"
  "demo 02  function calling  -  model zwraca decyzje, kod wykonuje"
  "demo 09  transfer  -  delegacja master -> specjalisci (adk web)"
  "demo 13  mcp  -  podpiecie serwera MCP (adk web)"
  "demo 14  injection  -  prompt injection bez guardraila (adk web)"
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
  "uv run adk web ex_06_pierwsze_narzedzie"
  "uv run adk web ex_07_instrukcja_grounding"
  "uv run adk web ex_08_docstring"
  "uv run adk web ex_09_argumenty"
  "uv run adk web ex_10_lancuch_narzedzi"
  "uv run adk web ex_11_analityka_iteracja"
  "uv run adk web ex_12_raport_wykres"
  "uv run adk eval ex_14_text_to_sql ex_13_eval/sql_agent.evalset.json --config_file_path ex_13_eval/test_config.json"
  "uv run adk web ex_14_text_to_sql"
  "uv run adk web ex_15_modele_i_diagnostyka"
  "uv run adk web ex_16_report_system"
  "uv run pytest ex_17_tests"
  "uv run adk web ex_18_guardrails"
  ":"
  "uv run python demo_01_halucynacja/run.py"
  "uv run python demo_02_function_calling/run.py"
  "uv run adk web demo_09_transfer"
  "uv run adk web demo_13_mcp"
  "uv run adk web demo_14_injection"
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
