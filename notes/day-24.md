# SQL

## Czym jest SQL

SQL Oznacza : 

Structured Query Language 

Jest to język służący do rpacy z relacyjnymi bazami danych. 

Za jego pomocą można między innymi : 

- pobierać dane
- filtrować rekordy
- sortować wyniki
- grupować i agregować dane
- łączyć tabele
- dodwać rekordy
- aktualizować rekordy
- usuwać rekordy
- tworzyć strukturę bazy 

Najważniejsze pierwsza zdanie SQL:

```sql
SELECT *
FROM orders;
```
Można je przeczytać : 

Wybierz wszystkie kolumny z tabeli orders

## SQL To język SQLite to silnik bazy danych

Te nazwy łatwo pomylić.

**SQL**

SQL jest językiem, w któym zapisujemy polecenia i pytania kierowane do bazy

**SQLite**

SQLite jest konkretnym silnikiem baz danych. Potrafi wykonywać zapytania SQL, a całą bazę może przechowywać w jednym lokalnym pliku, np.: 

orders.db

SQLite dobrze nadaje się do nauki, małych aplikacji, testów oraz lokalnego przetwarzania danych, ponieważ nie wymaga uruchamienia osobnego serwera. 

Później zaczniemy pracować w PostgreSQL. Podstawowe zapytania poznane w SQLite będą w dużej części wyglądały tak samo. 

SQL -> język
SQLite -> program wykonujący SQL i przechowujący bazę

## Baza danych, tabela, wiersz i kolumna 

Baza danych jest uporządkowanym zbiorem danych. Może zawierać wiele tabel. 

Tabela 

Tabela przypomina arkusz albo plik CSV

order_id    customer_name           total_amount        status      city
1001        Anna                    249.99              paid        Gdańsk
1002        Tomasz                  89.50               pending     Kartuzy

Wiersz

Jedne wiersz reprezentuje jeden rekord. W naszym przykładzie jest to jedno zamówienie 

Kolumna opisuje konkretną cechą rekordu, np.:

- order_id,
- customer_name,
- total_amount,
- status
- city

Porównanie z tym, co już znam 

CSV/PYTHOn                  Relacyjna baza danych
cały plik CSV               tabela
jeden słownik               wiersz
klucz słownika              kolumna
wartość słownika            wartość w komórce
lista słowników             zbiór wierszy

## Sechmat tabeli 

Schemat opisuje strukturę tabeli : 

Schemat opisuje struktrę tabeli: 

- nazwy kolumn
- typy danych
- ograniczenia
- klucze

Dzisiejsza tabela `orders` ma następujący schemat : 

```sql

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT NOT NULL,
    city TEXT NOT NULL
);

```

Nie trzeba jeszcze samodzielnie pisać `CREATE TABLE`. Dzisiejszy kod przygotuje dla Ciebie bazę. 

Najważniejsze typy w tym przykładzie. 

Typ SQLite          Znaczenie               Przykład
INTEGER             Liczba całkowita        1001
REAL                Liczba dzisiętna        249.99
TEXT                teks                    paid

`PRIMARY KEY` oznacza klucz główny, który jednoznacznie identyfikuje rekord. 
W Tabeli orders dwa wiersze nie powinny mieć tego samego order_id.

NOT NULL oznacza, że w danej kolmnie wymagana jest wartość

DO NULL wrócimy osobno. Narazie będziemy pracować na kompletynych danych.

## SQL jest językiem deklaratywnym 

W Pythonie często opisujesz dokładny algorytm : 

```python

paid_orders = []

for order in orders:
    if order["status"] == "paid":
        paid_orders.append(order)
```

Mówimy programowi krok po kroku 

1. Utwórz listę
2. Przejdź po rekordach
3. Sprawdź warunek 
4. Dodaj pasujący rekord 

W Sql opisujesz przede wszystkim wynik, które chcesz otrzymać : 

```sql

SELECT *
FROM orders
WHERE status = 'paid';

```

Mówimy bazie - Wybierz wszystko z Tabeli Orders gdzie status jest 'paid'

Silnik bazy danych sam decyduje, jak technicznie wykonać zapytanie.

Dlatego SQL nazywamy językiem deklaratywnym. 

## SELECT - co chce zobaczyć 

`SELECT` - określna kolumny, które mają znaleźć się w wyniku. 

Wszystkie kolumny 

```sql

SELECT *
FROM employees;

```

Gwiazdka oznacza wszystkei kolumny 

Wybrane kolumny

```sql

SELECT employee_id, employee_name
FROM employees;

```

Wynik będzie zawierał wyłącznie dwie wskazane kolumny

W zadaniach warto poznać SELECT *, ale w kodzie produkcyjnym, zazwyczaj lepiej jawnie podawać potrzebne kolumny. Dzięki temu : 

- wynik ma przewidywalną strukturę 
- nie pobieramy niepotrzebnych danych
- zapytanie jest czytelniejszym kotraktem 

## FROM - skąd pobieram dane ? 

`FROM` wskazuje tabelę, będącą źródłem danych 

```sql

SELECT employee_name
FROM employees;

```

Czytamy 

Wybierz kolumnę employee_name z tabeli employees 

W dzisiejszych zadaniach źródłem będzie tabela : 

`orders` 

Nie należy mylić nazwy tabeli `orders` z plikiem orders.csv. Po przygotowaniu bazy, dane z CSV zostaną zapisane w tabeli znajdującej się w orders.db

## Średnik 

Zapytanie SQL zwykle kończymy średnikiem

```sql

SELECT * 
FROM employees;

```

Średnik oznacza koniec instrukcji.

W niektórych narzędziach pojedyńcze zapytania wykonają się również bez niego, ale warto od razu nabrać nawyk `;` 

## Formatyowanie zapytania

SQL można zapisać w jednej linii : 

```sql

SELECT employee_id, employee_name FROM employees WHERE department = 'IT';

```

Czytelniej jest to jednak rozdzielić na części : 

```sql

SELECT employee_id, employee_name
FROM employees
WHERE department = 'IT';

```

Przyjmujemy zasady : 

- słowa kluczowe SQL zapisujemy wielkimi literami 
- każdą główną część umieszczamy w osobnej linii,
- nazwy tabel i kolumn zapisujemy małymi literami 
- instrukcję kończymy średnikiem

SQLite nie wymaga wielkich liter dla SELECT, ale taki styl znaczenie ułatwia czytanie zapytań

## WHERE - które wiersze chce otrzymać 

WHERE filtruje wiersze 

Przykład na tabeli pracowników 

```sql

SELECT employee_id, employee_name 
FROM employees
WHERE department = 'IT';

```

W wyniku pojawią się wyłączenie pracownicy działu IT.

Porównanie z Pythonem 

```py

if employee["department"] == "IT":
    ...
WHERE department = 'IT'

```

Najważniejsza różnica składniowa 

- Python porównuje przez == ,
- SQL porównuje przez = 

## Tekst w SQL

Wartości tekstowe zapisujemy w pojedyńczych cudzysłowach : 

```sql

WHERE department = 'IT'

```

Nie zapisujemy = IT, "IT" 

Bez cudzysłowów silnik może potrakować IT jako nazwę kolumny albo inny identyfikator. 

SQL odróżnia teksty od liczby

WHERE total_amount > 200 

Liczby nie wymgają cudzysłowów

## Operatory porównania 

Operator SQL        Znaczenie               Przykład
=                   równe                   status = 'paid'
!=                  różne                   status != 'paid'
| >                   większe                 total_amount > 200
| >=                większe lub równe       total_amount >= 200
<                   mniejsze                total_amount < 100
<=                  mniejsze lub równe      total_amount <= 100

W SQL lite można spotkać operartor <>, oznaczający różne. Jednak od samego początku przyjmniemy używanie czytelnego !=

## AND wszystkie warunki muszą być prawdziwe 

Przykład

```sql

SELECT employee_name, salary
FROM employees
WHERE department = 'IT'
    AND salary > 7000;
```
Wynik zawiera tylko rekordy, któe jednocześnie

- należą do działu IT
- mają wynagrodzenie więkskze niż 7000

Pórównanie z Pythonem

```py

if department = "IT" and salary > 7000:
    ...

```

## OR - wystarczy jeden prawdziwy warunek

Przykład

```sql

SELECT employee_name, department
FROM employees
WHERE department = 'IT'
    OR department = 'Finance';

```

Wynik zawiera pracowników z działu IT albo Fiannce 

Porównanie z pythonem 

```py

if department == "IT" or department == "Finance":
    ...

```

W bardziej złożonych warunkach, będziemy używać nawiasów. Na początek jednak proste przypadki

## SELECT nie zmienia danych

Zapytanie

```sql

SELECT *
FROM orders;
```

tylko odczytuje dane. Nie usuwa, nie aktualizauje nie dopisuje rekordów.
To dobra wiadomość na początek, można wykonywać zapytanie SELEC wiele razy, bez modyfikacji tabeli. 

Instrukcje zmieniające, pojawią się w późniejszym etapie

## Jak SQLite zwraca dane do Pythona ? 

Moduł sqlite3 domyślenie zwraca pojedyczy wiersz jako krotkę. Przykładowy wynik : 

(1001, 'Anna', 249.99, 'paid', 'Gdańsk')

Wiele wierszy to lista albo iterator zawierający kolejny krotki. 

To łączy SQL z moim poprzednim mateirałem

- tabela daje wiele wierszy
- jeden wiersz może być reprezentowany jako krotka
- kolejność wartośći odpowiada kolejności kolumn zpaisanych po `SELECT`

Jeżeli wykonam 

```sql

SELECT customer_name, status
FROM orders;

każda krotka będzie miała dwie wartości dokładniej w tej kolejności. 