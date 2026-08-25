# Dzień 22 - agregacja

## Najważniejsze

- Agregacja zamienia wiele rekordów w podsumowanie.
- Filtrowanie wybiera rekordy, a agregowanie liczy lub sumuje dane.
- Akumulator przechowuje wynik budowany krok po kroku.
- Słownik może działać jako zestaw liczników albo sum.

## Mini przykład

```python
status_counts = {}

for order in orders:
    status = order["status"]
    status_counts[status] = status_counts.get(status, 0) + 1
```

## Zapamiętaj

- `.get(key, 0)` jest wygodne przy licznikach.
- Grupowanie oznacza liczenie wyniku osobno dla każdej kategorii.
- Przed agregacją warto normalizować dane, np. statusy tekstowe.
- Agregacja pojawia się też w SQL i Pandas.

## Pytania na rozmowę

### Pytanie: Czym różni się filtrowanie od agregacji?

<details>
<summary>Przykładowa odpowiedź</summary>

> Filtrowanie wybiera rekordy spełniające warunek, a agregacja tworzy z wielu rekordów podsumowanie, np. liczbę lub sumę.

</details>

### Pytanie: Po co używać akumulatora?

<details>
<summary>Przykładowa odpowiedź</summary>

> Akumulator przechowuje wynik aktualizowany podczas przechodzenia po kolejnych rekordach.

</details>

### Pytanie: Jak słownik pomaga liczyć rekordy według statusu?

<details>
<summary>Przykładowa odpowiedź</summary>

> Status może być kluczem, a liczba jego wystąpień wartością zwiększaną dla każdego rekordu.

</details>
