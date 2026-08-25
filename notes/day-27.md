# PANDAS W PRAKTYCE sort_values(), head(), isin() i between()

## MAPA SQL i PANDAS odpowiadające na te same pytania : 

Pytanie                                     SQL                     PANDAS
Które wiersze spełniają warunek?            WHERE                   maska i .loc[]
Które kolumny pokazać?                      SELECT col_1, col_2     .loc[:, ["col_1", "col_2"]]
Jak ułożyć wiersze                          ORDER BY                .sort_values()
Ile pierwszych wierszy zwrócić              LIMIT                   .head()
Czy wartość należy do listy ?               IN                      .isin()
Czy wartość jest poza listą?                NOT IN                  ~isin()
Czy liczba jest w przedziale                BETWEEN                 .between()
Czy liczba jest poza przedziałem            NOT BEETWEEN            ~.between()

## sort_values() - odpowiednik ORDER BY

Metoda

```python

dataframe.sort_values(by="column_name")

```

zwraca wiersze ułożone według wskazanej kolumny 

Przykładowy DataFrame products: 

product_name                        category                price
Keyboard                            electronics             250
Notebook                            stationery              20
Mouse                               electronics             120
Monitor                             electronics             700

Kod:

```python

sorted_products = products.sort_values(by="price")

Da kolejność cen : 
```

20 -> 120 -> 250 -> 700

Paramter 

by = "price" mówi -> użej kolumny price jako kryterium sortowania.

SQL-owy odpowiedik -> ORDER BY price

## Sortowanie rosnąco 

Domyślnie sort_values() sortuje rosnąco: 

sorted_products = products.sort_values(by="price")

Jawny zapis : 

```python

sorted_products = products.sort_values(
    by="price",
    ascending=True,
)
```
Obie wersje dadzą ten sam wynik. Domyślnie ascending jest True, ale na początku warto pisać go jawnie, utrwalamy znaczenie parametru

Pandas                  SQL
ascending = True        ASC
sortowanie domyślne     ASC domyślnie

## Sortowanie malejące 

Aby sortować malejąco, od największej do najmniejszej : 

sorted_products = products.sort_values(
    by="price",
    ascending = False,
)

Odpowiednik SQL -> ORDER BY price DESC 

## Sortowanie po kilku kolumnach 

Załóżmy że chcemy 

1. Ułożyć produkty alfabetycznie według kategorii
2. Wewnątrz każdej kategorii ułożyć ceny malejąco. 

```python

sorted_products = products.sort_values(
    by=["category", "price"],
    ascending = [True, False],
)

```

Każda pozycja z ascending odpowiada pozycji z by

category -> True -> Czyli rosnąco
price -> False -> czyli malejąco

SQL-owy odpowiednik 

```sql

ORDER BY category ASC, price DESC;

```

Najpierw działa pierwsze kryterium. Drugie rozsztrzyga kolejność w obrębie takiej samej wartości pierwszej kolumny.

## Długość list musi się zgadzać

Jeżeli zapisujemy dwie kolumny :

by=["category", "price"]

I chcemy nadać im różne kierunku, podajemy dwie wartości :

ascending = [True, False]

Błędna liczba kierunków : 

```python

products.sort_values(
    by=["category", "price"],
    ascending=[True],
)

```

Jest błędne /\ 

Ale można podać, nie w liście 

```python

products.sort_values(
    by=["category", "price"], 
    ascending = True,
)

```

Wtedy ten sam kierunek zostanie użyty dla wszystkich wskazanych kolumn. 

## Trzecia kolumna jako rozstrzygnięcie remisu 

Wyobraźmy sobie, że dwa produkty z tą samą kategorią i ceną. 

KOd : 

```python

products.sort_values(
    by=["category", "price"],
    ascending=[True, False],
)
```
nie określa ich wzajemnej kolejności biznesowej. 

Można dodać jednoznaczny identyfikator: 

```python

products.sort_values(
    by=["category", "price", "product_id"],
    ascending=[True, False, True]
)
```
Dobra praktyka - Jeżeli kolejność ma znaczenie, należy dodać kryterium rozstrzygające remis. 


Ta sama zasada obowiązuje w SQL 

## sort_values() domyślnie nie zmienia źródła 

Kod

```python

sorted_products = products.sort_values(
    by="price",
    ascending=False,
)

```

Tworzy nowy wynik i przypisuje go do `sorted_products`.

DataFrame `products` pozostanie w swojej wcześniejszej kolejności.

Na tym etapie to zalecany styl, później przejdziemy do `inplace

W pracy z danymi jest ważna zasada, aby zachować dane wejściowe, a kolejne wyniki zapisywać pod opisowymi nazwami.

## indeks po sortowaniu 

DataFrame ma indeksy. W naszym pliku po wczytaniu będzie on wyglądał początkowo tak 

0, 1, 2, 3, ..., 11 

Po sortowaniu wartośc iindeksu przemieszczą sie razem ze swoimi wierszami 

Przykład

1   Notebook    20
2   Mouse       120
0   Keyboard    250
3   Monitor     700

Indeks

1,2,0,3

Nie oznacza błędu. Informuje, z którego wiersza źródłowego pochodzi rekord. 

W dalszych zadanich :

- nie resetujemy indeksu
- sprawdzamy kolejnośćs po order_id
- nie zakładamy że indeks po sortwaniu musi być 0,1,2,...,

reset_index() będzie w późniejszym etapie. 

## head() - pierwsze wiersze bieżącego wyniku 

Pokazuje 5 pierwszych wierszy w DF. 
Można manipulować i wpisać head(3) - pokaże tylko 3 wiersze. 

SQL-owy odpowiednik LIMIT 3 

Ważna różnica : 

- w SQL LIMIT jest klauzulą zapytania
- w Pandas head() jest metodą wywoływaną na DataFrame

## Najpierw sortowanie potem head()

Chcemy znaleźć 3 najdroższe produkty.

Poprawna kolejność myslenia

- ułóż wszystkie produkty od najdroższego
- pobierz pierwsze trzy 
Kod na przykładowych danych 
```python
sorted_products = products.sort_values(
    by="price",
    ascending=False,
)

top_three = sorted_products.head(3)

```

Można przeczytać : 

Posortuj produkty malejąco po cenie, a następnie weź trzy pierwsze.

Odpowiednik SQL 

```sql

SELECT order_id, product, price
FROM products
ORDER BY price DESC
LIMIT 3;

```

Najważniejsza zasada dnia : 

head() mówi ile, a wcześniejsze operacje mówią "które wiersze będą pierwsze" 

## Kolejnośćś operacji zmienia odpowiedź 

```python

result_a = (
    products
    .sort_values(by"price", ascending=False)
    .head(3)
)

## oraz : 

result_b = (
    products
    .head(3)
    .sort_values(by="price", ascending=False)
)

```

result_a : 

1. sortuje cały zbiór 
2. wybiera trzy najdroższe rekordy 

result_b : 

1. bierze pierwsze trzy koredy z pliku
2. sortuje tylko te trzy rekordy 

To nie jest ten sam wynik - Metody Pandas wykonują się w kolejności, w której je zapisujemy. 

## isin() - odpowiednik IN 

w SQL

```sql

WHERE category IN ('electronics', 'stationery')
```
w Pandas tworzymy maskę:

```python
category_mask = products["category"].isin(["electronics", "stationery"])
```

Wynikiem isin() jest Series zawierająca wartości logiczne: 

True
True
True
True

Każda wartość odpowiada jednemu wierszowi. 

Następnie filtrujemy za pomocą .loc[]

selected_products = products.loc[category_mask]

Czytamy

Sprawdź, czy kategoria każdego produktu znajduje się na liście dopuszczalnych kategorii, a potem pozostaw wiersze, dla których wynik jest prawdziwy. 

## isin() oczekuje wartośći podobnych do listy

Poprawnie 

```python

products["category"].isin(["electronics"]) 

```

Nawet jeśli sprawdzamy tylko jedną wartość, przekaż ją liście. 

Pojedyńczy tekst ni ejest tutaj listą dopuszczalnych wartości. Pandas zgłosi błąd typu

Dla jednej wartości zwykle prościej użyć : 

```python

products["category"] == "electronics"

``` 

Dla kilku konkretnych wartości isin() jest czytelniejsze niż wiele porównań połączonych przez | 

## Nie używamy operatora in dla całej Series

Pythonowy operator 

`value in collection` 

jest przydatny dla zwykłych list, słoników i innych kolekcji. 

Nie zapisujemy jednak maski Pandas w ten sposób. 

products["category"] in ["electronics", "stationery"]

Chcemy wykonać sprawdzenie osobno dla każdego wiersza, dlatego używamy : 

products["category"].isin(["electronics", "stationery"])

Do zapamiętania : 

Sytuacja                                    Narzędzie
jedna zwykła wartość i zwykła kolekcja      in
każda wartość w pandasowej Series           .isin()

## Odwracanie maski przez ~ 

NOT IN oznacza, że interesują Cie wartości spoza wskazanej listy.

Najpierw zwykła maska: 

category_mask = products["category"].isin(["electronics", "stationery"])

Odwrócona maska : 

outside_category_mask = ~products["category"].isin(
    ["electronics", "stationery"]
)

operator `~` zmienia : 

- True na False
- False na True
Nie używamy not

`not` oczekuje jednej wartość ilogicznej. Maska pandas zawiera osobną wartość logiczną dla każdego wiersza. 

## between() - odpowiednik BETWEEN

W SQL 

WHERE price BETWEEN 100 AND 300

W Pandas

```python

price_mask = products["price"].between(100,300)

```

Metoda zwraca maskę logiczną. Następnie można uczyć : 

selected_products = producst.loc[price_mask]

Czytamy : 

Dla każdej ceny sprawdź, czy mieści się od 100 do 300

Domyślnie obie granice są uwzględnienione. 

## Granice between ()

Kod 

products["price"].between(100, 300)

jest odpowiednikiem 

(products["price"] >= 100) & (products["price"]<=300)

Obejmuje 

- 100
- wszystkie wartości pomiędzy 
- 300
Można to zapisać jako przedział domknięty : 

[100, 300]

Metoda ma parametr `inclusive`, ale w dzisiejszych zadanich używamy domyslnego zachowania `inslusive=both` 

## Kolejność granic 

Poprawnie : 

products["price"].between(100, 300)

Najpierw dolna, później górna granica. Pandas nie zmieni argumentów automatycznie. 

## NOT BETWEEN

W SQL 

```sql

WHERE price NOT BETWEEN 100 AND 300
```
w Pandas

```python

outside_price_mask = ~products["price"].between(100,300)
```
Czyli pozostają wartości mniejsze niż 100 albo większe niż 300

Granica 100 i 300 należą do zwykłego between() dlatego po odwróceniu maski nie należą do wyniku.

## Łączenie isin() i between()

Maski można łączyć przez & 

```python

category_mask = producst["category"].isin(["electronics", "office"])

price_mask = products["price"].between(100,500)

final_mask = category_mask & price_mask 

selected_products = products.loc[
    final_mask,
    ["product_name", "category", "price"],
]
```
Czytamy 

Pozostaw produkty należące do jednej ze wskazanych kategorii oraz mające cenę od 100 do 500 włącznie. Pokaż trzy wskazane kolumny.

Kazdy frament ma jedną odpowiedzialność : 

Fragment                Rola
isin()                  sprawdzanie dopuszczalnych kategorii
between()               sprawdzanie przedziału cenu
&                       oba warunki muszą być prawdziwe
.loc[]                  wybór wierszy i kolumn 

## Nawiasy przy złożonych warunkach

Można zapisać maskę bez zmiennych pomocniczych 

```python

final_mask = (
    products["category"].isin(["electronics", "office"])
    & products["price"].between(100,500)
)

# Przy zwykłych porównaniach każdy warunek zapisujemy w nawiasach : 

final_mask = (
    (products["category"] == "electronics")
    & (products["price"] >= 100)
)

```

Metody isin() i between() już zwracają kompletnie Series logiczne, ale nawias otaczający cały wielowierszowy warunek nadal zwiększa czyetlność 

Nie użwamy and ani or do łączenia masek w Pandas

Logika                      Pandas
oba warunki                 &
co najmniej jeden warunek   |
odwrócenie maski            ~

## Zalecany styl : najpierw etapy 

Na początku lepiej zapisywać rozwiązania etapami : 

```python

category_mask = products["category"].isin(["electronics", "office"])

price_mask = products["price"] == 100

final_mask = category_mask & price_mask 

filtred_products = products.loc[
    final_mask,
    ["product_name", "category", "price"]
]

sorted_products = filtered_products.sort_values(
    by=["price", "product_name"],
    ascending=[False,True],
)

result = sorted_products.head(3)

print(result)

```

Zalety

- łatwo wydrukować każdą maksę
- łatwo sprawdzić rozmiar po filtrowaniu 
- łatwo znaleźć etap, na którym powstał błąd 
- nazwy zmiennych wyjaśniają intencję
- można porównać dane źródłowe i wynik 

## Łańcuch metod 

Ten sam rodzaj procesu, można zapiasć jako łańcuch

```python

result = (
    products.loc[
        final_mask,
        ["product_name", "category", "price"],
    ]
    .sort_values(
        by=["price", "product_name"],
        ascending=[False, True],
    )
    .head(3)
)

``` 

Czytamy od góy do dołu : 

- Wybiersz pasujące wiersze i kolumny 
- posortuj wynik
- pobierz trzy pierwsze rekordy 

Łańcuch metod jest dobry gdy : 

- ma kilka czytelnych etapów
- każdy etap działa na wyniku poprzedniego 
- potrafimy wyjaśnić kolejność 
- kod nie jest zagadką



## Kolejność pełnego procesu

Dla dzisiejszych zadań używamy kolejności : 

wczytanie 
\/
kontrola
\/
utworzenie maski
\/
filtrowanie i wybór kolumn 
\/
sortowanie
\/
head
\/
wyświetlenie wyniku 

## SQL i Pandas - pełne porównanie 

Pokaż trzy najdrośze produkty z dwóch dopuszcalnych kategorii i z przediału cenowego 

```sql

SELECT product_name, category, price
FROM products
WHERE category IN ('electronics', 'office') AND price BETWEEN 100 AND 500
ORDER BY price DESC, product_name ASC 
LIMIT 3; 

```

Pandas ma ogólny kształt

```py

mask = (
    products["category"].isin(["electronics", "office"])
    & products["price"].between(100, 500)
)

result = (
    products.loc[
        mask,
        ["product_name", "category", "price"],
    ]
    .sort_values(
        by=["price", "product_name"],
        ascending=[False, True],
    )
    .head(3)
)

```

Nie należy uczyć się tych bloków na pamięć. Najlepiej powiązać każdy fragment z pytaniem 

Etap                    SQL             Pandas
dopuszcalne wartości    IN              isin()
przedział               BETWEEN         between()
oba warunki             AND             &
wybór wierszy           WHERE           maska w .loc[]
wybór kolumn            SELECT          lista kolumn w .loc[]
kolejność               ORDER BY        sort_values()
liczba rekordów         LIMIT           head()
