# Dzień 8 - Python: warunki `if`, `elif`, `else`

## Najważniejsze

- Warunki pozwalają wykonać różny kod zależnie od danych.
- `if` sprawdza pierwszy warunek.
- `elif` sprawdza kolejny warunek, jeśli poprzedni był fałszywy.
- `else` obsługuje pozostałe przypadki.

## Mini przykład

```python
status = "paid"

if status == "paid":
    print("Order is paid")
elif status == "pending":
    print("Order is pending")
else:
    print("Unknown status")
```

## Zapamiętaj

- W Pythonie porównanie równości zapisujemy jako `==`.
- Wcięcia są częścią składni.
- Warunki często służą do walidacji danych.

## Pytania na rozmowę

### Pytanie: Czym różni się `if` od `elif`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `if` rozpoczyna sprawdzanie warunków, a `elif` sprawdza kolejny warunek tylko wtedy, gdy wcześniejsze nie zostały spełnione.

</details>

### Pytanie: Po co jest `else`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Obsługuje wszystkie przypadki, które nie spełniły wcześniejszych warunków `if` i `elif`.

</details>

### Pytanie: Dlaczego w Pythonie używamy `==`, a nie `=` do porównania?

<details>
<summary>Przykładowa odpowiedź</summary>

> `==` porównuje dwie wartości, natomiast `=` przypisuje wartość do zmiennej.

</details>
