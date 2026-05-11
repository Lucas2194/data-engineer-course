# Dzień 12 Python Słowniki dict

## Cel dnia 

Dzisiaj uczę się słowników, czyli typu danych `dict`

Słownik pozwala przechowywać dane w formie 
```text
klucz -> wartość
```

```python

order = {
    "order_id": 1001,
    "customer_name": "Anna Kowalska",
    "order_value": 249.99,
    "status": "paid"
}

```

Słowniki są bardzo ważne, bo przypominają pojedyńczy rekord danych. 
W data Engineeringu rekordy z API, JSON-a albo przetwarzanych danych często wyglądają podobnie do słowników. 

# Czym jest słownik

Słownik to kolekcja par:

``` klucz: wartość ```

Na przykład 

```python

customer = {
    "customer_id": 501,
    "name": "Anna Kowalska",
    "city": "Gdańsk"
}

``` 

W tym słowniku:
1. Customer_id to klucz
   - 501 to wartość
2. name to klucz
   - Anna Kowalska to wartość
3. city do klucz
   - Gdańsk to wartość

## Jak odczytać wartości z słownika ?

Wartości z słownika odczytuje się przez klucz 

```python

order = {
    "order_id": 1001,
    "order_value": 249.99,
    "status": "paid"
}

print(order["order_id"])
print(order["order_value"])
print(order["status"])

```

## sprawdzanie czy klucz istnieje

Sprawdzamy to poprzez słowo kluczowe ```in```

```python

order = {
    "order_id": 1001,
    "status": "paid"
}

if "status" in order:
    print("Klucz status istnieje.")
else:
    print("Brakuje klucza status.")

```

## Dodawanie nowego klucza 

Do słownika można dodać nowy klucz 

```python

order = {
    "order_id": 1001,
    "status": "paid"
}

order["currency"] = "PLN"

print(order)

```

## Zmiana wartości w słowniku 

```python 

order = {
    "order_id": 1001,
    "status": "paid"
}

order["status"] = "refunded"

print(order["status"])

```

## Lista słowników 

Jedna słownik może oznaczać jeden rekord, natomiast lista słowników, może oznaczać wiele rekordów. 

Przykład 

```python

orders = [
    {"order_id": 1001, "order_value": 249.99, "status": "paid"},
    {"order_id": 1002, "order_value": 99.99, "status": "pending"},
    {"order_id": 1003, "order_value": 0, "status": "unknown"}
]

```

To przypomina tabelę:

order_id	order_value	status
1001	249.99	paid
1002	99.99	pending
1003	0	unknown

Można przejść pętlą ```for``` po liście słowników 
Przykład 

```python

orders = [
    {"order_id": 1001, "order_value": 249.99, "status": "paid"},
    {"order_id": 1002, "order_value": 99.99, "status": "pending"}
]

for order in orders:
    print(order["order_id"])
    print(order["status"])

```

Czyli - > Dla każdego zamówienai z listy zamówień wypisz order_id i status

## Słowniki w data engineeringu 

Są bardzo pomocne przy pracy z danymi 

Przykłady zastosowań 

Rekord zamówienia:
order_id, customer_id, order_value, status

Rekord klienta:
customer_id, name, email, city

Informacje o pliku:
file_name, rows_count, error_percent

Wynik walidacji:
is_valid, errors_count, errors

Konfiguracja:
source_name, file_path, table_name

## Sprawdzanie wymaganych kluczy 

Można mieć listę wymaganych kluczy i sprwadzić czy każdy z nich istnieje w słowniku 

```python

required_keys = ["order_id", "order_value", "status"]

```

Logika

dla każdego wymaganego klucza: 
    jeśli klucza nie ma w słowniku
        dodaj błąd

To łączy 
- listę
- słownik
- pętle
- if
- not in
- append

18. Mini ściąga
Tworzenie słownika
order = {
    "order_id": 1001,
    "order_value": 249.99,
    "status": "paid"
}
Odczyt wartości
order["status"]
Dodanie nowego klucza
order["currency"] = "PLN"
Zmiana wartości
order["status"] = "refunded"
Sprawdzenie, czy klucz istnieje
if "status" in order:
    print("Klucz istnieje")
Sprawdzenie, czy klucza brakuje
if "status" not in order:
    print("Brakuje klucza")
Lista słowników
orders = [
    {"order_id": 1001, "status": "paid"},
    {"order_id": 1002, "status": "pending"}
]
Pętla po liście słowników
for order in orders:
    print(order["order_id"])
    
## 19. Najważniejsze rzeczy do zapamiętania

- Słownik przechowuje pary klucz-wartość.
- Słownik zapisuję w nawiasach klamrowych {}.
- Klucz opisuje, czym jest dana wartość.
- Wartość odczytuję przez klucz.
- Jeśli odczytam nieistniejący klucz, dostanę KeyError.
- Mogę sprawdzić, czy klucz istnieje przez in.
- Mogę dodać nowy klucz do słownika.
- Mogę zmienić wartość istniejącego klucza.
- Jeden słownik może oznaczać jeden rekord.
- Lista słowników może oznaczać wiele rekordów.
- Słowniki są bardzo ważne przy pracy z JSON, API i rekordami danych.

