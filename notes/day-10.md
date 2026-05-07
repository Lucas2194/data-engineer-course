# Dzień 10 - Python: Listy

## Cel dnia 

Dzisiaj uczę się list w Pythonie. 
Lista pozwala przechowywać wiele wartości w jednej zmiennej
Do tej pory jedna zmienna przechowywała jedną wartość

```python 
product = "Kubek"
products = ["Kubek", "Plakat", "Brelok"]

``` 

Listy będą bardzo ważne w dalszej nauce, bo w pracy z danymi często operuje się na wielu elementach : 

- wielu plikach
- wielu rekordach
- wielu statusach
- wielu kolumnach
- wielu błędach
- wielu wartościach liczbowyc

## Czym jest lista

Lista to kolekcja wartości 
Do list używamy nawiasów kwadratowych - > [] 
Elementy oddzielone sa przecinkami - > ['apple', 'pear', 'orange']
Możemy przechowywać różne zmienne w liście, nei musi być to koneicznei string. Na początku jednak, lepiej mieć listę jednych elemetnów. 

## Indeksy w liście. 

Elementy mają indeksy, Python liczy indeks od zera 
Dla listy

```python

producst = ["Kubek", "Plakat", "Brelok"] 

```

Indeksy wyglądają tak - > 

Indeks	Wartość
0	"Kubek"
1	"Plakat"
2	"Brelok"

Pierwszy element ma indeks 0 a nie 1 

# Odczytywanie elementu z listy 

Element z listy odczytuje się przez indeks 

```python

products = ["Kubek", "Plakat", "Brelok"]

print(products[0])
print(products[1])
print(products[2])

Wynik - > 

Kubek
Plakat
Brelok

``` 

Jeśli wystąpi błąd indexError - > Python próbuje odczytać element którgo nie ma, w tym wypadku byśym wpisywali products[3] 

## Funkcja len 

len() - > zwaraca liczbę elementów w liście 

```python

products = ["Kubek", "Plakat", "Brelok"]

print(len(products))

Wynik - > 3 

```

len() - odpowiadania na pytanie, ile elementów jest w tej liście. 

## Ostatni element listy

Najłatwiej to sprwadzić, wpisując index[-1] , analogicznie wpiszemy [-2] - będzie to przedostatni element listy

## Dodawanie elementu do listy

używamy append()

przykład

```python

products = ["Kubek", "Plakat"]

products.append("Brelok")

print(products)

```

Wynik - > ["Kubek", "Plakat", "Brelok"]

append() -> zmienia listę dodając nowy element na końcu

## Sprawdzanie elementów w liście

Operator in sprawdza, czy dana wartość znajduje się w liśćie

```python

products = ["Kubek", "Plakat"]

products.append("Brelok")

print(products)

``` 

Jest to czytelne i wygodne

Operator not in sprwadza, czy danej wartości nie ma w liście 

```python

allowed_statuses = ["paid", "pending", "cancelled", "refunded"]

status = "paid"

if status in allowed_statuses:
    print("Status jest poprawny.")
else:
    print("Status jest nieznany.")

```

## Zmiana elementu listy 

Element listy można zmienić po indeksie 

```python

products = ["Kubek", "Plakat", "Brelok"]

products[1] = "Plakat A3"

print(products)

``` 

Wynik ['Kubek', 'Plakat A3', 'Brelok']

