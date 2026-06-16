"""Ćwiczenie 7 - kompaktowanie kontekstu / rolling window - moduł 6. STARTER.

Problem: każda tura dokłada się do okna kontekstu. Po wielu turach prompt puchnie -
rośnie koszt, w końcu uderzasz w limit. Dwie techniki ratunkowe:
- rolling / sliding window: trzymaj ostatnie N eventów (starsze wypadają),
- kompaktowanie: starsze tury zwiń w streszczenie (model podsumowuje) i zostaw
  streszczenie zamiast surowych eventów.

ADK ma sliding-window compaction natywnie przez `events_compaction_config` na `App`.
Tu prowadzimy długą rozmowę i obserwujemy, jak okno się zwija - a mimo to agent
nadal pamięta wczesny fakt (kompaktowanie zachowuje sedno).

Uruchom: uv run python ex_07_kompaktowanie/starter.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.model import get_model  # noqa: E402

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.apps.app import App, EventsCompactionConfig  # noqa: E402
from google.adk.apps.llm_event_summarizer import LlmEventSummarizer  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions import InMemorySessionService  # noqa: E402
import google.genai.types as gt  # noqa: E402

APP = "ex07"
USER = "uczestnik"
SID = "s1"

session_service = InMemorySessionService()

agent = LlmAgent(
    name="rozmowca",
    model=get_model(),
    instruction="Odpowiadasz po polsku, krótko - jednym zdaniem.",
)

# TODO(you): skonfiguruj kompaktowanie (sliding window) i wstaw je do App poniżej.
#   COMPACTION = EventsCompactionConfig(
#       summarizer=LlmEventSummarizer(llm=get_model()),
#       compaction_interval=3,    # co ile eventów zwijać
#       overlap_size=1,           # ile eventów nakładki między oknami
#       event_retention_size=6,   # ile ostatnich eventów zostawić surowych
#   )
# Na razie None => kompaktowanie wyłączone (stan startowy).
COMPACTION = None

app = App(name=APP, root_agent=agent, events_compaction_config=COMPACTION)
runner = Runner(app=app, session_service=session_service)


# --- KLOCKI (gotowe) ----------------------------------------------------------
def powiedz(tekst: str) -> str:
    msg = gt.Content(role="user", parts=[gt.Part.from_text(text=tekst)])
    final = ""
    for ev in runner.run(user_id=USER, session_id=SID, new_message=msg):
        if ev.is_final_response() and ev.content and ev.content.parts:
            final = "".join(p.text or "" for p in ev.content.parts)
    return final


def pokaz_kompaktowanie() -> None:
    s = asyncio.run(session_service.get_session(app_name=APP, user_id=USER, session_id=SID))
    compactions = [e for e in s.events if getattr(e.actions, "compaction", None)]
    print(f"\nEventów w sesji: {len(s.events)} | zwinięć (compaction): {len(compactions)}")
    for i, e in enumerate(compactions, 1):
        c = e.actions.compaction
        txt = "".join(p.text or "" for p in (c.compacted_content.parts or [])) if c.compacted_content else ""
        print(f"  streszczenie {i}: {txt[:200].strip()}")


def main() -> None:
    asyncio.run(session_service.create_session(app_name=APP, user_id=USER, session_id=SID))

    # Długa rozmowa - okno rośnie tura po turze.
    tury = [
        "Mam na imię Piotr.",
        "Lubię gatunek Rock.",
        "Pracuję w Poznaniu.",
        "Mam kota.",
        "Piję kawę bez cukru.",
        "Jeżdżę rowerem do pracy.",
    ]
    for t in tury:
        powiedz(t)

    pokaz_kompaktowanie()

    # Pytanie o WCZESNY fakt - czy przetrwał zwijanie kontekstu?
    print("\nPytanie o wczesny fakt:")
    print("  agent:", powiedz("Jak mam na imię?"))


if __name__ == "__main__":
    main()
