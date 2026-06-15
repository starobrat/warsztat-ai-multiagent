"""ROZWIĄZANIE ćwiczenia 6 - pamięć długoterminowa (Memory ponad rozmowy) - moduł 6.

Trzy TODO wypełnione: instrukcja (kiedy load_memory), tools=[load_memory], oraz
zapis sesji 1 do pamięci. Efekt: sesja 2 (NOWA) odzyskuje fakt z sesji 1.

Uruchom: uv run python solutions/ex_06_pamiec_dlugoterminowa/solution.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.memory import InMemoryMemoryService  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions import InMemorySessionService  # noqa: E402
from google.adk.tools import load_memory  # noqa: E402
import google.genai.types as gt  # noqa: E402

APP = "ex06"
USER = "uczestnik"

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

# TODO 1: instrukcja - kiedy sięgać do pamięci długoterminowej.
INSTRUKCJA = (
    "Jesteś asystentem z pamięcią długoterminową. Odpowiadasz po polsku, krótko. "
    "Gdy odpowiedź NIE wynika z bieżącej rozmowy, użyj narzędzia load_memory, "
    "żeby sprawdzić wcześniejsze rozmowy z tym użytkownikiem. Nie zmyślaj - jeśli "
    "ani rozmowa, ani pamięć nie dają odpowiedzi, powiedz, że nie wiesz."
)

root_agent = LlmAgent(
    name="pamiec_dluga",
    model=get_model(),
    instruction=INSTRUKCJA,
    tools=[load_memory],  # TODO 2: narzędzie pamięci długoterminowej
)

runner = Runner(
    agent=root_agent,
    app_name=APP,
    session_service=session_service,
    memory_service=memory_service,
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


def zapisz_sesje_do_pamieci(sid: str) -> None:
    s = asyncio.run(session_service.get_session(app_name=APP, user_id=USER, session_id=sid))
    asyncio.run(memory_service.add_session_to_memory(s))


def main() -> None:
    nowa_sesja("s1")
    odp1, _ = powiedz("s1", "Mam na imię Piotr i pracuję nad raportem sprzedaży gatunku Rock.")
    print(f"Sesja 1 (agent): {odp1}")

    # TODO 3: zapisz zakończoną sesję 1 do pamięci długoterminowej.
    zapisz_sesje_do_pamieci("s1")

    nowa_sesja("s2")
    odp2, narzedzia = powiedz("s2", "Jak mam na imię i nad czym pracuję?")
    print(f"Sesja 2 (agent): {odp2}")
    print(f"Sesja 2 - użyte narzędzia: {narzedzia or '(żadne)'}")


if __name__ == "__main__":
    main()
