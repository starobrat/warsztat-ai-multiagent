"""Ćwiczenie 7 - kompaktowanie vs rolling window - moduł 6. STARTER.

Sedno: oba sposoby TNĄ okno kontekstu, ale różnią się tym, co zostaje.
Ta sama rozmowa, dwa biegi:
  A. KOMPAKTOWANIE - starsze tury model zwija w streszczenie; wczesny fakt
     (imię "Piotr") ma przeżyć, bo trafia do streszczenia.
  B. ROLLING WINDOW - trzymamy tylko ostatnie N tur; starsze wypadają, więc
     wczesny fakt ginie i agent go nie zna.

Twoje zadanie: włącz kompaktowanie (sekcja TODO niżej) i odpal. Dopóki COMPACTION
jest None, bieg A nic nie zwija - zobacz, jak zmienia się wynik po włączeniu.

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

# Wspólny scenariusz: WCZESNY fakt = imię, podane w turze 1.
TURY = [
    "Mam na imię Piotr.",            # <- wczesny fakt (tura 1)
    "Uczę się grać na ukulele.",
    "Pracuję w Poznaniu.",
    "Mam psa.",
    "Piję kawę bez cukru.",
    "Jeżdżę rowerem do pracy.",
]
PYTANIE = "Jak mam na imię?"
IMIE = "Piotr"  # wczesny fakt, którego losy śledzimy
OSTATNIE_N = 2  # rolling window: trzymamy tylko ostatnie N tur

# Domyślny szablon streszczenia w ADK jest po angielsku - wymuszamy polski.
# Ważne: kolejne zwinięcie streszcza poprzednie streszczenie, więc każemy mu
# ZAWSZE przenosić imię i wcześniejsze fakty - inaczej wczesny fakt może zniknąć.
STRESZCZAJ_PO_POLSKU = (
    "Streść PO POLSKU historię rozmowy użytkownika z agentem w 1-2 zdaniach. "
    "ZAWSZE zachowaj imię użytkownika oraz wcześniej ustalone fakty o nim - także "
    "jeśli pochodzą z wcześniejszego streszczenia. Nie pomijaj ich."
    "\n\n{conversation_history}"
)

# TODO(you): zbuduj kompaktowanie (sliding window) i podmień None poniżej.
#   COMPACTION = EventsCompactionConfig(
#       summarizer=LlmEventSummarizer(llm=get_model(), prompt_template=STRESZCZAJ_PO_POLSKU),
#       compaction_interval=4,    # co ile eventów zwijać starsze w streszczenie
#       overlap_size=1,           # nakładka między oknami
#   )
#   (ADK 2.2.0: token_threshold i event_retention_size MUSZĄ iść w parze - inaczej
#    ValidationError; tu zwijamy po liczbie eventów, więc ich nie ustawiamy.)
# Na razie None => kompaktowanie wyłączone (stan startowy: bieg A nic nie zwija).
COMPACTION = None


def _zbuduj_agenta() -> LlmAgent:
    return LlmAgent(
        name="rozmowca",
        model=get_model(),
        instruction=(
            "Jesteś rozmówcą. Odpowiadasz po polsku, jednym krótkim zdaniem - "
            "naturalnie reagujesz na to, co mówi użytkownik. Gdy pyta o fakt, "
            "którego w rozmowie NIE podał, powiedz wprost: Nie wiem. Nie zgaduj."
        ),
    )


def _odtworz_i_zapytaj(compaction, tury):
    """Świeża sesja: odtwórz podane tury, na końcu zadaj PYTANIE.

    Zwraca (odpowiedź_na_pytanie, sesja).
    """
    session_service = InMemorySessionService()
    app = App(name=APP, root_agent=_zbuduj_agenta(), events_compaction_config=compaction)
    runner = Runner(app=app, session_service=session_service)
    asyncio.run(session_service.create_session(app_name=APP, user_id=USER, session_id=SID))

    def powiedz(tekst: str) -> str:
        msg = gt.Content(role="user", parts=[gt.Part.from_text(text=tekst)])
        final = ""
        for ev in runner.run(user_id=USER, session_id=SID, new_message=msg):
            if ev.is_final_response() and ev.content and ev.content.parts:
                final = "".join(p.text or "" for p in ev.content.parts)
        return final

    for t in tury:
        powiedz(t)
    odp = powiedz(PYTANIE)
    sesja = asyncio.run(session_service.get_session(app_name=APP, user_id=USER, session_id=SID))
    return odp, sesja


def _streszczenia(sesja) -> list[str]:
    """Teksty streszczeń (compaction) zapisanych w sesji."""
    out = []
    for e in sesja.events:
        c = getattr(e.actions, "compaction", None)
        if c and c.compacted_content:
            out.append("".join(p.text or "" for p in (c.compacted_content.parts or [])))
    return out


def main() -> None:
    # A. KOMPAKTOWANIE - cała rozmowa, starsze tury zwijane w streszczenie.
    _, sesja_a = _odtworz_i_zapytaj(COMPACTION, TURY)
    streszcz = _streszczenia(sesja_a)
    imie_w_streszczeniu = any(IMIE in s for s in streszcz)

    print("=== A. Kompaktowanie (starsze tury -> streszczenie) ===")
    print(f"  podano tur: {len(TURY)} | zwinięć: {len(streszcz)}")
    for i, s in enumerate(streszcz, 1):
        print(f"  streszczenie {i}: {' '.join(s.split())}")
    if streszcz:
        print(
            f"  -> wczesne tury zwinięte; imię '{IMIE}' żyje w streszczeniu: "
            f"{'TAK' if imie_w_streszczeniu else 'NIE'}"
        )
    else:
        print("  -> brak zwinięć (kompaktowanie wyłączone) - wypełnij TODO, by starsze tury się zwinęły")

    # B. ROLLING WINDOW - trzymamy tylko ostatnie N tur, starsze wypadają.
    okno_b = TURY[-OSTATNIE_N:]
    imie_w_oknie_b = any(IMIE in t for t in okno_b)
    print(f"\n=== B. Rolling window (tylko ostatnie {OSTATNIE_N} tury, bez streszczenia) ===")
    print(f"  okno modelu: {', '.join(repr(t) for t in okno_b)}")
    print(
        f"  -> imię '{IMIE}' w oknie: {'TAK' if imie_w_oknie_b else 'NIE'} "
        f"(wczesna tura wypadła z okna)"
    )

    print(
        "\nPo włączeniu kompaktowania bieg A pokaże streszczenie z imieniem (TAK),\n"
        "a bieg B (samo obcięcie) wczesny fakt zgubi (NIE)."
    )


if __name__ == "__main__":
    main()
