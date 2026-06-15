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
  "05  pierwsze narzedzie  -  podlacz get_schema (adk web)"
  "06  instrukcja grounding  -  agent odmawia bez danych (adk web)"
  "07  docstring  -  kontrakt narzedzia (adk web)"
  "08  argumenty  -  narzedzie z parametrem (adk web)"
  "09  lancuch narzedzi  -  sekwencja wywolan (adk web)"
  "10  analityka iteracja  -  petla po gatunkach (adk web)"
  "11  raport wykres  -  artefakt PNG (adk web)"
  "12  ewaluacja  -  adk eval"
  "13  text-to-sql  -  agent pisze SQL (adk web)"
  "14  modele i diagnostyka  -  porownanie modeli (adk web)"
  "15  report_system  -  system wieloagentowy (adk web)"
  "16  testy  -  pytest"
  "17  guardrails  -  bezpieczenstwo (adk web)"
  "Wyjscie"
)
cmds=(
  "uv sync"
  "uv run python ex_00_setup/smoke_test.py"
  "uv run python ex_01_simple_call/starter.py"
  "uv run python ex_02_function_calling/starter.py"
  "uv run python ex_03_agentic_loop/starter.py"
  "uv run adk web ex_04_hello"
  "uv run adk web ex_05_pierwsze_narzedzie"
  "uv run adk web ex_06_instrukcja_grounding"
  "uv run adk web ex_07_docstring"
  "uv run adk web ex_08_argumenty"
  "uv run adk web ex_09_lancuch_narzedzi"
  "uv run adk web ex_10_analityka_iteracja"
  "uv run adk web ex_11_raport_wykres"
  "uv run adk eval ex_13_text_to_sql ex_12_eval/sql_agent.evalset.json --config_file_path ex_12_eval/test_config.json"
  "uv run adk web ex_13_text_to_sql"
  "uv run adk web ex_14_modele_i_diagnostyka"
  "uv run adk web ex_15_report_system"
  "uv run pytest ex_16_tests"
  "uv run adk web ex_17_guardrails"
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
