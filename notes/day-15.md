# Dzień 15 - Python: import i moduły

## Cel dnia 

Dzisiaj uczę się dzielić kod na kilka plików i używać importów

Do tej pory większość kodu pisałem w jednym pliku. To działa przy małych ćwicezniach, ale w większy projektach szybko robi się to nieczytelne

Import pozwalają używać funkcji z jednego pliku w innym pliku.

Przykład 

```python

from validators import is_valid_status

```

Dzięki temu mogę trzymać funkcje walidacyjne w osobnym pliku, a główną logikę programu w innym 

## Czym jest moduł 

Moduł w pytanie to plik z rozszerzeniem .py

np. -> validators.pl

Jeśli w tym pliku mam funkcję : 

```python

def is_valid_status(status):
    ...

```

to mogę ją zaimportować w innym pliku

## Po co dzielić kod na moduły

Dzielenie kodu na moduły pomaga

- uniknąć bardzo dużych plików.
- lepiej organizować projekt
- oddzielić różne odpowiedzialności
- łatwiej testować funkcję 
- używać tych samych funkcji w wielu miejsach
- budować bardzeij profesjonalną strukturę programu 

Przykład strukstury 

Przykład struktury:

```text

src/
└── day_15_modules/
    ├── main.py
    ├── validators.py
    ├── data.py
    └── reports.py

```

Znaczenie plików 

main.py - > główny plik programu
validators.py - > funkcje sprwadzające dane
data.py - > przykładowe dane 
reports.py - > funkcje wypisaujące raporty

## Najprostszy import funkcji 

Jeśli mam plik

validators.py

a w nim funkcje

```python

def is_valid_status(status):
    allowed_statuses = ['paid', 'pending', 'cancelled', 'refunded']
    return status in allwoed_statuses

# To w innym pliku mogę napisać.

from validators import is_valid_status 

# I potem mogę użyć ten funkcji 

print(is_valid_status("paid"))

```

Ważne - > nie piszę .py w imporcie

## Import wielu funkcji 

Z jednego modułu można zaimportować kilka funkcji 

```python

from validators import is_valid_status, is_positive_value

# Potem używać

is_valid_status("paid")
is_positive_value(100)

```

## Import całego moduły

Można też zaimportować cały moduł 

```python

import validators

# Tylko wtedy trzeba używać funkcji z nazwą modułu

validatos.is_valid_status("paid")

```

Ta forma jest czasami bardziej czytelna, bo widzę skąd pochodzi funkcja

Można spotkać zapis : 

```python

from validators import * 

``` 

Na tym etapie lepiej tego uniknać ponieważ :

- nie widać dokładnie, co zostało zaimportowane 
- trudniej zrozumieć, skąd pochodzi funkcja
- w większych projektach może prowadzić do bałaganu
- lepsze są jawne import

## Dane w osobnym module 

data.py

ten plik może zawierać funkcję, zwracającą dane tekstowe 

```python

def get_orders():
    return [
        {"order_id": 1001, "order_value": 249.99, "status": "paid"},
        {"order_id": 1002, "order_value": 0, "status": "pending"},
        {"order_id": 1003, "order_value": 99.99, "status": "unknown"},
    ]

```

w main.py mogę zrobić : 

```python

from data import get_orders

orders = get_orders()

```

## Główny plik main.py

Powinien łączyć wszystko w całość

Przykładowa logika 

- Pobierz dane
- Zweryfikuj dane
- Wypisz raport

Czyli w przyszłości kod w main.py może wyglądać logicznie tak: 

```python

orders = get_orders()
errors = validate_orders(orders)
print_validation_report(errors)

```

To już przypomina prosty pipeline danych

## __name__ == "__main__"

Czasami w pliku z funkcjami chcę mieć kod testowy

Problem: 

Jeśli kod testowy jest napisany normalnie na dole pliku, może wykonać się również przy imporcie. 

Dlatego używa się zapisu: 
```python
if __name__ == "__main__":
    ...
```

Kod wewnątrz tego bloku wykona się tylko wtedy, gdy uruchomię plik bezpośrednio. Nie wykona się wtedy, gdy zaimportuje ten plik w innym pliku.

Przykład : 

```python

def is_valid_status(status):
    allowed_statuses = ["paid", "pending", "cancelled", "refunded"]
    return status in allowed_statuses


if __name__ == "__main__":
    print(is_valid_status("paid"))

```

## Skąd uruchamiam plik? 

Przy importach ważne jest, skąd uruchamiam program. 

Na tym etapie najprostsza zasada: 

Jeśli pracuje w folderze src/day_15_modules, wchodzę do tego folderu i uruchamiam main.py stamtąd 

## Najważniejsze rzeczy do zapamiętania 

- Moduł to plik .py
- Import pozwala używać kodu z innego pliku
- W imporcie nie piszę .py
- Funkcje walidacyjne warto trzymać w osobnym pliku.
- Dane testowe można trzymać w osobnym pliku
- Raporty można trzymać w osobnym pliku
- main.py powinien łączyć całość
- __name__ == "__main__" chroni kod testowy przed uruchomieniem przy imporcie
- Dobra struktura projektu ułatwia rozwijanie programu 






