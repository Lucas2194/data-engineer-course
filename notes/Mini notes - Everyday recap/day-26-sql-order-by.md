# Dzień 26 - SQL: sortowanie, `LIMIT`, `IN` i `BETWEEN`

## Najważniejsze

- Bez `ORDER BY` kolejność rekordów nie jest gwarantowana.
- `ASC` sortuje rosnąco i jest kierunkiem domyślnym.
- `DESC` sortuje malejąco.
- `LIMIT` określa, ile pierwszych rekordów wyniku zwrócić.
- `IN` pozwala sprawdzić kilka konkretnych wartości.
- `BETWEEN` wybiera wartości z domkniętego przedziału, razem z jego granicami.
- Złożone zapytanie najlepiej budować i sprawdzać etapami.

## Mini przykład

Pięć największych opłaconych zamówień:

```sql
SELECT order_id, customer_name, total_amount
FROM orders
WHERE status = 'paid'
ORDER BY total_amount DESC
LIMIT 5;
```

Kilka statusów i przedział kwot:

```sql
SELECT order_id, status, total_amount
FROM orders
WHERE status IN ('paid', 'pending')
  AND total_amount BETWEEN 100 AND 500
ORDER BY status ASC, total_amount DESC;
```

Kolejność klauzul w zapytaniu:

```sql
SELECT ...
FROM ...
WHERE ...
ORDER BY ...
LIMIT ...;
```

## Pytania na rozmowę

### Pytanie: Czy SQL gwarantuje kolejność wierszy?

<details>
<summary>Przykładowa odpowiedź</summary>

> Nie. Jeśli potrzebuję określonej kolejności wyniku, używam `ORDER BY`. Bez tej klauzuli nie powinienem polegać na kolejności zwracanych rekordów.

</details>

### Pytanie: Czym różnią się `ASC` i `DESC`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `ASC` oznacza kolejność rosnącą i jest kierunkiem domyślnym. `DESC` oznacza kolejność malejącą.

</details>

### Pytanie: Dlaczego `LIMIT` często łączymy z `ORDER BY`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `LIMIT` ogranicza liczbę rekordów, ale sam nie określa, które rekordy mają być pierwsze. `ORDER BY` definiuje kolejność, więc razem pozwalają znaleźć na przykład trzy największe zamówienia.

</details>

### Pytanie: Czym `IN` różni się od `OR`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `IN` jest krótszym i czytelniejszym sposobem sprawdzenia, czy jedna kolumna ma jedną z kilku konkretnych wartości. Odpowiada kilku porównaniom równości tej samej kolumny połączonym przez `OR`.

</details>

### Pytanie: Czy `BETWEEN` obejmuje granice?

<details>
<summary>Przykładowa odpowiedź</summary>

> Tak. Warunek `x BETWEEN a AND b` odpowiada warunkowi `x >= a AND x <= b`.

</details>

## Ćwiczenie ustne

Bez patrzenia w notatkę opowiedz przez około minutę:

1. Jak znaleźć pięć największych zamówień ze statusem `paid`?
2. Dlaczego potrzebujesz `ORDER BY`?
3. Co robi `LIMIT`?
4. Jak wybrać kilka statusów?
5. Jak zapisać przedział kwot?

Nie musisz podawać całego zapytania z pamięci. Ważne, żeby logicznie opisać kolejne elementy.

## Ściąga do zapamiętania

- Bez `ORDER BY` kolejność rekordów nie jest gwarantowana.
- `ORDER BY column ASC` sortuje rosnąco.
- `ORDER BY column DESC` sortuje malejąco.
- `ASC` jest kierunkiem domyślnym.
- Kolejne kolumny w `ORDER BY` rozstrzygają remisy.
- Każda kolumna sortowania może mieć inny kierunek.
- `WHERE` filtruje rekordy przed uporządkowaniem wyniku.
- `LIMIT n` zwraca najwyżej `n` pierwszych rekordów wyniku.
- `LIMIT` nie oznacza automatycznie największych ani najmniejszych rekordów.
- `ORDER BY` mówi, które rekordy są pierwsze.
- `LIMIT` mówi, ile pierwszych rekordów zwrócić.
- `IN` sprawdza, czy wartość znajduje się na liście.
- `IN` często zastępuje kilka porównań równości połączonych przez `OR`.
- `NOT IN` odrzuca wartości z podanej listy.
- `BETWEEN a AND b` obejmuje `a` i `b`.
- `BETWEEN` odpowiada warunkowi `>= a AND <= b`.
- `NOT BETWEEN` wybiera wartości poza domkniętym przedziałem.
- Granice `BETWEEN` zapisujemy od dolnej do górnej.
- Kolejność klauzul to `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`.
- Złożone zapytanie budujemy i testujemy etapami.
