# Dzień 24 - SQL basic recap

## Najważniejsze

- SQL jest językiem pracy z relacyjnymi bazami danych.
- SQLite jest silnikiem bazy danych obsługującym SQL.
- Baza może zawierać wiele tabel.
- Tabela składa się z wierszy i kolumn.
- Schemat opisuje strukturę tabeli: kolumny, typy danych i ograniczenia.
- `SELECT` odczytuje dane i ich nie modyfikuje.

## Mini przykład

```sql
SELECT customer_name, total_amount
FROM orders
WHERE status = 'paid'
    AND total_amount > 150;
```

## Zapamiętaj

- `SELECT` określa kolumny wyniku.
- `FROM` wskazuje źródłową tabelę.
- `WHERE` filtruje wiersze.
- `*` oznacza wszystkie kolumny.
- Tekst zapisujemy w pojedynczych cudzysłowach.
- W SQL porównujemy przez `=`, a w Pythonie przez `==`.
- `AND` wymaga spełnienia wszystkich połączonych warunków.
- `OR` wymaga spełnienia przynajmniej jednego warunku.
- Jeden wiersz SQLite jest domyślnie zwracany do Pythona jako krotka.

## Pytania na rozmowę

### Pytanie: Czym różni się SQL od SQLite?

<details>
<summary>Przykładowa odpowiedź</summary>

> SQL jest językiem zapytań, a SQLite jest silnikiem bazy danych, który ten język obsługuje.

</details>

### Pytanie: Co robi `WHERE`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Filtruje wiersze i pozostawia tylko te, które spełniają podany warunek.

</details>

### Pytanie: Dlaczego `SELECT *` jest wygodne w nauce, ale nie zawsze najlepsze w produkcji?

<details>
<summary>Przykładowa odpowiedź</summary>

> Pobiera wszystkie kolumny, także niepotrzebne. To może zwiększać ilość przesyłanych danych i uzależniać kod od zmian struktury tabeli.

</details>
