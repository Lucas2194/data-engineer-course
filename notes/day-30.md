# GROUP BY SQL 
## Przypomnienie agregacji bez Group By

Zapytanie

```sql

SELECT COUNT(*) AS order_count
FROM orders;

```

Traktuje wszystkie 12 rekordów jako jeden zbiór. 

Można sobie to wyobrazić tak : 

12 rekordów 
\/
jedna grupa obejmująca całą tabelę 
\/
COUNT(*)
\/
1 wiersz wyniku z wartością 12 

Agregacja bez GROUP BY zwraca jeden wiersz podsumowania 

## Co robi Group BY

GROUP BY dzieli rekordy na zbiory, w których wybrana wartość jest taka sama. 

Przykładowa tabela products : 

product_id          category                        price
1                   accessories                     250
2                   office                          20
3                   accessories                     120
4                   screens                         700
5                   accessories                     50
6                   office                          400

Po grupowaniu według category powstają trzy grupy : 

accessories -> rekordy 1,3,5
office -> rekordy 2,6
screens -> rekordy 4

Każda grupa zmoże zostać osobno policzona, zsmuowana albo uśredniona. 

## Podstawowa składnai GROUP BY

Ogólny schemat 

```sql

SELECT
    group_column,
    AGGREGATE_FUNCTION(value_column) AS result_alias
FROM table_name
GROUP BY group_column;

-- Przykład na tabeli products : 

SELECT 
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category;

```

Wynik

category                product_count
accessories             3
office                  2
screens                 1

Szcześć rekordów wejściowych utworzyło trzy grupy, dlatego wynik zawiera trzy wiersze. 

## Jeden wiersz wyniku na jedną grupę

Najważniejsza zasada dzisiaj : 

Każda grupa utworzona przez GROUP BY daje jeden wiersz wyniku. 

Jeżeli tabela zawiera : 

- 12 rekordów
- 3 różne statusy 

to

GROUP BY status

utworzy trzy grupy i zwykle zwróci trzy wiersze.

Nie liczymy więc liczby rekordów zródłowych, tylko liczbę różnych wartości albo kombinacji użytych do grupowania. 

## Kolumna grupująca w SELECT 

W raporcie chcemy wiedzieć nei tylko, ile rekordów ma grupa, ale także która grupa jest opisywana.

Dlatego wybieramy

```sql

SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category;

```

`category` mówi, której grupy dotyczy licznik.

Bez tej kolumny : 

```sql

SELECT COUNT(*) AS product_count
FROM products
GROUP BY category;
```
Otrzymymamy 3 liczby, ale wynik nie będzie jasno wskazywał, do której kategorii należy każda z nich. 

Zapytanie może być poprawne składniowo i jednocześnie mało użyteczne

## Reguła kolumn w SELECT

W zapytaniu grupującym wybieramy : 

1. kolumny wymienione w GROUP BY
2. funkcje agregujące
3. stałe albo wyrażenia oparte na powyższych elementach 

Poprawny wzorzec : 

```sql

SELECT
    category,
    COUNT(*) AS product_count,
    SUM(price) AS total_price
FROM products
GROUP BY category;

-- Niebezpieczny wzorzec 

SELECT 
    category,
    product_id,
    SUM(price) AS total_price
FROM products
GROUP BY category;
```
`product_id`:

1. Nie jest funkcją agregująca 
2. Nie znajduje się w GROUP BY 
3. może mieć kilka różnych wartości wewnątrz jednej grupy 

Nie wiadomo więc, który product_id ma reprezentować całą kategorię.

## Pułapka SQLite : goła kolumna 

Kolumna znajdująca się w `SELECT`, ale niebędąca: 

- częścią GROUP BY 
- argumentem funkcji agregującej, 

jest często nazywaną gołą kolumną, po angielsku bare column. 

SQLite może wykonać takie zapytanie i wybrać wartość z jednego z rekordów grupy.
To nie oznacza, że wynik ma poprawne znaczenie biznesowe. 

Inne systemy baz danych, często odrzucą takie zapytanie błędem. 

Przyjmujemy przenośna zasadę : 

**Każda zwykła kolumna z SELECT powinna znajdować się w GROUP BY**

Nie wykorzystujemy specjalnego zachowania SQLite dla MIN() i MAX()

## COUNT(*) w każdej grupie

Przykład

```sql
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category;
```
COUNT(*) nie liczy już całej tabeli naraz. Liczy rekordy osobno wewnątrz każdej grupy. 

Można to zapisać tak : 

- accessories -> COUNT(*) = 3
- office -> COUNT(*) = 2
- screens -> COUNT(*) = 1 

Suma liczników wszystkich rozłączonych grup powinna dać liczbę rekordów wejściowych
3+2+1 = 6

To pierwsza kontrola zgodności raportu grupowego.

## SUM(), AVG(), MIN() i MAX() w grupach

Można obliczyć kilka miar dla każdej grupy : 
```sql
SELECT
    category,
    COUNT(*) AS product_count,
    SUM(price) AS total_price,
    ROUND(AVG(price), 2) AS average_price,
    MIN(price) AS minimum price,
    MAX(price) AS maximum_price
FROM products
GROUP BY category;
```

Każda funkcja widzi tylko rekordy należąco do aktualnej grupy.

Dla accessories funkcje pracują na : 

250, 120, 50.

Dla office dla 

20, 400 

Nie miesza się wartości między grupami. 

## Aliasy w raporcie grupowym 

Bez aliasów nagłowki mogą wyglądać tak : 

COUNT(*)
ROUND(AVG(price), 2)

Czytelniejsza są : 

COUNT(*) AS product_count
ROUND(AVG(price), 2) AS average_price

Alias opisuje znaczenie kolumny wyniku. Nie zmienia tabeli ani nazwy kolumny źródłowej. 

## GROUP BY nie gwarantuje kolejości

Zapytanie 

```sql

SELECT 
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category;

```

Nie gwarantuje kolejność grup.

SQLite może pozornie zwracać je alfabetycznie, ale nie wolno na tym polegać. 

Jeżeli kolejność jest cześcią wymagania, należy dodać ORDER BY

```sql

SELECT 
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY category ASC;

```

## Sortowanie według agregacji 

Możemy ułożyć grupy od największej do najmniejszej. 

```sql

SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC, category ASC;

```

Najpierw sortujemy po liczniku malejąco. Nazwa kategorii rozstrzyga remis.

W SQLite możemy używać aliasu product_count w ORDER BY

## Where działa przed GROUP BY

Przykładowe zapytanie : 

Ile produktów kosztujących co najmniej 100 znajduje się w każdej kategorii? 

```sql
SELECT
    category,
    COUNT(*) AS product_count
FROM products
WHERE price >= 100
GROUP BY category
ORDER BY product_count DESC, category ASC;
```

Proces 

FROM products
\/
WHERE price >= 100
\/
pozostając pasujące rekrody
\/
Group BY category
\/
COUNT(*) osobno w każdej grupie

WHERE usuwa rekordy, zanim grupy powstaną. 

## WHERE nie filtruje gotowych grup 

WHERE odpowiada na pytania dotyczące pojedyńczych rekordów : 

- kwota zamówień wynosi co najmniej 100
- miasto to Gdańsk
- status należy do wybranej listy

Nie używamy WHERE do warunków dotyczących gotowej agregacji : 

- grupa ma więcej niż dwa rekody
- suma grupy przekracza 500
- średnia grupy jest większa niż 200. 

Do filtrowania gotowyc grupy służy HAVING, ale jego składnie poznamy następnym razem.

Na dzisiaj : 

WHERE -> filtruje rekordy przed grupowaniem
HAVING -> będzie filtrować grupy po agregacji 

## Grupowanie po dwóch kolumnach

Można utworzyć grupę według kombinacji dwóch wartości : 

```sql

SELECT
    category,
    suppiler,
    COUNT(*) AS product_count
FROM products
GROUP BY category, suppiler
ORDER BY category ASC, suppiler ASC;
```

Grupą nie jest już sama kategoria. Grupą jest teraz para 
(category, suppiler)
Przykładowe grupy : 

(accessories, A)
(accessories, B)
(office, A)
(screens, C)

## GroupBY po dwóch kolumnach nie tworzy wszystkich możliwości 

SQL zwraca tylko kombinacje rzeczywiście występujące w danych. 

Jeżeli nie istnieje rekord

(screens, A)

to taka grupa nei pojawi się automatycznie z licznikiem zero. 

GROUP BY nie tworzy pełnej tabeli wszystkicih możliwych kombinacji.

To bedzie ważne podczas pracy z arportami, w któych brak wiersza i licznik równy zero mogą oznacząć coś innego. 

## Wszystkie zwykły kolumny grupujące umieść w GROUP BY

Poprawny wzorzec

```sql

SELECT
    category,
    suppiler,
    COUNT(*) AS product_count
FROM products
GROUP BY category, suppiler;

-- Jeżeli wybieramy category i suppiler obie kolumny powinny znaleźć się w GROUP BY
-- Niepoprawnie logicznie 

SELECT 
    category,
    suppiler,
    COUNT(*) AS product_count
FROM products
GROUP BY category;
```
W jeden kategorii może występować wielu dostawców. Nie wiadomo którego pokazać. 

## LIMIT po GROUP BY ograniczna grupy 

Przykład : 

SELECT 
    category,
    SUM(price) AS total_price
FROM products
GROUP BY category
ORDER BY total_price DESC, category ASC
LIMIT 2;

Proces

1. utwórz grupy
2. oblicz sumę każdej grupy
3. posortuj gotowe grupy 
4. zwróć dwie pierwsze grupy

Limit 2 nie oznacza, że agregacja zobaczyła tylko dwa produkty 

## GROUP BY bez agregacji 

ZAPYTANIE: 

SELECT category
FROM products
GROUP BY category;

może zwrócić jedną wartość dla każdej kategorii. Jeżeli celem jest wyłączenie usunięcie powtórzeń, czytelniejszym narzędziem jest zwykle DISTINCT 

Dzisiaj używamy GROUP BY do raportów z agregacjami.

## Grupowanie wartości NULL 

Jeżeli kolumna grupująca zawiera kilka wartości NULL, SQLite traktuje je na potrzebny grupowania jako należące do jednej grupy.

W aktualnym orders.csv nie ma NULL, więc nie zobaczymy takiej grupy.

Nie zmieniamy jednak danych, żeby ją stworzyć. Wystarcyz zapamiętać zasadę. 

## Tekst musi być ustandaryzowany 

Wartości : 

paid
Paid
PAID

mogą utworzyć osobne grrupy, jeżeli porównywanie tekstu rozróżnia wielkości liter.

Podobne problemy powowdują : 

- spacje na końcu
- literówki
- różne skróty
- polskie znaki zapisane na różne sposoby 

GROUP BY nie naprawia jakości danych. Grupuje dokładnie wartości, które znajdują się w tabelii

## Grupowanie po nazwie nie zawsze identyfikuje osobą.

W naszej małej tabeli grupowanie po customer_name jest wygodne.

W prawdziwym systemie dwóch klientów może mieć identyczne imię. Wtedy grupowanie po samej nazwie połączy ich w jedną osobę. 

Profesjonalnie grupowalibyśmy po stabilnym identyfikatorze : customer_id

nazwę można później dołączyć z tabeli klientów. JOIN poznamy w następnych lekcjach. 

W dzisiejszych danych nie ma customer_id, dlatego świadomie ćwiczmy na customer_name

## Kolejność zapisu klauzul 

Zapytanie zapisujemy w kolejności:

SELECT 
FROM
WHERE
GROUP BY
ORDER BY
LIMIT ;

Nie można umieścić WHERE po GROUP BY

## Logiczna kolejność działania 

Uproszczony model wykonania 

FROM
\/
WHERE
\/
GROUP BY
\/
agregacje dla każdej grupy
\/
SELECT
\/
ORDER BY
\/
LIMIT

To wyjaśnia 

- dlaczego WHERE działa przed agreacją 
- dlaczego LIMIT nie ogranicza rekordó wejściowcy
- dlaczego sortujesz gotowe wiersze grupy. 

# GROUP BY a poprzednie lekcje

Pytanie                                         Narzędzie
Ile jest wszystkich zamówień?                   COUNT(*) bez GROUP BY
Ile zamówień ma każdy status?                   GROUP BY status + COUNT(*)
Pokaż wszystkie zamóienia paid                  zwykły SELECT + WHERE
Jaka jest suma paid?                            SUM() + WHERE
Pokaż najdroższy cały rekord                    ORDER BY ... DESC LIMIT 1 
Jaka jest maksymalna kwota w każdej grupie?     GROUP BY + MAX()


