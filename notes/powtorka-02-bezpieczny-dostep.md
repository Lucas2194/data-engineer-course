# Powtórka R2 — Bezpieczny dostęp i konwersje

**Cel:** nauczyć się wyciągać dane tak, żeby kod **się nie wywalił** na brudnych danych.
To jest fundament zadania #2 z diagnostyki (`safe_get_total`), na którym się zaciąłeś.

Trzy klocki:
1. **`dict.get()`** — sięganie po klucz, który może nie istnieć,
2. **konwersje** `float()` / `int()` — i kiedy wybuchają,
3. **`try` / `except`** — łapanie wybuchu, żeby program szedł dalej.

Dlaczego to jest sedno pracy data engineera: dane z realnego świata są **brudne**.
Kolumna z kwotą ma czasem pusty string, czasem `"abc"`, czasem brakuje jej w ogóle.
Kod, który zakłada, że wszystko jest ładne, wywali się o 3:00 w nocy. Twój ma przetrwać.

---

## 1. Problem: kod, który wybucha

Dostęp do słownika przez `[]` **rzuca błędem**, gdy klucza nie ma:

```python
order = {"status": "paid"}
order["status"]        # "paid"  — jest OK
order["total_amount"]  # KeyError!  <- klucza nie ma, program pada
```

Podobnie konwersje. `float()` zamienia tekst na liczbę — ale tylko gdy się da:

```python
float("149.99")  # 149.99  — OK
float("abc")     # ValueError!  <- to nie jest liczba, program pada
float(None)      # TypeError!   <- None to nie tekst ani liczba, program pada
float("")        # ValueError!  <- pusty string to nie liczba
```

**Zapamiętaj te dwa typy błędów, bo będziesz je łapał:**
- **`ValueError`** — wartość jest złego *rodzaju treści* (`"abc"`, `""` — to tekst, ale nie liczba).
- **`TypeError`** — wartość jest złego *typu* (`None` — to w ogóle nie jest tekst).

---

## 2. `dict.get()` — sięganie, które nie wybucha

Zamiast `order["klucz"]` (wybucha przy braku) używasz `order.get("klucz")`.
Gdy klucza nie ma, dostajesz **`None`** zamiast błędu:

```python
order = {"status": "paid"}
order.get("status")        # "paid"
order.get("total_amount")  # None    <- brak klucza, ale BEZ błędu
```

Możesz podać **wartość domyślną** jako drugi argument — to, co ma wrócić przy braku:

```python
order.get("total_amount", 0)         # 0        <- brak klucza -> domyślne 0
order.get("status", "unknown")       # "paid"   <- klucz jest -> jego wartość
order.get("brak", "unknown")         # "unknown" <- klucza nie ma -> domyślne
```

**Zasada:** gdy klucz może nie istnieć, `.get(klucz, domyślne)` zamiast `[klucz]`.
To jedna z najczęstszych rzeczy, jakie napiszesz w tej pracy.

---

## 3. Konwersje `float()` / `int()`

`float("12.5")` → `12.5`. `int("7")` → `7`. Zamiana tekstu na liczbę.

Kluczowa wiedza — **co się da, a co wybucha:**

```python
float("149.99")   # 149.99   OK
float("89")       # 89.0     OK (int-owy tekst też przejdzie na float)
float(89)         # 89.0     OK (liczba na float)
float("12,50")    # ValueError!  <- PRZECINEK zamiast kropki nie przejdzie
float("abc")      # ValueError!
float("")         # ValueError!
float(None)       # TypeError!
```

Zwróć uwagę na `"12,50"` — w danych z Polski kwoty bywają z przecinkiem. `float()`
tego nie zje. (W R2 się tym nie zajmujemy, ale zapamiętaj, że to pułapka.)

---

## 4. `try` / `except` — łapanie wybuchu

To jest mechanizm, który mówi: „spróbuj to zrobić; jeśli wybuchnie — nie padaj,
tylko zrób plan B".

```python
try:
    liczba = float(value)      # SPRÓBUJ zamienić
except ValueError:
    liczba = 0.0               # jeśli był ValueError -> plan B
```

Czytasz to: „spróbuj `float(value)`. Jak poleci `ValueError`, złap go i ustaw `0.0`
zamiast pozwolić programowi paść".

**Łapanie kilku typów błędów naraz** — w nawiasie, po przecinku:

```python
try:
    liczba = float(value)
except (ValueError, TypeError):   # łapie OBA
    liczba = 0.0
```

To Ci jest potrzebne, bo `value` może być `"abc"` (ValueError) **albo** `None` (TypeError).

### Dlaczego NIE samo `except:`

Kusi, żeby napisać `except:` bez typu — łapie wszystko, mniej pisania. **Nie rób tego.**
Gołe `except:` połyka też błędy, o których *chciałbyś* wiedzieć (np. literówkę w nazwie
funkcji). Zamiast naprawić prawdziwy błąd, ukryjesz go. Na code review to nie przejdzie —
w firmie też nie. **Zawsze łapiesz konkretny typ.**

---

## 5. Wszystko razem — bezpieczne wyciąganie kwoty

Zadanie #2 z diagnostyki to złożenie trzech powyższych klocków. Schemat:

```python
def safe_get_total(order):
    value = order.get("total_amount")   # 1. sięgnij bezpiecznie (może być None)
    try:
        return float(value)             # 2. spróbuj zamienić na liczbę
    except (ValueError, TypeError):
        return 0.0                      # 3. cokolwiek poszło nie tak -> 0.0
```

Trzy rzeczy mogą pójść źle i wszystkie są tu obsłużone: brak klucza (`get` da `None`),
zły tekst (`ValueError`), zły typ (`TypeError`). Funkcja **nigdy nie wybucha** — a to
jest całe zadanie.

---

## 6. Demo — URUCHOM to najpierw

```
uv run python -m src.powtorka_02_bezpieczny_dostep.demo
```

Zobaczysz na żywo `.get()`, konwersje i `try/except` w akcji — łącznie z tym, co się
dzieje, gdy dane są brudne. Kod dema jest w `src/powtorka_02_bezpieczny_dostep/demo.py`.

---

## 7. Zadania

Plik: `src/powtorka_02_bezpieczny_dostep/exercises.py` — pięć funkcji z `pass`.
Jedna klasa naraz, od góry:

```
uv run pytest tests/test_powtorka_02.py::TestGetField -v
```

| # | Funkcja | Co ćwiczy |
|---|---------|-----------|
| 1 | `get_field` | `dict.get()` z domyślną wartością |
| 2 | `to_float` | `try/except`, konwersja → liczba albo `None` |
| 3 | `is_convertible_to_float` | ten sam wzorzec, ale zwraca `True`/`False` |
| 4 | `safe_get_total` | złożenie wszystkiego (to jest zadanie #2 z diagnostyki) |
| 5 | `format_total` | stretch: R2 + `:.2f` z R1 |

**Reguła 20 minut** obowiązuje. **Test to prawda** — gdy docstring i test się różnią,
wierzysz testowi.

---

## Wyniki (wypełniaj na bieżąco)

| # | Funkcja | Bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|-------------|------------|---------------------|
| 1 | `get_field` | | | |
| 2 | `to_float` | | | |
| 3 | `is_convertible_to_float` | | | |
| 4 | `safe_get_total` | | | |
| 5 | `format_total` | | | |

**Co wróciło od razu:**

**Co dalej sprawia problem:**

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| to raise (an exception) | rzucić (wyjątek) | `float("abc")` raises ValueError |
| to catch / to handle | złapać / obsłużyć | `except ValueError:` |
| default value | wartość domyślna | `.get(key, default)` |
| to convert / conversion | konwertować / konwersja | `float("12.5")` |
| exception | wyjątek | ValueError, TypeError |
| missing key | brakujący klucz | `order.get("brak")` |
