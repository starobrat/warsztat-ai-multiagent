"""Ćwiczenie 6 - pamięć faktów o użytkowniku (ponad sesjami) - moduł 6. STARTER.

W ex_05 fakt żył w STANIE sesji - nowa rozmowa zaczynała od zera. Tu idziemy
poziom wyżej: fakty o użytkowniku, które PRZEŻYWAJĄ kolejne rozmowy. Sztuczka to
stan z zasięgiem `user:` - klucz `user:...` jest przypisany do UŻYTKOWNIKA, nie do
pojedynczej sesji, więc widać go też w nowej rozmowie tego samego użytkownika.

Przepływ: w sesji 1 użytkownik podaje istotne fakty -> agent zapisuje je narzędziem
-> w sesji 2 (NOWEJ) agent odzyskuje je z `user:` state, bez dopytywania.

Uruchom: uv run python ex_06_pamiec_dlugoterminowa/starter.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions import InMemorySessionService  # noqa: E402
from google.adk.tools.tool_context import ToolContext  # noqa: E402
import google.genai.types as gt  # noqa: E402

APP = "ex06"
USER = "uczestnik"

# --- KLOCKI (gotowe) - serwis sesji ------------------------------------------
session_service = InMemorySessionService()


# --- KLOCKI (gotowe) - narzędzia zapisu i odczytu faktów o użytkowniku --------
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


# TODO(you) [krok 1]: napisz instrukcję agenta. Kiedy wołać `zapamietaj_fakt`
# (gdy user podaje trwały fakt o sobie), a kiedy `przypomnij_fakty` (gdy pyta,
# co o nim wiesz). Odpowiada po polsku, krótko. Gotowiec w README.
INSTRUKCJA = ""

root_agent = LlmAgent(
    name="pamiec_uzytkownika",
    model=get_model(),
    instruction=INSTRUKCJA,
    # TODO(you) [krok 2]: podłącz narzędzia -> tools=[zapamietaj_fakt, przypomnij_fakty]
    tools=[],
)

runner = Runner(
    agent=root_agent,
    app_name=APP,
    session_service=session_service,
)


# --- KLOCKI (gotowe) - pomocnicze, żeby nie pisać async w main ---------------
def nowa_sesja(sid: str) -> None:
    asyncio.run(session_service.create_session(app_name=APP, user_id=USER, session_id=sid))


def powiedz(sid: str, tekst: str) -> tuple[str, list[str]]:
    """Wysyła jedną wiadomość do agenta; zwraca (finalny tekst, lista narzędzi)."""
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
    # Sesja 1: użytkownik podaje trwałe fakty o sobie.
    nowa_sesja("s1")
    odp1, n1 = powiedz("s1", "Interesują mnie gatunki Rock i Jazz, a współpracuję z Jane Peacock.")
    print(f"Sesja 1 (agent): {odp1}")
    print(f"Sesja 1 - użyte narzędzia: {n1 or '(żadne)'}")

    # Sesja 2: NOWA rozmowa tego samego użytkownika - stan sesji 1 tu nie istnieje,
    # ale fakty z zasięgu user: przeżywają.
    nowa_sesja("s2")
    odp2, n2 = powiedz("s2", "Które gatunki mnie interesują i z kim współpracuję?")
    print(f"Sesja 2 (agent): {odp2}")
    print(f"Sesja 2 - użyte narzędzia: {n2 or '(żadne)'}")


if __name__ == "__main__":
    main()
