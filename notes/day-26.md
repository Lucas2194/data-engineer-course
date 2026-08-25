# SQL kontynuacja 

## Co już wiemy na temat SQL 

Zapytanie 

```sql

SELECT order_id, customer_name, total_amount
FROM orders
WHERE status = 'paid' AND total_amount > 150;

```

Odpowiada na pytanie : 

Które opłacone zamóienai mają wartość większą niż 150. 

Wynik zawiera właściwe rekordy, ale nie określiliśmy ich kolejności. 

Może się wydawać, że baza "naturalnie" zwraca rekordy według order_id. 
Nie wolno jednak na tym polegać. 

Jeżeli kolejność ma znaczenie dla wyniku biznesowego, trzeba zapisać ją jawnie. 

## Bez ORDER BY kolejność nie jest gwarantowana 

Zapytanie

SELECT order_id, customer_name, total_amount 
FROM orders;

mówi bazie : 

Zwróć wskazane kolumny ze wszystkich wierszy. 

Nie mówi

Ułóż rekordy według numeru zamówienia. 

Silnik może zwrócić wiersze w kolejności, któa akurat wynika ze sposobu przechowywania albo wykonania zapytania. 
Po zmianie danych, indeksu, silnika bazy albo planu, wykonanie kolejnośći może się zmienić. 

Najważniejsza zasada

**Jeżeli kolejność ma znaczenie, użyj `ORDER BY`**

Dotyczy to szczególnie : 

- raportów
- eksportów 
- rankingów
- wyszukiwania największych i najmniejszych wartości
- zapytań z `LIMIT`
- testów porównujących dokładną kolejność rekordów

## ORDER BY - sortowanie wyniku

Ogólny schemat 

```sql

SELECT columns
FROM table_name
ORDER BY column_name;

```

Przykład na tabeli `products` :

product_id      product_name                price           category
1               Keyboard                    250             electronics
2               Notebook                    20              stationery
3               Mouse                       120             electronics
4               Monitor                     700             electronics

Zapytanie

```sql

SELECT product_name, price
FROM products
ORDER BY price;

```

układa wynik według kolumny `price`

Domyślnie wartości są ułożone rosnąco       

product_name                price
Notebook                    20      
Mouse                       120
Keyboard                    250
Monitor                     700

`ORDER BY` nie zmienia danych przechowywania w tabeli. Zmienai kolejność wiersza w wyniku konktrenego zapytania

## ASC - kolejność rosnąca

ASC pochodzi od słowa -> ascending

Czyli rosnąco.

Jawny zapis: 

```sql

SELECT product_name, price
FROM products
ORDER BY price ASC;
```
Dla liczb oznacza to: najmniejsza -> największa 

Dla tekstu oznacza kolejność wynikająca z zasad porównywania tekstu używanych przez bazę.

Jeżeli nie podasz kierunku, SQL domyślnie zastosuje ASC:

ORDER BY price;

i:

ORDER BY price ASC;

Jest dokładnie tym samym, poda tą samą kolejność.

## DESC - kolejność malejąca 

DESC pochodzi od słowa -> descending - > czyli malejąco

Przykład 

```sql

SELECT product_name, price
FROM products 
ORDER BY price DESC;

```

Wynik

product_name            price
Monitor                 700
Keyboard                250
Mouse                   120
Notebook                20

Dla liczb

największa -> najmniejsza

Najczęstsze zastosowanie:

- najdroższe produkty
- największe zamówienia
- najnowsze zdarzenia 
- rekordy z najwyższym wynikiem
- ostatnio zaktualizowane dane 

## Sortowanie po kolumnach

Czasami jedna kolumna nie wystarcza. 

Załóżmy dane 

employee_name           department              salary
Anna                    IT                      7000
Marek                   Sales                   6500
Ola                     IT                      7000
Piotr                   IT                      6200

Chcemy najpierw pogrupować wyniki według działu alfabetycznie,
wewnątrz działu pokazać najwyższą pensję jako pierwszą
przy identycznej pensji ułożyć nazwiska alfabetycznie 

Zapytanie:

```sql

SELECT employee_name, department, salary
FROM employees
ORDER BY department ASC,
        salary DESC,
        employee_name ASC;
```
SQL czyta kolumny sortowania od lewej do prawej : 

1. department ASC jest kryterium głównym
2. salary DESC rozstrzyga rekordy z tym samym działem
3. employee_name ASC rozstrzyga pozostałe remisy 

Każda kolumna może mieć własny kierunek

## Remisy i deterministyczny wynik 

Założmy, że dwie osoby mają taką samą pensję:

employee_name           Salary
Anna                    7000
Ola                     7000

Zapytanie : 

```sql 
SELECT employee_name, salary
FROM employees
ORDER BY salary DESC;
```
gwarantuje, że obie osoby znajdą sięprzy wartości 7000, ale nie rozstrzyga, czy pierwsza będzie Anna czy Ola.
Jeżeli dokładna kolejność ma znaczenie:

```sql

SELECT employee_name, salary
FROM employees
ORDER BY salary DESC, emplyee_name ASC;

```

Drugie kryterium rozstrzyga remis

W praktyce częśto na koncu dodaje się unikalny identyfikator:

```sql

ORDER BY created_at DESC, event_id ASC;

```

Daje to powtarzalną kolejność również wtedy, gdy kilka rekordó ma identyczny czas

Słowo "deterministyczny" oznacza tutaj, że dla tych samych danych i reguł otrzymujemy jednoznacznie ustaloną kolejność.

## WHERE przed ORDER BY

Filrtowanie i sorotwanie można łączyć

```sql

SELECT product_name, price
FROM products
WHERE category = 'electronics'
ORDER BY price DESC;

```

Czytamy - Wybierz nazwę i cenę produktów, z tabeli produkty, gdzie kategoria to elektronika i ułóż według ceny od najwyższej do najniższej. 

Kolejność zapisu klauzul:

- SELECT
- FROM
- WHERE
- ORDER BY

SQL wymaga określonej kolejności klauzul.

## LIMIT - ograniczenie liczby wierszy 

`LIMIT` określna maksymalnąliczbę wierszy zwróconych przez zapytanie. 

Przykład 

```sql

SELECT product_name, price
FROM products
LIMIT 2;

```

Zapytanie zwróci najwyżej dwa rekordy.

Jeżeli wynik przed ograniczeniem zawiera jeden rekord, LIMIT 2 zwróci jeden. Nie tworzy on brakujących rekordów

Schemat

```sql

SELECT columns
FROM table_name
LIMIT numer;

```

`LIMIT` zapisujemy pod koniec zapytania

## Dlaczego LIMIT zwykle potrzebuje ORDER BY?

Zapytanie : 

```sql

SELECT product_name, price
FROM products
LIMIT 2;
```
oznacza : 

Zwróc dwa rekordy z wyniku o nieustalonej kolejności. 

Nie oznacza autoamtycznie : 

- dwóch najdroższych
- dwóch najtańszych 
- dwóch najnowszych
- dwóch najstarszych 

Jeżeli chce dwa najdroższe produkty : 

```sql

SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 2;

```

Najpeirw określamy kolejność, a następnie ograniczamy wyniki. 

Bardzo ważna zasada

**`LIMIT` mówi "ile", a `ORDER BY` mówi "Co jako pierwsze"**

Częsty temat podczas rozmówch technicznych. 

## Kolejność klauzul w dzsiejszym zapytaniu 

Pełen szkielet

```sql 

SELECT columns
FROM table_name
WHERE condition
ORDER BY column_name ASC
LIMIT number;

```

Ważne zapamiętać kolejność zapisu 

SELECT -> FROM -> WHERE -> ORDER BY -> LIMIT

Przykład

```sql

SELECT product_name, price
FROM products
WHERE category = 'electronics'
ORDER BY price DESC
LIMIT 3;

```

Nie każda klauzula jest zaswze potrzebna, ale jeśli występuję, musi znaleźć się w odpowiednim miejscu. 

Przykłady poprawnych skróconych zapytań

```sql

SELECT *
FROM products ;

SELECT *
FROM products
ORDER BY price DESC

SELECT *
FROM products
WHERE price > 100
LIMIT 5;

```

Ostatni przykład jest poprawny składniowo, ale nie definiuje, które pierwsze pięć pasujących rekordów, ma pojawić się jako pierwsze 

## IN - jedna kolumna, kilka dopuszczalnych wartości 

Poprzednio zapisaliśmy warynek podobny do : 

```sql

WHERE status = 'pending' OR status = 'cancelled'

```

Możemy zapisać go krócej

```sql

WHERE status IN ('pending', 'cancelled')

```

`IN` odpowiada na pytanie:

Czy wartość po lewej stronie, znajduje się w podanym zbiorze wartości ? 

Ogólny schemat 

```sql

column_name IN (value_1, value_2, value_3)

-- Dla tekstu

WHERE category IN ('electronics', 'stationery')

-- Dla liczb

WHERE product_id IN (1,3,7)

```

Każdą wartość tekstową zapisujemy w pojedynczych cudzysłowach. 

## IN a OR

Te dwa warunki są logiczne równoważne 

```sql

WHERE category = 'electronics' OR category = 'stationery' OR category = 'books'

-- oraz

WHERE category IN ('electronics', 'stationery', 'books')

```

`IN` jest szczególne czytelne gdy

- sprawdzamy jedną kolumnę
- porównujemy ją z kilkoma konkretnymi wartościami 
- wszystkie porównania używają równości
`IN` nie zastępuję każdego `OR`

Przykład 

```sql

WHERE category = 'electronics' OR price < 50

```

Tutaj sprawdzamy dwie różne kolumny i dwa różne rodzaje warunków. Zwykłe `OR` jest właściwe

## NOT IN - odrzucenie wskazanych wartości

`NOT IN` oznacza:

Wartość nie znajduje się w podanym zbiorze. 

Przykład 
```sql
SELECT product_name, category
FROM products
WHERE category NOT IN ('electronics', 'books')
```

Pozostaną produkty, których kategoria nie jest ani electronics, ani books.

Obecnie pracujemy z kompletnymi danymi, będzie to dużo bardziej pomocne, gdy poznamy NULL. 

## BETWEEN - przedział wartości 

Chcemy wybrać produkty kosztujące od 100 do 300 zł włącznie. 

Dłuższy zapis 

```sql

WHERE price >= 100 AND price <=  300

-- Zapis przez BETWEEN

WHERE price BETWEEN 100 AND 300 

```

Oba warunki są logiczne równoważne

**WAŻNA ZASADA** 

BETWEEN obejmuje dolną i górną granicę. 

Czyli 

price BETWEEN 100 AND 300 obejmuje również : 

- price = 100,
- price = 300.

Można to zapamiętać jako przedizał domknięty [100, 300]

## Kolejność granic BETWEEN 

Poprawny zapisy 

price BETWEEN 100 and 300 

oznacza

price >= 100 AND price <= 300

Nie należy odwracać granic 

price BETWEEN 300 and 100 

SSQL nie zmieni automatycznie miejscami. Taki warunek nie istnieje w praktyce. Najpierw wartość mniejsza następnie większa.

## NOT BETWEEN - wartości poza podziałem. 

Przykład 

WHERE price NOT BETWEEN 100 AND 300

oznacza

Cena mniejsza niż 100 albo większa niż 300

Logiczny odpowiednik:

```sql

WHERE price < 100 OR price > 300 

```

Ponieważ zwykłe BETWEEN obejmuje granice, NOT BETWEEN odrzuca również wartości równe obu granicom. Czyli 100 i 300 nie wchodzi. 

## BETWEEN nie zawsze zastępuje dwa porównania.

Jeżeli chcemy mieć przedział bez wartości granicznych: 

więcej niż 100 i mniej niż 300

Potrzebujemy 

WHERE price > 100 AND price < 300

Nie używany wtedy zwykłego BETWEEN, ponieważ ono uwzględni 100 i 300. 

Najpierw należy odczytać dokładnie pytanie 

- od 100 do 300 włącznie -> BETWEEN
- Co najmniej 100 i najwyżej 300 -> BETWEEN
- więcej niż 100, ale mniej niż 300 -> > oraz <

## Łączenie IN i BETWEEN

Można połączyć oba warunki: 
```sql
SELECT product_name, category, price
FROM products
WHERE category IN ('electronics', 'office') AND price BETWEEN 100 AND 500
ORDER BY price DESC;
```

Czytamy : 

Wybierz nazwę, kategorię i cenę produktów, z kategorii electronics albo office, których cena wynosi od 100 do 500 włącznie. Ułóż wynik od najwyższej ceny

Każda część odpowiada za inne zadanie : 

Fragment            Rola
SELECT              Wybór kolumn
FROM                Wskazanie tabeli
WHERE               Rozpoczęcie filtrowania
IN                  Dopuszczalne kategorie
BETWEEN             Przedział
AND                 oba warunki muszą być prawdziwe
ORDER BY ... DESC   Kolejność malejąca

## Pełne zapytanie z LIMIT

Przykład 

```sql

SELECT product_name, category, price
FROM products
WHERE category IN ('electronics', 'office') AND price BETWEEN 100 AND 500
ORDER BY price DESC, product_name ASC
LIMIT 3;
```
Kolejność myślenia:

1. Zródłem jest tabela products
2. Pozostają wskazane kategorie 
3. Cena musi należeć do przedziału 
4. Wynik jest sortowany malejąco po cenie
5. Nazwa rozstrzyga remis cenowy
6. Zwracane są najwyżej trzy pierwsze rekordy z tej kolejności
7. W wyniku widzimy tylko trzy kolumny wskazane po SELECT

To jest już prawdziwe, wieloelementowanie zapytanie analityczne 

## Nie należy mylić kolejności zapisu z czytaniem pytania

Zapytanie zpaisujesz

SELECT
FROM
WHERE
ORDER BY
LIMIT

Ale analizując sens biznesowy, można pomyśleć : 

1. Z jakiej tabeli korzystam
2. Które rekordy spełniają warunek ? 
3. Jakie kolumny chce zobaczyć
4. Jak ułożyć wynik?
5. Ile rekordów potrzebuję.

Najważniejsze jset to, aby wynik odpowiadał na pytanie. Sama poprawna składnia nie wystarczy. 

## Porównanie z Pandas - mapa pojęć. 

Nie będziemy dziś korzystać z PANDAS, zrobimy to w kolejnej lekcji. Tylko orientacyjna mapa

Pytanie                         SQL             Pandas 
Jak ułożyć rekordy              ORDER BY        sort_values()
Jak pobrać pierwsze rekordy?    LIMIT           head()
Czy wartość jest na liście?     IN              isin()
Czy liczba jest w przedziale?   BETWEEN         between() albo dwa warunki 

Na razie skupiamy się na SQL.

