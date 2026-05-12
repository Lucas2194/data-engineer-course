# Dzień 13 - Python `.get()`, `None` i bezpieczny odczyt z słownika

## Cel dnia

Dzisiaj uczę się bezpiecznego odczytu danych ze słownika 

w poprzednim dniu używałem zapisu

```python

order["status"]

```

Ten zapis działa, jeśli klucz "status" istnieje. 

Problem pojawai się wtedy, gdy klucza nie ma.  Python pokaże wtedy KeyError.

Dzisiaj poznaje metodę 

```python

order.get("status")

```

Pozwala odczytać wartość, bez zatrzymywania programu, nawet jeśli klucza nie ma. 

## Metoda .get()

Pozwala bezpiecznie odczytać wartości z słownika. 

```python

order = {
    "order_id": 1001,
    "order_value": 249.99
}

status = order.get("status")

print(status)

```

Wynik : None

## None - czym jest

None oznacza brak wartości. 

To specjalna wartość w Pythonie

None nie jest tym samym co : 

- test "None",
- liczba 0
- pusty tekst ""
- False

None oznacza - > brak danych / brak wartości / nic nie znalazłem 

```python

status = None

if status is None:
    print("Brakuje statusu")

```

Do sprawdzania używamy 

is None

albo

is not None

## Możemy używać get z wartością domyślną. 

Na przykład 

```python

order = {
    "order_id":1001,
    "order_value": 249.99
}

status = order.get("status", "unknown")

print(status)

```

Wynik 

Jeśli klucz istnieje, zwróci jego wartość. 
Jeśli klucza status nie ma, zwróć "unknown

## Kiedy używać [] ? 

Używamy, kiedy mamy 1000% pewność że klucz istnieje. 

## Kiedy używać get ? 

Używamy, kiedy nie mamy 1000% pewności czy klucz istnieje. 

Jest to bezpieczne do używania przy danych zewnętrznych np. 

- Danych z API 
- danych z pliku JSON
- danych z formularza
- danych z pliku CSV po konwersji
- rekordów, które mogą mieć braki

## if i else przy sprawdzaniu wartości 

przykładowy schemat 

```python

order_value = order.get("order_value")

if order_value is None:
    errors.append("Brakuje order_value")
else:
    if order_value <= 0:
        errors.append("order_value musi być większe od 0")

```

## Najważniejsze rzeczy do zapamiętania

- order["status"] może spowodobwać KeyError, jeśli klucza nie ma.
- order.get("status") zwraca None, jeśli klucza nie ma.
- .get() jest bezpieczniejsze przy danych, które mogą być niepełne. 
- None oznacza brak wartości
- Do sprawdzania None używam is None
- Przy liczbach najpierw sprwadzam czy wartość istnieje, dopiero potem porównuje je z liczbą
- W walidacji często chce zerbać wszystkie błędy, więc używam kilku osobnych if. 
- Dobre komunikaty błędów powinny mówić, którego rekordu i pola dotyczy problem

