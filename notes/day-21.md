# Dzień 21 — Diagnostyka po przerwie

**Data:** 2026-07-14
**Cel dnia:** zmierzyć, co realnie zostało w głowie po 7 tygodniach przerwy.

---

## Zasady (przeczytaj przed startem)

1. **Nie zaglądasz do starego kodu.** Katalogi `src/day_01` … `src/day_20` są dziś
   zakazane. Mierzymy, co pamiętasz, a nie co potrafisz skopiować. Zaglądanie
   zafałszuje wynik i skończy się tym, że w sierpniu będziemy powtarzać nie to, co trzeba.

2. **Dokumentacja jest dozwolona.** `docs.python.org`, `str.strip()`, sygnatura
   `csv.DictReader` — to nie ściąganie, to normalna praca. W firmie też będziesz
   sprawdzał składnię.

3. **Reguła 20 minut.** Zacinasz się na jednym zadaniu dłużej niż 20 minut → pytasz.
   Siedzenie 2h nad jednym błędem to nie hart ducha, tylko zmarnowany wieczór.

4. **Tabela na dole jest ważniejsza niż zielone testy.** Serio. Zielone testy powiedzą
   mi, że umiesz. Tabela powie mi, **czego nie umiesz** — a to jest informacja, za którą
   płacimy tym wieczorem.

---

## Jak pracować

Plik z zadaniami: `src/day_21_diagnostyka/exercises.py` — osiem funkcji, każda z
docstringiem opisującym, co ma robić. W środku jest `pass`. Twoim zadaniem jest
zamienić `pass` na działający kod.

Uruchomienie wszystkich testów:

    uv run pytest tests/test_day_21.py -v

Uruchomienie **jednego** zadania (tak pracuj — nie patrz na 26 czerwonych testów naraz):

    uv run pytest tests/test_day_21.py::TestFormatOrderSummary -v

Podgląd, dlaczego test padł (pokazuje oczekiwaną i otrzymaną wartość):

    uv run pytest tests/test_day_21.py::TestSafeGetTotal -v

**Kolejność — od najłatwiejszego do najtrudniejszego.** Nie skacz:

| # | Funkcja | Klasa testowa | Co sprawdza |
|---|---------|---------------|-------------|
| 1 | `format_order_summary` | `TestFormatOrderSummary` | f-stringi, formatowanie liczb, `.strip()` |
| 2 | `safe_get_total` | `TestSafeGetTotal` | `dict.get()`, `try/except`, konwersje typów |
| 3 | `filter_valid_amounts` | `TestFilterValidAmounts` | pętle, warunki, budowanie listy |
| 4 | `count_statuses` | `TestCountStatuses` | słowniki jako liczniki, normalizacja stringów |
| 5 | `split_valid_invalid` | `TestSplitValidInvalid` | walidacja, dwie listy naraz, zwracanie krotki |
| 6 | `read_csv_rows` | `TestReadCsvRows` | `csv.DictReader`, `pathlib`, obsługa braku pliku |
| 7 | `top_customers` | `TestTopCustomers` | agregacja + sortowanie po dwóch kluczach |
| 8 | `run_pipeline` | `TestRunPipeline` | **integracja wszystkiego** — to jest ten trudny |

Zadania 7 i 8 są celowo trudniejsze, niż wszystko, co robiłeś do dnia 20. Jeśli się na
nich zatniesz — to jest normalne i planowane. Ważne, żebyś **spróbował**, zanim poprosisz
o wskazówkę.

---

## Podpowiedzi ogólne (nie rozwiązania)

- Kwota z dwoma miejscami po przecinku: mechanizm nazywa się **format spec** w f-stringu.
  Szukaj w dokumentacji `Format Specification Mini-Language`, sekcja o `f`.
- „Nie może rzucić wyjątkiem" znaczy: `try` wokół konwersji, `except` łapiący **konkretne**
  typy błędów. `except:` bez typu to nie jest odpowiedź, którą przepuszczę na review.
- Sortowanie po dwóch kluczach naraz (malejąco po liczbie, rosnąco po nazwie) —
  szukaj argumentu `key=` w `sorted()`. Trik: liczbę można odwrócić minusem.
- W `run_pipeline` **użyj funkcji, które napisałeś wyżej**. Jeśli przepisujesz tę samą
  logikę drugi raz, robisz to źle — i to zobaczę na review.

---

## Wyniki diagnostyki

Wypełniaj **na bieżąco**, nie na koniec — po fakcie nie pamięta się, co bolało.

| # | Funkcja | Zrobione bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|----------------------|------------|---------------------|
| 1 | `format_order_summary` | | | |
| 2 | `safe_get_total` | | | |
| 3 | `filter_valid_amounts` | | | |
| 4 | `count_statuses` | | | |
| 5 | `split_valid_invalid` | | | |
| 6 | `read_csv_rows` | | | |
| 7 | `top_customers` | | | |
| 8 | `run_pipeline` | | | |

**Co mi całkowicie wypadło z głowy:**

**Co pamiętałem lepiej, niż się spodziewałem:**

---

## Mapa braków (wypełnia coach po review)

_Do uzupełnienia 16 lipca — na jej podstawie powstanie plan Fazy 1._
