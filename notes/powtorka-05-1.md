# R5

## Dlaczego pliki to serce Data Engineeringu ? 

Pipeline danych ma trzy etapy i nazywa się **ETL**:

```text
EXTRACT                   TRANSFORM               LOAD
(wyciągnij)               (przekształć)           (załaduj)
    |                           |                     |
plik / API   --------->  Twój Python   ---------> plik / baza
orders.csv              filtruj, licz               valid_orders.csv
```

**Wszystko co powtarzaliśmy do tej pory, to środkowa kolumna** . Formatowanie tekstu, bezpieczny dostęp, pętle, liczniki. Brakowało lewej i prawej : 
Skąd dane przychodzą i dokąd idą **R5 domyka lewą i prawą strone tego obrazka**

Po R5 powinenem napisać komplety pipeline. Nie fragment - całość.

Dlaczego CSV ? Bo to najczęstszy format wymiany danych między systemami : 
banki, sklepy, systemy magazynowe, eksporty z Excela, wyniki zapytań SQL. Zanim dojdzie się do Parquet, Json-a i baz - przechodzi się przez CSV. Wszędzie 

---

## `open()` i `with` - otwieranie, zamykanie 

Żeby dobrać się do pliku, trzeba go **otworzyć**, a po robocie **zamknąć** 

```python

with open("dane.csv", "r", encoding="utf-8") as file:
    test = file.read()
    # Tutaj plik jest JUŻ zamknięty - automatycznie 
```

`with` czytamy tak : otwórz plik, daj mi go nazwą `file`, a jak skończę ten blok - zamknij go, cokolwiek się wydarzy. Nawet gdy w środku poleci wyjątek, plik zostanie zamknięty. To się nazywa **context manager** ( menadżer kontekstu). 

**Dlaczego to ważne w praktyce** : niezamknięty plik to zablokowany zasób systemu. Przy jednym pliku nie zauważysz. Przy pipeline czytającym 5000 plików w pętli - program padnie na "too many open files". A na Windowsie niezamkniętego pliku często **nie da się usunąć ani nadpisać**

**Zasada** - zawsze `with`

## 3. `encoding="utf-8" - dlaczego zawse 

Plik na dysku to ciąg **bajtów** - liczb. `encoding` mówi Pythonowi, jak zmienić te liczby na litery. 

```python
with open("dane.csv", "r", encoding="utf-8") as file:
```

Gdy pominę `encoding`. Python bierze **domyśle kodowanie systemu**. Na Linuksie i Macu to zwykle UTF-8, więc działa, ale na Windowsie bywa również i wtedy polskie znaki potrafią się wysypać, bądź cały program potrafi się wywalić - > `UnicodeDecodeError`. 

Kod ma działać na wszystkich systemach. Na windowsie, linuksie i macu. Dlatego zawsze należy podać `encoding="utf-8`. Przy odczycie i zapisie. 

## 4. Tryby otwarcie `"r"`, `"w"`, `"a"` 
Drugi argument `open()` mówi, **co zamierzasz z plikiem zrobić**:

| Tryb | Nazwa | Co robi | Gdy plik nie istnieje |
|------|-------|---------|----------------------|
| `"r"` | read | czyta | ❌ `FileNotFoundError` |
| `"w"` | write | pisze — **kasuje całą dotychczasową treść!** | tworzy nowy |
| `"a"` | append | dopisuje na końcu | tworzy nowy |

```python
open("plik.csv", "r", encoding="utf-8") # czyta plik
open("plik.csv", "w", encoding="utf-8") # Pisze od zera, stara treść ginie 
open("plik.csv", "a", encoding="utf-8") # Dopisuje na końcu 
```
> **`"w"` kasuje plik w momencie otwarcia**, jeszcze zanim cokolwiek zapiszę.
> Otworzysz przez pomyłkę plik źródłowy w trybie `"w"` - dane przepadły. Nie ma cofnięcia
> W tym bloku zawsze zapisujemy do `output/`, nigdy do `data/` 

---

## Czytanie pliku tekstowego linia po linii

Otwarty plik można przejść **pętlą `for`** - dokładnie tak jak listę. 

```python

lines = []
with open ("notatka.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))
reutrn lines
```

**Skąd `rstrip("\n")`** - Każda linia w pliku kończy się niewidzialnym znakiem nowej linii `\n`. Gdy Python ją wczyta, ten znak zostaje w tekście :

```python
"Anna\n"          # Tak wygląda przed obcięciem
"Anna"            # Tak po obięciu 
```

**Dlaczego `.rstrip("\n")`, a nie `.strip()`** `.strip()` obcina spacje **z obu stron** - zguiłbym wcięcia i spacje na początku linii, które mogą być częścią danych. 
`.rstrip("\n")` - obcina tylko z prawej strony i tylko znak nowej linii. Precyzyjnie to, co chcemy. 

**Wariant alternatywny** 

```python
with open("notatka.txt", "r", encoding="utf-8") as file:
    return file.read().splitlines()
```

`.read()` - wciąga cały plik do jednego stringa. `.splitlines()` tnie go na listę bez znaków końca linii. Krócej **ALE** trzyma cały plik w pamięci naraz - przy pliku na 10GB to katastrofa. Pętla `for line in file:` czyta po jednej linii i pamięc zostaje wolna.

**Zasada DE:** - przy dużych danych zawsze pętla, nie `.read()`. 

## 6. CSV `csv.reader` vs `csv.DictReader`

Plik CSV to tabela zapisana jako tekst:

```text
order_id,customer_name,total_amount,status
1001,Anna Kowalska,149.99,paid
1002,Piotr Nowak,89.50,pending
```

Można by go czytać jak zwykły tekst i ciąć po przecinku (`.split(",")`) ale **nie robić tego w ten sposób!!!**. Wystarczy jedno pole, zawierająće przecinek w cudzysłowie:

```text
1003, "Kowalska, Anna", 220.00, paid
```

i Twój `.split(",")` rozjeżdza cały wiersz. Moduł `csv` z biblioteki standardowej zna te zasady i obsłuży je za mnie. 

```python

import csv

with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```text
['order_id', 'customer_name', 'total_amount', 'status']   # <- naglowek tez przychodzi!
['1001', 'Anna Kowalska', '149.99', 'paid']
```

Dostaje się ten moduł po **indeksie**: `row[0]`, `row[1]`, `row[2]`. 

**PROBLEM** - Kod staje się nieczytelny (`row[2]` - co to było?) i kruchy. Ktoś zmienia kolejność kolumn w źródle. 
Mój (`row[2]`) - nadal działa ale czyta co innego. Program się nie wywali, po prostu policzy bzdury. 
**To najgorszy rodzaj błędu w danych - Cichy**

### `csv.DictReader` - wiersz jako słownik 

```python
with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

```text
{'order_id': '1001', 'customer_name': 'Anna Kowalska', 'total_amount': '149.99', 'status': 'paid'}
{'order_id': '1002', 'customer_name': 'Piotr Nowak', 'total_amount': '89.50', 'status': 'pending'}
```

Dostaje się po nazwie kolumny `row["customer_name"]`. - Czytelne i odporne na zmianę kolejności kolumn.

Nagłówka nie ma, poszedł na klucze. 

** Dwie rzeczy które `DictReader` robi za mnie** 

1. Pierwszą linię trakuje jako nagłowek - i robi z niej klucze - nie dostanę jej jako wierszy danych 
2. Każdy kolejny wiersz zamienia w słownik.

`DictReader` daje dokładnie taką strukturę, na której ćwiczyliśmy w poprzednie dni - wszystko co napisałem w poprzednich blokach, zadziała na wierszach z CSV. 

**w R5 używamy wyłącznie `DictReader` - `csv.reader` - znam, wiem o co chodzi, ale w prakyce używa się `DictReader`

### Zwijanie do listy

```python
with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
return rows
```

`list(reader)` - przechodzi cały czytnik i pakuje wierwsze do listy. Równoważne pętli z `.append()`, tylko krócej 

> **`rows = list(reader)` musi być w ŚRODKU bloku `with`.** Poza nim, plik jest już zamknięty i dostanę `ValueError: I/O opertaion on closed file`. 

--- 

## 7. Wszystko z csv jest TEKSTEM

**To jest jedno w ważniejszych zdań w tym rozdziale** /\ 

```python
row = {"order_id": "1001", "total_amount": "149.99", "status": "paid"}
#                   ^^^^^^                 ^^^^^^^^
#                   TEKST                  TEKST, nie liczba!
```

w pliku widać `149.99` i mózg mówi liczba. Python widzi jedynie znaki. Moduł csv nie zgaduje typoów - i bardzo dobrze, bo zgadywanie typów to źrodło koszmarnych błędów. 

Co z tego wynika ? : 

```python
row["total_amount"] + 10         # TypeError : can only concatenate str
row["total_amount"] > 100        # TypeError '>' not supported str vs int
float(row["total_amount"]) + 10  # 159.99
``` 

A gdy pole jest puste, albo zaśmiecone, samo float wywala program, należy użyć bezpiecznie narzędzie z R2 - safefloat 

```python
amount = to_float(row.get("total_amount"))
if amount is None:
    amount = 0.0
```

**Reguła** - każda wartość z CSV, której chcesz użyć jako liczby, przechodzi przez `to_float`. Bez wyjątków. 

---

## 8. Nagłówki - `fieldnames` 

Czasami chcemy same nazwy kolumn, bez danych. `DictReader` trzyma je w `fieldnames`:

```python
with open("orders.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames     # ['order_id', 'customer_name', 'total_amount', 'status']
```

**Pułapka** 0 dla pustego pliku `.fieldnames` to `None`, a nie `[]`. A `None` później w kodzie, który spodziewa się listy, wybucha przy pierwszej pętli. 
Zabezpieczamy się w następujący sposób : 

```python
header = reader.fieldnames or []   # None -> []
```

`or` czytamy jako *weź `reader.fieldnames`, a jak to jest fałszywe (`None`) - weź `[]`*
To mechanizm truthiness 

**Drugi sposób na nagłowki** - z kluczy pierwszego wiersza: 

```python
headers = list(rows[0].keys())         # Działa tylko wtedy, gdy rows nie jest puste
```

Kiedy które ? PLik z samym nagłówkiem, bez danych, ma nagłówki ale zero wierszy. Wtedy `rows` jest puste i `rows[0]` wybuchnie `IndexError`. `fieldnames` zadziała. Ale przy zapisie masz tylko listę słowników - wtedy `rows[0].keys()` jest jedyną drogą

## 9. Zapis `csv.DictWriter` i `newline=""`

Odwrotność `DictReader`. Bierzę liste słowników i zapisuje jako CSV:

```python

import csv

rows = [
    {"order_id": "1001", "customer_name": "Anna", "status": "paid"},
    {"order_id": "1002", "customer_name": "Piotr", "status": "pending"},
]

headers = list(rows[0].keys()) # nazwy kolumn z pierwszego wiersza 

with open("output/wynik.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)0
```
Cztery rzeczy o których należy pamiętać:

1. **`fieldnames=headers`** - obowiązkowe - `DictWriter` musi wiedzieć, jakie kolumny i w jakiej kolejności ma zapisać. Ta lista wyznacza kolejność w pliku wynikowym.
2. `writer.writerheader()` - łatwo zapomnieć - bez tego plik nie ma peirwszej linii z nazwami kolumn. Wygląa prawie dobrze, a potem `DictReader` przy odczycie weźmie pierwszy wiersz danych za nagłówek i go zgubi z wyniku. 
3. `writerows(rows)` vs `write(row)` - liczba mnoga bierze całą listę, pojedyńcza jeden słownik. `writerows(rows)` == pętla `for row in rows: writer.writerow(row)`
4. `newline=""` - Na Windowsie obowiązkowe - Bez tego dostanę pustą linie między każdymi dwoma wierszami 

```text
order_id,customer_name

1001,Anna

1002,Piotr
```

Powód: moduł `csv` sam wstawia `\r\n` na końcu wiersza, a Windows dokłada od siebie drugie `\r`. `newline=""` mówi : * nie tłumacz znaków końca linii, `csv`  wie co robi. Do zapamiętania - **do zapisu CSV zawsze `newline=""`

---

## 10. `pathlib.Path - ścieżki jako obiety

Ścieżkę mozna trzymać jako zwykł tekst, ale to się często źle kończy 

```python
sciezka = "output" + "/" + "wynik.csv"    # ukośnik na sztywno
sciezka = "output\\wynik.csv"      # działa tylko na windows 
```

Windows używa `\`, Linux i Mac `/`. Serwer, na którym w końcu wyląduje kod, prawie na pewno stoi na Linuksie. Dlatego ścieżek nie należy sklejać ręcznie. 

```python
from pathlib import Path
```

`Path` to obiekt reprezentujący ścieżkę i sam wie, jakiego separatora użyć.

### Budowanie ścieżek ukośnikiem `/`
```python
folder = Path("output")
plik = folder / "wynik.csv"    # Path('output/wynik.csv')
gleboko = Path("output") / "2026" / "sierpien" / "wynik.csv"
```

To nie jest dzielenie. Operator `/` między `Path` a tekst został **przedefinioawny** na "sklej ścieżkę. Czyta się naturalnie, bo wygląa jak ścieżka. 

### Od czego liczy się ścieżka względna - `__file__` 

Zostaje pytanie, które łatwo przeoczyć `Path("data/orders.csv")` - od czego liczony jest ten `data/`?

Nie od pliku `.py` w którym napiłem **Od katalogu, z którego uruchomiłem program (cwd - current working directory).

```python
rows = read_csv_rows("data/orders.csv") # Działa, zależnie od tego, gdzie uruchamiam program. 
```

Odpalnie z głownego programu działa, gdy wejdziemy w inny folder to niestety już dostaniemy bład `FileNotFoundError`. Kod się nie zmienił, plik się nie ruszył, a mimo to nie działa. 

**Rozwiązanie** 

```python
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ORDERS_FILE = DATA_DIR / "orders.csv"
```

- `__file__` - zmienna, którą Python ustawia sam w każdym module: ścieżka do tego pliku 
- `.resolve()` - zmiana na ścieżkę absolutną.
- `.parent` - katalog w którym plik leży. 

Teraz program będzie działa niezależnie od tego, skąd się odpali. 

### Metody, któe należy znać 

```python
p = Path("src/day_20_csv/data/orders.csv")

p.exists() # True / False - czy istnieje?
p.name # 'orders.csv' - sama nazwa pliku
p.stem # 'orders' - nazwa bez rozszerzenia 
p.suffix # '.csv' - samo rozszerzenie
p.parent # Path('src/day_20_csv/data') - katalog nadrzedny
```

### Tworzenie katalogu

Zapis do `output/wynik.csv` wywali program, gdy katalog `output/` nie istenieje. 
Python nie tworzy katalogów sam :

```text
FileNotFoundError: [Errno 2] No such file or directory: 'output/wynik.csv'
```

Mylące, prawda? Komunikat mówi o pliku, a brakuje **katalogu**

```python
Path("output").mkdir(parents=True, exist_ok=True)
```

- `parents=True` - utwórz tez brakujące katalogi po dorze (`output/2026/sierpien`) za jednym razem. Bez tego dostanę błąd, jeśli brakuje pośredniego poziomu
- `exist_ok=True` - Jak katalog już jest, nie rób afery. Po prostu przejdź dalej.

**Te dwa argumenty ustawiamy zawsze razem** : Efekt - > Upewnij się że ten katalog istnieje - bezpiecznie do wywołania ile razy chcesz. Nazywa się to **idempotencją** - operacja, która można powtórzyć bez zmiany wyniku. Bardzo ważne pojęcia w pipeline'ach, bo pipeline'y się restartuje.

Przy zapisie pliku interesuje nas **katalog nadrzędny**

```python

path = Path("output/2026/wynik.csv")
path.parent.mkdir(parents=True, exist_ok=True) # Tworzy output/2026
# dopiero teraz najlepiej otworzyć ten plik do zapisu 
```

### `Path` czy `str` ? 

`open()` przyjmuje oba. Moje funkcje też powinny. Wystarczy jedna linia na wejściu: 

```python
def moja_funkcja(path):
    path = Path(path)     # tekst -> Path, Path - > Path ( bez zmian )
```

`Path(Path("x"))` to nadal `Path("x")` - bezpiecznie. Ta linia to bramka wejściowa. Od niej w dół mamy gwarancję, że pracujemy na `Path` i można wołać `.exists()`, `.parent`, `/`. Diagnostyka Dnia 21 mówi wprost. Może być Stringiem albo obiektem Path. Kod nadal musi sobie radzić z obydowma

---

## Brak pliku 

Plik może nie istnieć. To nie jest przypadek brzegowy, to codzienność. Dostawca nie wysłał danych, ktoś zmienił nazwę, katalog jeszcze jest pusty. 

Pipeline **nie ma prawa się wywalić** - z tego powodu. Ma zwrócić pusty wynik i hecać dalej. 

### Droga A - Sprawdź przed (LBYL) 

```python
path = Path(path)
if not path.exist():
    return []
with open(path, "r", encoding = "utf-8") as file:
    ...
```

**look Before You Leap* - popatrz zanim skoczysz. Czytalne. Wychodzisz z funkcji wcześnie. 

### Droga B - spróbuj i złap (EAFP)

```python
try:
    with open(path, "r", encoding="utf-8") as file:
        ...
except FileNotFoundError:
    return []
```

**Easier to Ask forgiveness then Permission** - łatwiej prosić o wybaczenie niż o pozwolenie. To bardziej *pythonowy* styl 

## 12 Round-trip - zapisz i odczytaj 

To sprawdzian : zapisz dane, odczytaj z powrotem, porównaj z orginałem. Jeśli się zgadza - zapis i odczyt są spójne.

```python
rows = [{"a": "1", "b":"2"}]
write_csv_rows("output/test.csv", rows)
wczytanie = read_csv_rows("output/test.csv")
assert wczytane == rows

