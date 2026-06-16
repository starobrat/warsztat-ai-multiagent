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
  "05  pamiec i sesje  -  stan sesji (adk web)"
  "06  pamiec dlugoterminowa  -  Memory ponad rozmowy (skrypt)"
  "07  kompaktowanie  -  rolling window + streszczanie (skrypt)"
  "08  narzedzie + grounding  -  get_schema + odmowa bez danych (adk web)"
  "09  docstring  -  kontrakt narzedzia (adk web)"
  "10  argumenty  -  narzedzie z parametrem (adk web)"
  "11  lancuch narzedzi  -  sekwencja wywolan (adk web)"
  "12  analityka iteracja  -  petla po gatunkach (adk web)"
  "13  raport wykres  -  artefakt PNG (adk web)"
  "14  text-to-sql  -  agent pisze SQL (adk web)"
  "15  ewaluacja  -  zbuduj test set + uruchom + metryki (adk eval)"
  "16  modele i diagnostyka  -  diagnoza: model / docstring / instrukcja (adk eval)"
  "17  delegacja / transfer  -  master -> sub_agents (adk web)"
  "18  sekwencja  -  SequentialAgent + output_key (adk web)"
  "19  rownoleglosc  -  ParallelAgent (adk web)"
  "20  petla agentow  -  LoopAgent (adk web)"
  "21  planner  -  system raportowy: planner (adk web)"
  "22  report_writer  -  system raportowy: artefakt (adk web)"
  "23  testy  -  pytest"
  "24  guardrail: tool  -  before_tool, blokuj SQL (adk web)"
  "25  guardrail: input  -  before_model, blokuj injection (adk web)"
  "26  guardrail: output  -  after_tool, redakcja danych (adk web)"
  "27  guardrail: blad  -  on_tool_error (adk web)"
  "---  DEMA prowadzacego  ---"
  "demo 01  halucynacja"
  "demo 02  function calling"
  "demo 09  transfer (adk web)"
  "demo 13  mcp (adk web)"
  "demo 14  injection (adk web)"
  "---  ROZWIAZANIA  ---"
  "sol 01  simple call"
  "sol 02  function calling"
  "sol 03  agentic loop"
  "sol 04  hello"
  "sol 05  pamiec i sesje"
  "sol 06  pamiec dlugoterminowa"
  "sol 07  kompaktowanie"
  "sol 08  narzedzie + grounding"
  "sol 09  docstring"
  "sol 10  argumenty"
  "sol 11  lancuch narzedzi"
  "sol 12  analityka iteracja"
  "sol 13  raport wykres"
  "sol 14  text-to-sql"
  "sol 15  ewaluacja  -  zielony na rozwiazanym SQL"
  "sol 16  diagnostyka  -  eval zielony na slabym modelu"
  "sol 17  delegacja / transfer"
  "sol 18  sekwencja"
  "sol 19  rownoleglosc"
  "sol 20  petla agentow"
  "sol 21  planner"
  "sol 22  report_writer"
  "sol 23  testy  -  SOLUTION.md"
  "sol 24  guardrail tool"
  "sol 25  guardrail input"
  "sol 26  guardrail output"
  "sol 27  guardrail blad"
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
  "uv run adk web ex_08_narzedzie_grounding"
  "uv run adk web ex_09_docstring"
  "uv run adk web ex_10_argumenty"
  "uv run adk web ex_11_lancuch_narzedzi"
  "uv run adk web ex_12_analityka_iteracja"
  "uv run adk web ex_13_raport_wykres"
  "uv run adk web ex_14_text_to_sql"
  "uv run adk eval ex_14_text_to_sql ex_15_ewaluacja/sql_agent.evalset.json --config_file_path ex_15_ewaluacja/test_config.json"
  "uv run adk eval ex_16_modele_i_diagnostyka ex_16_modele_i_diagnostyka/diagnostyka.evalset.json --config_file_path ex_16_modele_i_diagnostyka/test_config.json"
  "uv run adk web ex_17_delegacja_transfer"
  "uv run adk web ex_18_sekwencja"
  "uv run adk web ex_19_rownoleglosc"
  "uv run adk web ex_20_petla_agentow"
  "uv run adk web ex_21_planner"
  "uv run adk web ex_22_report_writer"
  "uv run pytest ex_23_tests"
  "uv run adk web ex_24_guardrail_tool"
  "uv run adk web ex_25_guardrail_input"
  "uv run adk web ex_26_guardrail_output"
  "uv run adk web ex_27_guardrail_blad"
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
  "uv run adk web solutions/ex_08_narzedzie_grounding"
  "uv run adk web solutions/ex_09_docstring"
  "uv run adk web solutions/ex_10_argumenty"
  "uv run adk web solutions/ex_11_lancuch_narzedzi"
  "uv run adk web solutions/ex_12_analityka_iteracja"
  "uv run adk web solutions/ex_13_raport_wykres"
  "uv run adk web solutions/ex_14_text_to_sql"
  "uv run adk eval solutions/ex_14_text_to_sql ex_15_ewaluacja/sql_agent.evalset.json --config_file_path ex_15_ewaluacja/test_config.json"
  "uv run adk eval solutions/ex_16_modele_i_diagnostyka ex_16_modele_i_diagnostyka/diagnostyka.evalset.json --config_file_path ex_16_modele_i_diagnostyka/test_config.json"
  "uv run adk web solutions/ex_17_delegacja_transfer"
  "uv run adk web solutions/ex_18_sekwencja"
  "uv run adk web solutions/ex_19_rownoleglosc"
  "uv run adk web solutions/ex_20_petla_agentow"
  "uv run adk web solutions/ex_21_planner"
  "uv run adk web solutions/ex_22_report_writer"
  "cat solutions/ex_23_tests/SOLUTION.md"
  "uv run adk web solutions/ex_24_guardrail_tool"
  "uv run adk web solutions/ex_25_guardrail_input"
  "uv run adk web solutions/ex_26_guardrail_output"
  "uv run adk web solutions/ex_27_guardrail_blad"
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
      read -rsn2 rest || true
      case "$rest" in
        '[A') sel=$(((sel - 1 + n) % n)) ;;
        '[B') sel=$(((sel + 1) % n)) ;;
      esac
      ;;
    "" | $'\n' | $'\r') run_selected ;;
    k | K) sel=$(((sel - 1 + n) % n)) ;;
    j | J) sel=$(((sel + 1) % n)) ;;
    q | Q) clear; exit 0 ;;
  esac
done
