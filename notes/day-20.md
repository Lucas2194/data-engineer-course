# Dzień 20 - Pliki CSV od podstaw 

## Cel dnia 

Dzisiaj uczę się pracować z plikami CSV w Pythonie 

CSV to jeden z najważniejszych formatów danych na początku nauki Data Engineeringu. W praktyce bardzo często dane trafiają do pipeline'u jako: 

```text

orders.csv
customers.csv
products.csv
transactions.csv
users.csv

```

CSV jest prosty, ale ma swoje pułapki. Na pierwszy rzut oka wygląd ajak zwykły tekst, ale w rzeczywistości repreztuje dane tabelaryczne. 

Po dzisiejszej lekcji trzeba zrobić : 

- Czym jest plik CSV 
- Czym różni się od zwykłego TXT
- czym jest nagłówek pliku CSV
- czym jest separator
- jak odczytać CSV w Pythonie
- jak pracować z csv.reader
- jak pracować z csv.DictReader
- dlaczego DictReader jest wygodniejszy od danych tabelarycznych 
- jak zapisać dane do CSV
- dlaczego CSV jest ważny w Data Engineeringu

## Czym jest CSV

dosłownie oznacza - > Comma-Separated Values -> wartości oddzielone przecinkami 

Przykład pliku csv 

```text

order_id,customer_name,total_amount,status
1001,Anna,249.99,paid
1002,Tomasz,89.50,pending
1003,Kasia,0,cancelled

```

Na ekranie wygląda to jak zwykły tekst, ale logcznie jest to tabela.

Ta tabela ma kolumny - > 

- order_id
- customer_name
- total_amount
- status

I wiersze - > 

- 1001, Anna, 249.99, paid
- 1002, Tomasz, 89.50, pending
- 1003, Kasia, 0, cancelled

Czyli CSV to prosty sposób zapisania tabeli w pliku tekstowym 

## CSV a TXT

Plik TXT może zawierać dowolony tekst :

```text

To jest zwykła notatka.
Moze mieć różne zadania.
Nie musi mieć struktury tabeli 

```

A plik CSV ma strukturę - > 

```text

kolumna1, kolumna2, kolumna3
wartosc1, wartosc2, wartosc3
wartosc1, wartosc2, wartosc3

```

Najważniejsza różnica

TXT - luźny tekst
CSV - dane tabelaryczne zapisane jako tekst

W data Engineerungi CSV jest ważny, bo bardzo często jest pierwszym formatem wymiany danych między systemami. 

## Nagłówek CSV

Pierwszy wiersz pliku CSV jest czesto nagłówkiem. Tak jak wyżej. 

```text

order_id, customer_name,total_amount,status

```

To nie są dane zamówienia, to nazwy kolumn

Dzięki nagłówkowi wiemy że : 

```text

1001 - > order_id
Anna - > customer_name
249.99 - > total_amount
paid - > status

```

Bez nagłówka dane są trudniejsze do zrozumienia. 

Da się je odczytać, ale trzeba z zewnątrz wiedzieć, co oznacza każda pozycja 

## Separator 

W klasycznym CSV reparatorem jest przecinek : `,`

Ale w polsce częseto spotkasz pliki z separatorem średnikowym: 

```text

1001;Anna;249.99;paid

```

Dlaczego? Bo w polskim Excelu przecinek bywa używany jako separator dziesiętny 

249,99 

Wtedy średnik jako separator kolumn jest bezpieczniejszy. 

Na tym etapie skupię się na przezcinku 

## Moduł CSV

Python ma wbudowany moduł do pracy z plikami CSV

```python

import csv

```

## csv.reader

Pierwszy sposób czytania CSV to csv.reader 

Przykład koncepcyjny 

```python

import csv

with open("data/orders.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

```

Wynik będzie mniej więcej taki: 

```text

['order_id', 'customer_name', 'total_amount', 'status']
['1001', 'Anna', '249.99', 'paid']
['1002', 'Tomasz', '89.50', 'pending']

```

Czyli

row[0]
row[1]
row[2]
row[3]

Każdy wiersz jest listą. To działa ale jset słabo czytelne 

Jeśli używasz csv.reader często musisz pamiętać indeksy: 

```python

order_id = row[0]
customer_name = row[1]
total_amount = row[2]
status = row[3]

```

To jest jednak kruchę, ponieważ ktoś zmieni kolejnośc kolumn w CSV, to kod moze zacząć źle interpretować dane. 

## csv.DictReader

tutaj python czyta CSV jako słownik 

Przykład koncepcyjny : 

```python

import csv

with open("data/orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

```

W tym wypadku pojedyńczy wiersz będzie wyglądał tak : 

```python

{
    "order_id": "1001",
    "customer_name": "Anna",
    "total_amount": "249.99",
    "status": "paid"
}

```

Jest to dużo czytelniejsze. 

Możesz dostać konkretne pole po nazwie kolumny

```python

row["order_id"]
row["customer_name"]
row["total_amount"]
row["status"]

```

## WAŻNA RZECZY 

Dane z CSV są tekstem. Gdy Python czyta CSV wartości są wczytywane jako test. 

Czyli nawetj eśli w pliku masz : 

249.99 to python widzi to jako "249.99" - To oznacza, że j eśli chcesz robić obliczenia, musisz wykonać konwersję. 

```python

amount_text = "249.99"
amount = float(amount_text)

```

To ważne, ponieważ na początku często zapominamy że dane z plików przychodzą jako tekst.

## Funkcja do czytania CSV

W tym dniu zaczynamy budować osobny moduł: 

csv_utils.py

To jest dobra praktyka, bo main.py nie powinien zaierać całej logiki czytania plików.

Kierunek Funkcji 

```python 

def read_orders_from_csv(file_path):
    ...

```

Ta funkcja powinna: 

- przyjąć ścieżkę do pliku CSV,
- otworzyć plik
- odczytać dane
- zwrócić listę zamówień

Docelowy wynik powinien być listą słowników. 

```python

[
    {
        "order_id": "1001",
        "customer_name": "Anna",
        "total_amount": "249.99",
        "status": "paid"
    },
    {
        "order_id": "1002",
        "customer_name": "Tomasz",
        "total_amount": "89.50",
        "status": "pending"
    }
]

```

Na razie wartość mogą zostać tekste. Konwersję zaczniemy robić ostrożnie w zadaniach.

## Dlaczego lista słowników? 

Bo to naturlna struktura dla danych tabelarycznych w podstawowym Pythonie.

Tabela

```text

order_id | customer_name | total_amount | status
1001     | Anna          | 249.99       | paid
1002     | Tomasz        | 89.50        | pending

```

Może być reprezentowana jako 

```python

[
    {"order_id": "1001", "customer_name": "Anna", "total_amount": "249.99", "status": "paid"},
    {"order_id": "1002", "customer_name": "Tomasz", "total_amount": "89.50", "status": "pending"},
]

```

Czyli : 

Jeden wiersz CSV = jeden słownik
cały plik CSV = lista słowników 

To podejście później bardzo dobrze przygotowuje do pracy z JSON, API i bazami danych

## Prosta Analiza danych z CSV 

Gdy masz listę zamówień, możesz zacząc zadania pytania : 

- Ile jest zamówień
- Ile zamówień ma status paid
- Ile zamówień ma status pending
- Czy są zamówienia z kwotą 0?
- Czy są zamówienia z kwotą ujmeną ?
- Jaka jest suma opłaconych zamówien?

To jest już mini analityka danych. 

Jeszcze nie używamy pandas. Na razie celowo robimy to czystym Python, żebym nauczył się mechaniki

Pandas przjdzie później i wtedy zobaczysz, że wiele rzeczy robi szybciej. Ale najpierw warto zrozumieć podstawy.

## Zapis CSV

CSV można też zapisywać. 

Do tego służy m.in csv.DictWriter

Przykład koncepcyjny 

```python

import csv

fieldnames = ["order_id", "customer_name", "total_amount", "status"]

with open("output/paid_orders.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        "order_id": "1001",
        "customer_name": "Anna",
        "total_amount": "249.99",
        "status": "paid"
    })

```

Na Windowsie ważny jest parametr:

newline =""

Bez niego przy zapisie CSV mogą się pojawić niepotrzebne puste linie między wierszami

`fieldnames` określa kolejność kolumn w zapisywanym pliku CSV

Przykład

```python

fieldnames = ["order_id", "customer_name", "total_amount", "status"]

```

To znaczy że nagłówek pliku będzie taki : 

```csv

order_id,customer_name,total_amount,status

```

Jeśli zmienię kolejność, zmieni to też kolejność w pliku wynikowym 

## Folder output

W Data Engineeringu często rozdziela siędane wejściowe i wyjściowe 

Dzisiaj przyjmujemy 

data/ - > dane wejściowe
output/ -> dane wygenerowane przez program 

## Dzisiejszy kierunek programu. 

Ma on robić doclowo coś takiego : 

- Odczytaj plik orders.csv
- Policz liczbę wszystkich zamówień
- Wypisz zamówienia na ekran
- Wykryj zamówienia z niepoprawną kwotą
- Odfiltruj zamówienia opłacone. 
- Zapisz opłacone zamówienia do output/paid_orders.csv
- Zapisz błędne zamóienai do output/invalid_orders.csv


