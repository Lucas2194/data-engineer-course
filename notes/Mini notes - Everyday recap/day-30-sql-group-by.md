# Dzień 30 - SQL: `GROUP BY`

## Mini-notatka do zapamiętania

```sql
-- Liczba rekordów w każdej grupie
SELECT
    group_column,
    COUNT(*) AS row_count
FROM table_name
GROUP BY group_column
ORDER BY group_column ASC;


-- Kilka agregacji w każdej grupie
SELECT
    group_column,
    COUNT(*) AS row_count,
    SUM(numeric_column) AS total_value,
    ROUND(AVG(numeric_column), 2) AS average_value,
    MIN(numeric_column) AS minimum_value,
    MAX(numeric_column) AS maximum_value
FROM table_name
GROUP BY group_column;


-- Filtrowanie rekordów przed grupowaniem
SELECT
    group_column,
    COUNT(*) AS row_count
FROM table_name
WHERE condition
GROUP BY group_column;


-- Grupowanie według kombinacji dwóch kolumn
SELECT
    first_group_column,
    second_group_column,
    COUNT(*) AS row_count
FROM table_name
GROUP BY first_group_column, second_group_column;


-- Największe grupy
SELECT
    group_column,
    SUM(numeric_column) AS total_value
FROM table_name
GROUP BY group_column
ORDER BY total_value DESC, group_column ASC
LIMIT 3;
```

## Najważniejsze zdania

> `GROUP BY` dzieli rekordy na grupy według wspólnych wartości.

> Jedna grupa tworzy jeden wiersz wyniku.

> `WHERE` filtruje rekordy przed utworzeniem grup.

> Zwykła kolumna z `SELECT` powinna znajdować się w `GROUP BY`.

> `ORDER BY` układa gotowe grupy.

> `LIMIT` ogranicza wynik grupowania, a nie rekordy wejściowe.

## Pytania na rozmowę

### Pytanie: Czym jest `GROUP BY`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `GROUP BY` dzieli rekordy według wspólnych wartości jednej lub kilku kolumn. Funkcje agregujące działają osobno w każdej grupie, a każda grupa tworzy jeden wiersz wyniku. Można w ten sposób policzyć liczbę albo sumę zamówień według statusu.

</details>

### Pytanie: Czym różni się `WHERE` od `HAVING`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `WHERE` filtruje pojedyncze rekordy przed grupowaniem. `HAVING` służy do filtrowania gotowych grup po wykonaniu agregacji.

</details>

### Pytanie: Jakie kolumny można wybrać w zapytaniu grupującym?

<details>
<summary>Przykładowa odpowiedź</summary>

> W `SELECT` umieszczam kolumny znajdujące się w `GROUP BY` oraz wyniki funkcji agregujących. Gołe kolumny spoza grupowania są ryzykowne, ponieważ nie wiadomo, który rekord powinny reprezentować. SQLite jest pod tym względem bardziej pobłażliwe niż wiele innych baz.

</details>

### Pytanie: Co robi `LIMIT` po `GROUP BY`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `LIMIT` ogranicza liczbę gotowych grup zwracanych w wyniku. Nie ogranicza rekordów wejściowych użytych do grupowania. Jeżeli ma wskazać największe grupy, najpierw trzeba je odpowiednio posortować.

</details>

### Pytanie: Jak zweryfikować raport grupowy?

<details>
<summary>Przykładowa odpowiedź</summary>

> Sprawdzam liczbę rekordów pozostałych po `WHERE`, liczbę utworzonych grup oraz sumę liczników grup. Porównuję też sumy grup z sumą całego filtrowanego zbioru, a w razie potrzeby kontroluję minimum, średnią i maksimum.

</details>

## Ćwiczenie ustne - 90 sekund

Bez patrzenia w notatkę wyjaśnij:

1. Czym jest grupa?
2. Co daje `GROUP BY status`?
3. Dlaczego wynik ma trzy wiersze?
4. Jak policzyć sumę każdej grupy?
5. Kiedy działa `WHERE`?
6. Dlaczego nie wybierać przypadkowej kolumny spoza grupowania?
7. Co oznacza grupowanie po dwóch kolumnach?
8. Jak działa `LIMIT`?
9. Jak skontrolować poprawność raportu?
