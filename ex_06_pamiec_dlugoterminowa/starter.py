"""Ćwiczenie 6 - pamięć długoterminowa (Memory ponad rozmowy) - moduł 6. STARTER.

W ex_05 fakt żył w STANIE sesji - nowa rozmowa zaczynała od zera. Tu idziemy
poziom wyżej: pamięć, która PRZEŻYWA wiele rozmów. W ADK to osobny serwis
(MemoryService) + narzędzie `load_memory`, którym agent sam przeszukuje przeszłość.

Przepływ: w sesji 1 użytkownik podaje fakt -> po rozmowie zapisujemy sesję do
pamięci -> w sesji 2 (NOWEJ) agent przez load_memory ten fakt odzyskuje.

Uruchom: uv run python ex_06_pamiec_dlugoterminowa/starter.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.memory import InMemoryMemoryService  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions import InMemorySessionService  # noqa: E402
from google.adk.tools import load_memory  # noqa: E402
import google.genai.types as gt  # noqa: E402

APP = "ex06"
USER = "uczestnik"

# --- KLOCKI (gotowe) - serwisy sesji i pamięci długoterminowej ---------------
session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()


# TODO(you): napisz instrukcję agenta. Klucz: gdy odpowiedź NIE wynika z bieżącej
# rozmowy, agent ma sięgnąć do pamięci długoterminowej narzędziem load_memory
# (a nie zmyślać). Odpowiada po polsku, krótko.
INSTRUKCJA = ""

root_agent = LlmAgent(
    name="pamiec_dluga",
    model=get_model(),
    instruction=INSTRUKCJA,
    # TODO(you): podłącz narzędzie pamięci długoterminowej -> tools=[load_memory]
    tools=[],
)

runner = Runner(
    agent=root_agent,
    app_name=APP,
    session_service=session_service,
    memory_service=memory_service,
)


# --- KLOCKI (gotowe) - pomocnicze funkcje, żeby nie pisać async w main --------
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


def zapisz_sesje_do_pamieci(sid: str) -> None:
    """Pobiera zakończoną sesję i dokłada ją do pamięci długoterminowej."""
    s = asyncio.run(session_service.get_session(app_name=APP, user_id=USER, session_id=sid))
    asyncio.run(memory_service.add_session_to_memory(s))


def main() -> None:
    # Sesja 1: użytkownik podaje fakt.
    nowa_sesja("s1")
    odp1, _ = powiedz("s1", "Mam na imię Piotr i pracuję nad raportem sprzedaży gatunku Rock.")
    print(f"Sesja 1 (agent): {odp1}")

    # TODO(you): zapisz zakończoną sesję 1 do pamięci długoterminowej.
    #   Wskazówka: masz gotowy helper zapisz_sesje_do_pamieci("s1").
    #   Bez tego kroku sesja 2 NIE będzie nic wiedzieć (jak w ex_05).

    # Sesja 2: NOWA rozmowa - stan sesji 1 tu nie istnieje.
    nowa_sesja("s2")
    odp2, narzedzia = powiedz("s2", "Jak mam na imię i nad czym pracuję?")
    print(f"Sesja 2 (agent): {odp2}")
    print(f"Sesja 2 - użyte narzędzia: {narzedzia or '(żadne)'}")


if __name__ == "__main__":
    main()
