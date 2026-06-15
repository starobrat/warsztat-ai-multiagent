# Ćwiczenie ex_05: pamięć i sesje (moduł 6)

<!-- [TODO Piotr - ŁUK / "gdzie jesteśmy": 1-2 zdania kontynuacji z ex_04.
Np.: w ex_04 agent rozmawiał, ale nic nie pamiętał między pytaniami w obrębie
tej samej rozmowy. Zanim dołożymy narzędzia do bazy - zobaczmy, co i jak agent
PAMIĘTA. Twój głos.] -->

## Co ćwiczymy
**Pamięć agenta w ADK.** Agent dostaje dwa narzędzia, które zapisują i czytają
**stan sesji** (`tool_context.state`). Zobaczysz, że w obrębie jednej rozmowy
agent pamięta - a w nowej sesji zaczyna od zera. Jeden koncept: różnica między
**sesją / stanem** a **pamięcią długoterminową**.

## Które narzędzia podpinamy
- `zapamietaj(fakt)` (gotowe, w `agent.py`) - dopisuje fakt do `state["notatki"]`.
- `przypomnij()` (gotowe, w `agent.py`) - zwraca to, co zapamiętano w tej sesji.

## Twoje zadanie
Patrz `agent.py` (`# TODO(you)`):
1. **Podłącz** `zapamietaj` i `przypomnij` do `tools`.
2. **Podmień instrukcję-placeholder** na instrukcję pamięci. Gotowiec:
   <!-- [TODO Piotr: wklej gotową instrukcję dla uczestnika - np.: gdy użytkownik
   podaje fakt o sobie (imię, rola, preferencja), zawołaj zapamietaj; gdy pyta,
   co o nim wiesz, zawołaj przypomnij; odpowiadaj po polsku.] -->
3. Uruchom `uv run adk web ex_05_pamiec_i_sesje`. Powiedz np. "mam na imię Piotr,
   pracuję jako architekt", potem zapytaj "co o mnie wiesz?".

## Jak sprawdzić, że działa
- Zakładka **Events**: widać `functionCall` z `zapamietaj`, potem `przypomnij`.
- Zakładka **State**: po zapamiętaniu pojawia się klucz `notatki` z faktami.
- **Nowa sesja** (nowy czat w adk web): agent NIE pamięta poprzednich faktów -
  to właśnie granica sesji. Pamięć długoterminowa (ponad sesje) to osobny temat.

## Praca z agentem AI
To repo ma bramkę sokratejską (patrz `CLAUDE.md`): asystent nie wklei Ci
rozwiązania, dopóki nie pokażesz, że rozumiesz. Poproś go, żeby przeprowadził Cię
przez to, **czym różni się stan sesji od pamięci długoterminowej** i **jak narzędzie
zapisuje dane do `state`** - nie o gotowy kod.

## "Działa", gdy
Agent w obrębie jednej rozmowy odtwarza fakty, które mu podałeś, a w zakładce
State widać klucz `notatki`. Po otwarciu nowej sesji zaczyna od zera.

## Pójdź dalej
<!-- [TODO Piotr - otwarte rozszerzenie + CLIFFHANGER do ex_08. Np.: agent pamięta,
ale wciąż nic nie wie o naszych danych - czas dać mu PIERWSZE narzędzie do bazy
(ex_08). Możesz też wspomnieć trwałe sesje (--session_service_uri, bonus B4)
i pamięć długoterminową. Twój głos.] -->
