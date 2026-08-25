# Dzień 11 - Python: pętla `for`

## Najważniejsze

- Pętla `for` pozwala przejść po elementach kolekcji.
- W data engineeringu pętle często służą do sprawdzania rekordów.
- W pętli można używać warunków `if`.
- Wyniki pracy pętli często zapisujemy do listy.

## Mini przykład

```python
orders = [
    {"order_id": 1001, "status": "paid"},
    {"order_id": 1002, "status": "pending"},
]

for order in orders:
    print(order["status"])
```

## Zapamiętaj

- `for item in items:` czytamy jako: dla każdego elementu w kolekcji.
- `range()` generuje sekwencję liczb.
- Pętla może zbierać błędy walidacji.
- Nazwa zmiennej w pętli powinna opisywać pojedynczy element.

## Pytania na rozmowę

### Pytanie: Po co używać pętli?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby wykonać tę samą operację dla wielu elementów bez powtarzania kodu.

</details>

### Pytanie: Czym jest `range()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> To funkcja tworząca zakres liczb, po którym można iterować, np. `range(3)` daje kolejno `0`, `1`, `2`.

</details>

### Pytanie: Jak pętla pomaga w walidacji wielu rekordów?

<details>
<summary>Przykładowa odpowiedź</summary>

> Pozwala przejść po każdym rekordzie, zastosować te same reguły i zebrać błędne rekordy lub komunikaty.

</details>
