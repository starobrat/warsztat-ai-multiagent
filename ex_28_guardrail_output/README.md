# Ćwiczenie ex_28: guardrail na wyjściu (after_tool)

## Co ćwiczymy
**Guardrail wyjściowy**: maskowanie danych wrażliwych PO tym, jak narzędzie je
zwróci, a ZANIM trafią do modelu i użytkownika. `after_tool_callback` dostaje
`(tool, args, tool_context, tool_response)` i jeśli zwróci `dict`, ADK użyje go
zamiast oryginalnej odpowiedzi narzędzia.

Trzeci z czterech guardraili. ex_26 pilnował akcji, ex_27 wejścia. Tutaj pilnujemy
WYJŚCIA - wyciek danych (e-maile, telefony klientów) to osobne ryzyko od injection.
Dalej: błędy (`ex_29`).

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`): napisz ciało `redact_sensitive_output`. Dla
`run_query`, jeśli `tool_response` ma `rows` (lista list), przepuść każdą komórkę
przez `_mask` (gotowe) i zwróć zmodyfikowany `tool_response`. W innym wypadku `None`.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `tool_response` to dict z `db.run_query`: klucze `columns`, `rows`, `row_count`.
- `rows` to lista wierszy, każdy wiersz to lista komórek. Maskuj komórka po komórce.
- `_mask` (gotowe) zwraca `***@***` / `***` dla e-maila/telefonu, resztę bez zmian.

## Jak sprawdzić
```
uv run python solutions/_verify.py solutions/ex_28_guardrail_output "Pokaż imię, nazwisko i email pierwszych 3 klientów"
```

## "Działa", gdy
W `ODPOWIEDZI NARZĘDZI` kolumna z e-mailem/telefonem jest zamaskowana (`***@***`,
`***`), a imię i nazwisko zostają widoczne. Model nie zna prawdziwych e-maili,
bo nigdy ich nie zobaczył.

## Pójdź dalej
- Maskuj po nazwie kolumny (`Email`, `Phone`), nie po wyglądzie wartości - pewniej.
- Co z adresem i fakturami? Gdzie postawić granicę "dane wrażliwe"?
- Połącz z `ex_26`: wejście + akcja + wyjście to trzy warstwy tej samej obrony.

<!-- [TODO Piotr: narracja - moment "agent może wygadać dane, których sam nie powinien widzieć"; analogia do maskowania PII w logach / RODO] -->
