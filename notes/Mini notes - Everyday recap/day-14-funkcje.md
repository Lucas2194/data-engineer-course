# Dzień 14 - Python: funkcje

## Najważniejsze

- Funkcja grupuje kod pod nazwą.
- Parametry pozwalają przekazać dane do funkcji.
- `return` zwraca wynik funkcji.
- Dobra funkcja robi jedną konkretną rzecz.

## Mini przykład

```python
def is_valid_status(status):
    allowed_statuses = ["paid", "pending", "cancelled"]
    return status in allowed_statuses

print(is_valid_status("paid"))
```

## Zapamiętaj

- Funkcję definiujemy przez `def`.
- Argument to konkretna wartość przekazana przy wywołaniu.
- `print()` pokazuje wartość na ekranie, a `return` oddaje wynik do dalszego użycia.
- Funkcje bardzo pomagają w walidacji i transformacji danych.

## Pytania na rozmowę

### Pytanie: Czym różni się parametr od argumentu?

<details>
<summary>Przykładowa odpowiedź</summary>

> Parametr to nazwa w definicji funkcji, a argument to konkretna wartość przekazana podczas jej wywołania.

</details>

### Pytanie: Po co używać `return`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `return` zwraca wynik funkcji do miejsca, z którego funkcję wywołano.

</details>

### Pytanie: Dlaczego jedna funkcja powinna mieć jedną odpowiedzialność?

<details>
<summary>Przykładowa odpowiedź</summary>

> Taka funkcja jest łatwiejsza do zrozumienia, przetestowania, ponownego użycia i poprawienia.

</details>
