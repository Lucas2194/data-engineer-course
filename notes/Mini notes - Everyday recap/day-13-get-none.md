# Dzień 13 - Python: `.get()` i `None`

## Najważniejsze

- `.get()` pozwala bezpiecznie odczytać wartość ze słownika.
- Gdy klucza nie ma, `.get()` zwraca `None` albo wartość domyślną.
- `None` oznacza brak wartości.
- Bezpieczny odczyt jest ważny przy danych niepewnej jakości.

## Mini przykład

```python
order = {"order_id": 1001, "status": "paid"}

city = order.get("city")
status = order.get("status", "unknown")
```

## Zapamiętaj

- `dict["key"]` zgłosi `KeyError`, jeśli klucza nie ma.
- `dict.get("key")` zwróci `None`, jeśli klucza nie ma.
- `dict.get("key", default)` zwróci wartość domyślną.
- `None` sprawdzaj przez `is None`.

## Pytania na rozmowę

### Pytanie: Kiedy lepiej użyć `.get()` zamiast `[]`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Gdy klucza może nie być w słowniku i nie chcesz otrzymać błędu `KeyError`.

</details>

### Pytanie: Co oznacza `None`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Oznacza brak wartości. Nie jest tym samym co `0`, pusty tekst ani `False`.

</details>

### Pytanie: Po co podawać wartość domyślną w `.get()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby zamiast `None` otrzymać ustaloną wartość, gdy klucz nie istnieje, np. `order.get("status", "unknown")`.

</details>
