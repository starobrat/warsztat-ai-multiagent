"""ROZWIĄZANIE ćwiczenia 7 - kompaktowanie kontekstu / rolling window - moduł 6.

TODO wypełnione: COMPACTION = EventsCompactionConfig(...) podłączone do App.
Efekt: w sesji pojawiają się zwinięcia (streszczenia), a agent nadal pamięta
wczesny fakt ("Piotr") mimo zwinięcia okna.

Uruchom: uv run python solutions/ex_07_kompaktowanie/solution.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
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

# TODO wypełnione: sliding-window compaction.
COMPACTION = EventsCompactionConfig(
    summarizer=LlmEventSummarizer(llm=get_model()),
    compaction_interval=3,    # co ile eventów zwijać (rolling window = 3)
    overlap_size=1,           # nakładka między oknami
)
# Uwaga (ADK 2.2.0): event_retention_size i token_threshold MUSZĄ być ustawione
# RAZEM - samo event_retention_size rzuca ValidationError. Tu zwijamy po liczbie
# eventów (compaction_interval), więc tych dwóch nie ustawiamy.

app = App(name=APP, root_agent=agent, events_compaction_config=COMPACTION)
runner = Runner(app=app, session_service=session_service)


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

    print("\nPytanie o wczesny fakt:")
    print("  agent:", powiedz("Jak mam na imię?"))


if __name__ == "__main__":
    main()
