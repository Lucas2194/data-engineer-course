# Obsługa błędów i odporny mini-pipeline CSV

## Pipeline działa nie tylko dla idealnych danych 

Program ćwiczeniowy częśto otrzeymuje dokłądnie takie dane, jakich oczekuje. 
Pipeline produkcujny nie ma tego komfortu.

Plik może zostać : 

- usunięty
- przeniesiony
- zapisany pod inną nazwą
- wysłany bez nagłówków 
- wyeksportowany bez jednej z kolumn
- zapisany w złym kodowaniu
- częsciowo uszkodzony 

Dlatego poprawny wynik dla prawidłowego pliku to tylko jeden z testów. 
Trzeba również zaplanować zachowanie programu dla błędych wejść.

W DE często się mówi, o odpowiedni pipelinu'u. Nie oznacza ona, że pipeline zawsze musi kontynuować pracę. Czasami najbardziej odpowiedzalnym zachowaniem jest szybkie zatrzymanie programu z jasnym komunikatem.

## Trzy poziomy błędów 

**Poziom 1 - Błąd techniczny odczytu**

Program nie może uzyskać dancyh wejściowych. 

Przykłady : 

- plik nie istnieje
- brak uprawień do odczytu 
- plik ma niezgodne kodowanie. 

W takiej sytuacji pipeline powinien się zatrzyć. Nie ma danych, które mógłby walidować lub transformować. 

**Poziom 2 - błąd struktury pliku**

Plik isteniej i można go otworzyć, ale nie ma wymaganej struktury. 

Przykłady : 

- plik jest całkowicie pusty
- plik nie ma nagłówka
- brakuje kolumny `status` 
- plik ma tylko nagłówek i zero rekordów. 

To również jest błąd krytyczny dla całego uruchomienia. 

**Poziom 3 - błąd pojedynczego rekordu**

Struktrua pliku jest prawidłowa, ale część wierszy zawiera błędne wartości.

Przykłady

- `total_amount` ma wartość `abc`
- status to `finished`
- brakuje nazwy klienta
- kwota jest mniejsza lub równa zero. 

Tutaj pipeline może kontynuować : 

- poprawne rekordy przetwarza dalej
- błędne zapisuje do invalid_orders.csv
- szczegóły umieszcza w raporcie walidacji

To rozróżnienie jest kluczowe 

Rodzai problemu                     Przykład                                 Decyzja pipeline'u
techniczny                          brak pliku                               zatrzymaj
strukturalny                        brak wymaganej kolumny                   zatrzymaj
dotycząca rekordu                   niepoprawna kwota w jednym miejscu       kontynuuj i raportuj

## Wyjątek a błąd walidacji

Wyjątek 

Wyjątek jest mechanizmem Pythona informującym, że podczas wykonywania kodu
wydarzyło się coś, co przerwało normalny przebieg programu

Przykład wyjątków

- `FileNotFoundError`,
- `PermissionError`,
- `UnicodeDecodeError`
- `ValueError`,
- `csv.Error`

Błąd walidacji

W moim projekcie validate_odrder() - nie zgłasza wyjątku dla niepoprawnego statusu. Dodaje opis problemu do listy errors. 

To właściwe zachowanie, ponieważ pojedyńczy niepoprawny rekord jest spodziewanym problem jakości danych,
a nie awarią całego programu.

wyjątek krytyczny -> przerwij uruchomienie
błąd rekordu -> zapisz problem i przetwarzaj pozostały rekordy. 

Nie każdy niepoprawny rekord powinien powodować wyjątek. Nie każdy wyjątek powinien być ignorowany. 

## Przypomnienie try/except

Podstawowy schemat 

```python

try:
    # operacja, które może zgłosić konkretny wyjątek
    ...
except FileNotFound as error:
    # reakcja na dokładnie ten rodzaj problemu
    ...

```

Przykład na innym pliku 

```python

from pathlib import Path

names_file = Path("data") / "names.txt"

try:
    with open(names_file, "r", encoding="utf-8") as file:
        names = file.readlines()
except FileNotFoundError:
    print("Nie znaleziono pliku: {name_file}")
```

Kod w try powinien obejmotwać operację, dla których naprawdę spodziewamy isę danego problemu.

Nie należy umieszczać całego programu, w jednym ogromnym try. Im większy blok, tym trudniej stwierdzić, która instrukacja spowodowała błąd. 

## Dlaczego nie używamy except Exception ? 

Taki zapis przechwytuje prawie każdy zwykł błąd programu: 

```python
try:
    ...
except Exception:
    print("Coś poszło nie tak")

```

Problem polega na tym, że może ukryć również błąd programisty, np. literówkę w nazwie zmiennej, albo niewłaściwe wywołanie funkcji.

Komunikat "coś poszło nie tak" nie mówi : 

- co się wydarzyło
- którego pliku dotyczy problem
- jak można go naprawić 

W dzisiejszym projekcie będziemy obsługiwać tylko takie przypadki, który można nazwać i dla których będzie odpowiednia reackjja. 

## Kilka wyjątków jedna reakcja.

Jeżeli kilka wyjątków, powinno prowadzić do tej samej reakcji, można umieścić w krtoce.

```python

try:
    ...
except (FileNotFoundError, PermissionError) as error:
    print(f"Nie udało się odczytać pliku: {error}")
```
Nadal są to konkretne wybrane wyjątki. Nie jest to odpowiednik łapania wszystkiego. 

W projekcie CSV przydatne będą : 

Wyjątek             Przykładowa przyczyna 
FileNotFoundError   błędna ścieżka albo brak pliku
PermissionError     plik jest niedostępny dla programu
UnicodeDecodeError  plik nie jest zapisany w oczekiwanym kodowaniu
csv.Error           parser CSV wykrył problem z formatem
ValueError          wykryliśmy niepoprawną struukturę i sami zgłosiliśmy problem

## Co robi raise 

`raise` pozwala świadomie zgłosić wyjątek 

Przykład na innym problemie 

```python

def calculate_average(values):
    if not values:
        raise ValueError("Nie można obliczyć średniej z pustej listy")
    
    return sum(values) / len(values)
```

Funkcja wykrywa sytuację, w któej nie można wykonać swojego zadania zgodnie z kontraktem. Zamiast zwrócić przypadkowy wynik, zgłasza czytelny problem. 

Wywołując kod można go obłużyć:

```python

try:
    average = calculate_average([])
except ValueError as error:
    print(f"Błą dannych: {error}")
```

W dzisiejszym projekcie użyjemy `ValueError`, gdy plik CSV istnieje, ale nie może być prawidłoym wejściem pipeline'u. np. brakuje wymaganych kolumn. 

## Zwrócić None czy zgłosić wyjątek ?

Oba podejścia są spotykane, ale trzeba ustalićjasny kontrakt funkcji. 

Zwracanie None 

read_data() - > lista rekordów albo None 

kod wywołujący musi zawsze sprawdzić wynik 

Zgłoszanie wyjątku

Read_data() -> lista rekordów 
problemy krytyczny -> wyjątek 

Kod wywołujący otrzymuje listę tylko wteddy, gdy odczyt się udał. W przeciwnym razie normalny przepływ zostaje przerwany i sterowanie przechodzi do except. 

W Dniu 21 ćwiczyliśmy wariant z `None`. dzisiaj świadomie przećwiczymy drugi wariant. Funkcja odczytująca nie ukrywa problemu, lecz pozwala wyjątkowi dotrzeć do `main()`. 

To nie oznacza, że jedno podejście jest zawsze poprawne, a drugie zawsze błędne. 
Najważniejszym jest jasny i konsekwentny kontrakt. 

## Nagłowek i fieldnames 

Po utworzenie csv.DictReader nazwy kolumn dostępne są w 

```python
reader.fieldnames
```

Dla pliku 

order_id, customer_name, total_amount, status
1001, Anna, 249.99, paid

wartość będzie podoba do: 

["order_id", "customer_name", "total_amount", "status"]

Dla całkowicie pustego pliku fieldnames może mieć wartość None.

Samo otwarcie pliku bez wyjątku nie oznacza więc jeszcze, żę otrzymaliśmy prawidłowy CSV.

## Sprawdzanie wymaganych kolumn

Pipeline zamówień oczekje kolumn : 

```python

required_columns = [
    "order_id",
    "customer_name",
    "total_amount",
    "status",
]
```
Musimy porównaj je z kolumnami obecnymi w pliku 

przykład innych danych 

```python
required = ["employee_id", "name", "department"]
actual = ["employee_id", "name"]
missing = []

for column in required:
    if column not in actual:
        missing.append(column)
```
Wynik:

["department"]

Jeżeli lista missing jest pusta, plik nie spełnia kontraktu struktury.

Nie sprawdzmy kolejność kolumn. `DictReader` korzysta z nazw, dlatego plik może mieć wymagane kolumny w innej kolejności.

Nie odrzucamy równieżpliku tylko dlatego, że zawiera dodatkową kolumnę. Na tym etapie wymagamy obenośći minimum potrzebego pipeline'owi.

## Pusty plik a plik bez rekordów 

To dwa różne przypadki.

**Całkowicie pusty plik** 

Nie zawiera nawet nagłówka:

reader.fieldnames może być wtedy None

Plik zawierający tylko nagłówek 

order_id, customer_name, total_amount, status

Struktura kolumn istnieje, ale lista rekordó po odczycie będzie pusta.

W dzisiejszym pipeline'ie oba przypadki potraktujemy jako błąd krytyczny, ale warto zwrócićdla nich dwa różne komunikaty. 
Ułatwia to znalezienie przyczyny. 

## Fail Fast

Fail fast oznacza możliwe szybkie zatrzymanie procesu, gdy dalsze działanie nie ma sensu. 

Jeżeli brakuje kolumny total_amount, nie powinniśmy : 

- próbować walidować rekordów
- tworzyć transofmracji
- zapisywać nowych plików wynikowych
- informowac że przetworzono zero zamówień

Powinniśmy natomiast: 

1. wykryć bproblem bezposędnio po otwarciu pliku. 
2. podać czytelny komunikat
3. zakończyć program niezerowym kodem 

To chroni przed tworzeniem wyników, któe wyglądaj wiarygodnie ale pochodzą z nieprawidłowego wejścia. 

## Kody zakończenia programu 

System operacyjny otrzeymuje informacę, czy program zakończył się powodzeniem

Najczęsta konwecja 

0 -> sukces
wartość różna od 0 -> błąd 

W Pythonie można zakończyć program kodem 1: 

```python
import sys
sys.exit(1)
```

Dlaczego to jest ważne?

Pipeline możę być uruchomiony automatycznie przez inne narzędzie. Człowiek nie musi obserwować konsoli. Kod zakończenia pozwala narzędiu rozpoznać, że proces isę nie udał. 

Na poźniejszych etapach, podobą informację wykorzystają między innymi systemi orkiestracji i CI/CD

W PowerShellu po uruchomieniu programu można sprawdzić kod: 

```powershell
python main.py
$LASTEXITCODE
```

Po sukcesie otrzymamy 0, a po kontrolowanym błędzie krytycznym 1.

## Gdzie obsłużyć błąd?

Przyjmiemy na dziś następująca odpowiedzialność : 

csv_utils.py

- otwiera i odczytuje plik
- sprawdza podstawoą strukturę
- zgłasza wyjątek, jeśli nie może zwrócićprawdiłowej listy zamówień

validator.py

- sprawdza obeność wymaganych kolumn,
- waliduje wartości poszczególnych rekordów

main.py

- wywołuje odczyt
- przechwytuje przewidziane błędy krytyczne
- wyświetla czytelny komunikat 
- kończy program kodem `1`
- po udanym odczycie steruje resztą pipelinu'u 

reports.py

- buduje raport jakości rekordów 
- nie podejmuje decyzji o zatrzymaniu programu 

Zasada Funkcja najbliżej danych wykrywa i opisuje problem, a warstaw sterująca decyduje jak zakończyć całę uruchomienie. 
