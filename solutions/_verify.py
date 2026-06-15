"""Harness weryfikacyjny prowadzącego (NIE część rozwiązań).

Uruchamia agenta ADK z rozwiązania programowo (InMemoryRunner), wysyła jedną
wiadomość i wypisuje: wywołania narzędzi (functionCall + args), odpowiedzi
narzędzi oraz finalny tekst. Dzięki temu da się potwierdzić sekcję "Działa, gdy"
z README bez klikania w `adk web`.

Użycie:
    uv run python solutions/_verify.py <katalog_agenta> "<wiadomość>" ['{"state":...}']

Przykład:
    uv run python solutions/_verify.py solutions/ex_08_pierwsze_narzedzie "Jakie tabele są w bazie?"
"""

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from google.adk.runners import InMemoryRunner  # noqa: E402
import google.genai.types as gt  # noqa: E402


def load_root_agent(ex_dir: Path):
    agent_path = ex_dir / "agent.py"
    spec = importlib.util.spec_from_file_location(f"sol_{ex_dir.name}", agent_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.root_agent


def run_once(ex_dir: Path, message: str, state: dict | None = None) -> dict:
    root_agent = load_root_agent(ex_dir)
    runner = InMemoryRunner(agent=root_agent, app_name="verify")
    svc = runner.session_service
    try:
        svc.create_session_sync(app_name="verify", user_id="u", session_id="s", state=state or {})
    except AttributeError:
        import asyncio

        asyncio.run(svc.create_session(app_name="verify", user_id="u", session_id="s", state=state or {}))

    msg = gt.Content(role="user", parts=[gt.Part.from_text(text=message)])
    tool_calls: list = []
    tool_responses: list = []
    final_text = ""
    for ev in runner.run(user_id="u", session_id="s", new_message=msg):
        if ev.content and ev.content.parts:
            for part in ev.content.parts:
                if getattr(part, "function_call", None):
                    fc = part.function_call
                    tool_calls.append({"name": fc.name, "args": dict(fc.args or {})})
                if getattr(part, "function_response", None):
                    fr = part.function_response
                    tool_responses.append({"name": fr.name, "response": fr.response})
        if ev.is_final_response() and ev.content and ev.content.parts:
            final_text = "".join(p.text or "" for p in ev.content.parts)
    return {"tool_calls": tool_calls, "tool_responses": tool_responses, "final": final_text}


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    ex_dir = Path(sys.argv[1]).resolve()
    message = sys.argv[2]
    state = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None

    result = run_once(ex_dir, message, state)
    print(f"\n=== {ex_dir.name} ===")
    print(f"PYTANIE: {message}")
    print("\nWYWOŁANIA NARZĘDZI:")
    if result["tool_calls"]:
        for tc in result["tool_calls"]:
            print(f"  -> {tc['name']}({tc['args']})")
    else:
        print("  (żadne)")
    print("\nODPOWIEDZI NARZĘDZI:")
    for tr in result["tool_responses"]:
        resp = str(tr["response"])
        print(f"  <- {tr['name']}: {resp[:300]}")
    print(f"\nFINALNA ODPOWIEDŹ:\n  {result['final']}")


if __name__ == "__main__":
    main()
