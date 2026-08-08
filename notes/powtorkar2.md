## Bezpieczny dostęp danych i konwersje 

1. **`dict.get()`** sięganie po klucz który może nie istnieć.
2. **konwersje** `float()` i `int()` i kiedy wybuchają. 
3. ** `try` / `except` ** - łapanie wybuchu aby program szedł dalej

Jest to sedno pracy data enginera, ponieważ w prawdziwym życiu, dane które przychodzą są **brudne** . Kolumna z kwotą czasami ma pusty string, czasaemi `"abc"`, czasami brakuje jej wogóle. Kod, który zakłada, że wszystko jest ładnie, wywali się o 3 w nocy. Muszę pracować tak, aby przetrwał. 

## 1. Problem: kod, który wybucha

Dostęp do słownika przez `[]` **rzuca błędem** gdy klucza nie ma:

```python

order = {"status":"paid"}
order["status"] # 'paid' - jest OK
order["total_amount"] # KeyError! klucza nie ma, program pada
```

Podobne konwersje. `float()` - zmienia tekst na liczbę, ale tylko gdy się da:

```python

float("149.99") # 149.99 - OK 
float("abc")   # ValueError! <- To nie jest liczba, program pada
float(None)   # TypeError! < None to nie jest tekst ani liczba, program pada
float("")    # ValueError! <- pusty string, to nie liczba, program pada 

```

**Zapamiętać dwa typy błędów, bo one będą najczęściej do wyłapania**

- **`ValueError`** - wartość jest złego *rodzaju* czyli powinna być liczba a jest tekst - > `"abc"`, `""` 
- **`TypeError`** - wartość jest złego *typu* (`None` - to wogólnie jest tekst, ani liczba) 

---

## 2. `dict.get()` - sięgnie po klucz i nie wywala od razu programu.

Zamiast `order["klucz"]` ( wywala przy braku ), lepiej użyć `order.get("klucz")`. Gdy nie ma klucza, dostaje **`None`** zamiast błędu 

```python

order = {"status":"paid"}
order.get("status") # "paid"
order.get("total_amount") # None <- Brak klucza, ale bez błędu (wywalenie programu)

```

Można podać **wartość domyślną** jako drugi argument - czyli to, co ma zwrócić jeśli klucza nie będzie 

```python
order.get("total_amount", 0) # 0 <- brak klucza, domyślnie 0
order.get("status", "unknown") # "paid" < klucz jest -> jego wartość
order.get("brak", "unknown") # "unknown" < klucza nie ma - > domyślnie
```

**Zasada** gdy klucz może nie istnieć `.get(klucz, domyślnie)` zamiast `[klucz]`. To jest z najczęsztyszch rzeczy w pracy

## 3. Konwersje `float()` / `int()` 

`float("12,5")` - > `12,5`. `int("7")` - > `7` - > Zamiana tekstu na liczbę, gdy wszystko jest ok. 

Kluczowa wiedza **co się da, a co może wywalić program**

```python
float("149,99") # 149.99 OK
float("89") # 89.0 OK 
float(89) # 89.0 OK
float("12,50") # ValueError! <- PRZECINEK, zamiast kropki nie przejdzie
float("abc") # ValueError!
float("") # ValueError!
float(None) # TypeError!
```

**WAŻNE** w danych z Polski często mogą być przecinki, patrz wyżej `"12,50"`, przy konwersji float to nie przejdzie, gdyż musi być z kropką. 

---

## 4. `try` / `except` - łapanie wywalenia programu 

To jest mechanizm, który mówi "spróbuj zrobić to, jeśli wywróci program, nie podaj tylko zrób plan B. 

```python

try:
    liczba = float(value)   # Spróbuj zmienić na float
except ValueError:
    liczba = 0.0            # jeśli był Value Error -> plan B
```

Należy czytać to w ten sposób - > spróbuj `float(value)`. Jak poleci `ValueError`, złap go i ustaw `0.0` zamiast pozwolić programowi paść

**Łapanie kilku błędów naraz** - w nawiasie, po przecinku 

```python
try:
    liczba = float(value)
except (ValueError, TypeError):
    liczba = 0.0
```

Ważne bo value może być `"abc"` (ValueError) albo `None` (TypeError)

## Dlaczego NIE samo `except:`

Kusi żeby napisać samo except bez wskazania jaki to błąd, jest to błędna praktyka, ponieważ niektóre błędy chcesz wyłapać. Np. Literówka w nazwie, zły przcinek, cokolwiek. Zamiast naprawić błędy, ukryjesz go. Na code review to nie  przejdzie, firma też będzie na to źle patrzeć. 

**Zawsze łapię kkonkretny typ** 

## 5. Wszystko razem 

```python

def safe_get_total(order):
    value = order.get("total_amount")    # 1. sięgniej bezpiecznie (może być None)
    try:
        return float(value)              # 2. Spróbuj zamienić na liczbę
    except(ValueError, TypeError):
        return 0.0                       # 3. Jeśli coś poszło nie tak - > 0.0

```

Trzy rzeczy mogą tutaj pójść źle i wszystkie są tu obsłużone: brak klucza (`get` dla `None`), zły tekst (`ValueError`), zły typ (`TypeError`). Funkcja **nigdy nie wywali** - a to bardzo ważne

