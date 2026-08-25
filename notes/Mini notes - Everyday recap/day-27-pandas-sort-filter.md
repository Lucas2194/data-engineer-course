# Dzień 27 - Pandas: sortowanie i filtrowanie

## Mini-notatka do zapamiętania

```python
# Sortowanie rosnąco
sorted_df = df.sort_values(
    by="column_name",
    ascending=True,
)

# Sortowanie malejąco
sorted_df = df.sort_values(
    by="column_name",
    ascending=False,
)

# Kilka kolumn i różne kierunki
sorted_df = df.sort_values(
    by=["column_a", "column_b"],
    ascending=[True, False],
)

# Pierwsze n wierszy bieżącego wyniku
first_rows = sorted_df.head(n)

# Wartość należy do listy
mask = df["column_name"].isin(["value_a", "value_b"])

# Wartość nie należy do listy
mask = ~df["column_name"].isin(["value_a", "value_b"])

# Przedział z obiema granicami
mask = df["numeric_column"].between(lower, upper)

# Poza przedziałem
mask = ~df["numeric_column"].between(lower, upper)

# Filtrowanie → wybór kolumn → sortowanie → pierwsze n
result = (
    df.loc[
        mask,
        ["column_a", "column_b"],
    ]
    .sort_values(
        by="column_b",
        ascending=False,
    )
    .head(n)
)
```

Jedno zdanie do zapamiętania:

> Najpierw ustalam, które rekordy pasują i jak mają być ułożone, a dopiero potem wybieram pierwsze `n`.

## Pytania na rozmowę

### Pytanie: Co robi `sort_values()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `sort_values()` sortuje wiersze według wartości wskazanej kolumny lub kolumn. Kierunek określa parametr `ascending`. Metoda domyślnie zwraca nowy `DataFrame`, a dodatkowa kolumna sortowania może rozstrzygać remisy.

</details>

### Pytanie: Czym różni się `head()` od `sort_values()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `sort_values()` zmienia kolejność wyniku, natomiast `head(n)` wybiera pierwsze `n` wierszy z bieżącej kolejności. `head()` samo nie znajduje największych wartości, dlatego przy TOP N najpierw trzeba określić kolejność.

</details>

### Pytanie: Co robi `isin()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `isin()` działa element po elemencie na `Series` i sprawdza, czy każda wartość należy do listy dopuszczalnych wartości. Zwraca maskę logiczną, którą można przekazać do `.loc[]`.

</details>

### Pytanie: Co robi `between()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `between()` sprawdza, czy każda wartość mieści się między wskazanymi granicami, i zwraca maskę logiczną. Domyślnie uwzględnia obie granice, a wynik można odwrócić operatorem `~`.

</details>

### Pytanie: SQL czy Pandas?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żadne z nich nie jest zawsze lepsze. SQL wykonuje operacje w silniku bazy danych i jest naturalny dla danych znajdujących się w bazie. Pandas pracuje zwykle na `DataFrame` w procesie Pythona i jest wygodny do eksploracji oraz transformacji plików. Wybór zależy między innymi od źródła, rozmiaru danych i miejsca wykonania.

</details>

## Ćwiczenie ustne — 90 sekund

Bez patrzenia w notatki wyjaśnij:

1. Jak znalazłbyś trzy największe zamówienia w Pandas?
2. Dlaczego najpierw sortujesz, a potem wywołujesz `head(3)`?
3. Jak wybrałbyś dwa statusy?
4. Jak wybrałbyś kwoty od 100 do 300 włącznie?
5. Jak sprawdziłbyś poprawność wyniku?

Nie podawaj wyłącznie nazw metod. Wyjaśnij kolejność procesu.
