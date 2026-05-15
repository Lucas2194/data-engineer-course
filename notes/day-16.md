# Dzień 16 0 Python: funkcje pomicznice, main() i przepływ programu 

## Cel dnia

Dzisiaj uczę się porządkować program za pomocą funkcji `main()` i małych funkcji pomoczniczych. 

Po poprzednim dniu potrafięjuż dzielić kod na moduły, np.:

- `main.py`
- `data.py`
- `validators.py`
- `reports.py`

Dzisiaj uczę się jak sprawić, żeby `main.py` był czytelnym głównym przepływem programu

## Czym jest main()?

`main()` to zwykła funkcja, której programiści często używają jako głównego punktu startowego pgoramu. 

Przykład:

```python

def main():
    print("Program startuje")

if __name__ == "__main__":
    main()

```

Kod w main() uruchomi się wtedy, gdy plik zostanie uruchomiony bezpośrendio.

## Po co używać main()?

Funkcja main pomaga: 

- uporządkować główny przepływ programu
- uniknąć luźnego kodu na dole pliku
- lepiej rozumieć od czego zaczyna się program
- łatwiej testować pojedyńcze funkcje
- przygotowac kod pod większe projekty
- przygotować się do budowanie pipelinów danych

## Dobry schemat main.py

Przykładowy główny przepływ: 

```python

from data import get_orders
from validators import validate_orders
from reports import print_errors, print_summary


def main():
    orders = get_orders()
    errors = validate_orders(orders)

    print_errors(errors)
    print_summary(orders, errors)


if __name__ == "__main__":
    main()

```

To jest plik czytelny, bo pokazuje główne kroki programu:

1. pobierz dane
2. sprawdź dane
3. wypisz błędy
4. wypisz podsumowanie

## Funkcje pomocnicznce 

To takie, które są odpowiedzialne za jedną konkretną rzecz. Małe funkcje

```python

def is_valid_status(status):
    allowed_statuses = ["paid", "pending", "cancelled", "refunded"]
    return status in allowed_statuses

```

Ta funkcja odpowiada tylko na pytanie:

Czy status jest poprawny

## Dobra funkcja robi jedną rzecz 

Lepiej mieć kilka małych funkcji, niż jedną ogromną

Gorszy kierunke : 

```python

def process_orders():
    # pobiera dane
    # waliduje dane
    # wypisuje raport
    # liczy statystyki
    ...

```

Lepszy Kierunek : 

```python

orders = get_orders()
errors = validate_orders(orders)
print_errors(errors)
print_summary(orders, errors)

```

## Funkcja może wywoływać inną funkcję 

```python

def validate_orders(orders):
    all_errors = []

    for order in orders:
        order_errors = validate_order(order)
        all_errors.extend(order_errors)

    return all_errors

```

Tutaj validate_orders() używa validate_order().

## append() VS extend()

append() dodaje jeden element do listy.

Jeśli chcesz dodać listę do istniejącej listy powstanie lista w liście. 

extend() dodaje elementy z jednej listy do drugiej listy

To jest przydatne, gdy chce połączyć błędy z wielu zamówień w jedną listę.

## Funkcje logiczne a funkcje raportujące. 

- funkcje logiczne powinny zwracać dane przez return
- funckje raportujące mogą używać print()

```text

validators.py → return
data.py       → return
reports.py    → print
main.py       → łączy wszystko

```

## Podział odpowiedzialności w projekcie. 

data.py :

- odpowiada za dane
- może mieć funkcję get_orders()

vlalidators.py

- odpowiada za sprawdzanie danych
- może mieć funkcje is_valid_status(), validate_order(), validate_orders()

reports.py

- odpowiada za wypisywanie wyników
- może mieć funkcje print_errors(), print_summary()

main.py

- odpowiada za główny przepływ programu
- powinienen łączyć kroki, ale nie zawierać całej logiki

Dobra kolejność w pliku python

```text

1. importy
2. stałe / konfiguracja
3. funkcje
4. main()
5. if __name__ == "__main__":
       main()

```

## Stałe 

to wartości, których nie planuje się zmieniać w trakcie działania programu. 
W pythonie często zapisuje się je wielkimi literami 
np.

```python

ALLOWED_STATUSES = ["paid", "pending", "cancelled", "refunded"]
MIN_ORDER_VALUE = 0

```

## Najważniejsze rzeczy do zapamiętania 

1. main() to zwykła funkcja używana jako główny punkt startowy programu
2. Kod główny warto wkładać do main()
3. Na dole pliku warto używać if __name__ == "__main__":
4. Funkcje powinny robić jedną rzecz
5. Funkcja może wywołać inną funkcję.
6. append() dodaje jeden element
7. extend() dodaje elementy z innej listy
8. Funkcje logiczne zwykle powinny zwracać dane
9. Funkcje raportujące mogą wypisywać dane
10. main.py powinein pokazywać głóny przepływ programu
11. Taki styl przygotowuje do budowania pipeline;ów danych

