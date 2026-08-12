# Powtórka R5 — Pliki: CSV, ścieżki i brak pliku

**To jest najobszerniejszy blok w całym torze.** Nie dlatego, że jest najtrudniejszy —
dlatego, że dotyka **granicy Twojego programu ze światem zewnętrznym**. Do tej pory dane
miałeś podane w kodzie: listy, słowniki, wpisane na sztywno. Od teraz dane **przychodzą
z zewnątrz** i **wychodzą na zewnątrz**. To jest cała robota data engineera.

> **Zakres — sprawdzone:** wszystko poniżej robiłeś już na **dniu 18** (pliki, `open`,
> `with`, `FileNotFoundError`) i **dniu 20** (CSV, `DictReader`, `DictWriter`, `Path`,
> `mkdir`). Twój własny kod `src/day_20_csv/csv_utils.py` używa tego wszystkiego.
> To jest **prawdziwa powtórka**. Jedyny nowy element, oznaczony niżej jako
> **[NOWE]**, to fixture `tmp_path` w pytest — potrzebny, żeby testować pliki.

---

## Spis treści

- [Powtórka R5 — Pliki: CSV, ścieżki i brak pliku](#powtórka-r5--pliki-csv-ścieżki-i-brak-pliku)
  - [Spis treści](#spis-treści)
  - [1. Dlaczego pliki to serce Data Engineeringu](#1-dlaczego-pliki-to-serce-data-engineeringu)
  - [2. `open()` i `with` — otwieranie i zamykanie](#2-open-i-with--otwieranie-i-zamykanie)
  - [3. `encoding="utf-8"` — dlaczego zawsze](#3-encodingutf-8--dlaczego-zawsze)
  - [4. Tryby otwarcia: `"r"`, `"w"`, `"a"`](#4-tryby-otwarcia-r-w-a)
  - [5. Czytanie pliku tekstowego linia po linii](#5-czytanie-pliku-tekstowego-linia-po-linii)
  - [6. CSV: `csv.reader` vs `csv.DictReader`](#6-csv-csvreader-vs-csvdictreader)
    - [`csv.reader` — wiersz jako **lista**](#csvreader--wiersz-jako-lista)
    - [`csv.DictReader` — wiersz jako **słownik**](#csvdictreader--wiersz-jako-słownik)
  - [7. Wszystko z CSV jest TEKSTEM](#7-wszystko-z-csv-jest-tekstem)
  - [8. Nagłówki — `fieldnames`](#8-nagłówki--fieldnames)
  - [9. Zapis: `csv.DictWriter` i `newline=""`](#9-zapis-csvdictwriter-i-newline)
  - [10. `pathlib.Path` — ścieżki jak obiekty](#10-pathlibpath--ścieżki-jak-obiekty)
    - [Budowanie ścieżek ukośnikiem `/`](#budowanie-ścieżek-ukośnikiem-)
    - [Metody, które musisz znać](#metody-które-musisz-znać)
    - [Tworzenie katalogu](#tworzenie-katalogu)
    - [`Path` czy `str`?](#path-czy-str)
  - [11. Brak pliku — dwie drogi](#11-brak-pliku--dwie-drogi)
    - [Droga A — sprawdź przed (LBYL)](#droga-a--sprawdź-przed-lbyl)
    - [Droga B — spróbuj i złap (EAFP)](#droga-b--spróbuj-i-złap-eafp)
    - [Którą wybrać?](#którą-wybrać)
  - [12. Round-trip: zapisz i odczytaj](#12-round-trip-zapisz-i-odczytaj)
  - [13. **\[NOWE\]** `tmp_path` — jak testować pliki](#13-nowe-tmp_path--jak-testować-pliki)
  - [14. Pułapki, które Cię ugryzą](#14-pułapki-które-cię-ugryzą)
  - [15. Demo — URUCHOM to najpierw](#15-demo--uruchom-to-najpierw)
  - [16. Zadania](#16-zadania)
    - [Zasady](#zasady)
  - [Wyniki (wypełniaj na bieżąco)](#wyniki-wypełniaj-na-bieżąco)
  - [Słowniczek (dopisz do `notes/english/glossary.md`)](#słowniczek-dopisz-do-notesenglishglossarymd)

---

## 1. Dlaczego pliki to serce Data Engineeringu

Pipeline danych ma trzy etapy i nazywa się to **ETL**:

```text
   EXTRACT              TRANSFORM            LOAD
   (wyciągnij)          (przekształć)        (załaduj)
       │                     │                   │
   plik / API  ──────>  Twój Python  ──────>  plik / baza
   orders.csv           filtruj, licz         valid_orders.csv
```

**Wszystko, co umiałeś do tej pory — R1 do R4 — to jest środkowa kolumna.**
Formatowanie tekstu, bezpieczny dostęp, pętle, liczniki. Brakowało Ci lewej i prawej:
skąd dane przychodzą i dokąd idą. **R5 domyka lewą i prawą stronę tego obrazka.**

Po R5 potrafisz napisać kompletny pipeline. Nie fragment — całość.

Dlaczego akurat CSV? Bo to najczęstszy format wymiany danych między systemami:
banki, sklepy, systemy magazynowe, eksporty z Excela, wyniki zapytań SQL. Zanim dojdziesz
do Parquet, JSON-a i baz — przechodzisz przez CSV. Wszędzie.

---

## 2. `open()` i `with` — otwieranie i zamykanie

Żeby dobrać się do pliku, trzeba go **otworzyć**. A po robocie — **zamknąć**.

Wersja, której **nie piszemy**:

```python
file = open("dane.csv", "r")
tekst = file.read()
file.close()               # trzeba pamietac! a jak w srodku wybuchnie blad - nie zamknie sie
```

Wersja poprawna — `with`:

```python
with open("dane.csv", "r", encoding="utf-8") as file:
    tekst = file.read()
# tutaj plik jest JUZ zamkniety - automatycznie
```

`with` czytasz tak: **„otwórz plik, daj mi go pod nazwą `file`, a jak skończę ten blok —
zamknij go, cokolwiek się wydarzy"**. Nawet gdy w środku poleci wyjątek, plik zostanie
zamknięty. To się nazywa **context manager** (menedżer kontekstu).

**Dlaczego to ważne w praktyce:** niezamknięty plik to zablokowany zasób systemu.
Przy jednym pliku nie zauważysz. Przy pipelinie czytającym 5000 plików w pętli —
program padnie na „too many open files". A na Windowsie niezamkniętego pliku często
**nie da się usunąć ani nadpisać**.

**Zasada:** zawsze `with`. Nigdy gołego `open()` bez `with`.

Zwróć uwagę na wcięcie — dokładnie ta sama zasada, która ugryzła Cię w R4:

```python
with open("dane.csv", "r", encoding="utf-8") as file:
    ...                    # 4 spacje wiecej = W SRODKU bloku, plik OTWARTY
...                        # z powrotem na lewo = ZA blokiem, plik ZAMKNIETY
```

Jeśli spróbujesz czytać z pliku **poza** blokiem `with`, dostaniesz
`ValueError: I/O operation on closed file`.

---

## 3. `encoding="utf-8"` — dlaczego zawsze

Plik na dysku to ciąg **bajtów** — liczb. `encoding` mówi Pythonowi, jak zamienić te
liczby na litery.

```python
with open("dane.csv", "r", encoding="utf-8") as file:
```

Gdy pominiesz `encoding`, Python bierze **domyślne kodowanie systemu**. Na Linuksie
i Macu to zwykle UTF-8, więc działa. **Na Windowsie to bywa `cp1250`** — i wtedy:

- polskie znaki wychodzą jako krzaki: `Å‚ÃƒÂ³dÅº` zamiast `łódź`,
- albo program wybucha: `UnicodeDecodeError`.

Twój kod ma działać u Ciebie na Windowsie **i** na serwerze z Linuksem. Dlatego
**zawsze podajesz `encoding="utf-8"` jawnie** — przy odczycie i przy zapisie.

To nie jest ozdobnik. To jest jedna z najczęstszych przyczyn awarii pipeline'ów
w prawdziwych firmach.

---

## 4. Tryby otwarcia: `"r"`, `"w"`, `"a"`

Drugi argument `open()` mówi, **co zamierzasz z plikiem zrobić**:

| Tryb | Nazwa | Co robi | Gdy plik nie istnieje |
|------|-------|---------|----------------------|
| `"r"` | read | czyta | ❌ `FileNotFoundError` |
| `"w"` | write | pisze — **kasuje całą dotychczasową treść!** | tworzy nowy |
| `"a"` | append | dopisuje na końcu | tworzy nowy |

```python
open("plik.csv", "r", encoding="utf-8")    # czytam
open("plik.csv", "w", encoding="utf-8")    # pisze OD ZERA - stara tresc GINIE
open("plik.csv", "a", encoding="utf-8")    # dopisuje na koncu
```

> ⚠️ **`"w"` kasuje plik w momencie otwarcia**, jeszcze zanim cokolwiek zapiszesz.
> Otworzysz przez pomyłkę plik źródłowy w trybie `"w"` — dane przepadły. Nie ma cofnięcia.
> W tym bloku zawsze piszemy do `output/`, nigdy do `data/`.

---

## 5. Czytanie pliku tekstowego linia po linii

Otwarty plik możesz przejść **pętlą `for`** — dokładnie tak, jak listę z R3:

```python
lines = []
with open("notatka.txt", "r", encoding="utf-8") as file:
    for line in file:              # plik chodzi sie petla, linia po linii
        lines.append(line.rstrip("\n"))   # obetnij znak konca linii
return lines
```

**Skąd `rstrip("\n")`?** Każda linia w pliku kończy się niewidzialnym znakiem nowej
linii `\n`. Gdy Python ją wczyta, ten znak zostaje w tekście:

```python
"Anna\n"                    # tak wyglada linia PRZED obcieciem
"Anna"                      # tak wyglada PO .rstrip("\n")
```

**Dlaczego `.rstrip("\n")`, a nie `.strip()`?** `.strip()` obcina spacje **z obu stron** —
zgubiłbyś wcięcia i spacje na początku linii, które mogą być częścią danych.
`.rstrip("\n")` obcina **tylko z prawej i tylko znak nowej linii**. Precyzyjnie to,
co chcesz.

**Wariant alternatywny** (dobry do zapamiętania):

```python
with open("notatka.txt", "r", encoding="utf-8") as file:
    return file.read().splitlines()    # wczytaj CALOSC, potem potnij na linie
```

`.read()` wciąga cały plik do jednego stringa, `.splitlines()` tnie go na listę bez
znaków końca linii. Krócej. **Ale** trzyma cały plik w pamięci naraz — przy pliku
na 10 GB to katastrofa. Pętla `for line in file:` czyta po jednej linii i pamięć
zostaje wolna.

**Zasada DE:** przy dużych danych zawsze pętla, nie `.read()`.

---

## 6. CSV: `csv.reader` vs `csv.DictReader`

Plik CSV to tabela zapisana jako tekst:

```text
order_id,customer_name,total_amount,status
1001,Anna Kowalska,149.99,paid
1002,Piotr Nowak,89.50,pending
```

Można by go czytać jak zwykły tekst i ciąć po przecinku (`.split(",")`), ale **nie rób
tego nigdy**. Wystarczy jedno pole zawierające przecinek w cudzysłowie:

```text
1003,"Kowalska, Anna",220.00,paid
```

i Twój `.split(",")` rozjeżdża cały wiersz. Moduł `csv` z biblioteki standardowej
zna te zasady i obsłuży je za Ciebie.

```python
import csv
```

### `csv.reader` — wiersz jako **lista**

```python
with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```text
['order_id', 'customer_name', 'total_amount', 'status']    <- naglowek tez przychodzi!
['1001', 'Anna Kowalska', '149.99', 'paid']
```

Dostajesz się po **indeksie**: `row[0]`, `row[1]`, `row[2]`.

**Problem:** kod staje się nieczytelny (`row[2]` — co to było?) i **kruchy**. Ktoś
zmienia kolejność kolumn w źródle, Twój `row[2]` nadal działa, tylko czyta co innego.
Program nie wybuchnie — po prostu policzy bzdury. **To najgorszy rodzaj błędu w danych:
cichy.**

### `csv.DictReader` — wiersz jako **słownik**

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

Nagłówka **nie ma** wśród wierszy — poszedł na klucze.

Dostajesz się po **nazwie kolumny**: `row["customer_name"]`. Czytelnie i odpornie
na zmianę kolejności kolumn.

**Dwie rzeczy, które `DictReader` robi za Ciebie:**
1. **Pierwszą linię traktuje jako nagłówek** i robi z niej klucze — nie dostaniesz
   jej jako wiersz danych.
2. Każdy kolejny wiersz zamienia w słownik.

I zobacz, co się właśnie stało: **`DictReader` daje listę słowników — czyli dokładnie
tę strukturę, na której ćwiczyłeś przez R2, R3 i R4.** `order.get("status")`,
`order.get("customer_name", "")`, `to_float(order.get("total_amount"))` — wszystko,
co napisałeś w poprzednich blokach, działa na wierszach z CSV **bez żadnej zmiany**.

To nie przypadek. Cały tor był budowany pod ten moment.

**W R5 używamy wyłącznie `DictReader`.** `csv.reader` znasz, wiesz, że istnieje, ale
w praktyce sięgasz po `DictReader`.

### Zwijanie do listy

```python
with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)        # cały plik naraz -> lista slownikow
return rows
```

`list(reader)` przechodzi cały czytnik i pakuje wiersze do listy. Równoważne pętli
z `.append()`, tylko krócej.

> ⚠️ **`rows = list(reader)` musi być W ŚRODKU bloku `with`.** Poza nim plik jest już
> zamknięty i dostaniesz `ValueError: I/O operation on closed file`. To ta sama zasada
> wcięcia, która ugryzła Cię w R4 — tylko tu bije mocniej.

---

## 7. Wszystko z CSV jest TEKSTEM

**To jest najważniejsze zdanie w tym rozdziale.**

```python
row = {"order_id": "1001", "total_amount": "149.99", "status": "paid"}
#                   ^^^^^^                 ^^^^^^^^
#                   TEKST                  TEKST, nie liczba!
```

W pliku widzisz `149.99` i mózg mówi „liczba". Python widzi **znaki**: `1`, `4`, `9`,
`.`, `9`, `9`. Moduł `csv` **nie zgaduje typów** — i bardzo dobrze, bo zgadywanie
typów to źródło koszmarnych błędów.

Co z tego wynika:

```python
row["total_amount"] + 10          # ❌ TypeError: can only concatenate str
row["total_amount"] > 100         # ❌ TypeError: '>' not supported str vs int
float(row["total_amount"]) + 10   # ✅ 159.99
```

A gdy pole jest puste albo zaśmiecone (`""`, `"brak"`, `"-"`), samo `float()` wybucha.
**Masz na to gotowe narzędzie z R2:**

```python
amount = to_float(row.get("total_amount"))
if amount is None:
    amount = 0.0
```

**Reguła:** każda wartość z CSV, której chcesz użyć jako liczby, przechodzi przez
`to_float`. Bez wyjątków.

---

## 8. Nagłówki — `fieldnames`

Czasem chcesz same nazwy kolumn, bez danych. `DictReader` trzyma je w `.fieldnames`:

```python
with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames        # ['order_id', 'customer_name', 'total_amount', 'status']
```

**Pułapka:** dla **pustego pliku** `.fieldnames` to `None`, nie `[]`. A `None` w kodzie,
który spodziewa się listy, wybucha przy pierwszej pętli. Zabezpieczasz się tak:

```python
headers = reader.fieldnames or []      # None -> []
```

`or` czytasz: *„weź `reader.fieldnames`, a jak to jest fałszywe (`None`) — weź `[]`"*.
To ten sam mechanizm truthiness, o który potknąłeś się w R2 (`if float(value):` przy `"0"`).

**Drugi sposób na nagłówki** — z kluczy pierwszego wiersza:

```python
headers = list(rows[0].keys())         # dziala TYLKO gdy rows nie jest puste
```

Kiedy który? Plik z samym nagłówkiem, bez danych, ma **nagłówki, ale zero wierszy**.
Wtedy `rows` jest puste i `rows[0]` wybuchnie `IndexError`. `.fieldnames` zadziała.
Ale przy **zapisie** masz tylko listę słowników — wtedy `rows[0].keys()` jest jedyną drogą.

---

## 9. Zapis: `csv.DictWriter` i `newline=""`

Odwrotność `DictReader`. Bierze listę słowników i zapisuje jako CSV:

```python
import csv

rows = [
    {"order_id": "1001", "customer_name": "Anna", "status": "paid"},
    {"order_id": "1002", "customer_name": "Piotr", "status": "pending"},
]
headers = list(rows[0].keys())          # nazwy kolumn z pierwszego wiersza

with open("output/wynik.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()                # 1. zapisz linie naglowka
    writer.writerows(rows)              # 2. zapisz wszystkie wiersze naraz
```

Cztery rzeczy, o których trzeba pamiętać:

**1. `fieldnames=headers` — obowiązkowe.** `DictWriter` musi wiedzieć, jakie kolumny
i **w jakiej kolejności** ma zapisać. Ta lista wyznacza kolejność w pliku wynikowym.

**2. `writer.writeheader()` — łatwo zapomnieć.** Bez tego plik nie ma pierwszej linii
z nazwami kolumn. Wygląda prawie dobrze, a potem `DictReader` przy odczycie weźmie
Twój pierwszy **wiersz danych** za nagłówek i cicho zgubi go z wyniku.

**3. `writerows(rows)` vs `writerow(row)`** — liczba mnoga bierze całą listę,
pojedyncza jeden słownik. `writerows(rows)` == pętla `for row in rows: writer.writerow(row)`.

**4. `newline=""` — na Windowsie obowiązkowe.** Bez tego dostaniesz **pustą linię
między każdymi dwoma wierszami**:

```text
order_id,customer_name

1001,Anna

1002,Piotr
```

Powód: moduł `csv` sam wstawia `\r\n` na końcu wiersza, a Windows dokłada od siebie
drugie `\r`. `newline=""` mówi: *„nie tłumacz znaków końca linii, `csv` wie, co robi"*.
Zapamiętaj jako zaklęcie: **do zapisu CSV zawsze `newline=""`**.

---

## 10. `pathlib.Path` — ścieżki jak obiekty

Ścieżkę można trzymać jako zwykły tekst, ale to się źle kończy:

```python
sciezka = "output" + "/" + "wynik.csv"      # ❌ ukosnik na sztywno
sciezka = "output\\wynik.csv"               # ❌ dziala tylko na Windows
```

Windows używa `\`, Linux i Mac `/`. Serwer, na którym w końcu wyląduje Twój kod,
prawie na pewno stoi na Linuksie. Dlatego ścieżek **nie sklejasz ręcznie**.

```python
from pathlib import Path
```

`Path` to obiekt reprezentujący ścieżkę — i sam wie, jakiego separatora użyć.

### Budowanie ścieżek ukośnikiem `/`

```python
folder = Path("output")
plik = folder / "wynik.csv"          # Path('output/wynik.csv')
gleboko = Path("output") / "2026" / "sierpien" / "wynik.csv"
```

To nie jest dzielenie. Operator `/` między `Path` a tekstem został **przedefiniowany**
na „sklej ścieżkę". Czyta się naturalnie, bo wygląda jak ścieżka.

### Od czego liczy się ścieżka względna — `__file__`

Zostaje pytanie, które łatwo przeoczyć: `Path("data/orders.csv")` — **od czego**
liczony jest ten `data/`?

Nie od pliku `.py`, w którym to napisałeś. **Od katalogu, z którego uruchomiłeś
program** (cwd — *current working directory*).

```python
rows = read_csv_rows("data/orders.csv")     # dziala... zaleznie od tego, GDZIE stoisz
```

Odpal z głównego folderu projektu — działa. Wejdź do `src/` i odpal to samo —
`FileNotFoundError`. Kod się nie zmienił, plik się nie ruszył. To jedna z tych
rzeczy, które na Twoim laptopie działają, a na serwerze nie.

**Rozwiązanie: przyklej ścieżkę do KODU, nie do terminala.**

```python
BASE_DIR = Path(__file__).resolve().parent   # katalog, w ktorym lezy TEN plik .py
DATA_DIR = BASE_DIR / "data"
ORDERS_FILE = DATA_DIR / "orders.csv"
```

- `__file__` — zmienna, którą Python ustawia sam w każdym module: ścieżka do tego pliku.
- `.resolve()` — zamień na ścieżkę absolutną, rozwiń `..` i symlinki. Nawyk, nie ozdoba.
- `.parent` — katalog, w którym plik leży.

Teraz program trafi do danych niezależnie od tego, skąd go odpalisz — z terminala,
z crona, z Airflow.

**Wyżej niż o jeden poziom:**

```python
# plik: src/powtorka_05_pliki_csv/exercises.py
HERE    = Path(__file__).resolve().parent    # src/powtorka_05_pliki_csv
PROJECT = HERE.parents[1]                    # korzen repo (DWA poziomy w gore)
```

`.parents[N]` indeksuje od zera: `parents[0]` to to samo co `.parent`.

> **Zasada:** ścieżki jako **stałe WIELKIMI literami na górze modułu**, liczone od
> `BASE_DIR`. Nigdzie w kodzie nie ma `"data/orders.csv"` wpisanego z palca — jest
> `ORDERS_FILE`. Przenosisz katalog → poprawiasz jedną linię, nie piętnaście.
> Masz to już u siebie w `src/day_20_csv/main.py`.

### Metody, które musisz znać

```python
p = Path("src/day_20_csv/data/orders.csv")

p.exists()      # True / False  - czy istnieje?
p.name          # 'orders.csv'  - sama nazwa pliku
p.stem          # 'orders'      - nazwa bez rozszerzenia
p.suffix        # '.csv'        - samo rozszerzenie
p.parent        # Path('src/day_20_csv/data')  - katalog nadrzedny
```

### Tworzenie katalogu

Zapis do `output/wynik.csv` **wybuchnie**, gdy katalog `output/` nie istnieje.
Python nie tworzy katalogów sam:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'output/wynik.csv'
```

Mylące, prawda? Komunikat mówi o pliku, a brakuje **katalogu**.

```python
Path("output").mkdir(parents=True, exist_ok=True)
```

- `parents=True` — utwórz też brakujące katalogi po drodze (`output/2026/sierpien`
  za jednym razem). Bez tego dostaniesz błąd, jeśli brakuje pośredniego poziomu.
- `exist_ok=True` — **jak katalog już jest, nie rób afery**. Bez tego drugie uruchomienie
  programu wywala `FileExistsError`.

**Te dwa argumenty ustawiasz zawsze razem.** Efekt: „upewnij się, że ten katalog
istnieje" — bezpieczne do wywołania ile razy chcesz. Nazywa się to **idempotencją**:
operacja, którą można powtórzyć bez zmiany wyniku. Bardzo ważne pojęcie w pipeline'ach,
bo pipeline'y się restartuje.

Przy zapisie pliku interesuje Cię **katalog nadrzędny**:

```python
path = Path("output/2026/wynik.csv")
path.parent.mkdir(parents=True, exist_ok=True)     # tworzy output/2026
# dopiero teraz mozesz otworzyc plik do zapisu
```

**Dokładnie to napisałeś na dniu 20** w `csv_utils.py`. Zajrzyj tam — to Twój kod.

### `Path` czy `str`?

`open()` przyjmuje **oba**. Twoje funkcje też powinny. Wystarczy jedna linia na wejściu:

```python
def moja_funkcja(path):
    path = Path(path)        # tekst -> Path, Path -> Path (bez zmian)
```

`Path(Path("x"))` to nadal `Path("x")` — bezpiecznie. **Ta linia to Twoja bramka
wejściowa:** od niej w dół masz gwarancję, że pracujesz na `Path` i możesz wołać
`.exists()`, `.parent`, `/`. Diagnostyka Dnia 21 wprost tego wymaga:
*„Może być STRINGIEM albo obiektem Path. Twój kod musi radzić sobie z obydwoma."*

---

## 11. Brak pliku — dwie drogi

Plik może nie istnieć. Zawsze. To nie jest przypadek brzegowy — to **codzienność**:
dostawca nie wysłał danych, ktoś zmienił nazwę, katalog jeszcze pusty.

Pipeline **nie ma prawa się wywalić** z tego powodu. Ma zwrócić pusty wynik i jechać dalej.

### Droga A — sprawdź przed (LBYL)

```python
path = Path(path)
if not path.exists():
    return []                     # brak pliku -> pusty wynik, koniec
with open(path, "r", encoding="utf-8") as file:
    ...
```

*Look Before You Leap* — „popatrz, zanim skoczysz". Czytelne. Wychodzisz z funkcji
wcześnie (**early return** — dokładnie ten wzorzec, którym domknąłeś `highest_spender`
w R4).

### Droga B — spróbuj i złap (EAFP)

```python
try:
    with open(path, "r", encoding="utf-8") as file:
        ...
except FileNotFoundError:
    return []
```

*Easier to Ask Forgiveness than Permission* — „łatwiej prosić o wybaczenie niż
o pozwolenie". To jest **pythonowy** styl i Twój `try/except` z R2.

### Którą wybrać?

Obie są poprawne — diagnostyka Dnia 21 wprost to mówi. Ale:

**Droga B jest bezpieczniejsza**, bo droga A ma dziurę. Między `path.exists()`
a `open()` mija ułamek sekundy. Jeśli w tym czasie ktoś skasuje plik — `exists()`
powiedziało „jest", a `open()` i tak wybucha. Nazywa się to **race condition**
(wyścig). Na Twoim laptopie nie zobaczysz tego nigdy. W produkcyjnym pipelinie,
gdzie dwa procesy ruszają ten sam katalog — jak najbardziej.

**W R5 używaj `try/except FileNotFoundError`.** `Path.exists()` przydaje Ci się
osobno — gdy pytasz o istnienie pliku jako **informację** (zadanie #8), a nie jako
zabezpieczenie przed otwarciem.

> ⚠️ **`except:` bez typu jest zabronione.** Łapie absolutnie wszystko — także Twoje
> własne literówki, `KeyboardInterrupt` i błędy pamięci. Ukrywa bugi, zamiast obsługiwać
> błędy. Zawsze `except FileNotFoundError:` — konkretny typ. Znasz to z R2.

---

## 12. Round-trip: zapisz i odczytaj

**Round-trip** to sprawdzian: zapisz dane, odczytaj z powrotem, porównaj z oryginałem.
Jeśli się zgadza — zapis i odczyt są spójne.

```python
rows = [{"a": "1", "b": "2"}]
write_csv_rows("output/test.csv", rows)
wczytane = read_csv_rows("output/test.csv")
assert wczytane == rows          # ✅ zgadza sie
```

To jest wzorzec testowania, który zobaczysz w `tests/test_powtorka_05.py`. Ale jest
w nim **haczyk wart zapamiętania**:

```python
rows = [{"order_id": 1001, "amount": 149.99}]    # LICZBY
write_csv_rows("output/test.csv", rows)
wczytane = read_csv_rows("output/test.csv")
# wczytane == [{"order_id": "1001", "amount": "149.99"}]    <- TEKSTY!
```

**Round-trip przez CSV gubi typy.** Zapisujesz `int`, wczytujesz `str`. Bo CSV
to format tekstowy — nie ma w nim miejsca na informację „to była liczba".

To nie jest błąd Pythona. To ograniczenie **formatu**. I dokładnie dlatego w prawdziwych
pipeline'ach po CSV przychodzą Parquet i bazy danych — one typy pamiętają.

---

## 13. **[NOWE]** `tmp_path` — jak testować pliki

**To jedyny element R5, którego wcześniej nie miałeś.** Nie musisz go pisać —
musisz go **rozumieć**, gdy zobaczysz w testach.

Problem: testy funkcji plikowych potrzebują plików. Ale gdzie je tworzyć?
Zaśmiecać repo? Nadpisać coś przez pomyłkę? Dwa testy walczące o ten sam plik?

pytest rozwiązuje to fixture'em **`tmp_path`**:

```python
def test_czyta_plik(tmp_path):              # <- wystarczy wpisac nazwe w nawiasie
    plik = tmp_path / "orders.csv"          # tmp_path to Path do PUSTEGO katalogu
    plik.write_text("a,b\n1,2\n", encoding="utf-8")

    assert read_csv_rows(plik) == [{"a": "1", "b": "2"}]
```

Jak to działa:

1. Wpisujesz `tmp_path` jako **argument funkcji testowej**. Nic nie importujesz,
   nic nie tworzysz.
2. pytest widzi tę nazwę, tworzy **świeży, pusty katalog tymczasowy** i podaje go
   jako `Path`.
3. **Każdy test dostaje własny katalog.** Testy się nie mieszają.
4. Po testach pytest sprząta.

To się nazywa **fixture** — gotowy kawałek środowiska, który pytest wstrzykuje
do testu na podstawie **nazwy argumentu**. Nie ma tu magii do zapamiętania poza jedną
rzeczą: **nazwa musi brzmieć dokładnie `tmp_path`**.

Dwie metody `Path`, które zobaczysz w testach:

```python
plik.write_text("tresc", encoding="utf-8")    # zapisz tekst do pliku (skrot na with open)
plik.read_text(encoding="utf-8")              # wczytaj caly plik jako tekst
```

To skróty na cały blok `with open(...)`. Wygodne w testach. **W kodzie produkcyjnym
zostajemy przy `with open()`** — bo tam potrzebujesz kontroli nad trybem, `newline`
i czytaniem linia po linii.

---

## 14. Pułapki, które Cię ugryzą

Lista rzeczy, na których wykłada się każdy — łącznie ze mną:

| # | Pułapka | Objaw | Lek |
|---|---------|-------|-----|
| 1 | `list(reader)` **poza** blokiem `with` | `ValueError: I/O operation on closed file` | wcięcie do środka `with` |
| 2 | brak `newline=""` przy zapisie | puste linie między wierszami | `newline=""` w `open(..., "w")` |
| 3 | brak `writeheader()` | plik bez nagłówka; przy odczycie ginie pierwszy wiersz | dodaj `writer.writeheader()` |
| 4 | katalog nie istnieje | `FileNotFoundError` przy **zapisie** | `path.parent.mkdir(parents=True, exist_ok=True)` |
| 5 | brak `encoding="utf-8"` | krzaki albo `UnicodeDecodeError` | zawsze podawaj jawnie |
| 6 | `float(row["total_amount"])` na pustym polu | `ValueError: could not convert` | `to_float` z R2 |
| 7 | traktowanie wartości z CSV jak liczb | `TypeError: can only concatenate str` | konwersja przed liczeniem |
| 8 | `.fieldnames` przy pustym pliku | `None`, potem `TypeError` w pętli | `reader.fieldnames or []` |
| 9 | otwarcie pliku źródłowego w trybie `"w"` | **dane skasowane** | pisz tylko do `output/` |
| 10 | `rows[0].keys()` na pustej liście | `IndexError: list index out of range` | sprawdź `if not rows:` **przed** |

**Pułapki 1 i 4 są odpowiednikiem tego, na czym poległeś w R4** — jedna to wcięcie
(co jest w bloku, a co poza), druga to kolejność operacji (najpierw katalog, potem plik).
Ta sama umiejętność, inne przebranie.

---

## 15. Demo — URUCHOM to najpierw

```
uv run python -m src.powtorka_05_pliki_csv.demo
```

Zobaczysz na żywo: odczyt pliku tekstowego, `DictReader`, nagłówki, tworzenie katalogu,
zapis przez `DictWriter`, round-trip i obsługę brakującego pliku. Demo pisze do
katalogu tymczasowego — niczego Ci nie zaśmieci.

Kod jest w `src/powtorka_05_pliki_csv/demo.py` — **przeczytaj go**, nie tylko uruchom.
Jest tam wszystko, czego potrzebujesz do zadań.

Plik z danymi do oglądania: `src/powtorka_05_pliki_csv/data/orders.csv`. Otwórz go
w edytorze — zobacz, że to zwykły tekst.

---

## 16. Zadania

Plik: `src/powtorka_05_pliki_csv/exercises.py`. Na górze masz **gotowe** `to_float`
(z R2 — nie zmieniaj, używaj). Osiem funkcji z `pass`. Jedna klasa naraz:

```
uv run pytest tests/test_powtorka_05.py::TestReadTextLines -v
```

| # | Funkcja | Co ćwiczy | Reuse |
|---|---------|-----------|-------|
| 1 | `read_text_lines` | `with open`, pętla po pliku, `FileNotFoundError` | — |
| 2 | `read_csv_rows` | **payoff diag #6**: `DictReader` → lista słowników | — |
| 3 | `get_headers` | `.fieldnames`, pułapka `None` | — |
| 4 | `ensure_dir` | `Path.mkdir(parents=True, exist_ok=True)` | — |
| 5 | `write_csv_rows` | `DictWriter`, `newline=""`, `writeheader()` | **#4** |
| 6 | `copy_csv` | round-trip: odczyt + zapis | **#2 + #5** |
| 7 | `filter_csv_by_status` | prawdziwy ETL: wczytaj → odfiltruj → zapisz | **#2 + #5** |
| 8 | `csv_summary` | integracja: raport o pliku | **#2 + #3** |

**Drabinka jest celowa.** Zadania 1–5 to klocki. Zadania 6–8 **składają klocki** —
jeśli 1–5 zrobisz porządnie, 6–8 są krótkie. Jeśli zaczniesz przepisywać logikę
zamiast wołać własne funkcje, 6–8 zrobią się długie i zobaczę to na review.

### Zasady

- **Reguła 20 minut** — zacinasz się dłużej, piszesz.
- **Test to prawda.** Gdy docstring i test się różnią — wierzysz testowi.
- **DRY** — #5 użyj #4, #6 i #7 użyj #2+#5, #8 użyj #2+#3.
- **`except` łapie konkretny typ** — `except FileNotFoundError:`, nigdy gołe `except:`.
- **Nazwy zmiennych po angielsku** — `rows`, `headers`, `path`, `count`. Od tego bloku
  zaczynamy. Repo jest Twoim portfolio.
- **Nie ruszaj `data/orders.csv`.** Piszesz tylko tam, gdzie każe test.

---

## Wyniki (wypełniaj na bieżąco)

| # | Funkcja | Bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|-------------|------------|---------------------|
| 1 | `read_text_lines` | | | |
| 2 | `read_csv_rows` | | | |
| 3 | `get_headers` | | | |
| 4 | `ensure_dir` | | | |
| 5 | `write_csv_rows` | | | |
| 6 | `copy_csv` | | | |
| 7 | `filter_csv_by_status` | | | |
| 8 | `csv_summary` | | | |

**Co wróciło od razu:**

**Co dalej sprawia problem:**

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| path | ścieżka | `Path("data/orders.csv")` |
| file handle | uchwyt pliku | `as file` w `with open(...)` |
| to open / to close | otworzyć / zamknąć | `open()`, `with` zamyka sam |
| encoding | kodowanie znaków | `encoding="utf-8"` |
| header / headers | nagłówek / nagłówki | pierwsza linia CSV |
| row | wiersz | jeden słownik z `DictReader` |
| column | kolumna | klucz w słowniku wiersza |
| delimiter / separator | separator | przecinek w CSV |
| to read / to write | czytać / zapisywać | `"r"` / `"w"` |
| to append | dopisać | tryb `"a"` |
| to overwrite | nadpisać | tryb `"w"` — **kasuje treść** |
| directory / folder | katalog | `Path("output")` |
| parent directory | katalog nadrzędny | `path.parent` |
| to create a directory | utworzyć katalog | `.mkdir(parents=True, exist_ok=True)` |
| missing file | brakujący plik | `FileNotFoundError` |
| to raise / to catch an exception | rzucić / złapać wyjątek | `try` / `except` |
| context manager | menedżer kontekstu | `with` |
| idempotent | idempotentny | `exist_ok=True` — powtórzysz bez szkody |
| round-trip | obieg tam i z powrotem | zapisz → odczytaj → porównaj |
| temporary directory | katalog tymczasowy | `tmp_path` w testach |
| fixture | fixture, gotowe środowisko testu | argument `tmp_path` |
| pipeline | pipeline, potok danych | `read → filter → write` |
| ETL (Extract-Transform-Load) | wyciągnij-przekształć-załaduj | cały rozdział 1 |
