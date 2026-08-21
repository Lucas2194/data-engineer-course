# Agregacja

## Czym jest agregacja 

Oznacza zebranie wielu rekordów i utworzenie na ich podstawie podsumowania. 

Przykładowe pytania agregujące :

- ile zamówień ma każdy status.
- Jaka jest suma zamówień dla każdego statusu 
- ile razy użyto każdej metody dostaw
- ilu klientów pochodzi z każdego miasta
- ile razy wystąpił każdy rodzaj błędu 

Mam wiele rekordów wejściowych, ale wynikiem jest mniejsza struktura podsumowujące dane. 

Przykład 

paid
pending
paid
cancelled
paid

Po agregacji : 

{
    "paid": 3,
    "pending": 1,
    "cancelled": 1,
}

Pięc rekordów wejściowych zostało zamienionych w trzy wartości podsumowujące. 

## Filtrtowanie a agregowanie 

To dwie różne operacje. 

Filtrowanie - wybiera rekordy spełniające warunek 

5 zamówień -> wybierz paid -> 3 zamówienia 

Dzień wcześniej robiła to funkcja get_paid_orders().

Wynikiem nadal była lista pełnych zamówień.

Agregowanie

Agergowanie oblicza podsumowanie 

5 zamówień -> policz według statusu -> słownik z licznikami 

Wynikiem nie muszą być pełne rekordy. Może nim być liczba albo słownik podsumowujący. 

Operacja                Pytanie                             Przykładowy wynik
filtrowanie             które zamówienia są paid            lista zamówień
agregowanie             ile zamówień ma każdy status        słownik liczników
agregowanie             jaka jest suma dla kazdego statusu  słownik sum 

## Akumulator

Akumulator to zmienna w której podczas pętli przechowujemy dotychczasowy wynik. 

Prosty akumulator z poprzedniej lekcji total = 0.0 

```python

total = 0.0

for amount in amounts:
    total = total + amount
```

Po każdej iteracji total zawiera sumę elementów przetworzonych do tej pory. 

Podobnie działa licznik :

```python

count = 0

for value in values:
    if value > 0:
        count += 1
```

W obu przypadkach istnieje tylko jeden akumulator:

- jedna suma
- albo jeden licznik

Co jednak zrobić, jeśli potrzebujemy osobnego licznika dla paid, osobnego dla pending i osobnego dla canelled?

Użyjemy słownika.

## Słownik jako zestaw liczników. 

Słownik pozwala powiązać kategorię z jej licznikiem:

```python
counts = {
    "paid": 3,
    "pending": 1,
    "cancelled" 1,
}
```

W tym słowniku: 

- kluczem jest nazwa kategorii
- wartością jest liczba jej wystąpień 

Nie musimy z góry wiedzieć, jakie statusu pojawią się w danych. Słownik może tworzyć kolejne klucze, podczas działania programu.

To ważna przewaga nad rozwiązaniem zawierającym osobne zmienne : 
```python
paid_count = 0 
pending_count = 0
cancelled_count = 0
```

Takie osobne zmienne działałby tylko dla kategorii znanych wcześniej. Gdyby w danych pojawił się nowy status, np. refunded, musielibyśmy zmieniać kod. 

Słownik obsłuży nową kategorię automatycznie. 

## Metoda get()

Przypomnijmy działanie get():

```python

value = dictionary.get(key, default_value)
```
Metoda:

- zwraca wartośc przypisaną do klucza, jeśli klucz istnieje
- zwraca wartość domyslną, jeśli klucza nie ma, 
- nie zgłasza KeyError dla brakującego klucza

Przykład

```python

counts = {"cat": 2}

print(counts.get("cat", 0)) # 2 
print(counts.get("dog", 0)) # 0

```

Ważne `get()` tylko pobiera wartość. Samo wywołanie tej metody nie dodaje ani nie aktualizuje niczego w słowniku. 

## Wzorzec licznika słownikowego 

Założmy, że liczymy wystąpenie zwierząt: 

```python
animals = ["cat", "dog", "cat", "bird", "cat"]
counts = {}

for animal in animals:
    current_count = counts.get(animal, 0)
    counts[animal] = current_count + 1 
```
Najważniejsze są dwie linie:

```python

current_count = counts.get(animal, 0)
counts[animal] = current_count + 1 

```

Czytamy je tak : 

- Pobierz dotychczasowy licznik danego zwierzęcia. 
- Jeśli tego zwierzęcia jeszcze nie ma, przyjmij zero
- Dodaj jeden
- Zapisz nową wartość pod właściwym kluczem

Po zrozumieniu wersji dwuetapowej można ją zapisać krócej:

```python

counts[animal] = counts.get(animal, 0) + 1 

```

Obie wersje wykonują dokładnie tę samą operację. 

Na początku lepiej korzystać z wersji dwuetapowej. Czytelność na początku jest ważniejzsa niżskrócenie kodu o jednąlinie. 

## Ręczne prześledzenie pętli 

Dane:

animals = ["cat", "dog", "cat"]

Stan słownika zmienia się następująco :

Iteracja    `animal`            Poprzednia wartość          Nowa wartość        Cały słownik
start       --------            ------------------          ------------        {}
1            cat                       0                         1              {"cat" :1}
2            dog                       0                         1              {"cat": 1, "dog": 1}
3            cat                       1                         2              {"cat": 2, "dog": 1}

W trzeciej iteracji kucz cat już istnieje. Dlattego get("cat", 1) zwraca 1, a nie wartość domyślną 0. 

## Alternatywa z if/else

Ten sam licznk można zapisać bez get():
```python

for animal in animals:
    if animal in counts:
        counts[animal] = counts[animal] + 1
    else:
        counts[animal] = 1 
```

Ta wersja pokazuje pełną logikę 

- istniejący klucz zwiększamy
- brakujący klucz tworzymy z wartością 1. 

Wersja z get() jest krótszym zapisem tej samej operacji : 

counts[animal] = counts.get(animal, 0) + 1 

## Grupowanie i sumowanie 

Nie zawsze chcemy dodawać 1. Możemy dodawać wartość z rekordu. 

Przykładowe dane : 

```python

sales = [
    {"category": "books", "amount": 40.0},
    {"category": "games", "amount": 120.0},
    {"category": "books", "amount": 25.0},
]

```

Chcemy obliczyć sumę sprzedaży dla każdego kategorii : 

```python

totals = {}

for sale in sales:
    category = sale["category"]
    amount = sale["amount"]
    current_total = totals.get(categorry, 0.0)
    totals[category] = current_total + amount

Wynik : 

{
    "books" : 65.0,
    "games" : 120.0,
}

```

Porównanie dwóch najważniejszych wzorców : 

1. Liczenie rekordów
   counts[key] = counts.get(key,0) + 1
2. Sumowanie wartości
   totals[key] = totals.get(key, 0.0) + value 

Różnica polega wyłącznie na tym, co dodajemy 

- licznik dodaje 1 
- suma dodaje wartość z rekordu 

# Normalizacja przed agregacją 

Należy zawsze pamiętać, że mimo że te same statusy, mogą inaczej wyglądać w pliku - > ["paid", " PAID ", "PaId"]. 
Dla człowieka oznaczjaą to samo, dla Pythona są to trzey rózne napisy. 
Bez normalizacji moglibyśmy otrzymać : 

```python
{
    "paid": 1,
    " PAID ": 1,
    "PaId": 1,
}

```

Dlatego przed użyciem statusu jako klucza, należy go ujednolicić 

- usunąć spacje z początku i końca
- zmienić litery na małe
- zdecydować co zrobić z wartością None albo brakiem pola 

## Agregacja danych zagnieżdzonych 

Pole delivery w zamóieniu może być słownikiem: 

```python
{
    "city": "Gdańsk",
    "method": "parcel_locker"
}

```

Może też mieć wartość: 

None 

Jeśli agregujemy metody dostawymy, najpierw bezpiecznie musimy pobrać delivery, a dopiero potem method

Schemat myślenia 

pobierz delivery
    ↓
Czy delivery jest słownikiem?
    ↓
Tak: pobierz method     nie: użyj "missing"
    ↓
zwiększ licznik wybranego klucza

Nie należy od razu wykonywać delivery.get("method") zanim nie upewnimy się, żę delivery nie jest None. 

## Dlaczego osbne funkcje?

Każda funkcja powinna odpowiadać na jedno konkretne pytanie : 

- count_orders_by_status() -> ile z zamówień ma każdy status?
- sum_orders_by_status() -> jaka jest suma dla każdego statusu?
- count_delivery_methods() -> ile razy wystąpiła każda metoda dostawy?

Dzięki temu: 

- łatwiej sprawdzić pojedynczy wynik
- łatwiej znaleźć błąd 
- kod w main() pozostaje czytelny
- funkcje można wykorzystać ponownie
- później łatwiej będzie napisać testy 
main() powinien sterować przypływem, a nie zawierać szczególy wszystkich obliczeń

## Związek z SQL i Pandas 

W czystym Pythonie samemu trzeba budować słowniki i aktualizować je w pętli 

W SQL podobną operację wykonuje GROUP BY: 

```sql

SELECT status, COUNT(*)
FROM orders
GROUP BY status;
```
W Pandas podobna idea pojawi się przy groupby()

Ważna jest idea : 

wybierz klucz grupowania -> zbierz rekordy należące do tej samej grupy - > wykonaj obliczenia dla każdej grupy. 


