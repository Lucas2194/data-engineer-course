# Dzień 29 - Pandas: funkcje agregujące

## Mini-notatka do zapamiętania

```python
# Liczba wierszy - odpowiednik COUNT(*)
row_count = len(dataframe)
row_count = dataframe.shape[0]


# Liczba wszystkich pozycji Series
element_count = series.size


# Liczba niepustych wartości - odpowiednik COUNT(column)
known_value_count = series.count()


# Podstawowe agregacje
total_value = series.sum()
average_value = series.mean()
minimum_value = series.min()
maximum_value = series.max()


# Kilka agregacji
summary = series.agg(["count", "sum", "mean", "min", "max"])


# Filtrowanie przed agregacją
mask = dataframe["column"] == value
selected_values = dataframe.loc[mask, "numeric_column"]
result = selected_values.sum()


# Pusta suma wymagająca przynajmniej jednej wartości
result = empty_series.sum(min_count=1)
```

## Najważniejsze zdania

> `len(dataframe)` liczy wiersze, a `series.count()` liczy niepuste wartości.

> Najpierw filtrujesz rekordy, potem wykonujesz agregację.

> Pojedyncza agregacja `Series` zwykle zwraca skalar.

> `.agg()` z listą funkcji zwraca zestaw metryk.

> Domyślna suma pustej `Series` w Pandas wynosi `0.0`, inaczej niż `SUM()` w SQL.

> `.max()` zwraca największą wartość, a nie cały rekord.

## Pytania na rozmowę

### Pytanie: Jak policzyć rekordy w Pandas?

<details>
<summary>Przykładowa odpowiedź</summary>

> Do policzenia wszystkich wierszy `DataFrame` używam `len(dataframe)` albo `dataframe.shape[0]`. `series.count()` liczy niepuste wartości w jednej `Series`, natomiast `DataFrame.count()` liczy niepuste wartości osobno w każdej kolumnie.

</details>

### Pytanie: Jak obliczyć sumę tylko dla wybranych rekordów?

<details>
<summary>Przykładowa odpowiedź</summary>

> Najpierw tworzę maskę logiczną. Następnie przez `.loc[]` wybieram pasujące rekordy i właściwą kolumnę liczbową. Na otrzymanej `Series` wywołuję `.sum()`.

</details>

### Pytanie: Czym różni się SQL `SUM()` od Pandas `.sum()` dla pustego zbioru?

<details>
<summary>Przykładowa odpowiedź</summary>

> SQL zwraca `NULL`, natomiast Pandas domyślnie zwraca `0.0`. Parametr `min_count=1` może wymusić w Pandas wynik `NaN`. Ta różnica ma znaczenie przy interpretowaniu raportu, ponieważ brak danych nie zawsze powinien oznaczać zero.

</details>

### Pytanie: Co robi `.agg()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `.agg()` pozwala wykonać jedną lub kilka funkcji agregujących na `Series` albo `DataFrame`. Dla `Series` i listy funkcji zwraca `Series`, której indeks opisuje wykonane agregacje.

</details>

### Pytanie: Czy `.max()` zwraca cały rekord?

<details>
<summary>Przykładowa odpowiedź</summary>

> Nie. `.max()` zwraca największą wartość. Aby na obecnym poziomie otrzymać cały rekord, używam `sort_values(...).head(1)`, a ewentualny remis rozstrzygam dodatkową kolumną.

</details>

## Ćwiczenie ustne - 90 sekund

Bez patrzenia w notatkę wyjaśnij:

1. Jak policzyć wszystkie wiersze?
2. Jak policzyć niepuste kwoty?
3. Jak obliczyć sumę zamówień `paid`?
4. Jak obliczyć kilka metryk jednym `.agg()`?
5. Co stanie się dla pustego zbioru?
6. Jak braki danych wpływają na średnią?
7. Jak znaleźć wartość maksimum?
8. Jak znaleźć cały rekord maksimum?
9. Jak uzgodnić wyniki Pandas z SQL?
