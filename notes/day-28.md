# Agregacja

## Czym jest agregacja ? 

To operacja która łączy informacje z wielu wierszy w wynik 

Przykładowa dane: 

product_id      product_name            price
1               Keyboard                250
2               Notebook                20
3               Mouse                   120
4               Monitor                 700

Zwykłe zapytanie

```sql

SELECT price
FROM products;
```
zwarca cztery wiersze

price
250
20
120
700

Zapytanie agregujące:

```sql

SELECT SUM(price)
FROM products;

```

Zwraca jeden wiersz 

SUM(price)
1090

Cztery wejściowe zostały połączone w jedną sumę. 

Możemy zapisać ten proces

250, 20, 120, 700
\/
SUM(price)
\/
1090

## Agregacja nie oznacza grupowania 

Słowo "agregacja" i "grupowanie" są powiązane, ale nie znaczą dokładnie tego samego

Zapytanie : 

```sql

SELECT SUM(price)
FROM products;

```

Wykonuje agregację na wszystkich rekord jako jednyym zbiorze. 

Nie ma tutaj GROUP BY.

Dopiero przyszłe zapytania o ogólnym kształcie:

```sql

SELECT category, SUM(price)
FROM products
GROUP BY category;

```

Podzieliłoby produkty na osobne grupy.

Takie zapytania zostawimy sobie na później. 

## Zwykłe zapytanie a zapytanie agregujące. 

Zwykłe zapytanie 

```sql

SELECT product_name, price
FROM products
WHERE price > 100;
```
Kazdy pasujący produkt tworzy osobny wiersz wyniku.

Jeżeli pasuja trzy produkty, otrzymujemy trzy wiersze. 

Zapytanie agregujące 

```sql

SELECT COUNT(*)
FROM products
WHERE price > 100;
```
Wynik mówi, ile produktów spełnia warunek 

Jeżeli pasują trzy produky, otrzeymujemy : 

COUNT(*)
3 

To nadal jeden wiersz wyniku

Najważniejsza różnica 

Rodzaj zapytania                Co zwraca?
zwykłe                          osobne rekordy
agregujące bez GROUP BY         jeden wiersz podsumowania

# COUNT(*) - liczenie wszystkich wierszy 

Ogólny schemat 

```sql

SELECT COUNT(*)
FROM table_name;

-- szybki przykład

SELECT COUNT(*)
FROM products;
```
Wynik: 4 

Count(*) - liczy wiersze 

Gwiazdka w tym miejscu oznacza - > Policz każdy wiersz należący do analizowania zbioru 

Nie oznacza - Wyświetl wszystkie kolumny 

Znaczenie * zależy od miejsca

Zapis           Znaczenie
SELECT *        pokaż wszystkei kolumny 
COUNT(*)        policz wszystkie wiersze

## COUNT(*) zwraca jeden wiersz

Tabela może mieć : 

- 4 rekordy
- 12 rekordów
- milion rekordów 


Zapytanie : 

SELECT COUNT(*)
FROM table_name;

bez Group BY zwraca jeden wiersz zawierający liczbę. 

Przykład 

12 wierszy wejściowych
\/ 
COUNT(*)
\/
1 wiersz wyniku z wartością 12

Nie należy mylić : 

- wartości znajadującej się w wyniku
- liczby wierszy wyniku 

Dla COUNT(*) można otrzymać

wartość: 12
liczba wierszy w wyniku: 1 

## Alias przez AS

Domyślna nazwa kolumny : 

COUNT(*)

jest mało wygodna w raporcie. Możemy nadać alias

```sql

SELECT COUNT(*) AS product_count
FROM products;
```
Wynik : 

product_count
4 

`AS` nie zmienia nazwy kolumny w tabeli. Nadaję nazwę kolumnie wyniku konkretnego zapytania. 

Porównanie : 

Element                 Znaczenie
COUNT(*)                obliczenie
AS product_count        nazwa wyniku 

Należy uzywać aliasów zapisanych po angielsku, małymi literami i w stylu `snake_case`.

Dobre nazwy : 

- order_count
- total_revenue
- average_amount
- minimum_amount
- maximum_amount

## COUNT(*) razem z WHERE

Chcemy policzyć tylko drogie produkty: 

```sql

SELECT COUNT(*) AS expensive_product_count
FROM products
WHERE price > 200;
```
Kolejność logiczna

- FROM wskazuje dane wejściowe
- WHERE pozostawia pasujące wiersze
- COUNT(*) liczby pozostałe wiersze
- SELECT zwraca obliczony wynik 

Możemy to zapisać 

wszystkie rekordy 
\/
WHERE
\/
Pasujące rekordy 
\/
COUNT(*)
\/
Jedna liczba

Najważniejsza zasada

**WHERE filtrtuje wiersze przez agregacją** 

## COUNT(*) a COUNT(column_name)

Zobacz : 

```sql

SELECT COUNT(*)
FROM producst;

-- oraz : 

SELECT COUNT(price)
FROM products;

```

COUNT(*):
- liczy wszystkie wiersze

COUNT(price): 
- liczy tylko wiersze, w których price nie jest NULL.
Jeżeli każda cena ma wartość, oba wyniki są równe. 

Przykład: 

product_name                price
Keyboard                    250
Notebook                    Null
Mouse                       120

Wtedy:

COUNT(*) = 3
COUNT(price) = 2

W naszej tabeli orders kolumna total_amount nie zawiera NULL, więc: 

COUNT(*) = COUNT(total_amount) = 12 

Ta równość wynika z jakości obecnych danych. Nie jest uniwersalną metodą


## Czym jest null ? 

NULL oznacza brak wartości albo wartość nieznaną 

Nie jest tym samym co :

- liczba 0
- pusty tekset ''
- tekst 'NULL'
- wartość logiczna FALSE

Dzisiaj jeszczen ie będziemy dodawać ani modyfikować braków. Jednak podstawowa wiedza pomiędzy NULL a agregacjami 

Tabela zachowania : 

Funkcja             Co robi z NULL?

COUNT(*)            liczy wiersz
COUNT(column)       pomija brak w tej kolumnie
SUM(column)         pomija braki
AVG(column)         pomija braki
MIN(column)         pomija braki
MAX(column)         pomija braki

Do null wrócimy w lekcji poświęconej jakości danych 

## SUM() - suma wartości 

Ogólny schemat

```sql

SELECT SUM(numeric_column)
FROM table_name;

-- przykład 

SELEC SUM(price) AS total_price
FROM products;

```

Dla cen
250+20+120+700 = 1090 

Wynik wynosi: 

total_price
1090 

`SUM()` potrzebuje wyrażenie lub kolumny liczbowej.

Nie zapisuj 

SUM(*)

COUNT(*) - ma specjalną składnię. Nie oznacza to, że każda funkcja agregująca przyjjmuje gwiazdkę. 

## SUM() razem z WHERE 

Chcemy obliczyć sumęcen tylko produktów elektronicznych: 

SELECT SUM(price) AS electronics_total
FROM products
WHERE category = 'electronics';

SUM() nie sumuje najpierw całej tabeli

Najpierw WHERE pozostawia produkty z kategorii electronics, a następnei SUM() dodaje ich ceny. 

To oznacza 

FROM -> WHERE -> SUM 

Nie oznacza

SUM całej tabeli -> WHERE

Agregacja zawsze działa na zbiorze, który pozostał po filtrowaniu. 

## AVG() - średnia arytmetyczna

Ogólny schemat

```sql

SELECT AVG(numeric_column)
FROM table_name;

```

Przykład 

```sql

SELECT AVG(price) AS average_price
FROM products;

```

Dla czterech cen : 

(250 + 20 + 120 + 700) / 4 = 272.5

Wynik

average_price
272.5

AVG() oblicza średnią z wartości innych niż NULL.

Jeżeli jedna z czterech cen byłaby NULL, średnia zostałąby obliczona z tech znanych wartości, a nie z czterech rekordów. 

## ROUND () - czytelne wyświetlanie średniej.

Średnia może mieć wiele cyfr po przecinku

Przykład : 

```sql

SELECT AVG(price) AS average_price
FROM products;

```

Można otrzymać wynik podobny do : 217.35833333333333

Dla raportu często wystarczą dwa miejsca po przecinku

SQLite udostępnia funkcje ROUND():

```sql

SELECT ROUND(AVG(price), 2) AS average_price
FROM products;
```
Czytamy :

Oblicz średnią cenę, a następnie zaokrąglij wynik do dwóch miejsc po przecinku. 

Ważne : 

- AVG() - wykonuje agregację
- ROUND() - formatuje wartość liczbową wyniku
- zaokrąglenie nie zmienia danych w tabeli. 

W zadaniach używajmy ROUND(..., 2) - gdy polecenie tego wymaga. 

## MIN() - najmniejsza wartość 

Ogólny schemat

```sql

SELECT MIN(numeric_column)
FROM table_name;

-- Przykład

SELECT MIN(price) AS minimum_price
FROM products;

```

Wynik: 

minimum_price
20

MIN(price) odpowiada na pytanie - > Jaka jest najmniejsza cena? 

Nie odpowiada na - > Który produkt ma najmniejszą cenę? 

To dwie różne rzeczy 

## MAX() - największa wartość

Ogólny schemat. 
```sql
SELECT MAX(numeric_column)
FROM table_name;

-- przykład

SELECT MAX(price) AS maximum_price
FROM products;

```

Wynik

maximum_price
700

MAX(price) zwraca największa wartość kolumny

Nie zwraca automatycznie : 

- identyfikatora produktu 
- nazwy produku
- całego wiersza

## MAX() a ORDER BY .. LIMIT 1 

Mamy dwa pytania 

A - Jaka jest największa cena 

Właściwe narzędzie 

```sql

SELECT MAX(price) AS maximum_price
FROM products;

```

Wynik zawiera jedną wartość 

B - Który produkt jest najdroższy 

```sql

SELECT *
FROM products
ORDER BY price DESC, product_id ASC 
LIMIT 1;

```

Wynik zawiera cały rekord 

Mapa decyzji : 

Potrzeba                            Rozwiązanie 
tylko największa wartość            MAX(column)
cały rekord z największa wartością  ORDER BY ... DESC LIMIT 1

Później poznamy także inne rozwiązania, między innymi podzapytania i funkcje okienkowe. 

## Kilka agregacji w jednym SELECT 

Można obliczyć kilka statystyk jednocześnie : 

```sql

SELECT
    COUNT(*) AS product_count,
    SUM(price) AS total_price,
    ROUND(AVG(price), 2) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products;
```
Wynik nadal zawiera jeden wiersz : 

product_count       total_price     average_price       minimum_price       maximum_price
        4           1090            272.50              20                  700

Każde wyrażenie po SELECT tworzy jedną kolumnę wyniku.

Całe zapytanie 

Dla całego zbioru produktów policz liczbę rekordów, sumę cen, średnią cenę, najmniejszą cenę i najwięszką cene. 

## Formatowanie wieloelementowego SELEC

Zalecany zapis: 

```sql

SELECT
    COUNT(*) AS row_count,
    SUM(price) AS total_price,
    ROUND(AVG(price), 2) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products;

```

Każde wyrażenie znajduje się w osobnym wierszu. 

Przecinek zapisujemy po każdym wyrażeniu poza ostatnim. 

Błędnie

```sql

SELECT
    COUNT(*) AS row_count
    SUM(price) AS total_price
FROM products;

```

Między wyrażeniami brakuje przecinka. 

Czytelne formatowanie jest szczególnie ważne, gdy raport zawiera wiele metryk

## Where i kilka agregacji 

Przykład 

```sql

SELECT 
    COUNT(*) AS electronics_count,
    SUM(price) AS electronics_total,
    ROUND(AVG(price), 2) AS electronics_average,
    MIN(price) AS electronics_minimum,
    MAX(price) AS electronics_maximum
FROM proructs 
WHERE category = 'electronics';
```

Każda funkcja działa na tym samym przefiltrowanym zbiorze. 

Nie jest tak, że : 

- COUNT() - widzi inne rekordy
- SUM() - widzi inne rekordy 
- AVG() - widzi inne rekordy

Wspólny WHERE dotyczy całego zapytania

## Jedna grupa bez GROUP BY 

Zapytanie agregujące bez GROUP BY traktuje cały wynik po WHERE jako jedną grupę. 

Przykład : 

```sql

SELECT 
    COUNT(*) AS selected_count,
    SUM(price) AS selected_total
FROM products
WHERE category IN ('electronics', 'office');
```
Niezależnie od tego, czy po filtrze zostały : 

- 2 wiersze
- 20 wierszy
- 2000 wierszy

agregacja zwróci jeden wiersz podsumowania

Dopiero GROUP BY utworzy wiele grupy i potencjalnei wiele wierszy wyniku 

## Co siędzieje, Gdy WHERE nie znajduje rekordów ? 

Przykład

```sql

SELECT COUNT(*) AS product_count
FROM products
WHERE category = 'somethingnotexisting';

Jeżeli żaden rekord nie pasuje : 

product_count
0 

COUNT(*) zwraca 0 

-- Dla porównania : 

SELECT
    COUNT(*) AS product_count,
    SUM(price) AS total_price,
    AVG(price) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products
WHERE category = 'nonexistent';
```
Dla pustego zbioru SQLite zwraca: 

product_count       total_price     average_price       minimum_price       maximum_price
0                   NULL            NULL                NULL                NULL

Dlaczego?

- liczba rekordów wynosi zero
- nie istnieje suma znanych wartości w standardowym SUM()
- nie istnieje średnia
- nie istnieje najmniejsza wartość
- nie istnieje największa wartość

Nie należy myśleć, że NULL to 0 w swojje głowie. To różne informację. 

## Zapytanie agregujące nadal zwraca wiersz dla pustego wejścia

To subtelna, ale ważna zasada.

Zapytanie : 

```sql

SELECT COUNT(*) AS product_count
FROM products
WHERE category = 'nonexistent';
```

nie zwraca zera wierszy 

Zwraca

Jeden wiersz z wartością 0

Tak samo zapytanie z SUM() zwróci : 

Jeden wiersz z wartością NULL 

Agregcacja bez GROUP BY tworzy jeden wiersz podsumowania także wtedy, gdy WHERE nie pozostawił żadnego rekordu. 

## Nie należy mieszać zwykłej kolumny z agregacją

Zobacz :

```sql

SELECT product_name, MAX(price)
FROM products;

```

Na pierwszy rzut oka, może wyglądać jak pytanie : 

Pokaż nazwę najdrośżego produktu i jego cenę. 

Jest to niestety niebezpieczny sposób myślenia. 

MAX(price) agreguje wiele rekordów do jednej wartości, ale product_name jest zwykła kolumną. Nie wskazaliśmy standardowej reugił, z którego wiersza ma pochodzić nazwa. 

SQLite ma własne, szczególne zasady dotyczące takich "gołych kolumn". Inne silniki, na przykład PostgreSQL zwykle odrzuca podobne zapytanie, a w bardziej złożonych przypadkach SQLite może dobra wartość z arbitralnego wiersza. 

Na obecnym etapie, najlepiej sotosować zasadę 

W zapytaniu agregującym bez GROUP BY wybieramy wyłącznie agregację stałe albo wyrażenia oparte na agregacjach. 

Poprawne : 

```sql

SELECT MAX(price) AS maximum_price
FROM products;

```

Jeżeli potrzebujemy całego rekordu : 

```sql

SELECT product_id, product_name, price
FROM products
ORDER BY price DESC, produt_id ASC
LIMIT 1

```

## Dlaczego SQLite może ukryć błąd myślenia ? 

Niektóre silniki SQL zgłaszją błąd dla zapytania : 

```sql

SELECT product_name, COUNT(*)
FROM products;
```
SQLite może je wykonać. 

Nie oznacza to, że zapytanie dobrze odpowiada na pytanie biznesowe. 

Może zwrócić 

- prawidłową liczbę wszystkich produktów
- nazwę pochodzącą z jednego wybranego wiersza
Ta nazwa nie opisuje liczby wszystkich produktów.

To przykład ważnej zasady : 

**KOd może się wykonać i nadal być logicznie błędy**

Jako DE nie należy oceniać zapytania wyłącznie po braku komunikatu o błędzie 

## LIMIT nie ogranicza danych wejściowych agregacji 

Zobacz na : 

```sql

SELECT COUNT(*) AS product_count
FROM products
LIMIT 2;

```

COUNT(*) - najpierw tworzy jeden wiersz wyniku 

LIMIT 2 - może zwrócić maksymalnie dwa wiersze wyniku, ale dostępny jest tylko ejden wiersz agregacji

Nie oznacza to : 

Policz dwa peirwsze produkty 

Jeżeli tabela ma 1000 produktów, wynik nadal będzie wynosił 1000. 

Należy zapamiętać : 

- WHERE - ograniczna rekordy przed agregacją. 
- LIMIT - ograniczna gotowe wiersze wyniku 
- agregacja bez GROUP BY tworzy jeden wiesz wyniku 

Ograniczenie wejścia do pierwszych rekordów wymagałoby innej konsturkcji. Np.  - podzapytania - tego jeszcze nie używamy

## ORDER BY - przy jednym wirszu agregacji 

Zapytanie : 

```sql

SELECT MAX(price) AS maximum_price
FROM products
ORDER BY price DESC;

``` 

nie jest sposobem na znalezienie rekordu najdrośzego produktu. 

Agregacja bez GRIUP BY daje jeden wiersz. Sortowanie jednego wierszu niczego nie zmienia.

Jeżeli potrzebujemy 

- samej wartości maksymalnej -> MAX(price)
- całego rekordu -> ORDER BY price DEC LIMIT 1 
Najpierw najlepiej nazwać oczekiwany kształt wyniku

## Dzisiejsze zapytania 

Podstawowy szkielet 

```sql

SELECT aggregate_expression AS alias
FROM table_name
WHERE condition

-- Przykład

SELECT
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS average_price
FROM products
WHERE category IN ('electronics', 'office');

```

Kolejnośc zapisu:

SELECT -> FROM -> WHERE

Kolejnośc logicznego myślenia

FROM -> WHERE -> agregacja -> wynik SELECT

## Agregacja i typ wyniku 

Funkcje mogą zwracać różne typy wartości 

W Uproszczeniu 

Funkcja             Typowy wynik
COUNT(*)            liczba całkowita
SUM(integer_column) zwykle liczba całkowita
SUM(real_column)    liczba zmiennoprzecinkowa
AVG(...)            liczba zmiennoprzecinkowa
MIN(...)            typ porównywanych wartości
MAX(...)            typ porównywanych wartości

W orders kolumna total_amount jest typu REAL dlatego : 

- suma jets liczbą zmiennoprzecinkową
- srednia jest liczbą zmiennoprzecinkową
- minimum i maksimum moga być pokazane z .0 

Na przykłąd 

55.0
520.0

To nie zmienia ich znaczenia biznesowego

## Kwoty i precyzja 

W orders.csv używamy kwot zmiennoprzecinkowych, aby zachować prostę kursu. 

Liczby zmiennoprzecinkowe są przybliżeniem. W większych systemach finansowych kwoty często przechowuje się : 

- jako liczbą całkowitą w najmniejszej jednostce, na przykład groszach
- albo jako typ dziesiętny udostpęniany prze zkonkretną bazę danych. 
Nie bedziemy dzisiaj przebudowywać danych

Na razie : 

- używamy istniejącego REAL 
- kontroluj wyniki 
- do prezentacji można użyć ROUND(..., 2),
- pamiętamy, że zaokrąglenie wyniku nie naprawia sposobu przechowywania danych 

## Agregacja SQL a wcześniejsza agregacja w Pythonie.

w Pythonie zapisywaliśmy 

```py

total = 0
for order in orders:
    total += order["total_amount"]

```

w SQL silnik wykonuje iterację i obliczenie za Ciebie 

```sql

SELECT SUM(total_amount) AS total_amount
FROM orders;

```

Pytanie biznesowe podobne 

Jaka jest łączna wartość zamówień ?

Różni się miejsca wykonanai

Narzędzie               Gzdie odbywa się obliczenie ? 
Python                  w programie Python
Pandas                  w DF w procesie Pythona
SQL                     w silniku bazy danych

## Kontrola wyniku przez niezależne zależności : 

DE powineien nie tylko otrzymać wynik, ale także sprawdzić czy jest wiarygodny. 

Dla statusów w naszych danych : 

paid: 7
pending: 3 
calcelled: 2

Kontrola iczby :

7 + 3 + 2 = 12 

Jeżeli suma osobnych liczników nie zgadzałaby się z COUNT(*) powinniśmy sprwadzić : 

- czy istnieją inne statusu 
- czy wystepuje NULL
- czy warunki sa kompletne
- czy dane nie zostały zdublowane 

Podobnie można kontrolować sumy 

suma paid 
+ suma pending
+ suma cancelled
= suma wszystkich zamówień 

Takie uzgodnienie wyników często nazywa się kontrolą zgodności albo rekosyliacją


