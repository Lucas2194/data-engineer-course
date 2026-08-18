# R6 — Sortowanie i składanie funkcji

> ## ⚠️ To NIE jest powtórka
>
> Bloki R1–R5 odświeżały materiał, który już przerabiałeś w dniach 1–20.
> **R6 jest inny.** Sprawdziłem greppem całe repo przed napisaniem tej notatki:
>
> | Technika | Wystąpienia w dniach 1–20 |
> |----------|---------------------------|
> | `sorted()` | **0** |
> | `key=` | **0** |
> | `lambda` | **0** |
> | `reverse=True` | **0** |
> | `.sort()` | **0** |
> | wycinek `[:n]` | **0** |
>
> Widzisz to wszystko **pierwszy raz**. Jeśli pójdzie wolniej niż R5 — to nie jest
> regres, tylko normalna cena za nowy materiał. Nie interpretuj tego jako cofnięcia się.
>
> (Tło: przy R4 zdarzyło się to samo, tylko wyszło na jaw dopiero po fakcie. Zapisaliśmy
> wtedy regułę: *grep przed budową bloku*. To jest jej pierwsze zastosowanie.)

---

## Spis treści

1. [Po co sortowanie w danych](#1-po-co-sortowanie-w-danych)
2. [`sorted()` — podstawa](#2-sorted--podstawa)
3. [`sorted()` vs `.sort()` — dwie różne rzeczy](#3-sorted-vs-sort--dwie-różne-rzeczy)
4. [`reverse=True` — malejąco](#4-reversetrue--malejąco)
5. [`key=` — po czym właściwie sortujemy](#5-key--po-czym-właściwie-sortujemy)
6. [`lambda` — funkcja bez nazwy](#6-lambda--funkcja-bez-nazwy)
7. [Krotki — para w jednym pudełku](#7-krotki--para-w-jednym-pudełku)
8. [`.items()` — słownik jako lista par](#8-items--słownik-jako-lista-par)
9. [Dwa kryteria naraz — trik z minusem](#9-dwa-kryteria-naraz--trik-z-minusem)
10. [Wycinek `[:n]` — pierwsze n elementów](#10-wycinek-n--pierwsze-n-elementów)
11. [Stabilność sortowania](#11-stabilność-sortowania)
12. [Pułapki, które Cię ugryzą](#12-pułapki-które-cię-ugryzą)
13. [Demo — uruchom to najpierw](#13-demo--uruchom-to-najpierw)
14. [Część A — zadania z testami](#14-część-a--zadania-z-testami)
15. [Część B — projekt bez testów](#15-część-b--projekt-bez-testów)
16. [Wyniki](#16-wyniki)
17. [Słowniczek](#17-słowniczek)

---

## 1. Po co sortowanie w danych

Zapytaj dowolnego analityka, czego chce od danych, a padnie jedno z dwóch:
*„pokaż mi największych"* albo *„pokaż mi najnowsze"*. Jedno i drugie to sortowanie.

Praktycznie każdy raport, który w życiu zobaczysz, kończy się posortowaną listą:

- 10 klientów, którzy wydali najwięcej,
- produkty z największą liczbą zwrotów,
- najwolniejsze zapytania SQL,
- ostatnie 100 błędów z loga.

W SQL napiszesz na to `ORDER BY` i `LIMIT`. W Pythonie robisz dokładnie to samo,
tylko nazywa się `sorted()` i `[:n]`. Uczysz się teraz jednego pojęcia w dwóch
językach naraz — za dwa tygodnie zobaczysz je po stronie SQL i będzie znajome.

---

## 2. `sorted()` — podstawa

`sorted()` bierze cokolwiek, po czym da się przejść (listę, krotkę, klucze słownika)
i zwraca **nową, posortowaną listę**.

```python
liczby = [5, 1, 4, 2]
sorted(liczby)                  # [1, 2, 4, 5]

imiona = ["Piotr", "Anna", "Marek"]
sorted(imiona)                  # ['Anna', 'Marek', 'Piotr']
```

Teksty sortują się alfabetycznie, liczby rosnąco. To jest domyślne zachowanie i
w połowie przypadków wystarcza.

**Uwaga na polskie znaki i wielkie litery.** Python porównuje teksty po kodach znaków,
a nie po zasadach polskiego alfabetu:

```python
sorted(["ala", "Ala", "Ćma", "cma"])     # ['Ala', 'Ćma', 'ala', 'cma']
```

Wielkie litery mają niższe kody niż małe, więc idą pierwsze. `Ć` też ląduje nie tam,
gdzie oczekuje człowiek. Jeśli chcesz kolejność „ludzką", normalizujesz przed
sortowaniem (`.lower()`) — o tym w rozdziale 5.

---

## 3. `sorted()` vs `.sort()` — dwie różne rzeczy

To jest pierwsza pułapka i wraca regularnie.

```python
liczby = [5, 1, 4]

nowa = sorted(liczby)      # zwraca NOWA liste; `liczby` zostaje [5, 1, 4]
liczby.sort()              # zmienia `liczby` W MIEJSCU; zwraca None
```

| | co robi z oryginałem | co zwraca |
|---|---|---|
| `sorted(x)` | nie rusza | nową listę |
| `x.sort()` | sortuje w miejscu | **`None`** |

Rozpoznajesz ten wzorzec? To ta sama zasada, na którą wpadłeś w R5 przy `.mkdir()`:
**metoda, która coś zmienia, zwraca `None`.** `.sort()` należy do tej samej rodziny
co `.append()` i `.update()`.

```python
liczby = liczby.sort()     # ❌ liczby == None, dane zniknely
```

**W tym bloku używamy wyłącznie `sorted()`.** Powód jest zawodowy, nie estetyczny:
funkcja, która po cichu przestawia listę należącą do kogoś innego, jest funkcją,
której nikt nie chce wołać. Dostajesz dane → zwracasz nowe dane → wejście zostaje
nietknięte. To się nazywa *nie mieć efektów ubocznych* i jest jedną z tych rzeczy,
które odróżniają kod produkcyjny od skryptu.

`.sort()` ma sens, gdy lista jest Twoja własna, prywatna i duża (nie kopiujesz jej
w pamięci). Póki co: `sorted()`.

---

## 4. `reverse=True` — malejąco

```python
sorted([5, 1, 4])                  # [1, 4, 5]
sorted([5, 1, 4], reverse=True)    # [5, 4, 1]
```

Tyle. Jeden argument nazwany. Prawie każdy raport biznesowy chce `reverse=True`,
bo „top 10" oznacza od największego.

---

## 5. `key=` — po czym właściwie sortujemy

Tu zaczyna się prawdziwa robota.

Domyślnie `sorted()` porównuje **całe elementy**. Ale co, jeśli elementem jest słownik?

```python
orders = [
    {"customer_name": "Anna",  "total_amount": "150.00"},
    {"customer_name": "Piotr", "total_amount": "90.00"},
]
sorted(orders)      # ❌ TypeError: '<' not supported between instances of 'dict' and 'dict'
```

Python mówi wprost: *nie umiem porównać dwóch słowników*. I słusznie — po czym miałby
je porównywać? Po nazwie? Po kwocie? Po liczbie kluczy? Nie ma jak zgadnąć.

**`key=` to Twoja odpowiedź na to pytanie.** Podajesz funkcję, która z jednego elementu
wyciąga wartość do porównania.

```python
slowa = ["kot", "a", "abcd"]
sorted(slowa, key=len)             # ['a', 'kot', 'abcd']
```

Przeczytaj to dosłownie: *„posortuj `slowa`, a do porównywania używaj ich `len`"*.

Trzy rzeczy, które musisz tu zobaczyć:

1. **`len` bez nawiasów.** Nie wołasz `len()`. Przekazujesz **samą funkcję** — Python
   zawoła ją sobie, raz dla każdego elementu. `len` z nawiasami byłoby wywołaniem
   *teraz*, a Ty chcesz dać przepis *na później*.
   (Ta sama różnica, która ugryzła Cię w R5: `writer.writeheader` vs `writeheader()`.
   Tam nawiasów brakowało i nic się nie działo. Tu nawiasy byłyby błędem.)
2. **Wynik zawiera oryginalne elementy**, nie długości. `key=` decyduje o *kolejności*,
   nie o *zawartości*.
3. **Funkcja dostaje jeden element naraz** i ma zwrócić coś, co da się porównać.

Możesz podać dowolną funkcję, także własną:

```python
def kwota(order):
    return float(order["total_amount"])

sorted(orders, key=kwota)          # dziala
```

I to jest w pełni poprawne rozwiązanie. Ale dla trzyliterowej funkcji, używanej
w jednym miejscu, jest krótszy sposób.

---

## 6. `lambda` — funkcja bez nazwy

`lambda` to funkcja zapisana w jednej linii, bez nadawania jej nazwy.

```python
kwota = lambda order: float(order["total_amount"])
#       ^^^^^^ ^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#       slowo  argument       co zwraca
```

To jest **dokładnie to samo**, co:

```python
def kwota(order):
    return float(order["total_amount"])
```

Bez `return`, bez dwukropka po nawiasie, bez nazwy. Po `lambda` piszesz argumenty,
po dwukropku jedno wyrażenie — i to wyrażenie jest zwracane.

W praktyce nigdy nie przypisujesz jej do zmiennej (od tego jest `def`). Wsadzasz ją
prosto tam, gdzie jest potrzebna:

```python
sorted(orders, key=lambda order: float(order["total_amount"]))
```

Czytaj po polsku: *„posortuj orders, a do porównania weź z każdego zamówienia pole
total_amount zamienione na liczbę"*.

**Kiedy `lambda`, a kiedy `def`:**

| Sytuacja | Czego użyć |
|----------|------------|
| jedno wyrażenie, użyte raz, w miejscu | `lambda` |
| potrzebujesz `if`, pętli, kilku linii | `def` |
| ta sama logika w kilku miejscach | `def` (i nazwij ją!) |
| chcesz to przetestować osobno | `def` |

**`lambda` nie jest sposobem na sprytniejszy kod.** Jest sposobem na uniknięcie
nazywania czegoś, co nazwy nie potrzebuje. Jeśli Twoja `lambda` robi się dłuższa
niż linia — to znak, że powinna być `def`.

> ⚠️ **Pułapka konwersji.** W CSV wszystko jest tekstem. `sorted(rows, key=lambda r: r["total_amount"])`
> posortuje Ci **teksty**, czyli alfabetycznie: `"1000.00"` wyląduje przed `"90.00"`,
> bo znak `1` jest przed `9`. To jest cichy błąd — nic nie wybucha, tylko raport kłamie.
> Zawsze konwertuj wewnątrz `key=`.

---

## 7. Krotki — para w jednym pudełku

Krotka (*tuple*) to lista, której nie da się zmienić. Zapisujesz ją nawiasami okrągłymi
albo w ogóle bez nawiasów:

```python
para = ("Anna", 250.0)
para[0]        # 'Anna'
para[1]        # 250.0

para[0] = "X"  # ❌ TypeError: 'tuple' object does not support item assignment
```

Po co komu lista, której nie można zmienić? Bo krotka mówi coś innego niż lista:

- **lista** = „zbiór rzeczy tego samego rodzaju, może rosnąć" → `["Anna", "Piotr"]`
- **krotka** = „jedna rzecz złożona z kilku części, o stałym układzie" → `("Anna", 250.0)`

`("Anna", 250.0)` to nie są dwie rzeczy. To jest **jeden wynik**: klient i jego suma.
Pozycja ma znaczenie — na zerze zawsze nazwa, na jedynce zawsze kwota.

Krotki możesz rozpakować do osobnych zmiennych, i to jest bardzo czytelne:

```python
name, total = ("Anna", 250.0)
# name  == 'Anna'
# total == 250.0

for name, total in [("Anna", 250.0), ("Piotr", 120.0)]:
    print(f"{name}: {total:.2f} zl")
```

**Krotki porównują się po kolei, od lewej.** To będzie kluczowe w rozdziale 9:

```python
(1, "b") < (2, "a")      # True  - decyduje pierwszy element (1 < 2)
(1, "a") < (1, "b")      # True  - pierwsze rowne, wiec decyduje drugi
```

Najpierw sprawdzam pierwsze elementy. Remis? Dopiero wtedy patrzę na drugie. Dokładnie
tak, jak układa się nazwiska: najpierw litera, przy remisie następna.

---

## 8. `.items()` — słownik jako lista par

Znasz to z R4. Przypomnienie w jednej linii, bo za chwilę będzie potrzebne:

```python
totals = {"Anna": 250.0, "Piotr": 120.0}

list(totals.items())     # [('Anna', 250.0), ('Piotr', 120.0)]
```

`.items()` daje pary `(klucz, wartość)` — czyli **krotki**. I to jest most między
R4 a R6: agregacja produkuje słownik, a raport potrzebuje posortowanej listy.
`.items()` łączy jedno z drugim.

Ważne: **słownika nie sortujesz.** Zamieniasz go na listę par i sortujesz listę.

---

## 9. Dwa kryteria naraz — trik z minusem

To jest serce tego bloku. Przeczytaj wolno.

Zadanie brzmi: *posortuj klientów po sumie malejąco, a przy remisie alfabetycznie
po nazwie*.

Dwa kryteria, w **przeciwnych kierunkach**. Kwota malejąco, nazwa rosnąco. `reverse=True`
tu nie pomoże, bo odwraca **wszystko naraz** — dostałbyś nazwy od Z do A.

```python
totals = {"Anna": 250.0, "Zofia": 250.0, "Piotr": 250.0, "Marek": 120.0}
```

Rozwiązanie wykorzystuje to, czego nauczyłeś się w rozdziale 7: **krotki porównują się
po kolei**. Wystarczy, że `key=` zwróci krotkę:

```python
sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))
# [('Anna', 250.0), ('Piotr', 250.0), ('Zofia', 250.0), ('Marek', 120.0)]
```

Rozbierzmy to na części:

- `totals.items()` → lista par `("Anna", 250.0)`, `("Zofia", 250.0)`, …
- `pair` to jedna taka para. `pair[0]` to nazwa, `pair[1]` to suma.
- `key=` zwraca **krotkę dwuelementową**: `(-250.0, "Anna")`.
- Sortowanie jest rosnące. Ale kwota jest **ze znakiem minus**, więc największa suma
  daje najmniejszą liczbę i ląduje pierwsza. Odwróciliśmy kierunek dla jednego pola,
  nie ruszając drugiego.
- Gdy pierwsze elementy są równe (remis w kwocie), Python przechodzi do drugiego —
  czyli do nazwy, sortowanej normalnie, rosnąco.

**Dlaczego nie `reverse=True`:**

```python
sorted(totals.items(), key=lambda p: (p[1], p[0]), reverse=True)
# [('Zofia', 250.0), ('Piotr', 250.0), ('Anna', 250.0), ('Marek', 120.0)]
#   ^^^^^ Zofia przed Anna - alfabet tez sie odwrocil. ZLE.
```

Zapamiętaj regułę: **`reverse=True` obraca całą kolejność; minus obraca jedno pole.**
Gdy kryteria idą w tę samą stronę — `reverse=True`. Gdy w przeciwne — minus w krotce.

> ⚠️ **Minus działa tylko na liczbach.** `-"Anna"` to `TypeError`. Jeśli musisz odwrócić
> kolejność tekstów przy jednoczesnym rosnącym innym polu, minus odpada i robi się to
> inaczej (dwa przejścia sortowania — patrz rozdział 11). W tym bloku tego nie potrzebujesz,
> ale wiedz, że ograniczenie istnieje.

Czytelniejszy wariant tego samego, gdy para ma nazwy:

```python
sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))
```

Możesz też rozpakować argumenty w samej lambdzie — ale nie rób tego, dopóki nie
poczujesz się pewnie. `pair[0]` i `pair[1]` są w porządku i widać, co się dzieje.

---

## 10. Wycinek `[:n]` — pierwsze n elementów

```python
lista = ["a", "b", "c", "d", "e"]

lista[:3]      # ['a', 'b', 'c']   - pierwsze trzy
lista[2:]      # ['c', 'd', 'e']   - od trzeciego do konca
lista[1:3]     # ['b', 'c']        - od indeksu 1 do 3 (3 NIE wchodzi)
```

To się nazywa *slice* (wycinek). Do „top N" potrzebujesz tylko pierwszej formy.

**Najlepsza własność wycinka: nie wybucha.** Nawet gdy prosisz o więcej, niż jest:

```python
["a", "b"][:10]      # ['a', 'b']   - zadnego bledu, po prostu tyle, ile jest
[][:5]               # []
```

Dlatego `top_customers(orders, 10)` przy trzech klientach zwróci trzech i nie musisz
tego przypadku obsługiwać osobno. Porównaj z `lista[10]`, które przy dwóch elementach
wywala `IndexError`. **Wycinek jest bezpieczny, indeks nie.**

To ten sam rodzaj prezentu co `list(reader)` w R5 — przypadek brzegowy załatwia się sam,
jeśli użyjesz właściwego narzędzia.

---

## 11. Stabilność sortowania

Jedna własność, o której warto wiedzieć, bo tłumaczy, dlaczego pewne rzeczy działają.

Sortowanie w Pythonie jest **stabilne**: elementy, które są sobie równe według `key=`,
zachowują swoją **pierwotną kolejność względem siebie**.

```python
dane = [("b", 1), ("a", 1), ("c", 0)]
sorted(dane, key=lambda p: p[1])
# [('c', 0), ('b', 1), ('a', 1)]
#             ^^^^^^^^^^^^^^^^ 'b' przed 'a', bo tak bylo w wejsciu
```

Praktyczna konsekwencja: **kilka kryteriów można też zrobić kilkoma sortowaniami,
od najmniej do najważniejszego.**

```python
wynik = sorted(pary, key=lambda p: p[0])                    # najpierw wg nazwy
wynik = sorted(wynik, key=lambda p: p[1], reverse=True)     # potem wg kwoty
```

Efekt identyczny jak trik z minusem, i działa też dla tekstów. Trik z krotką jest
krótszy i jednoprzebiegowy, więc w tym bloku używamy jego — ale gdy trafisz na
przypadek, w którym minus nie zadziała, wiesz już, że masz drugą drogę.

---

## 12. Pułapki, które Cię ugryzą

| Pułapka | Co się dzieje | Jak uniknąć |
|---------|---------------|-------------|
| `lista = lista.sort()` | `lista` staje się `None` | używaj `sorted()` |
| `key=len()` zamiast `key=len` | `TypeError`, brak argumentu | przekazujesz funkcję, nie wynik |
| `sorted(orders)` na słownikach | `TypeError: '<' not supported` | zawsze `key=` przy słownikach |
| sortowanie kwot z CSV bez konwersji | `"1000"` przed `"90"`, **cicho** | `float()` wewnątrz `key=` |
| `reverse=True` przy dwóch kryteriach | odwraca też alfabet | minus w krotce |
| `-"Anna"` | `TypeError` | minus tylko na liczbach |
| `lista[n]` do wzięcia top N | `IndexError` przy krótkiej liście | wycinek `lista[:n]` |
| sortowanie słownika wprost | sortujesz same klucze, tracisz wartości | `.items()` najpierw |

---

## 13. Demo — uruchom to najpierw

**Zanim napiszesz jedną linię zadania**, uruchom demo i przeczytaj jego kod:

```
uv run python -m src.powtorka_06_sortowanie.demo
```

Demo pokazuje wszystkie techniki z tej notatki na prawdziwych danych z
`src/powtorka_06_sortowanie/data/orders.csv`. Niczego nie zapisuje na dysk.

Ta zasada obowiązuje od R1 i ani razu nie zawiodła: **kod, który przeczytałeś
i uruchomiłeś, pisze się dwa razy szybciej niż kod, który znasz tylko z opisu.**

---

## 14. Część A — zadania z testami

Plik: `src/powtorka_06_sortowanie/exercises.py` — pięć zadań.
Testy: `tests/test_powtorka_06.py`.

```
uv run pytest tests/test_powtorka_06.py::TestSortNames -v
```

Drabinka jest celowa — każde następne zadanie stoi na poprzednim:

| # | Funkcja | Czego uczy |
|---|---------|-----------|
| 1 | `sort_names` | goły `sorted()`, `reverse=`, „nowa lista" |
| 2 | `sort_by_length` | `key=` z gotową funkcją, bez `lambda` |
| 3 | `sort_orders_by_amount` | `key=lambda` + konwersja tekstu na liczbę |
| 4 | `sorted_totals` | `.items()` + krotka `(-kwota, nazwa)` ← **serce bloku** |
| 5 | `top_customers` | składanie 3+4 + wycinek ← **payoff diagnostyki #7** |

### Zasady (te same co zawsze)

- Demo przed zadaniami. Nie na odwrót.
- Jedna klasa testów naraz.
- Reguła 20 minut: zacinasz się dłużej → pytasz.
- Test to prawda. Gdy docstring i test się różnią — wierzysz testowi.
- **DRY**: #5 używa #3 i #4. Jeśli przepisujesz tam sortowanie od zera, robisz to źle.
- `except` łapie konkretny typ.
- Nazwy zmiennych po angielsku.
- **Ruff przed pytestem**: `uv run ruff check src/powtorka_06_sortowanie/exercises.py`.
  To jest darmowa runda — w R5 złapałby Ci 2 błędy z 5, zanim zobaczyłeś traceback.

---

## 15. Część B — projekt bez testów

**To jest nowość w formacie kursu i główne danie tego bloku.**

Pełna treść: [`src/powtorka_06_sortowanie/PROJEKT.md`](../src/powtorka_06_sortowanie/PROJEKT.md).

Dostajesz pusty plik i opis tego, co program ma robić. **Nie ma stubów. Nie ma testów.
Nie ma podanych sygnatur.** Sam decydujesz, jakie funkcje napisać, co mają przyjmować
i co zwracać.

Do części B siadasz **dopiero po zaliczeniu części A** — będziesz z niej korzystał.

Uprzedzam uczciwie: to będzie trudniejsze, niż wygląda, i nie z powodu materiału.
Materiał będzie ten sam. Trudność bierze się z tego, że pusty plik nie mówi Ci,
od czego zacząć — a tego jeszcze nie ćwiczyłeś ani razu. **To jest dokładnie ten mięsień,
który zatrzymał Cię w diagnostyce Dnia 21.**

---

## 16. Wyniki

Wypełniaj na bieżąco — to jest Twój ślad, ile naprawdę zajęło.

### Część A

| # | Funkcja | Testy | Czas | Gdzie się zaciąłem |
|---|---------|-------|------|--------------------|
| 1 | `sort_names` | / | | |
| 2 | `sort_by_length` | / | | |
| 3 | `sort_orders_by_amount` | / | | |
| 4 | `sorted_totals` | / | | |
| 5 | `top_customers` | / | | |

### Część B

| Etap | Zrobione | Czas | Uwagi |
|------|----------|------|-------|
| Wczytanie i podział danych | ☐ | | |
| Zapis dwóch plików CSV | ☐ | | |
| Raport tekstowy | ☐ | | |
| Podsumowanie na ekranie | ☐ | | |
| Liczby zgadzają się z tabelą kontrolną | ☐ | | |

---

## 17. Słowniczek

Dopisz do `notes/english/glossary.md`.

| EN | PL | W kodzie |
|----|----|----------|
| sort | sortować | `sorted(rows)` |
| sorted | posortowany | `sorted()` zwraca nową listę |
| key | klucz (tu: kryterium) | `key=len` |
| reverse | odwrotnie | `reverse=True` |
| ascending | rosnąco | domyślnie |
| descending | malejąco | `reverse=True` albo minus |
| tie | remis | ta sama wartość, decyduje drugie kryterium |
| tiebreaker | rozstrzygnięcie remisu | `(-total, name)` |
| tuple | krotka | `("Anna", 250.0)` |
| pair | para | `(klucz, wartość)` z `.items()` |
| unpack | rozpakować | `name, total = pair` |
| slice | wycinek | `lista[:10]` |
| top N | pierwsze N | `sorted(...)[:n]` |
| stable sort | sortowanie stabilne | równe elementy nie zmieniają kolejności |
| lambda | funkcja anonimowa | `lambda x: x["amount"]` |
| anonymous function | funkcja bez nazwy | to samo co `lambda` |
| in place | w miejscu | `.sort()` zmienia oryginał |
| side effect | efekt uboczny | funkcja zmienia coś poza sobą |
| aggregate | agregować | `{klient: suma}` |
| ranking | ranking | posortowana lista wyników |
| pipeline | potok przetwarzania | wczytaj → przetwórz → zapisz |
