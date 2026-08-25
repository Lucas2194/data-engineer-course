# Dzień 12 - Python: słowniki `dict`

## Najważniejsze

- Słownik przechowuje dane jako pary klucz-wartość.
- Klucz opisuje, jaką wartość chcemy odczytać.
- Jeden słownik może reprezentować jeden rekord danych.
- Lista słowników może reprezentować wiele rekordów.

## Mini przykład

```python
order = {
    "order_id": 1001,
    "customer_name": "Anna",
    "status": "paid",
}

print(order["status"])
```

## Zapamiętaj

- `dict["key"]` odczytuje wartość po kluczu.
- `key in dict` sprawdza, czy klucz istnieje.
- Do słownika można dodawać nowe klucze.
- W data engineeringu słowniki są wygodne przy danych z CSV, JSON i API.

## Pytania na rozmowę

### Pytanie: Czym jest klucz w słowniku?

<details>
<summary>Przykładowa odpowiedź</summary>

> To nazwa, za pomocą której odczytujemy przypisaną do niej wartość.

</details>

### Pytanie: Jak sprawdzić, czy słownik ma wymagany klucz?

<details>
<summary>Przykładowa odpowiedź</summary>

> Operatorem `in`, np. `"order_id" in order`.

</details>

### Pytanie: Dlaczego rekord zamówienia dobrze pasuje do słownika?

<details>
<summary>Przykładowa odpowiedź</summary>

> Każde pole rekordu ma nazwę i wartość, np. klucz `status` oraz wartość `"paid"`.

</details>
