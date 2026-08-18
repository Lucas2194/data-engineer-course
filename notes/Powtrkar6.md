## Po co sortowanie w danych. 

Gdy zapytamy dowolnego analityka, czego chce od danych, to najczęściej padnie jedno z dwóch : * pokaż mi największe * albo * pokaż mi najnowsze * , jedno i drugie ma być posortowane. 

Praktycznie każdy raport, który w życiu zobaczę, kończy się na posortowanej liście. 

- 10 klientów którzy wydali najwięcej,
- produkty z największą liczbą zwrotów
- najwolniejsze zapytania SQL
- ostatnie 100 błędów z loga

w SQL napiszę `ORDER BY` i `LIMIT`. W Pythonie robisz dokładnie to samo, tylko nazywa się `sorted()` i `[:n]`. 

---

## `sorted()` - podstawa 

`sorted()` - bierze cokolwiek, po czym da się przejść (listę, krotkę, klucze słownika) i zwraca **nową, posortowaną listę**

```python
liczby = [5,1,4,2]
sorted(liczby)

imiona = ["Piotr", "Anna", "Marek"]
sorted(imiona)
```

Teksty sortują się alfabetycznie, liczby rosnąco. To jest domyślne zachowanie i w połowie przypadków wystarcza. 

**Uwaga na polskie znaki i Wielkie litery** - Python porównuje teksty po kodach znaków, a nie po zasadach polskiego alfabetu - > Duże litery będą przed małymi - > , mamy A , C, Z, a, z - > Po srotwaniu będzie A, C, Z, a, z

## `sorted()` vs `.sort()` - dwie różne rzeczy 

To jest pierwsza pułapka i wraca on regularnie. 

```python

liczby = [5,1,4]
nowa = soretd(liczby) # zwraca NOWĄ listę: lista `liczby` zostaje [5,1,4]
liczby.sort() # zmienia liczby w 'miejscu' ; zwraca None
```

Czyli nie można zrobić czegoś takiego 

```python
liczby = liczby.sort()
```

Ponieważ dane znikną, gdyż .sort() zmienia funkcję "w miejscu". 

**Najpowszechniej będziemy używać `sorted()`** - Powód jest zawodowy, nie estetyczny : funkcja, która po cichu przestawia listę należącą do kogoś innego, jest funkcją, której nikt nie chce wołać. 
Dostaje dane - zwracam nowe dane - wejście zostaje nietknietę. 
To się nazywa, * nie mieć efektów ubocznych * i jest jedną z tych r zeczy, która odróźniają kod produkcyjny od skryptu. 

`sort()` ma sens, gdy lista jest moja własna, prywatna i duża ( nie kopiujesz jej w pamięci). Póki co będziemy używać `sorted()`

---

## `reverse = True` - malejąco 

```python
sorted([5,1,4]) # [1,4,5]
sorted([5,1,4], reverse=True) # [5,4,1]
```

Czyli zmieniamy kolejność. 

---

## `key=` - po czym właściwie sortujemy

Tu zaczyna się prawdziwa robota

Domyślnie `sorted()` porównuje **całe elementy**. Ale co, jeśli elementem jest słownik? 

```python
orders = [
    {"customer_name": "Anna",  "total_amount": "150.00"},
    {"customer_name": "Piotr", "total_amount": "90.00"},
]
sorted(orders) # TypeError 
```

Python mówi wprost: *nie umiem porównać dwóch słowników*. I słuszanie - po czym miałby je porównywać. Po nazwie, kwocie? Po liczbie kluczy? Nie ma jak zgadnąć?

**`key=` - To odpowiedź na pytanie:** - Podajesz funkcję, która z jednego elementu wyciąga wartość do porównania 

```python
slowa = ["kot", "a", "abcd"]
sorted(slowa, key=len) # ['a', 'kot', 'abcd']
```

Czytam to dosłownie *posortuje `slowa`, a do porównania użyj ich `len`*

Trzy ważne rzeczy : 

1. **`len`** - nie wywołuje funkcji `len()`. Przekazuje samą funkcję - Python sam ją sobię wywoała. Raz dla każdego elementu.
2. **Wynik zawiera oryginalne elementy** - nie długości. `key=`, decyduje o *kolejności* a nie o zawartości
3. **Funkcja dostaje jeden element naraz** - i ma zwrócić coś, co się da porównać. 

Można podać dowolną funkcję, także własną. 

```python
def kwota(order):
    return float(order["total_amount"])

sorted(orders, key=kwota)     # działa
```

I to jest w pełni poprawne rozwiązanie. Ale dla trzyliterowej funkcji, używanej w jednym miejscu jest krótszy sposób. 

---

## 6. `lambda` - funkcja bez nazwy

`lambda` to funkcja zapisana w jednej linii, bez nadawania jej nazwy

```python
kwota = lambda order: float(order["total_amount"])
```

To jest **dokładnie to samo** co:

```python
def kwota(order):
    return float(order["total_amount"])
```

Bez `return`, bez dwukropka po nawiasie, bez nazwy. Po `lambda` piszemy argumenty, po dwykropku jedno wyrażenie - i to wyrażenie jest zwracane.

W praktyce, nigdy nie przpisuje jej do zmiennej (od tego jest `def`). Wsadzamy jąprosta tam, gdzie jest potrzebna:

```python
sorted(orders, key=lambda order: float(order["total_amount"]))
```

Czyli po polsku - > *posortuj orders, a do porównania weź z każdego zamówienia pole total_amount zamienione na liczbę"*

**Kiedy `lambda`, a kiedy `def`:**

Sytuacja                             | Czego użyć
Jedno wyrażenie użyte raz, w miejscu | `lambda` 
potrzebujesz if, pętli, kilku linii  | `def` 
ta sama logika w kilku miejsach      | `def` 
chce to przetestowaćosobno           | `def`  

**`lambda` nie jest sposobem na sprytniejszy kod **. Jest sposobem na uniknięcie nazywania czegoś, co nazwy nie potrzebuje. Jeśli lambda robi się dłuższa niż jedna linia - to znak że powinna być funkcja `def`. 

**Pułapka konwersji** - w CSV wszystko jest tekstem. `sorted(rows, key = lambda r: r["total_amount"])`
> posortuje Ci **teksty** czyli alfabetycznie : `"1000.00"` wyląduje przed `"90.00"`,
> bo znak `1` jest przed `9`. To jest cichy błąd, nic nie wywala programu, tylko raport kłamie. 
> Zawsze nalezy konwertować wewnątrz `key=`

---

## Krotki - para w jednym pudełku 

Krotka (*tuple*) - to lista, któej nie da się zmienić. Zapisujemy ją nawiasami okrągłymi albo w ogólnie bez nawiasów:

```python

para = ("Anna", 250.0)
para[0] # "Annaa"
para[1] # 250.0

para[0] = "X" # TypeError : 'tyle' object does not support item assignment
```

Na co komu lista, której nie da się zmienić? Bo tupla mówi coś innego niż lista:

- **lista** - zbiór rzeczy tego samego rodzaju, może rosnąć - > `["Anna", "Piotr"]` 
- **tupla** - jedna rzecz złożona z kilku części, o stałym układzie -> `("Anna", 250.0)` 
  
`("Anna", 250.0)` to nie są dwie rzeczy. To jest **jeden wynik**: klient i jego suma. 
Pozycja ma znaczenie - na zerze zawsze nazwa, na jedynce zawsze tupla. 

Tuple można rozpakować do osobnych zmiennych i to jest bardzo czytelne:

```python
name, total = ("Anna", 250.0)

for name, total in [("Anna", 250.0), ("Piotr", 120.0)]:
    print(f"{name}: {total:.2f} zl")
```

**Tuple porównują sie po kolei, od lewej**

```python
(1, "b") < (2, "a") # True - decyduje pierwszy element (1 < 2)
(1, "a") < (1, "b") # True - pierwsze równe, więc decyduje drugi 
```

Najpierw sprawdzamy pierwszy element. Remis? Dopiero wtedy patrzymy na drugi element. Dokładnie tak, jak układa się nazwiska: najpierw litera, przy remisie następna. 

---

## `.items()` - słownik jako lista par

```python
totals = {"Anna": 250.0, "Piotr": 120.0}

list(total.items()) # [('Anna', 250.0), ('Piotr', 120.0)]
```

`.items()` - daje pary `(klucz, wartość)` - czyli tuple. I to jest most między r4 a r6: agregacja produkuje słwonik, a raport potrzebuje posortowanej listy.c
`.items()` - łączy jedno z drugim.

Ważne ** słownika nie sortujesz ** - Zamieniam go na listę par i sortuje listę. 

## Dwa kryteria naraz - trik z minusem 

To jest serce tego bloku. 

Zadanie brzmi *posortuj klientów po sumie malejąco, a przy remisie alfabetycznie po nazwie* 

Dwa kryteria w przeciwnych kierunkach. Kwota malejąco, nazwa rosnąco. `reverse=True` - tu nie pomoże, bo odwraca **wszystko naraz** - dostałbym nazwy od Z do A. 

```python
totals = {"Anna":250, "Zofia":250.0, "Piotr", 250.0, "Marek":120.0}
```

Rozwiązanie wykorzystuje to, co było w rozdziale 7: Krotki porównuje się pokolei. Wystarczy że `key=` zwróci krotkę:

```python
sorted(total.items(), key=lambda pair: (-pair[1], pair[0]))
# [('Anna', 250.0), ('Piotr', 250.0), ('Zofia', 250.0), ('Marek', 120.0)]
```

Rozbierzmy to na części:

- `total.items()` -> lista par `("Anna", 250.0)`, `("Zofia", 250.0)`, ... 
- `pair` to jedna taka para. `pair[0]` to nazwa, `pair[1]` to suma.
- `key=` zwraca krotkę **dwuelementową**: `(-250, "Anna")`.
- Sortowanie jest rosnące. Ale kwota jest z **znakiem minus**, więc najwieksza suma daje najmniejszą liczbę i ląduje pierwsza. Odwróciliśmy kierunek dla jednego pola, nie ruszając drugiego. 
- Gdy pierwsze elementy są równe (remis w kwocie), Python przechodzi do drugiego, czyli do nazwy, sortowanej normalnie, rosnąco. 

**Dlaczego bez `reverse = True`:**

```python
sorted(total.items(), key=lambda p: (p[1], p[0]), reverse=True)
# [('Zofia', 250.0), ('Piotr', 250.0), ('Anna', 250.0), ('Marek', 120.0)]
#   ^^^^^ Zofia przed Anna - alfabet tez sie odwrocil. ZLE.
```

Należy zapamiętać reugłę **`reverse=True` obraca całą kolejność; minus obraca jedno pole**. Gdy kryteria idą w tę samą stronę - `reverse=True`. Gdy przeciwnie - minus w krotce 

>> **Minus działa tylko na liczbach** `-"anna"` to `TypeError`. Jeśli trzeba odwrócić kolejność tekstów, przy jednoczesnym rosnącym innym polu, to minus odpadai robi się to inaczej. Ważne żeby wiedzeić, że ograniczenia istnieje. 

Czytelniejszy wariant tego samego, gdy para ma nzwy:

```python
sorted(totals.items(), key=lambda pair(-pair[1]. pair[0]))
```

Można też rozpakować argumenty w samej lambdzie, ale lepiej tego nie robić, dopóki nie poczuje się człowiek pewnie. 

## 10. Wycinek `[:n]` - pierwsze n elementów

```python

lista = ["a", "b", "c", "d", "e"]
lista[:3] # a,b,c - > pierwsze 3
lista[2:] # c, d, e -> od trzeciego do końca
lista[1:3] # b,c - od indeksu 1 do 3 ( 3 nie wchodzi ! )

```

To się nazywa *slice* (wycinek). 
**Najlepszą własnością wycinka: nie wywala programu** - Nawet gdy proszę o więcej, niż jest: 

```python
["a", "b"][:10] # a,b - zadnego błędu, po prostu tyle ile jest
[][:5] # [] 

```

Dlatego `top_customers(orders, 10)` przy trzech klientach zwróci trzech i nie trzeba obsługiwać przypadku osobno. Przy liscie lista[10], założmy że ma dwa elementy to wywala `IndexError`. 

## Stailność sortowania 

Jedna własność o której warto wiedzieć, bo tłumaczy dlaczego pewne rzeczy działają. 

Sortowanie w Pythonie jest **stabilne**: elementy, które są sobie równe według `key=`, zachowują pierwotną kolejność względem siebie. 

```python
dane = [("b", 1), ("a", 1), ("c", 0)]
sorted(dane, key=lambda p: p[1])
# [('c', 0), ('b', 1), ('a', 1)]
#             ^^^^^^^^^^^^^^^^ 'b' przed 'a', bo tak bylo w wejsciu

```

Praktyczna konsekwencja: **kilka kryterów można też zrobić kilkoma sortowaniami, od najmniej do najważniejszego** 

```python
wynik = sorted(pary, key=lambda p: p[0]) # najpierw według nazwy
wynik = sorted(wynik, key=lambda p: p[1], reverse=True) # potem wg kwoty
```

Efekt identyczny jak trik z minusem, i działa też dla tekstów. Trik z krotką jest krótszy i jednoprzebiegowy, więc w tym bloku używamy jego - ale gdy trafi się na przypadek, w którym minus nie działa, jest inna droga. 

---

