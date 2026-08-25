# Dzień 9 - Python: `and`, `or`, `not`

## Najważniejsze

- Operatory logiczne pozwalają łączyć warunki.
- `and` wymaga, żeby wszystkie warunki były prawdziwe.
- `or` wymaga, żeby przynajmniej jeden warunek był prawdziwy.
- `not` odwraca wynik logiczny.

## Mini przykład

```python
status = "paid"
total_amount = 249.99

if status == "paid" and total_amount > 200:
    print("High value paid order")
```

## Zapamiętaj

- `and` jest dobre do reguł typu: musi spełnić A i B.
- `or` jest dobre do reguł typu: wystarczy A albo B.
- `not` pomaga czytać warunki odwrotne, np. `not is_valid`.
- Przy bardziej złożonych warunkach używaj nawiasów dla czytelności.

## Pytania na rozmowę

### Pytanie: Kiedy `and` zwraca `True`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Gdy wszystkie połączone nim warunki są prawdziwe.

</details>

### Pytanie: Kiedy `or` zwraca `True`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Gdy przynajmniej jeden z połączonych warunków jest prawdziwy.

</details>

### Pytanie: Co robi `not`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Odwraca wartość logiczną: `True` zmienia na `False`, a `False` na `True`.

</details>
