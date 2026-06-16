# DEMO 00: system, który zbudujemy (moduł 1, slajd 11)

Demo dla PROWADZĄCEGO - "zobaczcie, co tu zbudujemy". Nie jest to ćwiczenie.

## Uruchomienie
```bash
uv run adk web demo_00_system
```
Otwórz `adk web`, wybierz agenta `demo_system_chinook`.

## Scenariusz pokazu
1. **Struktura bazy:** zapytaj "Jak wygląda struktura tej bazy?" - agent woła
   `get_schema` i opisuje tabele Chinook.
2. **Dowolne pytanie analityczne**, np.:
   - "Którzy wykonawcy sprzedali się najlepiej? Zrób wykres top 10."
   - "Pokaż sprzedaż wg gatunku - wykres."
   Agent sam pisze SELECT, wykonuje go (`run_query`) i rysuje wykres
   (`narysuj_wykres_slupkowy`) - PNG ląduje w zakładce **Artifacts**.
3. **Pointa:** nie zaprogramowaliśmy tego pod konkretne pytanie. Agent sam dobiera
   SQL i narzędzia w pętli. Przez dwa dni rozbieramy to na części:
   - pętla agentyczna (moduł 4),
   - narzędzia + grounding (moduł 6, ćw. ex_08-ex_13),
   - text-to-SQL (ćw. ex_14),
   - ewaluacja i diagnostyka (moduł 7-8),
   - system wieloagentowy (moduł 9+).

## Co pod maską
Ten sam zestaw klocków, którego uczestnicy użyją w ćwiczeniach:
`common.tools.db` (get_schema, run_query - read-only Chinook),
`common.tools.charts` (bar_chart_artifact), `common.model` (get_model, LiteLLM/OpenAI).
