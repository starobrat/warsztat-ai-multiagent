# Bonus B2: Agent z wyszukiwaniem w sieci

## Zadanie
Wzbogać raport o kontekst spoza bazy. Dodaj wyszukiwanie web, żeby agent mógł
np. dopisać krótki komentarz rynkowy obok danych sprzedażowych.

## Uwaga
Wbudowany `google_search` w ADK działa natywnie z modelami Gemini. Na OpenRouter
zrób to jako zwykłe narzędzie-funkcję: wywołanie dowolnego API wyszukiwania
(np. Tavily, Brave Search API) opakowane w funkcję z docstringiem.

## Czego się uczysz
Łączenie dwóch źródeł (baza + sieć) w jednej odpowiedzi - typowy wzorzec RAG-owy.
