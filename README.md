# AI Multi-Agentic - ćwiczenia

Repozytorium ćwiczeniowe do dwudniowego szkolenia z budowy aplikacji agentowych
i systemów wieloagentowych. Budujemy jeden projekt warstwami: **agenta raportowego**
na bazie sklepu z muzyką (Chinook), od ręcznej pętli agentycznej aż po system
wieloagentowy z ewaluacją i guardrailami.

Stack: **Python + Google ADK 2.0 + OpenRouter** (jeden klucz na całe szkolenie),
zarządzanie przez **uv**.

---

## Wymagania

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (zarządzanie zależnościami i uruchamianiem)
- git
- Klucz API OpenRouter: https://openrouter.ai/keys (jeden klucz wystarczy na obie części)

## Setup (5 minut)

```bash
git clone <URL-tego-repo>
cd sages-adk-multiagent

uv sync                       # instaluje zależności
cp .env.example .env          # następnie wklej swój OPENROUTER_API_KEY do .env

uv run 00_setup/smoke_test.py # jeśli zobaczysz odpowiedź modelu - jesteś gotowy
```

---

## Jak to jest poukładane

```
data/chinook.sqlite      Baza sklepu z muzyką (11 tabel). Licencja MIT - patrz NOTICE.md
00_setup/                Smoke test - sprawdza, czy setup działa

part1_loop/              CZĘŚĆ 1: pętla agentyczna RĘCZNIE (bez ADK)
  01_simple_call/          wywołanie LLM + parametry
  02_function_calling/     function calling napisany samodzielnie
  03_agentic_loop/         pętla agentyczna na bazie Chinook

part2_adk/               CZĘŚĆ 2: Google ADK 2.0
  agents/                  agenci uruchamiani przez `adk web part2_adk/agents`
    hello/                   pierwszy agent (gotowy, referencja)
    sql_agent/               agent SQL (starter)
    sql_agent_to_tune/       agent z celowo słabą instrukcją - do tuningu
    report_system/           system wieloagentowy: planner -> dane -> raport (starter)
    sql_agent_guarded/       agent z guardrailem (bezpieczeństwo)
  tools/                   gotowe KLOCKI: db, wykresy, PDF, Excel, HTML
  evals/                   test set + szablony (ewaluacja)
  tests/                   testy automatyczne (pytest)

bonus/                   bezpieczniki B1-B7 - opcjonalne, gdy zostanie czas
solutions/               kompletne rozwiązania ćwiczeń
```

**Każde ćwiczenie ma własny `README.md`** (w swoim katalogu) z opisem: co ćwiczymy,
co jest w zakresie, a co przyjdzie później. Zacznij ćwiczenie od przeczytania go —
i Twój asystent AI też się nim kieruje, żeby trzymać Cię w temacie danego ćwiczenia.

## Najważniejsze komendy

```bash
# Część 1 - uruchamianie skryptów
uv run part1_loop/01_simple_call/starter.py

# Część 2 - interfejs webowy ADK (rozmowa, trace, ewaluacja)
uv run adk web part2_adk/agents

# Część 2 - agent w terminalu
uv run adk run part2_adk/agents/hello

# Ewaluacja z CLI
uv run adk eval part2_adk/agents/sql_agent part2_adk/evals/sql_agent.evalset.json \
    --config_file_path part2_adk/evals/test_config.json

# Testy automatyczne
uv run pytest part2_adk/tests
```

## Co przerabiamy (skrót)

**Dzień 1** - od zera do agenta: ograniczenia LLM -> wywołanie i parametry ->
function calling własnoręcznie -> pętla agentyczna -> wejście w ADK -> narzędzia,
sesje, pamięć -> **ewaluacja już pierwszego dnia**.

**Dzień 2** - skala i jakość: tuning promptów na test secie -> wieloagentowość ->
system raportowy (planner + dane + artefakty) -> testy automatyczne -> MCP i A2A ->
bezpieczeństwo. Wychodzisz z odpowiedzią na pytanie "na co uważać".

Pełny plan modułów: dokument planu szkolenia (u prowadzącego).

---

## Troubleshooting

- **`adk: command not found`** - uruchamiaj przez `uv run adk ...` (działa w środowisku projektu).
- **Brak odpowiedzi / 401** - sprawdź, czy `OPENROUTER_API_KEY` jest w `.env` i czy masz środki na koncie OpenRouter.
- **Agent nie widzi bazy** - uruchamiaj komendy z katalogu głównego repo (ścieżki do `data/chinook.sqlite` są względne do korzenia).
- **Model słabo woła narzędzia** - zmień `OPENROUTER_MODEL` w `.env` na mocniejszy (np. `anthropic/claude-3.5-sonnet`).

## Asystent AI w tym repo

Repo zawiera pliki instrukcji dla asystentów AI (`CLAUDE.md`, `AGENTS.md`,
`.github/copilot-instructions.md`, `.cursor/rules/`). Ustawiają one Twojego
asystenta w tryb **korepetytora**. Asystent **nie wygeneruje rozwiązania na samo
"rozwiąż mi to"** — najpierw poprosi, żebyś wytłumaczył, czym jest dane zadanie,
jak działa i jak je zaimplementować. Dopiero gdy pokażesz, że rozumiesz (i sam
podejmiesz decyzje projektowe), pomoże Ci to zakodować. Po drodze będzie
naprowadzać, zadawać pytania i prostować błędne wyobrażenia.

To celowe. Możesz uczyć się z asystentem "zgodnie ze sztuką" — ale kod ma być
efektem Twojego zrozumienia, nie skrótem przez prompt.

## Licencje

Kod: MIT (patrz `LICENSE`). Baza Chinook: MIT, (c) Luis Rocha (patrz `NOTICE.md`).
