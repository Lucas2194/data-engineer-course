# Dzień 10 - Python: listy

## Najważniejsze

- Lista przechowuje wiele wartości w jednej zmiennej.
- Elementy listy mają indeksy zaczynające się od `0`.
- Lista może przechowywać teksty, liczby, słowniki i inne obiekty.
- Listy są bardzo częste przy pracy z rekordami danych.

## Mini przykład

```python
statuses = ["paid", "pending", "cancelled"]

print(statuses[0])
statuses.append("refunded")
print(len(statuses))
```

## Zapamiętaj

- `list[0]` pobiera pierwszy element.
- `list[-1]` pobiera ostatni element.
- `append()` dodaje element na końcu.
- `len()` zwraca liczbę elementów.
- Operator `in` sprawdza, czy element jest na liście.

## Pytania na rozmowę

### Pytanie: Dlaczego pierwszy indeks to `0`?

<details>
<summary>Przykładowa odpowiedź</summary>

> W Pythonie indeks oznacza przesunięcie od początku kolekcji, więc pierwszy element znajduje się w odległości `0`.

</details>

### Pytanie: Co robi `append()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Dodaje jeden element na końcu listy.

</details>

### Pytanie: Jak sprawdzić, czy status jest na liście dozwolonych statusów?

<details>
<summary>Przykładowa odpowiedź</summary>

> Operatorem `in`, np. `status in allowed_statuses`.

</details>
