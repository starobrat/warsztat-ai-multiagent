# Ćwiczenie ex_16: modele i diagnostyka (moduł 8)

## Co ćwiczymy
**Diagnostyka: gdzie naprawdę jest problem - model, opis narzędzia czy instrukcja?**
Agent sklepu muzycznego ma kilka narzędzi, ale ich **opisy (docstringi) wprowadzają
w błąd**. Słabszy model słucha opisów dosłownie, wybiera **złe narzędzie** i oblewa
eval (czerwony). Znasz test i wiesz, czego oczekuje - Twoje zadanie to **zdiagnozować
warstwę** i zazielenić go.

## Znasz test, do którego pracujesz
Test set: `diagnostyka.evalset.json` (3 przypadki). Dla każdego wiadomo, **które
narzędzie** powinno paść i z jakim argumentem - np. "Ile utworów AC/DC sprzedaliśmy?"
ma wywołać `sales_by_artist`, a "Jakie albumy nagrał AC/DC?" -> `albums_by_artist`.
Kryterium trajektorii jest **ostre** (`tool_trajectory_avg_score: 1.0`): liczy się,
KTÓRE narzędzie agent wybrał. Zły wybór = czerwony.

## Dlaczego agent chodzi na słabszym modelu
Startuje na słabszym modelu (`get_weak_model`). Mocny model **maskuje** złe opisy -
i tak trafi w intencję klienta, więc nigdy nie zobaczyłbyś czerwonego. Słabszy słucha
docstringów dosłownie: zły opis = zły wybór narzędzia. To samo w sobie jest lekcją -
**im słabszy model, tym bardziej liczy się opis narzędzia i instrukcja**.

## Twoje zadanie
1. Uruchom eval i zobacz czerwony:
   ```bash
   uv run adk eval ex_16_modele_i_diagnostyka \
       ex_16_modele_i_diagnostyka/diagnostyka.evalset.json \
       --config_file_path ex_16_modele_i_diagnostyka/test_config.json
   ```
2. **Zdiagnozuj, którą warstwę naprawić** - czytaj raport evalu: jakie narzędzie agent
   wywołał zamiast oczekiwanego? To wskazuje na **opis narzędzia** (docstring). Czy w
   ogóle sięgnął po narzędzie? Jeśli nie - to **instrukcja**. Czy nawet z dobrym opisem
   się myli? To **model**.
3. **Napraw opisy narzędzi** w `agent.py` (`# TODO(you)`): docstring to kontrakt, po
   którym model wybiera narzędzie. Nie zmieniaj nazw funkcji ani ich środka.
4. (Opcjonalnie) dopracuj `instruction`: powiedz wprost, kiedy którego narzędzia użyć.
5. Uruchom eval ponownie - aż **zielony**.

## Porównaj modele (część diagnostyczna)
Sprawdź, jak **różne modele** radzą sobie z tym samym zadaniem - to oddziela problem
"model" od problemu "opis/instrukcja":
- Podmień `get_weak_model()` na `get_model()` (mocniejszy) i zobacz, czy mocniejszy
  model trafia w narzędzia **mimo** kiepskich opisów (zwykle tak - dlatego maskuje błąd).
- Możesz też wskazać konkretny model OpenAI bez zmiany kodu, ustawiając zmienną
  środowiskową przed uruchomieniem, np.:
  ```bash
  OPENAI_MODEL_WEAK=gpt-4o-mini uv run adk eval ex_16_modele_i_diagnostyka ...
  ```
- Aktualna lista modeli OpenAI (do podstawienia): https://platform.openai.com/docs/models

## Poza zakresem (świadomie zabronione lub później)
- **Zmiana nazw narzędzi albo ich środka** - naprawiasz OPISY i instrukcję, nie logikę.
- Dodawanie nowych funkcji agentowi - to nie tutaj.
- Tworzenie nowych test case'ów - moduł 7 (`ex_15_ewaluacja/`).
- Testy automatyczne / pytest - moduł 12 (`ex_23_tests/`).

## "Działa", gdy
Eval świeci na zielono, a Ty potrafisz powiedzieć, **która warstwa** była źródłem
problemu (model / opis narzędzia / instrukcja) i dlaczego.

## Pójdź dalej
- Zepsuj z powrotem jeden docstring i sprawdź na mocnym modelu (`get_model`) - czy
  mocniejszy model nadal trafia? Gdzie jest granica "maskowania" złego opisu?
- Dorzuć czwarty przypadek do evalsetu (np. sprzedaż innego wykonawcy) i znów dociśnij.
