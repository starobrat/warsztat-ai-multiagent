"""ROZWIĄZANIE ćwiczenia 6 - pamięć faktów o użytkowniku (ponad sesjami) - moduł 6.

Dwa TODO wypełnione: instrukcja (kiedy zapisać fakt, kiedy przypomnieć) oraz
tools=[zapamietaj_fakt, przypomnij_fakty]. Fakty trafiają do stanu z zasięgiem
`user:`, więc sesja 2 (NOWA) odzyskuje je bez dopytywania.

Uruchom: uv run python solutions/ex_06_pamiec_dlugoterminowa/solution.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions import InMemorySessionService  # noqa: E402
from google.adk.tools.tool_context import ToolContext  # noqa: E402
import google.genai.types as gt  # noqa: E402

APP = "ex06"
USER = "uczestnik"

session_service = InMemorySessionService()


# Klucz "user:fakty" ma zasięg UŻYTKOWNIKA - przeżywa kolejne sesje tego usera.
def zapamietaj_fakt(kategoria: str, wartosc: str, tool_context: ToolContext) -> str:
    """Zapisuje trwały fakt o użytkowniku (ma przeżyć kolejne rozmowy).

    Wołaj, gdy użytkownik podaje coś stałego o sobie - np. ulubione gatunki
    muzyczne albo z kim współpracuje.
    kategoria: krótka etykieta faktu, np. "gatunki" albo "współpracownicy".
    wartosc: treść faktu, np. "Rock, Jazz".
    """
    fakty = dict(tool_context.state.get("user:fakty", {}))
    fakty[kategoria] = wartosc
    tool_context.state["user:fakty"] = fakty
    return f"Zapamiętano: {kategoria} = {wartosc}"


def przypomnij_fakty(tool_context: ToolContext) -> dict:
    """Zwraca fakty zapamiętane o użytkowniku (także z poprzednich rozmów)."""
    return dict(tool_context.state.get("user:fakty", {}))


# TODO 1: instrukcja - kiedy zapisać fakt, a kiedy go przypomnieć.
INSTRUKCJA = (
    "Jesteś asystentem, który pamięta fakty o użytkowniku. Odpowiadasz po polsku, krótko. "
    "Gdy użytkownik podaje trwały fakt o sobie (np. ulubione gatunki, z kim współpracuje), "
    "zapisz go narzędziem zapamietaj_fakt (dobierz krótką kategorię). Gdy pyta, co o nim "
    "wiesz, wywołaj przypomnij_fakty i odpowiedz na podstawie wyniku. Jeśli danego faktu "
    "nie ma, powiedz, że nie wiesz - nie zmyślaj."
)

root_agent = LlmAgent(
    name="pamiec_uzytkownika",
    model=get_model(),
    instruction=INSTRUKCJA,
    tools=[zapamietaj_fakt, przypomnij_fakty],  # TODO 2
)

runner = Runner(
    agent=root_agent,
    app_name=APP,
    session_service=session_service,
)


def nowa_sesja(sid: str) -> None:
    asyncio.run(session_service.create_session(app_name=APP, user_id=USER, session_id=sid))


def powiedz(sid: str, tekst: str) -> tuple[str, list[str]]:
    msg = gt.Content(role="user", parts=[gt.Part.from_text(text=tekst)])
    final, narzedzia = "", []
    for ev in runner.run(user_id=USER, session_id=sid, new_message=msg):
        if ev.content and ev.content.parts:
            for p in ev.content.parts:
                if getattr(p, "function_call", None):
                    narzedzia.append(p.function_call.name)
        if ev.is_final_response() and ev.content and ev.content.parts:
            final = "".join(p.text or "" for p in ev.content.parts)
    return final, narzedzia


def main() -> None:
    nowa_sesja("s1")
    pyt1 = "Interesują mnie gatunki Rock i Jazz, a współpracuję z Jane Peacock."
    odp1, n1 = powiedz("s1", pyt1)
    print("=" * 70)
    print("SESJA 1 (nowa rozmowa)")
    print(f"  Ty:    {pyt1}")
    print(f"  Agent: {odp1}")
    print(f"  Użyte narzędzia: {n1 or '(żadne)'}")

    nowa_sesja("s2")
    pyt2 = "Które gatunki mnie interesują i z kim współpracuję?"
    odp2, n2 = powiedz("s2", pyt2)
    print("=" * 70)
    print("SESJA 2 (NOWA rozmowa - stan sesji 1 tu nie istnieje, fakty user: przeżywają)")
    print(f"  Ty:    {pyt2}")
    print(f"  Agent: {odp2}")
    print(f"  Użyte narzędzia: {n2 or '(żadne)'}")
    print("=" * 70)


if __name__ == "__main__":
    main()
