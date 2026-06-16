"""Ćwiczenie ex_22: LoopAgent - pętla z warunkiem stopu (moduł 11). STARTER.

Sequential = po kolei, Parallel = naraz. LoopAgent = POWTARZAJ ten sam krok, aż
warunek stopu. Tu agent iteracyjnie skraca hasło reklamowe i SAM kończy pętlę
narzędziem exit_loop, gdy uzna, że jest dość krótkie. max_iterations to twarda
poprzeczka bezpieczeństwa (pętla nie kręci się w nieskończoność).

Narzędzie exit_loop jest gotowe (google.adk.tools). Twoje zadanie: złożyć LoopAgent
z agenta-iteratora i ustawić limit iteracji.

Uruchom: uv run adk web ex_22_petla_agentow (albo adk run ex_22_petla_agentow).
"""

from common.model import get_model

from google.adk.agents import LoopAgent, LlmAgent
from google.adk.tools import exit_loop


# Agent-iterator - w każdej iteracji skraca hasło i decyduje, czy kończyć. GOTOWY.
skracacz = LlmAgent(
    name="skracacz",
    model=get_model(),
    description="Iteracyjnie skraca hasło reklamowe, aż będzie krótkie i mocne.",
    instruction=(
        "Skracasz hasło reklamowe w pętli, jedna iteracja = jedno skrócenie.\n"
        "Dotychczasowa najlepsza wersja: {haslo_robocze?}\n"
        "Jeśli powyżej jest już jakaś wersja, skróć JĄ; jeśli puste, skróć hasło "
        "z prośby użytkownika.\n"
        "ZAWSZE napisz w odpowiedzi nową, krótszą wersję hasła (mniej słów, "
        "mocniej) - to jest wynik tej iteracji.\n"
        "Dopiero gdy hasło ma maksymalnie 4 słowa i nie da się go sensownie "
        "skrócić, na końcu tej samej odpowiedzi wywołaj narzędzie exit_loop, żeby "
        "zakończyć pętlę."
    ),
    tools=[exit_loop],
    output_key="haslo_robocze",
)

# TODO(you): złóż LoopAgent z agenta skracacz. Ustaw max_iterations jako twardy
# limit (np. 5), żeby pętla na pewno się zatrzymała, nawet gdyby model nie wywołał
# exit_loop. sub_agents=[skracacz].
root_agent = LoopAgent(
    name="petla_skracania",
    description="Powtarza skracanie hasła, aż będzie krótkie (lub do limitu iteracji).",
    # TODO(you): sub_agents=[...] oraz max_iterations=...
    sub_agents=[],
)
