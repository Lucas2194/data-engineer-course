# Dzień 16 - `main()`, funkcje pomocnicze i przepływ programu

## Najważniejsze

- `main()` opisuje główny przepływ programu.
- Funkcje pomocnicze wykonują mniejsze zadania.
- Czytelny program ma jasny podział odpowiedzialności.
- Stałe pomagają unikać magicznych wartości w kodzie.

## Mini przykład

```python
ALLOWED_STATUSES = ["paid", "pending", "cancelled"]

def main():
    print("Start pipeline")

if __name__ == "__main__":
    main()
```

## Zapamiętaj

- `main()` nie jest obowiązkowe, ale mocno porządkuje kod.
- Funkcja logiczna zwraca wynik, np. `True` albo `False`.
- Funkcja raportująca przygotowuje komunikat albo raport.
- `append()` dodaje jeden element, a `extend()` dodaje wiele elementów.

## Pytania na rozmowę

### Pytanie: Po co używać `main()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby główny przebieg programu był zebrany w jednym, czytelnym miejscu.

</details>

### Pytanie: Czym różni się funkcja logiczna od raportującej?

<details>
<summary>Przykładowa odpowiedź</summary>

> Funkcja logiczna przetwarza dane lub podejmuje decyzję, a raportująca prezentuje albo zapisuje wynik.

</details>

### Pytanie: Kiedy użyjesz `append()`, a kiedy `extend()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `append()` dodaje jeden element, a `extend()` dodaje do listy wszystkie elementy z innej kolekcji.

</details>
