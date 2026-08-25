# Dzień 17 - obsługa błędów

## Najważniejsze

- Wyjątek to sytuacja, w której program nie może normalnie kontynuować pracy.
- `try/except` pozwala obsłużyć przewidywalne błędy.
- Najczęstsze błędy w danych to między innymi `ValueError`, `KeyError` i `TypeError`.
- Nie warto łapać zbyt szerokiego `except`, bo ukrywa prawdziwe problemy.

## Mini przykład

```python
value = "249.99"

try:
    amount = float(value)
except ValueError:
    amount = None
```

## Zapamiętaj

- `ValueError` pojawia się np. przy nieudanej konwersji.
- `KeyError` pojawia się przy braku klucza w słowniku.
- `TypeError` pojawia się przy operacji na złym typie danych.
- `isinstance()` sprawdza typ wartości.
- Normalizacja tekstu pomaga porównywać dane.

## Pytania na rozmowę

### Pytanie: Kiedy użyć `try/except`, a kiedy zwykłego `if`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `if` służy do sprawdzania przewidywalnych warunków, a `try/except` do obsługi operacji, które mogą zgłosić wyjątek, np. konwersji tekstu na liczbę.

</details>

### Pytanie: Dlaczego `except Exception` bywa niebezpieczny?

<details>
<summary>Przykładowa odpowiedź</summary>

> Łapie prawie wszystkie wyjątki i może ukryć błąd programistyczny. Lepiej obsługiwać konkretne typy błędów.

</details>

### Pytanie: Co oznacza `None` w funkcji walidującej?

<details>
<summary>Przykładowa odpowiedź</summary>

> Znaczenie zależy od ustalonej umowy funkcji. Może oznaczać np. brak błędu albo brak poprawnej wartości, dlatego powinno być jasno opisane.

</details>
