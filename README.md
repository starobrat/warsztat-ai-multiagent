# AI Multi-Agentic - ćwiczenia

Repozytorium ćwiczeniowe do dwudniowego szkolenia z budowy aplikacji agentowych
i systemów wieloagentowych. Budujemy jeden projekt warstwami: **agenta raportowego**
na bazie sklepu z muzyką (Chinook), od ręcznej pętli agentycznej aż po system
wieloagentowy z ewaluacją i guardrailami.

Stack: **Python + Google ADK 2.0 + OpenAI** (jeden klucz na całe szkolenie),
zarządzanie przez **uv**.

---

## Wymagania

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (zarządzanie zależnościami i uruchamianiem)
- git
- Klucz API OpenAI: https://platform.openai.com/api-keys (jeden klucz wystarczy na obie części)

## Setup (5 minut)

```bash
git clone <URL-tego-repo>
cd sages-adk-multiagent

uv sync                       # instaluje zależności
cp .env.example .env          # następnie wklej swój OPENAI_API_KEY do .env

uv run 00_setup/smoke_test.py # jeśli zobaczysz odpowiedź modelu - jesteś gotowy
```

Najprościej w trakcie warsztatu: `./run.sh` - menu strzałkami (↑/↓, Enter), z którego
odpalisz `uv sync`, smoke test i kolejne ćwiczenia bez wpisywania komend.

---

## Jak to jest poukładane

Ćwiczenia są ponumerowane po kolei (00 -> 10) i idą w tempie szkolenia. Część 1
(01-03) robisz RĘCZNIE, bez ADK. Część 2 (04-10) to Google ADK 2.0.

```
data/chinook.sqlite      Baza sklepu z muzyką (11 tabel). Licencja MIT - patrz NOTICE.md
common/                  Wspólny kod: llm.py (część 1), model.py (ADK) + tools/ (KLOCKI)
  tools/                   gotowe KLOCKI: db, wykresy, PDF, Excel, HTML

00_setup/                Smoke test - sprawdza, czy setup działa

# CZĘŚĆ 1: pętla agentyczna RĘCZNIE (bez ADK)
01_simple_call/          wywołanie LLM + parametry
02_function_calling/     function calling napisany samodzielnie
03_agentic_loop/         pętla agentyczna na bazie Chinook

# CZĘŚĆ 2: Google ADK 2.0 (każdy agent: `adk web <katalog>`)
04_hello/                pierwszy agent (gotowy, referencja)
05_sql_agent/            agent SQL (starter)
06_evaluation/           test set + szablony (ewaluacja, moduł 7)
07_sql_agent_tuning/     agent z celowo słabą instrukcją - do tuningu (moduł 8)
08_report_system/        system wieloagentowy: planner -> dane -> raport (starter)
09_tests/                testy automatyczne (pytest, moduł 12)
10_guardrails/           agent z guardrailem (bezpieczeństwo, moduł 14)

bonus/                   bezpieczniki B1-B7 - opcjonalne, gdy zostanie czas
solutions/               kompletne rozwiązania ćwiczeń
```

**Każde ćwiczenie ma własny `README.md`** (w swoim katalogu) z opisem: co ćwiczymy,
co jest w zakresie, a co przyjdzie później. Zacznij ćwiczenie od przeczytania go —
i Twój asystent AI też się nim kieruje, żeby trzymać Cię w temacie danego ćwiczenia.

Agentów ADK uruchamiasz po jednym, wskazując jego katalog: `adk web 05_sql_agent`
otwiera w przeglądarce dokładnie tego agenta (rozmowa, trace, ewaluacja).

## Najważniejsze komendy

```bash
# Część 1 - uruchamianie skryptów
uv run 01_simple_call/starter.py

# Część 2 - interfejs webowy ADK (rozmowa, trace, ewaluacja) - wskaż katalog agenta
uv run adk web 05_sql_agent

# Część 2 - agent w terminalu
uv run adk run 04_hello

# Ewaluacja z CLI
uv run adk eval 05_sql_agent 06_evaluation/sql_agent.evalset.json \
    --config_file_path 06_evaluation/test_config.json

# Testy automatyczne
uv run pytest 09_tests
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
- **Brak odpowiedzi / 401** - sprawdź, czy `OPENAI_API_KEY` jest w `.env` i czy masz środki na koncie OpenAI.
- **Agent nie widzi bazy** - uruchamiaj komendy z katalogu głównego repo (ścieżki do `data/chinook.sqlite` są względne do korzenia).
- **Model słabo woła narzędzia** - zmień `OPENAI_MODEL` w `.env` na mocniejszy model OpenAI.

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
