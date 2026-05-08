# Dzień 11 - Python pętla 'for'

## Cel dnia 

Dzisiaj uczę się pętli for

Pętla for pozwala wykonać ten sam fragment kodu, dla każdego elementu z listy

Przykład:

```python
files = ["orders.csv", "customers.csv", "products.csv"]

for file in files:
    print(file)
```

Dzięki tej pętli nie trzeba pisać osobnego print dla każdego elementu listy

## Po co są pętle

Pętle służą do automatycznego powtarzania kodu 

Bez pętli

```python

files = ["orders.csv", "customers.csv", "products.csv"]

print(files[0])
print(files[1])
print(files[2])

```

Z Pętlą

```python

files = ["orders.csv", "customers.csv", "products.csv"]

for file in files:
    print(file)

```

W pętli używamy file jako pojedyńczy element listy, który jest akutlanie przetwarzany. Dobra praktyka - > 

Lista	Pojedynczy element
files	file
products	product
errors	error
statuses	status
columns	column
orders	order

## Pętla z IF 

Pętle można łączyć z warunkami 

```python

statuses = ["paid", "pending", "unknown", "cancelled"]
allowed_statuses = ["paid", "pending", "cancelled", "refunded"]

for status in statuses:
    if status in allowed_statuses:
        print(f"Status poprawny: {status}")
    else:
        print(f"Status nieznany: {status}")

``` 

To jest bardzo ważny schemat 

DLA KAŻDEGO ELEMENTU Z LISTY : 
    Sprawdź warunek
    wykonaj odpowiedni kod

## Pętla i lista błędów 

```python

statuses = ["paid", "pending", "wrong_status", "cancelled"]
allowed_statuses = ["paid", "pending", "cancelled", "refunded"]

errors = []

for status in statuses:
    if status not in allowed_statuses:
        errors.append(f"Nieznany status: {status}")

print(errors)

```

Co robi program ? 

1. Tworzy listę statusów
2. Tworzy listę dozwolonych statusów
3. Tworzy pustą listę błędów
4. Przechodzi przez każdy status
5. Jeśli status jest niedozwolony, dodaje błąd do listy
6. Na końcu wypisuje listę błędów 

## range

Pozwala wygenerować sekwencję liczb 

```python

for number in range(5):
    print(number)
```

output : 
0
1
2
3
4

range(5) oznacza - > od 0 do 4
range(1,6) oznacza - > od 1 do 5

## Pętla w kontekście Data Engineeringu

Dla każdego pliku CSV:
    sprawdź nazwę
    sprawdź liczbę wierszy
    sprawdź kolumny
    zapisz wynik

Dla każdego statusu:
    sprawdź, czy jest dozwolony

Dla każdej kolumny:
    sprawdź, czy istnieje w pliku

Dla każdego błędu:
    wypisz komunikat

Dla każdego rekordu:
    sprawdź poprawność danych

15. Mini ściąga
Podstawowa pętla po liście
for item in items:
    print(item)
Pętla po plikach
for file in files:
    print(file)
Pętla z warunkiem
for status in statuses:
    if status in allowed_statuses:
        print("OK")
    else:
        print("Błąd")
Pętla z listą błędów
errors = []

for status in statuses:
    if status not in allowed_statuses:
        errors.append(status)
Pętla z licznikiem
count = 0

for value in values:
    if value > 0:
        count = count + 1
Pętla z range()
for number in range(5):
    print(number)
## 16. Najważniejsze rzeczy do zapamiętania
1 Pętla for pozwala przejść przez każdy element listy.
2 Kod wewnątrz pętli musi być wcięty.
3 Lista i pojedynczy element powinny mieć czytelne nazwy.
4 for file in files oznacza: dla każdego pliku z listy plików.
5 Pętle można łączyć z if.
6 Pętle można łączyć z append().
7 Pętle można używać do zliczania błędów.
8 Pętle są podstawą automatyzacji.
9 W Data Engineeringu pętle przydadzą się do pracy z wieloma plikami, statusami, kolumnami i rekordami.