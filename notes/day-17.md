# Dzień 17 - Python, obsługa błędów, try/except i bezpieczne dane

 ## Cel dnia 

 Dzisiaj uczę się obsługiwać błędy w Pythonie

 W prawdziwych projektach często dane są niepoprawne

 - brakuje wartości
 - liczby są zapisane jako tekst
 - tekstu nie da sięzamienić na liczbę
 - w słowniku brakuje klucza
 - wartość ma zły typ
 - plik lub źródło danyych może nie istnieć 

Dobry program nie powineien wywracać sięprzy pierwswzym błędzie. Powinien umieć wykryć problem i zareagować w kontrolowowany sposób

## Czym jest wyjątek 

Wyjątek to  sytuacja, w któej Python nie może normalnie wykonać kodu 

```python

int("abc")

```

Ten kod spowoduje błąd, bo tekstu `abc` nie da się zamienić na liczbę. 

## Value Error

Pojawia się wtedy, gdy wartość ma zły format

Przykład 

```python

int("abc")
float("brak")

```

Python rozumie co chcemy zrobić, ale podana wartość się do tego nie nadaje

## KeyError

pojawia się wtedy, gdy probuje pobrać ze słownika klucz, którego nie ma

Przykład 

```python 

order = {"status" : "paid"}
print(order["order_value"])

```

Bezpieczniejsza wersja

```python

order.get("order_value")

Jeśli klucza nie ma, get() zwróci None. 

```

## TypeError

Pojawia sięwtedy, gdy probuje sięwykonać operacją na niepasującym typie danych 

Przykład 

```python

value = None
print(value <= 0)

```

Python nei wie, jak porównać None z liczbą 

## try/except

Pozwala obsłużyć błąd bez zatrzymywania programu 

Schemat 

```python

try: 
    # kod, który może spowodować błąd 
except ValueError:
    # co zrobić, jeśli wystąpi Value Error

# Przykład 

try:
    value = float('abc')
except ValueError:
    value = None

```

Program się nie wywróci. Zmienna value dostanie None

## Łapanie kilku błędów 

Można złapać kilka typów błędów naraz

```python

try:
    value = float(raw_value)
except (ValueError, TypeError):
    value = None

```

To oznacza

Jeśli wystąpi ValueError albo TypeError, ustaw value na None.

## Nie używać zbyt szerokiego except 

Słaby styl :

```python

try:
    # dużo kodu
except:
    print("Błąd")

```

Problem:

- nie wiem jaki błąd wystąpił.
- mogę ukryć prawdziwy problem
- turniej debugować program

Lepszy styl

```python

try:
    value = float(raw_value)
except (ValueError, TypeError):
    value = None

```

## Kiedy używać if, a kiedy try/except ? 

if jest dobry gdy mogę łatwo sprwadzić warunek 

```python

if status not in allwoed_statuses:
    errors.append("Niepoprawny status")

```

try/except jest dobry, gdy operacja może się nie udać 

Przykład 

```python

try:
    value = float(raw_value)
except (ValueError, TypeError):
    value = None

```

- Używaj if, gdy sprawdzasz logikę biznesową (np. czy status jest na liście, czy koszyk jest pusty, czy klient ma 18 lat).

- Używaj try...except, gdy Twój program styka się ze światem zewnętrznym, na który nie masz wpływu (użytkownik, pliki, internet, zamiana typów danych).

## Funkcja pomocnicza 

Często warto zrobić sobie funkcję pomocniczą 

Przykład 

```python

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

```

Taka funkja zwraca : 

- liczbę, jeśli konwersja się udała
- None, jeśli konwersja się nie udała

## None jako informacja o braku wartości

None często oznacza : 

- brak wartości
- nie udało się czegoś przetworzyć
- wartość jest nieznana

przykład 

```python

converted_value = safe_float(raw_value)

if converted_value is None:
    errors.append('Niepoprawna wartość')

```

Do sprawdzania None używam 

if value is None:

a nie 

if value == None:

Do sprawdzania czy coś nie jest None używam negacji czyli - > if value is not None

## Uwaga na if not value

Ponieważ dla Pythona 0 jest fałszem 

Dlatego w walidacji warto pisać precyzyjnie : 

```python

if value is None:
    errors.append("Brak Wartości")
elif value <= 0:
    errors.append("Wartość musi być większa od 0")

```

## Normalizacja tekstu

Dane tekstowe często mająspacje, albo różnią się wielkością liter.

```python

status = " PAID "

``` 

Można użyć : 

```python

status.strip().lower()

```

Wynik - > "paid"

strip() -> usuwa spacje z początku i końca tekstu 
lower() -> zmienia tekst na małe litery

## isinstance()

isinstance() sprawdza typ danych 

Przykład 

```python

isinstance("paid", str)

```

wynik - > True 

```python

isinstance(123, str)

```

wynik - > false 

## Najważniejsze rzeczy do zapamiętania 

- Wyjątek do błąd, który może zatrzymać program
- try/except -> pozwala obsłużyć błąd
- ValueError pojawia się przy złej wartości
- KeyError pojawia sięprzy braku klucza w słowniku
- TypeError pojawia sięprzy złym typie danych 
- Lepiej łapać konkretne błędy niż używać pustego except 
- safe_float() to dobry przykład funkcji pomocniczej 
- None może oznaczać brak lub niepoprawną wartość
- Do sprawdzenia None używam is None
- W walidacji lepiej być precyzyjnym niż pisać if not value 
- strip() i lower() pomagają normalizować tekst
- Obsługa błędów jest podstawą pracy z brudnymi danymi 