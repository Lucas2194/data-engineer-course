# Dzień 21 - JSON

## Najważniejsze

- JSON to popularny format wymiany danych.
- JSON jest podobny do słowników i list w Pythonie, ale jest formatem tekstowym.
- Dane JSON mogą być zagnieżdżone.
- Moduł `json` służy do odczytu i zapisu JSON w Pythonie.

## Mini przykład

```python
import json

with open("data/orders.json", encoding="utf-8") as file:
    orders = json.load(file)
```

## Zapamiętaj

- `json.load(file)` czyta JSON z pliku.
- `json.loads(text)` czyta JSON z tekstu.
- Serializacja zamienia obiekt Pythona na JSON.
- Deserializacja zamienia JSON na obiekt Pythona.
- Przy JSON trzeba obsługiwać błędy formatu i brakujące pola.

## Pytania na rozmowę

### Pytanie: Czym JSON różni się od słownika Pythona?

<details>
<summary>Przykładowa odpowiedź</summary>

> JSON jest tekstowym formatem wymiany danych, a słownik jest obiektem istniejącym w pamięci programu Pythona.

</details>

### Pytanie: Czym różni się `load()` od `loads()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `json.load()` odczytuje JSON z obiektu pliku, a `json.loads()` przetwarza tekst zawierający JSON.

</details>

### Pytanie: Dlaczego JSON jest ważny w API?

<details>
<summary>Przykładowa odpowiedź</summary>

> Jest powszechnym, niezależnym od języka formatem przesyłania ustrukturyzowanych danych między systemami.

</details>
