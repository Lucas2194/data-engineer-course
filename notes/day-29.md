# MAPA SQL -> PANDAS 

Pytanie                             SQL(*)                  PANDAS
Ile jest wierszy?                   COUNT(*)                len(dataframe) albo dataframe.shape[0]
Ile jest niepustych wartości?       COUNT(column)           series.count()
Jaka jest suma?                     SUM(column)             series.sum()
Jaka jest średnia?                  AVG(column)             series.mean()
Jakie jest minimum?                 MIN(column)             series.min()
Jakie jest maksimum?                MAX(column)             series.max()
Kilka agregacji                     kilka funkcji w SELECT  series.agg([])
Filtrowanie przed agregacją         WHERE                   maska i .loc[]

Najważniejsze podobieństwo:

Zarówno w SQL jak i Pandas najpierw ustalamy zbiór rekordów wejsciowych, a dopiero potem wykonujemy agregację.

## Agregacja zmniejsza wymiar wyniku 

Przygotujmy sobie osobny przykład, niezwiązany z zdaniami : 
```py
prices = pd.Series([250.0, 20.0, 120.0, 700.0], name="price")
```

Series zawiera cztery wartości:

250.0
20.0
120.0
700.0

Po wykonaniu 

```py

total_price = prices.sum()
```

Otrzymujemy jedną wartość

1090.0

Można to zapisać tak : 

Series z 4 wartościami
\/
sum()
\/
jedna wartość liczbowa

To odpowiednik zmiany : 

wiele rekordów SQL -> jeden wiersz podsumowania 

## Najpierw wybieramy właściwą Series

Agregację kwot wykonujemy na kolumnie kwot:

prices = products["price"]
total_price = prices.sum()

Nie zaczynamy od : 

products.sum()

DataFrame może zawierać : 

- liczby
- tekst
- daty
- wartości logiczne 

DataFrame.sum() działa kolumnami i może również łączyć teksty. Wynik nie musi odpowiadać pytaniu biznesowemu. 

Bezpieczny nawyk na obecnym etapie : 

Najpierw wskaż konkretną kolumnę, a potem wykonaj agregację. 

## Wynik pojedynczej agreacji jest skalarem

Przykład

result = prices.sum()

print(result)
print(type(result))

Nie otrzymujemy DataFrame ani Series. Otrzymujemy pojedyńcza wartość, czyli skalar. W zależności od danych może być to na przykład : 

- int 
- float
- numpy.int64
- numpy.float64

Na tym etapie najważniejsze jest rozróżnienie: 

Operacja                            Typowy wynik
wybór jednej kolumny                Series
filtrowanie wierszy                 DataFrame albo Series
pojedyncza agregacja Series         skalar
kilka agregacji przez .agg([...])   Series

## len() - liczba wierszy

Najprostszy sposób policzenia rekordów DF 

row_count = len(products)

len(dataframe) liczy wiersze. Nie sprawdza, czy wartości w poszczególnych kolumnach są puste. 

Jest to najbliższy praktyczny odpowiednik: 

COUNT(*)

Można także użyć :


row_count = products.shape[0]

shape zwraca krotkę

(liczba_wierszy, liczba_kolumn)

Dlatego shape[0] oznacza liczbę wierszy, a shape[1] liczbę kolumn. 

## .size - liczba elementów Series

Dla pojedynczej Series : 

element_count = prices.size

size jest własnością, a nie metodą. 

Poprawnie

prices.size 

Niepoprawnie 

prices.size()

.size liczy wszystkie pozycje, również te zawierające brak danych. 

## .count() - liczba niepopsutych wartości

Przykład : 

example = pd.Series([100,0, None, 300.0])

Wynik:

print(example.size) # 3 
print(example.count()) # 2 

Dlaczego? 

- .size widzi trzy pozycje
- .count() pomija brakujące wartości

Odpowiednik SQL : 

SQL                 Pandas
COUNT(*)            len(dataframe)
COUNT(column)       series.count()

W moim obecnym orders.csv kolumna total_amount nie ma braków, dlatego

len(orders) == orders["total_amount"].count()

To nie oznacza, że te dwie operacje zawsze się łączą i są takie same

## Uwaga na DataFrame.count()

Kod

orders.count()

nie zwraca jednej liczby wierszy. Zwraca liczbę niepustych wartości osobno dla kązdej kolumny.

Typowym wynikiem jest series. 

order_id        12
customer_name   12
total_amount    12
status          12
city            12

Jeżeli pytanie brzmi : 

Ile rekordów ma DataFrame?

Używamy

len(orders)

Jeżeli pytanie brzmi: 

Ile niepustych wartości znajduje się w każdej kolumnie ? 

Wtedy orders.count() jest odpowiednim narzędziem.

## .sum() - suma wartości 

Na przykładowej series

prices = pd.Series([250.0, 20.0, 120.0, 700.0])
total_price = prices.sum()

Wynik: 

1090.0

Pandas nie zmienia wartości Series. Oblicza nowy wynik. 

Odpowiednik SQL

SELECT SUM(price)
FROM products;

## .mean() - średnia artymetyczna

Przykład

average_price = prices.mean()

Pandas oblicza 

suma wartości / liczba niepustych wartości

Do zaokrąglenia pojedynczego wyniku używamy wbudowanego round() 

rounded_average = round(average_price, 2)

Rozdzielamy pojęcia:

- mean() wykonuje agregację
- round(..., 2) tylko zaokrągla otrzymany wynik
Zaokrąglenie nie zmienia danych źródłowych

# .min() i max()

Przykład

minimum_price = prices.min()
maximum_price = prices.max()

Otrzymujemy dwie wartości :

20.0
700.0

Tak samo jak w SQL:

- .min() nie zwraca całego produktu
- .max() nie zwraca całego produktu

Zwracają tylko najmniejszą albo największa wartość analizowanej Series.

## Maksymalna wartość a cały rekord

Pytanie A 

Jaka jest największa cena - > rozwiązanie : 

products["price"].max()

Pytanie B : 

Który produkt jest najdroższy? 

Na obecnym poziomie powinniśmy użyć : 

```python

most_expensive_product = (
    products
    .sort_values(
        by=["price", "product_id"],
        ascending=[False,True],
    )
    .head(1)
)

```

To samo rozróżnienei występowało w SQL: 

Pytanie                 SQL                         Pandas
największa wartosć      MAX(column)                 series.max()
cały rekord             ORDER BY ... DESC LIMIT 1   sort_values(...).head(1)

## Filtrowanie przed agregacją

Przykładowe dane:

products = pd.DataFrame(
    {
        "products_id":[1,2,3,4],
        "category": ["accessories", "office", "accessories", "screens"],
        "price": [250.0, 20.0, 120.0, 700.0],
    }
)

Pytanie

Jaka jest suma cen produktów z kategorii accessories? 

proces : 

```py

category_mask = products["category"] == "accessories"
selected_prices = products.loc[category_mask, "price"]
total_price = selected_prices.sum()

total_price = (
    products.loc[
        products["category"] == "accessories",
        "price",
    ]
    .sum()
)

```

Odpowiednik SQL 

SELECT SUM(price)
FROM products
WHERE category = 'accessories';

## Kolejnośc operacji ma znaczenie 

Poprawny model 

Data frame
\/ maska
pasujące wiersze
\/ wybór kolumny
Series wartości
\/ agregacje
skalar albo Series podsumowania

Nie możemy najpierw wykonać .sum() a później filtrować wyniku maską. Po .sum() nie ma już rekordów. Mamy tylko jedną liczbę

Niepoprawna kolejność myslenia: 

agregacja -> filtrowanie rekordów 

Poprawna kolejność

filtrowanie rekordów -> agregacja

## Kilka agregacji jako osobne skalary 

Można zapisać 

price_count = prices.count()
total_price = prices.sum()
average_price = prices.mean()
minimum_price = prices.min()
maximum_price = prices.max()

Każda zmienna przechowuje jeden wynik

Ten sposób jest czytelny i dobry podczas nauki i debugowania. Widzimy wtedy każdy krok osobno. 

## .agg() - kilka agregacji jednym poleceniem 

Gdy już rozumiemy pojedyncze metody możemy przygotować raport : 

price_summary = prices.agg(["count", "sum", "mean", "min", "max])

Wynikiem jest Series

count 4.0
sum 1090.0
mean 272.5
min 20.0
max 700.0

Indeks Series zawiera nazwy agregacji : 

count, sum, mean, min, max

To nie jest pięć wierszy wejściowych. Jest to pięc metryk opisujących jeden zbiór wartości

## Dlaczego count może wyglądać jak 4.0 ? 

Wynik .agg([...]) jest jedną Series. Wszystkie jej elementy mają wspólny typ.

Jezeli suma, średnia, minimum i maksimum są liczbami zmiennoprzecinkowi, Pandas może przechowywać również wynik count jako : 

4.0

Liczba policzonych wartości nadal wynosi cztery. Zapis 4.0 nie oznacza czterech i kawałka. Wynika ze wspólnego typu Series.

## Zaokrąglanie raportu

Zaport zwrócony przez .agg() możemy zaokrąglić:

rounded_summary = price_summary.round(2)

.round(2) - zwraca nową Series. Nie zmienia źródłowych cen.

Nie zaokrągalamy danych przed obliczeniem średniej, jeżeli pytanie dotyczy średniej oryginalnych wartości. Najpierw wykonujemy agregację, potem sfromatujemy wyniki. 

## .agg() po filrtowaniu 

Możemy połączyć poznane etapy - > 

category_mask = products["category"] == "accessories"
selected_prices = products.loc[category_mask, "price"]

category_summary = selected_prices.agg(
    ["count", "sum", "mean", "min", "max"]
)

```python

category_summary = (
    products.loc[
        products["category"] == "accessories",
        "price",
    ]
    .agg(["count", "sum", "mean", "min", "max"])
)

```

## Pusty zbiór w Pandas

Przykład : 

empty_prices = products.loc[
    products["category"] == "nonexistent",
    "price"
]

Ta Series nie zawiera żadnych wartości.

Typowe wyniki:

len(empty_prices) # 0 
empty_prices.count() # 0 
empty_prices.sum() # 0.0
empty_prices.mean() # NaN
empty_prices.min() # NaN
empty_prices.max() # Nan

Nan oznacza brak możliwego do obliczenia wyniku liczbowego. 

## Ważna różnica: pusty zbiór w SQL i PANDAS

Operacja                SQL Dla pustego zbioru              Pandas domyślnie
liczba                  0                                   0
suma                    NULL                                0.0
średnia                 NULL                                NaN
minimum                 NULL                                NaN
maksimum                NULL                                Nan

Najbardziej zdradliwa różnica dotyczy sumy

Pandas domyślnie pozwala, aby suma pustej Series wynosiła 0.0. 
SQL zwraca NULL

To nie jest drobiazg. Przy porównywaniu raportów z dwóch technologii musimy wiedzieć że : 

- naprawdę wystąpiły rekordy o sumie 0
- nie było żadnych rekordów
- wszystkie wartości były puste

## min_count=1 - suma wymagających wartości : 

Jeżeli chcemy, aby suma pustej Series zwróciła brak wyniku, używamy : 

empty_prices.sum(min_count=1)

Wynik 

NaN

min_count=1 oznacza

Do obliczenia sumy wymagam co najmniej jednej niepustej wartości : 

To zachowanie jest bliższe SQL-owemu SUM() dla pustego zbioru.

Nie używamy min_count = 1 mechanicznie wszęzie. Najpierw ustalamy znaczenie biznesowe, którego potrzebuje raport.

## Domyślne pomijanie braków - skipna = True

Większość omawianych metod domyślnie pomija NaN:

values = pd.Series([100.0, None, 300.0])

values.sum() # 400.0
values.mean() # 200.0
values.min() # 100.0
values.max() # 300.0

Domyślnie działa parametr :

skipna=True

Po wymuszeniu:

values.sum(skipna=False)
values.mean(skipna=False)

wynikiem będzie NaN, ponieważ brak danych uczestniczy w obliczeniu

Pytanie nie brzmi więc tylko : 

Jak policzyć średnią ? 

Profesjonalne pytanie : 

Czy brakujące wartośći powinny zostać pominiętę, potraktowane jako zero czy zgłoszone jako problem jakości danych. 

## Agregacje nie zmieniają źródłowego DataFrame 

Operacje : 

orders["total_amount"].sum()
orders["total_amount"].mean()
orders["total_amount"].agg(["min", "max"])

nie zmieniają orders.

Po zadanich można sprawdzić print(orders.shape) - > Nadal wynikiem powinno vbyć (12,5)

## SQL i PANDAS - pełne porównanie procesu

Pytanie : 

Jaka jest średnia cena produktów z kategorii accessories ? 

SQL - 

SELECT ROUND(AVG(price), 2) AS average_price
FROM products
WHERE category = 'accessories';

```python

category_mask = products["category"] == "accessories"
seelcted_price = products.loc[category_mask, "price"]
average_price = round(selected_prices.mean(), 2)

# łańcuch

average_price = round(
    products.loc[
        products["category"] == "accessories",
        "price"
    ]
    .mean(),
    2,
)

```

Mapowanie : 

SQL                 PANDAS
FROM products       DataFrame products
WHERE ...           maska i .loc[]
price               wybrana Series
AVG(price)          .mean()
ROUND(...,2)        round(...,2)

## Typ wyniku zależy od operacji

Przed uruchomieniem kodu, najlepiej jak będziemy przewidywć nie tylko wartość, ale również typ wyniku. 

Kod                                             Typowy Wynik
orders                                          DataFrame
order["total_amount"]                           Series
orders.loc[mask]                                DataFrame
orders.loc["mask", "total_amount"]              Series
len(orders)                                     liczba całkowita
orders["total_amount"].sum()                    skalar liczbowy
orders["total_amount"].agg([...])               Series
orders.count()                                  Series

To częśty temat rozmów technicznych i bardzo pomocny przy etapie debugowania. 

## Precyzja liczb zmiennoprzecinkowych 

Kwoty są zapisane jako float. Komputer przechowuje takie liczby binarnie, dlatego czasami może pojawić się wynik podobny do : 

129.826666666666666666666666

To nie musi oznaczać błędu w danych

Do prezentacji raportu możemy użyć 

round(result, 2)

Podczas kontroli sum zaokrąglamy obie strony dopiero po obliczeniu 

round(status_total, 2) == round(all_total, 2)

W prawdziwych systemach finansowych często użwa się typu dzisiętnego zamiast float, ale Decimal nie jest tematem na dzisiaj. 

## Czego nie robimy dzisiaj ? 

Dzisiaj jeszcze nie wprowadzamy groupby() itp. Narzędzia te zostawimy na później. 


