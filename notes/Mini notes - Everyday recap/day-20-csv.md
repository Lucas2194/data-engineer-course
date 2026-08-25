# Dzień 20 - pliki CSV od podstaw

## Najważniejsze

- CSV to tekstowy format danych tabelarycznych.
- Pierwszy wiersz często jest nagłówkiem z nazwami kolumn.
- Moduł `csv` pomaga poprawnie czytać i zapisywać CSV.
- `csv.DictReader` zwraca każdy wiersz jako słownik.

## Mini przykład

```python
import csv

with open("data/orders.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
```

## Zapamiętaj

- CSV jest tekstem, ale reprezentuje tabelę.
- Separator oddziela kolumny, najczęściej jest to przecinek.
- `DictReader` używa nagłówków jako kluczy słownika.
- Dane z CSV często wymagają konwersji typów.
- Wyniki pipeline'u warto zapisywać do folderu `output`.

## Pytania na rozmowę

### Pytanie: Czym CSV różni się od zwykłego TXT?

<details>
<summary>Przykładowa odpowiedź</summary>

> CSV jest plikiem tekstowym o ustalonej strukturze tabeli: wiersze zawierają pola rozdzielone separatorem, często z nagłówkiem kolumn.

</details>

### Pytanie: Co robi `csv.DictReader`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Czyta CSV i zwraca każdy wiersz jako słownik, w którym kluczami są nazwy kolumn.

</details>

### Pytanie: Dlaczego po odczycie CSV trzeba sprawdzać typy danych?

<details>
<summary>Przykładowa odpowiedź</summary>

> Ponieważ wartości z CSV są odczytywane jako tekst i przed obliczeniami mogą wymagać walidacji oraz konwersji.

</details>
