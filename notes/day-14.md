# Dzień 14 - python funkcje 

## Cel dnia

Dzisiaj uczę się funkcji 

Funckja pozwala zamknąć fragment kodu pod jedną nazwą 

Przykład 

```python

def say_hello():
    print("Cześć")

say_hello()

```

Są one bardzo ważne, bo pomagają porządkować kod, uniknać powtarzania i tworzyć czytelniejsze programy

## Po co są funkcję 

Bez funkcji kod moze szybko stać się długi i chaotyczny

Funkcje pomagają 

- podzielić program na mniejsze części
- nazwać fragmenty logiki
- uzywać tego samego kodu wiele razy
- łatwiej poprawić program
- łatwiej testować pojedyńcze fragmenty
- pisać kod podobny do prawidzych pipeline'ów danych

Przykład logiczny

Zamiast pisać całą walidację wiele razy,
tworzę funkcje validate_order()
i używam jej dla różnych zamówień

## Definiowanie funkcji 

Funkcję definiuję przez słowo def

Schemat

```python

def nazwa_funkcji():
    kod_funkcji

# Przykład

def say_hello():
    print("cześć")

```

Elemenety :

- def oznacza definicję funkcji
- say_hello to nazwa funkcji
- () to nawiasy funkcji
- : rozpoczyna blok kodu
- wcięty kod należy do funkcji

## Wywołanie funkcji 

Samo zdefiniowanie funkcji jej nie uruchamia. 

Trzeba zrobić wywołanie. Aby zrobić to z poprzednią funkcją, należy 

```python

def say_hello():
    print("Cześć!")

# wywołanie 

say_hello()

```

## funkcja bez parametrów nie przyjmuje żadnych danych z zewnątrz 

```python

def show_course_goal():
    print("Moim celem jest Junior Data Engineer")

show_course_goal()

```

Ta funkcja zawsze robi to samo 

## Funkcja z parametrem 

Parametr pozwala przekazać dane do funkcji 

Przykład 

```python

def greet_user(name):
    print(f'Cześć, {name}')

# Wywołanie 

greet_user("Łukasz")
greet_user("Anna")

```

## Parametr a argument

Parametr to nazwa używana w definicji funkcji 

```python

def greet_user(name):
    print(name)

# Tutaj name to parametr 

```

Argument to konkretna wartość przekazana przy wywołaniu 

```python

greet_user("Łukasz")

```

Tutaj "Łukasz" jest argumentem

Łatwiej :

parametr - > miejsce na wartość
argument - > konrketna wartość

## Funkcja z kilkoma parametrami 

Funkcja może przyjmować więćej niż jeden parametr 

Przykład 

```python

def show_order_summary(product_name, quantity, unit_price):
    total = quantity * unit_price
    print(f"Produkt: {product_name}")
    print(f"Liczba sztuk: {quantity}")
    print(f"Razem: {total:.2f} zł")

```

Wywołanie

```python

show_order_summary("Kubek z kotem", 3, 39.99)

```

## Return

return zwraca wynik z funkcji 

```python

def calculate_total(quantity, unit_price):
    total = quantity * unit_price
    return total

```

Wywołanie 

```python

order_total = calculate_total(3, 39.99)
print(order_total)

```

Funkcja oblicza wynik i oddaje go do dalszego użycia

## print() a return

print() pokazuje coś na ekranie 
return zwraca wynik z funkcji 

Przykład z print 

```python

def add_numbers(a, b):
    print(a + b)

```

Ta funkcja pokazuje wynik, ale nie oddaje go do dalszego użycia 

Przykład z return: 

```python

def add_numbers(a+b):
    return a + b

```

Ta funkcja zwraca wynik, który można zapisać do zmiennej.

```python

result = add_numbers(2,3)

```

Najważniejsza różnica 

print() - > Pokazuje wynik użytkownikowi 
return - > przekaż wynik dalej w programie.

## Funckaj zwracająca True albo False

Funkcja może zzwracać wartość logiczną 

```python

def is_valid_status(status):
    allowed_statuses = ["paid", "pending", "cancelled", "refunded"]
    return status in allowed_statuses

```

Wywołanie 

```python

print(is_valid_status("paid"))
print(is_valid_status("unknown"))

```

Wynik

True
False

Funkcje któe zwracają True albo False często mają nazwy zaczynające się od :

- is_
- has_
- can_
- should_
  

## Funkcja sprawdzają wartość 

Przykład 

```python

def is_positive_order_value(order_value):
    return order_value > 0

```

Ta funkcja odpowiada na pytanie : 

Czy wartość zamówienie jest większa od 0

dla 

```python

is_positive_order_value(100)

```

Wynik to True

Jeśli wstawimy tam zero, wynik będzie False

## Funkcja walidująca dane 

Funkcja może zwracać listę błędów.

Schemat logiczny

def validate_order(order):
    utwórz pustę listę errors
    sprawdź pole zamówienia
    jeśli coś jest nie tak, dodaj błąd
    zwróć errors

To jest dobry wzorzec w data enginreingu bo funkcja może przyjąć jeden rekord i zwrócić informację o błędach. 

## Funckje w Data engineeringu 

Pomagają one budować pipeline'y

Przykładowe kroki 

- extract - pobierz dane
- validate - sprwadź dane
- transform - przekształć dane
- load - zapisz dane 

Można to rozbić na funkcje 

```python

def extract_data():
    pass

def validate_data():
    pass

def transform_data():
    pass

def load_data():
    pass

```

## jedna funkcja - jedna odpowiedzialność

Dobra funkcja powinna robić jedną konkretną rzecz 

Przykłady 

calculate_order_total - > liczy wartość zamówienia
is_valid_status - > sprawdza status
validate_order - > walidfuje jedno zamówienie 
print_errors - > wypisuje błędy

