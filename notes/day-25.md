# Pandasa

## Czym jest Pandas 

Pandas jest biblioteką Pythona przeznaczoną do pracy z danymi tabelarycznymi. 

Biblioteka to gotowy zestaw narzędzi, który możemy dołączyć do własnego programu. Nie musimy samodzielnie pisać od początku kodu odpowiedzialnego za :

- odczyt tabeli
- wybieranie kolumn
- filtrowanie wierszy
- analizowanei typów danych
- sortowanie
- agregowanie
- łączenie zbiorów 
- zapis wyników 

Pandas jest szczególnie wygodny poczas

- ekspolracji danych
- sprawdzanie jakości plików
- przygotowanie transformacji
- budowanie niewielkich i średnich pipelinów
- prototypowanie rozwiązania
- porównywanie danych z róźnych źródeł 

Pandas działa wewnąrz programu Python. SQL natomiast wyysłamy do silnika bazy danych. To ważna różnica

Narzędzie           Gdzie wykonuje się operacja?                Typowe źródło danych
czysty Python       w programie Python                          TXT, CSV, JSON, API
Pandas              w programie Python                          CSV, EXCEL, JSON, SQL
SQL                 W silniku bazy danych                       tabele bazy danych

Pandas nie jest bazą danych. DataFrame istniej eprzede wszystkim w pamięci uruchomionego programu. 

# Import Pandas

Standardowy import wygląda tak : 

```python

import pandas as pd

```

`pandas` to nazwa biblioteki, a `pd` jest przyjętym powszechnie skrócem. Dzięki aliasowi zpaisujemy. 

pd.read_csv(...)

zamiast: 

pandas.read_csv(...)

Alias nei zmienia działania biblioteki. Jest tylko krótszą nazwą używaną w kodzie. 

Nie należy odkrywać świata na nowo, używaj zawsze pd - a nie żadne p czy pan. W prawdziwych projektach każdy spodziewa się pd. 

## Wczytanie CSV przed read_csv()

Najważniejsza linia dzisiaj 

```python

orders = pd.read_csv(CSV_FILE)

```

Czytamy je następująco. Wczytaj wskazany plik CSV przz CSV_FILE i zapisz otrzymaną tabelę w zmiennej orders. 

pd.read_csv():

1. otwiera plik
2. odczytuje nagłówki
3. tworzy nazwy kolumn 
4. odczytuj rekordy 
5. próbuje rozponać typ każdej kolumny
6. zwraca DataFrame

Możemy to sprawdzić:

print(type(orders))

Wynik będzie podobny do:

<class 'pandas.DataFrame>

Ważne: Pandas próbuje rozpoznać typy

W poprzednich lekcjach csv.DictReader zwracał wartości CSV jako tekst. Samemu wykonywaliśmy między innymi

```python

int(row["order_id"])
float(row["total_amount"])
```

Pandas podczas `read_csv()` sam próbuje ustalić odpowiednie typy kolumn.

To jest wygodne, ale nie oznacza, że zawsze odgadnie je zgodnie z naszymi kontraktem danych. Dlatego DE po wczytaniu danych sprawdza typy, a nie zakłada, że wszystko jest poprawne. 

## Czym jest DataFrame

DataFrame jest dwuwymiarową strukturą danych przypominającą tabelę.

Ma : 

- wiersze
- kolumny
- nazwy kolumn
- indeks wierszy
- typy danych dla każdej kolumny

Przykład : 

indeks      Product_name                price       category
0           Keyboard                    250         electronics
1           Notebook                    20          stationery
2           Mouse                       120         electronics

DataFrame nie jest dokładnie zwykłą listą słowników, chociaż może reprezentować podobne dane. 

Porównanie 

Czysty Python                   Pandas
lista słowników                 DataFrame
jeden klucz w każdym słowniku   kolumna
jeden słownik                   wiersz
ręczna pętla                    operacja na całej kolumnie

## Czym jset Series?

Series jest jednowymiarową strukturą Pandas. Najczęściej można o niej pomyśleć, jak o jednej kolumnie DataFrame

Jeżeli `products` jest DataFrame, zapis:

product_names = products["product_name"]

zwróci Series

Natomiast:

selected_products = products[["product_name", "price"]]

zwróci DataFrame, ponieważ wybieramy kilka kolumn.

Najważniejsza różnica składni 

kod                             Wynik
df["column"]                    Series
df[["colummn"]]                 DataFrame z jedną kolumną
df[["column_a", "column_b"]]    DataFrame z wieloma kolumnami

Podwójne nawiasy nie są specjalnym operatorem Pandas. Zewnętrze nawiasy wybierają dane z DataFrame, a wewnęrznę tworzą zwykła listę nazw kolumn: 

columns_to_select = ["products_name", "price"]
selected = products["columns_to_selec"]

To samo zapisane krócej

selected = products[["product_name", "price"]]

## Indeks w DataFrame

Po wczytaniu naszego CSV Pandas wyświetli po lewej stronie liczy 

    order_id        customer_name       total_amount        status      city
0   1001            Anna                249.99              paid        Gdańsk
1   1002            Tomasz              89.50               pending     Kartuzy
2   1003            Kasia               120.0               paid        Gdynia

Liczby `0`,`1`,`2` nie pochodzą z CSV. To indeks utworzony przez Pandas.

W tej tabeli:

- indeks techniczny pierwszeggo wiersza to `0` 
- biznesowy identyfikator zamówienia to order_id = 1001

Nie są tym samym

na razie indeks pozostawimy bez zmian. Później bedzie wybieranie danych po etykiecie i pozycji oraz świadome ustawianie indeksów

## Pierwsze oglądanie danych - head()

Nie zaczynamy pracy z nieznanym plikiem od wyspiwaynia całej tabeli.

Lepiej użyć

```python

print(orders.head())

```

head() domyślnie zwraca peirwszych 5 wierszy

Można podać inną liczbę np. x.orders(3) - > To zwróci 3 wiersze i tak dalej. 

head() nie usuwa pozostałych rekordów z orders. Tworzy wynik zawierający początkowy fragment danych. 

Na myłm zbiorze można wykonać : 

```python

print(orders)

```

Ale na pliku mającym milion wierszy byłoby to nieczytelne i niepraktyczne. 

## Liczba iwerszy i kolumn - shape 

Każdy DateFrame ma atrybut `shape` 

```python

print(orders.shape)
```
Dla naszych danych wynik powinien wynosić 

(12,5)

Jest to krotka

(liczba wierszy, liczba kolumn)

Możemy pobrać obie wartości

row_count = orders.shape[0]
column_count = orders.shape[1]

Ponieważ jestem zeznajomiony z rozpakowywaniem tupli można zapiasć 

row_count, column_count = orders.shape 

`shape` jest atrybutem, dlatego nie zapisujemy shape(). 

len() a shape 

```python

print(len(orders)) # Zwróci liczbę wierszy czyli 12

```

Kod                 Wynik
len(orders)         liczba wierszy
orders.shape[0]     liczba wierszy
orders.shape[1]     liczba kolumn
orders.shape        krotka: wiersze i kolumny

## Nazwy kolumn - columns

Nazwy kolumn sprawdzam przez 

print(orders.columns)

Zobaczymy obiekt podobny do:

Index(['order_id', 'customer_name', 'total_amount', 'status', 'city'], dtype='str')

To nie jest zwykła lista. Na dzisiaj najważniejsze jest jednak to, że można szybko sprawdzić : 

- czy wszystkie wymagane kolumny istnieją
- czy nazy nie zawierają literówek 
- w jakiej kolejności występują

Jeżeli chcemy, możemy otrzymać zwykłą listę.

print(orders.columns.tolist())

## Typy kolumn - dtypes

Typ każdej kolumny sprawdzimy przez :

print(orders.dtypes)

Powinienem zobaczyć typy, odpowiadające mniej więcej temu podziałowi : 

Kolumna                 Rodzaj danych
order_id                liczba całkowita
customer_name           tekst
total_amount            liczba dzisiętna
status                  tekst
city                    tekst

Nazwy typów pandas, mogą zależeć od wersji biblioteki i sposobu wczytania danych. 
Nie należy więc się do tego przywiązywać , czy tekst zostanie opisany jako str, string albo object. 

Najważniejsze aby rozpoznawać, któe kolumny są liczbowe a które tekstowe.

Dlatego to istotne ? 

Jeżeli `total_amount` zostałoby wczytane jako tekst, porównanie : 

orders["total_amount"] > 200

nie działałoby zgodnei z naszym zamiarem.

DE sprawdza typy przed rozpoczęciem transformacji.

## Szybki raport o DataFrame - info()

Jedną z pierwszych metod używanych po wczytaniu danych jset : 

orders.info()

W tym wypadku nie używamy print 

info() samo wypisuje między innymi:

- liczbę wierszy
- nazwy kolumn 
- liczbę wartości niepustych
- typ każdej kolumny
- przybliżone użycie pamięci 

Nie należy zapisywać 

`print(orders.info())` - Metoda najpierw wyświetli raport, a potem dodatkowo wyświetli None

##  Minimalna kontrola po wczytaniu danych 

Dobrym pierwszym kontaktem z plikiem może wyglądać tak: 

print(orders.head())
print(orders.shape)
print(orders.columns)
print(orders.dtypes)

albo

print(orders.head())
orders.info()

Nie chodzi o bezmyślnie uruchamianie wszystkich metod. Zadajemy konrketne pytania : 

- Czy wczytałem właściwy plik?
- Czy dane wyglądają sensownie?
- Ile mam rekordów i kolumn ?
- Czy nazwy kolumn są poprawne? 
- Czy typy danych odpowiadają zawartości ? 

## Wybór jednej kolumny 

Załóżmy przykładowo DataFrame products z kolumnami : 

- product_name 
- price
- category 

Jedną kolumnę wybieramy tak:

product_names = products["product_name"]
print(product_names)

Wynikiem jest Series

Można sprawdzić :

print(type(product_names))

Dlaczego nazwa kolumny jest tekstem? 

W zapisie : 

products["product_name"] 
"product_name" jest etykietą kolumny, której szukamy w DF. 

Jeśli napiszesz nieistniejącą nazwę : 

products["product"] 

Pandas zgłosi KeyError

Wtedy najlepiej sprawdzić kolumny -> print(products.columns)

## Wybór kilku kolumn

Wybieramy przez listę nazw 

product_view = products[["product_name", "price"]]
print(product_view)

Wynikiem jest DataFrame zaierający:

- wszystkie wiersze
- tylko dwie wskazane kolumny
- kolumny w takiej kolejności, jak w przekazanej liście 

Porównanie z SQL

```sql

SELECT product_name, price
FROM products;

```

W obu przypadkach wybieramy kolumny, które mają znaleźć się w wyniku 

## Warunek tworzy maskę logiczną 

Załóżmy, że products["price"] zawiera

250
20
150

Warunek

products["price"] > 100

nie zwraca od razu przefiltrowanej tabeli. Zwraca Series wartości logicznych:

True
False
True

Dla każdego wiersza Pandas odpowiada na pytanie 

Czy cena w wierszu j est większa niż 100?

Taki zestaw wartości `True` i `False` nazywamy maską logiczną albo maskąboolowską.

Możemy ją zapisać w zmiennej

expensive_mask = products["price"] > 100
print(expensive_mask)

Maska ma tyle elementów, ile wierszy ma DataFrame 

## Filtrowanie wierszy przez .loc[]

Maskę przekazujemy do .loc[]

expensive_mask = products["price"] > 100
expensive_products = producst.loc[expensive_mask]

W wyniku pozostaną tylko wiersze, dla których maska zawiera True. 

Można zapisać w jednej instrukcji 

```python

expensive_products = products.loc[products["price"] > 100]

```

Na początku jednak, można rozdzieliać na dwa kroki : 

1. Zbuduj maskę
2. Sprawdź maskę 
3. użyj maski do filtorwania 

Łatwiej wtedy znaleźć błąd 

Dlaczego używamy .loc[] ? 

Pandas pozwala również spotkać zapis 

products[products["price"] > 100]

Jest poprawny, ale `.loc[]` wyraźniej pokazuje, że wybieramy wiersze, a za chwilępozwoli nam jednocześnie wskazać kolumny 

W naszych rozważaniach/lekcjach jako podstawowy zapis filtrowania przyjmujemy .loc[]

## Jednoczesny wybór wierszy i kolumn 

.loc[] może otrzymać dwa elementy :

df.loc[wiersze, kolumny]

Przykład

```python

expensive_products = products.loc[
    products["price"] > 100,
    ["product_name", "price"]
]

```

Pierwszy elememnt określa wiersze : 

products["price"] > 100

Drugi element określa kolumny : 

["product_name", "price"]

Porównanie z SQL: 

SELECT product_name, price
FROM products
WHERE price > 100; 

Można przeczytać kod Pandas : 

Z DataFrame products wybierz wiersze, w któych cena jest większa niż 100, oraz pokaż tylko kolumny product_name i price

## Równość w SQL i Pandas

SQL - WHERE status = 'paid' 

W Pandas warunek wygląda tak : 

orders["status"] == "paid" 

Narzędzie               Porównanie równości
SQL                     = 
Python i Pandas         ==

Python jest biblioteką Pythona, dlateggo stosujemy operator Pythona

## Dwa warunki 

W SQL używany był AND

```sql

SELECT product_name, price
FROM products
WHERE category = 'electronics' AND price > 200;

```

W Pandas odpowiednikiem dla masek jest & 

```python

selected_products = products.loc[
    (products["category"] == "electronics")
    & (products["price"] > 200),
    ["product_name", "price"]
]

```

& - oznacza tutaj 

Oba warunki dla danego wierszą muszą być prawdziwe. 

Dlaczego nie używamy AND?

Pythonowe AND służy do łączenia pojedynczych wartości logicznych.

W Pandas każdy warunek tworzy całą Series True i False. Chcemy porównać obie maski element po elemencie, dlatego używamy `&` 

Dlaczego każdy warunek ma nawiasy ?

Poprawnie 

(products["category"] == "electronics") & (products["price"] > 200)

Nawiasy jednoznacznie oddzielają oba pełne warunki i zapewniają właściwą kolejność wykonwywania operatrów. 

Należy przyjąć zasadę : 

Jeden warunek Pandas = jedna para nawiasów 

## Dwa warunki - operator | 

W SQL używaliśmy OR:

```sql

SELECT product_name, category
FROM products
WHERE category = 'eletronics' OR category = 'stationery';

```

W Pandas odpwoiednikiem dla masek jest | 

```python

selected_products = products.loc[
    (products["category"] == "electronics")
    | (products["category"] == "stationery"),
    ["product_name", "category"],
]

```

| - oznacza tutaj : 

Przyjmij jeden warunek dla danego wiersz, musi być prawdziwy. 

Nie używamy pythonowego or, ponieważ ponownie pracujemy na całym Series, a nie na dwóch pojedyńczych wartościach 

## Operatory porównania w Pandas

Operatory porównanie wyglądają tak samo jak w zwykłym Pythonie 

Znaczenie                       Pandas/Python       SQL
równe                           ==                  =
różne                           !=                  !=
większe                         >                   >
mniejsze                        <                   <
większe lub równe               >=                  >=
mniejsze lub równe              <=                  <=
oba warunki                     &                   AND
przynajmniej jeden warunek      |                   OR   

## DataFrame po filtrowaniu 

Załóżmy

expensive_products = products.loc[products["price"] > 100]

Zmienna expensive_products zawiera nowy wynik filtorwania. Orygilany DataFrame products nadal zawiera wszystkie rekordy.

Można to sprawdzić

print(product.shape)
print(expensive_products.shape)

To waażny nawyk: wynik ransformacji zapisujemy zawsze pod nazwą mówiąca co zawiera. 

Nazwy takie jak:

- x = ...
- data2 = ...
- result123 = ...
utrudniają rozumienie pipelinu'u

Lepsze przykłady : 

- paid_orders = ...
- high_value_orders = ...
- orders_from_gdansk = ...

## Kolejność: najpierw warunek, potem kolumny 

W zapisie:

result = products.loc[
    products["price"] > 100,
    ["product_name", "price"],
]

myśl w kolejności

1. Jaki data frame jest źródłem? - products
2. Które wiersze mają pozostać - cena większa niż 100. 
3. Któe koolumny chce zobaczyć? - nazwa i cena
4. Gdzie zapisujęwynik - result 

W SQL kolejnośćzpaisu jest inna

1. SELECT - kolumny
2. FROM - tabela
3. WHERE - wiersze

Nie należy tłumaczyć kodu znak po znaku. Najpierw należy ustalićpytanie biznesowe, a dopiero potem wybrać odpowiednią składnię. 

## Porównanie czystego Pythona, SQL i Pandas.

Pytanie biznesowe.

Któe opłacone zamóienai mają wartość większą niż 150 ? 

Czysty Python

```python

selected_orders = []

for order in orders:
    if order["status"] == "paid" and order["total_amount"] > 150:
        selected_orders.append(order)

```

SQL

```sql

SELECT *
FROM ORDERS
WHERE status = 'paid' AND 'total_amount > 150;

```

Pandas 

```python

selected_orders = orders.loc[
    (orders["status"] == "paid")
    & (orders["total_amount"] > 150),
]

```