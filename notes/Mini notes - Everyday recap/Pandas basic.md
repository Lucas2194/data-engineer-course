# Dzień 25 - Pandas basic

## Najważniejsze

- Pandas jest biblioteką Pythona do pracy z danymi tabelarycznymi.
- Standardowy import to `import pandas as pd`.
- `pd.read_csv(path)` wczytuje CSV i zwraca `DataFrame`.
- `DataFrame` jest strukturą dwuwymiarową: ma wiersze i kolumny.
- `Series` jest strukturą jednowymiarową i często reprezentuje jedną kolumnę.
- Po wczytaniu danych najpierw je kontrolujemy, a dopiero później transformujemy.

## Mini przykład

```python
import pandas as pd

orders = pd.read_csv("data/orders.csv")

paid_orders = orders.loc[
    (orders["status"] == "paid")
    & (orders["total_amount"] > 150),
    ["order_id", "customer_name", "total_amount"],
]
```

## Zapamiętaj

- Indeks nie musi być tym samym co biznesowy identyfikator rekordu.
- `head()` pokazuje początek danych.
- `shape` zwraca krotkę `(liczba_wierszy, liczba_kolumn)`.
- `len(df)` zwraca liczbę wierszy.
- `columns` pokazuje nazwy kolumn.
- `dtypes` pokazuje typ każdej kolumny.
- `info()` daje szybki raport o strukturze `DataFrame`.
- `df["column"]` zwraca `Series`.
- `df[["column"]]` zwraca `DataFrame` z jedną kolumną.
- `df[["a", "b"]]` wybiera kilka kolumn.
- Warunek dla kolumny tworzy maskę wartości `True` i `False`.
- `df.loc[mask]` filtruje wiersze.
- `df.loc[mask, ["a", "b"]]` filtruje wiersze i wybiera kolumny.
- W Pandas równość zapisujemy przez `==`, a w SQL przez `=`.
- Maski łączymy przez `&` i `|`, a każdy warunek umieszczamy w nawiasach.
- Wynik filtrowania warto zapisywać pod opisową nazwą.

## Pytania na rozmowę

### Pytanie: Czym jest Pandas?

<details>
<summary>Przykładowa odpowiedź</summary>

> Pandas to biblioteka Pythona do wczytywania, sprawdzania, przekształcania i analizowania danych tabelarycznych.

</details>

### Pytanie: Czym różni się `DataFrame` od `Series`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `DataFrame` jest dwuwymiarową tabelą z wierszami i kolumnami, a `Series` jest jednowymiarową kolekcją, często jedną kolumną tabeli.

</details>

### Pytanie: Co sprawdzasz po wczytaniu pliku CSV?

<details>
<summary>Przykładowa odpowiedź</summary>

> Między innymi pierwsze wiersze, rozmiar tabeli, nazwy kolumn, typy danych, brakujące wartości i duplikaty.

</details>

### Pytanie: Czym różni się filtrowanie w Pandas od `WHERE` w SQL?

<details>
<summary>Przykładowa odpowiedź</summary>

> Cel jest podobny: wybrać pasujące wiersze. SQL używa klauzuli `WHERE`, a Pandas maski logicznej, np. `df[df["status"] == "paid"]`.

</details>

### Pytanie: Dlaczego w Pandas używamy `&` zamiast `and`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `&` łączy wartości logiczne element po elemencie w `Series`. Operator `and` oczekuje pojedynczej wartości `True` albo `False`.

</details>

Nie ucz się odpowiedzi słowo w słowo. Powiedz je własnymi słowami i pokaż na przykładzie `orders`.
