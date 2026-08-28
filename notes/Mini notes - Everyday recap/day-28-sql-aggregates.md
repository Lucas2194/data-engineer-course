# Dzień 28 - SQL: funkcje agregujące

## Mini-notatka do zapamiętania

```sql
-- Liczba wszystkich wierszy
SELECT COUNT(*) AS row_count
FROM table_name;


-- Liczba niepustych wartości kolumny
SELECT COUNT(column_name) AS known_value_count
FROM table_name;


-- Suma
SELECT SUM(numeric_column) AS total_value
FROM table_name;


-- Średnia do dwóch miejsc
SELECT ROUND(AVG(numeric_column), 2) AS average_value
FROM table_name;


-- Minimum i maksimum
SELECT
    MIN(numeric_column) AS minimum_value,
    MAX(numeric_column) AS maximum_value
FROM table_name;


-- Kilka metryk po filtrowaniu
SELECT
    COUNT(*) AS row_count,
    SUM(numeric_column) AS total_value,
    ROUND(AVG(numeric_column), 2) AS average_value,
    MIN(numeric_column) AS minimum_value,
    MAX(numeric_column) AS maximum_value
FROM table_name
WHERE condition;
```

## Najważniejsze zdania

> `WHERE` wybiera wiersze przed agregacją.

> Agregacja bez `GROUP BY` zwraca jeden wiersz podsumowania.

> `COUNT(*)` liczy wiersze, a `COUNT(column)` liczy niepuste wartości.

> `MAX(column)` zwraca wartość maksymalną, a nie cały rekord.

## Pytania na rozmowę

### Pytanie: Czym jest funkcja agregująca?

<details>
<summary>Przykładowa odpowiedź</summary>

> Funkcja agregująca działa na zbiorze wierszy lub wartości i tworzy wynik podsumowujący. Przykładami są `COUNT`, `SUM`, `AVG`, `MIN` i `MAX`. Bez `GROUP BY` cały przefiltrowany zbiór jest traktowany jako jedna grupa.

</details>

### Pytanie: Czym różni się `COUNT(*)` od `COUNT(column)`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `COUNT(*)` liczy wszystkie wiersze, natomiast `COUNT(column)` liczy tylko niepuste wartości wskazanej kolumny. Różnica pojawia się wtedy, gdy kolumna zawiera `NULL`.

</details>

### Pytanie: Kiedy działa `WHERE`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `WHERE` filtruje rekordy wejściowe przed wykonaniem agregacji, dlatego funkcje agregujące obliczają wynik tylko dla rekordów spełniających warunek.

</details>

### Pytanie: Co się dzieje dla pustego zbioru?

<details>
<summary>Przykładowa odpowiedź</summary>

> Agregacja bez `GROUP BY` nadal zwraca jeden wiersz. `COUNT(*)` daje `0`, natomiast `SUM`, `AVG`, `MIN` i `MAX` dają `NULL`. `NULL` nie jest tym samym co zero.

</details>

### Pytanie: Czy `MAX()` zwraca cały rekord?

<details>
<summary>Przykładowa odpowiedź</summary>

> Nie. `MAX(column)` zwraca największą wartość wskazanej kolumny. Aby na obecnym poziomie otrzymać cały rekord, używam `ORDER BY column DESC LIMIT 1`, a ewentualny remis rozstrzygam dodatkową kolumną.

</details>

### Pytanie: Dlaczego nie mieszać zwykłych kolumn z agregacjami?

<details>
<summary>Przykładowa odpowiedź</summary>

> Agregacja składa wiele wierszy w wynik podsumowujący, a zwykła kolumna nadal pochodzi z pojedynczego wiersza. Bez reguły grupowania nie wiadomo, który wiersz ma reprezentować wynik. SQLite bywa w tej kwestii pobłażliwe, ale inne bazy mogą odrzucić takie zapytanie.

</details>

## Ćwiczenie ustne — 90 sekund

Bez patrzenia w notatki wyjaśnij:

1. Czym jest agregacja?
2. Jak policzyć zamówienia?
3. Jak policzyć sumę tylko zamówień `paid`?
4. Czym różnią się `COUNT(*)` i `COUNT(total_amount)`?
5. Co stanie się przy braku pasujących rekordów?
6. Jak znalazłbyś wartość największego zamówienia?
7. Jak znalazłbyś cały rekord największego zamówienia?
8. Jak sprawdziłbyś wiarygodność raportu?

Mów pełnymi zdaniami, nie samymi nazwami funkcji.
