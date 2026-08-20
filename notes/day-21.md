# Json

## 1. Czym jest JSON

JSON oznacza: 

JavaScript Object Notation 

Jest to tekstowy foramt zapisu i wymiany danych. 

Na przykład

```json
{
    "order_id": 1001,
    "customer_name": "Anna",
    "total_amount": 249.99,
    "status": "paid"
}
```
JSON wygląa podobnie do słownika Pythona, ale słownikiem nie jest. 

- JSON jest tekstem zapisanym według określonych reguł 
- Słownik jest obiektem istniejącym w pamięci uruchomionego programu.

Python może zmienić tekst JSON na słownik lub listę. Może też wykonać operację w drugą stronę i zapisać obiekty Pythona jako JSON.

## JSON a słownik Pythona

Python:
```python
order = {
    "order_id":1001,
    "is_paid":True,
    "discount_code": None,
}
```
JSON
```json
{
    "order_id":1001,
    "is_paid": true,
    "discount_code": null
}
```
Najważniejsze różnice : 

JSON    Python 
true    True
false   False
null    None
obiekt  dict
tablica list
tekst   str
liczba całkowita    int
liczba dziesiętna   float

W prawidłowym JSON-ie:

- nazwy pól i teksty zapisujemy w podwójnych cudzysłowach,
- nie używamy True, False ani None
- Nie wolno zostawić zbędnego przecinka po ostatnim elemencie,
- standardowy JSON nie obsługuje komentarzy. 

Niepoprawny JSON:

```json
{
    'customer_name': 'Anna',
    'is_paid': True,
}
```

Poprawny JSON:
```json
{
    "customer_name": "Anna",
    "is_paid": true
}
```

## Dlaczego JSON jest tak ważny w Data Engineeringu?

JSON często pojawia się jako

- Odpowiedź z API
- wiadomość przesyłana pomiędzy systemami
- zapis zdarzenia lub logu
- plik konfiguracyjny
- dane pobierane z aplikacji internetowych
- format wejściowy albo wyjściowy pipeline'u 

Przykładowa odpowiedź API może zawierać : 

```json

{
    "customer":{
        "id": 501,
        "name": "Anna"
    },
    "orders": [
        {"order_id": 1001, "amount":249.99},
        {"order_id": 1002, "amount":120.00}
    ]
}
```

W przeciwieństwie do CSV JSON może przechowywać dane zagnieżdzone:

- słownik wewnątrz słownika
- listę wewnątrz słownika
- słowniki wewnątrz listy

## CSV a JSON

Cecha                       CSV                       JSON
Podstawowa struktura        tabela                    obiekty i listy
Zagnieżdzanie               praktycznie brak          tak
Typy po odczycie            zwykle str                int, float, bool, None, str
Typowe użycie               tabele i eksporty         API i dane złożone
Czytelność prostych tabel   bardzo dobra              dobra
Czytelność danych złożonych słaba                     bardzo dobra

W dniu 20 wartość 249.99 z CSV została odczytana jako tekst "249.99".

W JSON-ie liczba 249.99 zostanie po odczycie zamieniona na falot automaatycznie, o ile w pliku nie umieścisz jej w cudzysłowie.

## Moduł Json

Python posiada wbudowany moduł json

import json

Nie trzeba instalować żadnej dodatkowej biblioteki. 

Najważniejsze funkcje

**Funkcja**             **Co robi**
json.load(file)         odczytuje JSON z otwartego pliku
json.loads(text)        odczytuje JSON z tekstu
json.dump(data,file)    zapisuje dane do otwartego pliku
json.dumps(data)        zmienia dane na tekst JSON

Pomocna reguła

litera s oznacza string, czyli tekst

- load - plik
- loads - string 
- dump - plik
- dumps - string

## Odczyt JSON z pliku

Przykład koncepcyjny

```python
import json
from pathlib import Path

file_path = Path("data") / "settings.json"

with open(file_path, "r", encoding="utf-8") as file:
    settings = json.load(file)

print(settings)
print(type(settings))

```

Jeżeli główną strukturą pliku jest obiekt JSON, wynikiem będize zwykle dict 

Jeżeli główną strukturą jest tablica: 

```json

[
    {"order_id": 1001, "status": "paid"},
    {"order_id": 1002, "status": "pending"}
]

Wynikiem json.load() będzie lista, a jej elementami będą słowniki

```

## load() a loads()

json.load() pracuje z otwartym plikiem: 

```python
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
```

json.loads() pracuej  z tekstem

```python

json_text = '{"status": "paid", "amount": 120.0}'
data = json.loads(json_text)
```
Po wykonaniu loads() zmienna data będzie słownikiem Pythona.

Na tym etapie najcześciej będziemy używać json.load() 

Zapis JSON 

```python

import json

profile = {
    "name" : "Łukasz",
    "active" : "True,
    "skills" : ["Python", "Git"],
}

with open("output/profile.json", "w", encoding="utf-8") as file:
    json.jump(profile, file, ensure_ascii=False, indent=4)
```
Znaczenie parametrów

- ensure_ascii = False - polskie znaki pozostają czytelne
- indent=4 - plik zostaje estetycznie sformatowany. 

Bez ensure litera Ł mogłaby zostać zapisana jako kod Unicode.
ten plik nadal byłby poprawny, ale mniej wygodny do czytania

## Dane zagnieżdzone 

Przykładowe zamówienie 

```json

order = {
    "order_id": 1001,
    "customer_name": "Anna",
    "tags": ["vip", "newsletter"],
    "delivery": {
        "city": "Gdańsk",
        "method": "parcel_locker",
    },
}
```

Dostęp do danych

```python
print(order["customer_name"])
print(order["tags"][0])
print(order["delivery"]["city"])
```

Czytamy od lewej strony

pobierz pole delivery
jego wartością jest kolejny słownik
z tego słownika pobierz pole city

Bezpieczenijszy wariant

```python
delivery = order.get("delivery")

if delivery is not None:
    city = delivery.get("city")
    print(city)
```

To ważne, ponieważ delivery może mieć wartość None. 

## Obłusga błędów

Brak pliku. 

Jeśli ścieżka nie istnieje, open() może zgłosić FileNotFoundError

Ten błąd jest znany

Niepoprawny JSON

Jeżeli plik ma błędną składnie, json.load() zgłosi:

json.JSONDecodeError

Przykład błędu w pliku

```json

{
    "name": "Anna",
    "status": "paid"
}
```
Pomiędzy polami brakuje przecinka

Schemat obsługi

```python

try:
    ...
except FileNotFoundError:
    ...
except json.JSONDecodeError:
    ...

```

Nie należy uzywać except Exception bez konkretnego powodu. Programista powinien wiedzieć, jaki rodzaj błędu bedzię próbował obsłużyć.

## Serializacja i deserializacja 

Deserializacja 

Json - > obiekty Pythona

Wykonujemy ją między innymi json.load() i json.loads()

Serializacja 

Obiekty Pythona -> JSON

Wykonują ją między innymi json.dump() i json.dumps()

Proste zdanie do zapamiętania 

**json.load() deserializuje dane z pliku JSON do obiektów Pythona**
**a json.dump() serializuje obiekty Pythona do pliku JSON**
