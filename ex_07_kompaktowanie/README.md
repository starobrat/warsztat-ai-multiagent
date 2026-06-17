# Ćwiczenie: kompaktowanie kontekstu / rolling window (moduł 6)

## Co ćwiczymy
Zarządzanie **rosnącym kontekstem**. Każda tura dokłada się do okna kontekstu - po
wielu turach prompt puchnie: rośnie koszt, spada jakość, w końcu uderzasz w limit
tokenów. Dwie techniki: **rolling window** (trzymaj ostatnie N eventów) i
**kompaktowanie** (starsze tury zwiń w streszczenie). ADK ma sliding-window
compaction natywnie - tu ją włączasz i obserwujesz.

## Zakres tego ćwiczenia
- `App(events_compaction_config=EventsCompactionConfig(...))`.
- `LlmEventSummarizer` jako "zwijacz" starszych eventów (streszczenia po polsku
  przez `prompt_template`).
- Kontrast dwóch biegów na tej samej rozmowie:
  - **A. kompaktowanie** - starsze tury zwinięte w streszczenie, wczesny fakt
    (imię) przeżywa, bo trafił do streszczenia,
  - **B. rolling window** - trzymamy tylko ostatnie N tur, wczesny fakt wypada
    z okna i agent go nie zna.

## Poza zakresem (przyjdzie później)
- Pamięć długoterminowa (Memory) - ex_06 (osobny mechanizm, nie mylić).
- Produkcyjne strojenie progów tokenowych - tu pokazujemy mechanizm, nie tuning.
- Narzędzia bazodanowe i agenci `adk web` - od ex_08.

## Koncepcja w pigułce
- **Rolling / sliding window**: bierzesz tylko ostatnie N eventów, starsze wypadają.
  Tanie, ale gubisz wczesny kontekst.
- **Kompaktowanie (compaction)**: starsze tury model zwija w streszczenie;
  streszczenie zostaje w oknie zamiast surowych eventów. Drożej, ale pamięta sedno.

ADK robi sliding-window compaction: co `compaction_interval` eventów zwija starsze w
streszczenie, z nakładką `overlap_size`, żeby nie zgubić styku okien.

## Twoje zadanie
Patrz `starter.py` (`# TODO(you)`): zbuduj `COMPACTION` jako `EventsCompactionConfig`
(z `LlmEventSummarizer(llm=get_model(), prompt_template=STRESZCZAJ_PO_POLSKU)`, ustaw
`compaction_interval` i `overlap_size`) i podmień `COMPACTION = None`. Uruchom i
porównaj: jak zmienia się bieg A po włączeniu kompaktowania (0 zwinięć -> zwinięcia
+ streszczenie), oraz dlaczego bieg B (rolling window) gubi imię.

## Wskazówki (jeśli pracujesz bez agenta AI)
- `EventsCompactionConfig` i `App` importujesz z `google.adk.apps.app`.
- `LlmEventSummarizer` z `google.adk.apps.llm_event_summarizer` - bierze `llm=`.
- Mały `compaction_interval` (np. 3) szybciej pokaże efekt na krótkiej rozmowie.

## "Działa", gdy
Po włączeniu kompaktowania bieg **A** raportuje co najmniej jedno zwinięcie ze
streszczeniem (po polsku), w którym przetrwało imię -> `imię 'Piotr' żyje
w streszczeniu: TAK` - mimo że surowa tura 1 została zwinięta. Bieg **B**
(rolling window: ostatnie N tur) pokazuje `imię 'Piotr' w oknie: NIE` - wczesna
tura wypadła z okna. Z `COMPACTION = None` bieg A nie ma żadnych zwinięć
(`wypełnij TODO`).

Dowód jest deterministyczny (sprawdzamy zawartość okna, nie swobodną odpowiedź
modelu) - dlatego wynik jest taki sam przy każdym uruchomieniu.

## Pójdź dalej
- Zwiększ `compaction_interval` - od ilu eventów pojawia się pierwsze zwinięcie?
- Porównaj z czystym rolling window (obcięcie bez streszczenia): co wtedy dzieje się
  z wczesnym faktem? Dlaczego kompaktowanie go ratuje, a obcięcie nie?
- Skrajny wariant: `include_contents='none'` na agencie - agent bez historii w ogóle.
