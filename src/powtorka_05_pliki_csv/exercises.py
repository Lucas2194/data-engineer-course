"""Powtorka R5 - pliki: CSV, sciezki i brak pliku.

Zakres: with open(), encoding, csv.DictReader/DictWriter, newline="", pathlib.Path,
        mkdir(parents=True, exist_ok=True), FileNotFoundError.

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-05-pliki-csv.md (caly - to najobszerniejszy blok)
    2. Uruchom demo:  uv run python -m src.powtorka_05_pliki_csv.demo
    3. Przeczytaj kod dema - jest tam wszystko, czego potrzebujesz

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_05.py::TestReadTextLines -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.

ZASADY TEGO BLOKU:
    - DRY: #5 uzyj #4; #6 i #7 uzyj #2 i #5; #8 uzyj #2 i #3.
      Drabinka jest celowa - jesli 1-5 zrobisz porzadnie, 6-8 sa krotkie.
    - except lapie KONKRETNY typ: `except FileNotFoundError:`, nigdy gole `except:`.
    - encoding="utf-8" ZAWSZE - przy odczycie i przy zapisie.
    - newline="" ZAWSZE przy zapisie CSV.
    - Nazwy zmiennych PO ANGIELSKU: rows, headers, path, count. Od tego bloku zaczynamy.
    - NIE ruszaj data/orders.csv. Piszesz tylko tam, gdzie kaze test.
"""

import csv  # noqa: F401  (bedzie potrzebny od zadania #2)
from pathlib import Path  # noqa: F401  (bedzie potrzebny od zadania #4)


# ---------------------------------------------------------------------------
# GOTOWE - z R2. NIE zmieniaj tej funkcji. Masz jej UZYWAC, gdy bedziesz
# potrzebowal liczby z pola CSV (bo z CSV wszystko przychodzi jako TEKST).
# ---------------------------------------------------------------------------
def to_float(value) -> float | None:
    """Zamien wartosc na float. Gdy sie nie da - zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def read_text_lines(path) -> list[str]:
    """Wczytaj plik tekstowy i zwroc jego linie jako liste.

    Dostajesz:
        path - sciezka do pliku. Moze byc TEKSTEM ("dane/plik.txt") albo obiektem Path.
               Twoj kod musi radzic sobie z obydwoma (open() przyjmuje oba, wiec
               tutaj nie musisz nic konwertowac).

    Zwracasz:
        Liste tekstow - jedna linia pliku = jeden element listy.
        Znak konca linii ("\\n") ma byc OBCIETY.
        Gdy plik NIE ISTNIEJE -> pusta lista []. Bez wyjatku.
        Gdy plik jest PUSTY   -> pusta lista [].

    Przyklady:
        Plik o tresci:
            Anna
            Piotr

        read_text_lines("ludzie.txt")   -> ["Anna", "Piotr"]
        read_text_lines("nie_ma.txt")   -> []

    Uwagi:
        - Wzorzec z notes, rozdzial 2 i 5: `with open(path, "r", encoding="utf-8")`.
        - Po pliku chodzisz petla, jak po liscie: `for line in file:`.
        - Obcinasz TYLKO znak konca linii: `line.rstrip("\\n")`.
          NIE uzywaj .strip() - to obcieloby tez spacje z poczatku linii,
          a one moga byc czescia danych.
        - Brak pliku: `try` / `except FileNotFoundError:` -> `return []`.
          KONKRETNY typ wyjatku, nigdy gole `except:`.
        - Pilnuj wciecia: czytanie MUSI byc w srodku bloku `with`. Poza nim plik
          jest juz zamkniety (ValueError: I/O operation on closed file).

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestReadTextLines -v
    """

    lines = []

    try:
        with open(path, "r", encoding = "utf-8") as file:
            for line in file:
                lines.append(line.rstrip("\n"))
        return lines
    except(FileNotFoundError):
        return []


def read_csv_rows(path) -> list[dict]:
    """Wczytaj plik CSV i zamien go na liste slownikow. PAYOFF - zadanie diagnostyczne.

    To jest dokladnie zadanie #6 z diagnostyki Dnia 21 (read_csv_rows).
    Napiszesz je tutaj raz porzadnie i tam bedzie za darmo.

    Dostajesz:
        path - sciezka do pliku CSV (TEKST albo Path).

    Zwracasz:
        Liste slownikow. Jeden slownik = jeden wiersz DANYCH.
        Klucze slownika = nazwy kolumn z pierwszej linii pliku (naglowka).
        WSZYSTKIE wartosci sa TEKSTAMI - csv nie zamienia typow za Ciebie.

        Gdy plik NIE ISTNIEJE          -> pusta lista [].
        Gdy plik ma SAM NAGLOWEK       -> pusta lista [] (zero wierszy danych).

    Przyklady:
        Plik o tresci:
            order_id,customer_name,total_amount,status
            1001,Anna,149.99,paid
            1002,Piotr,89.50,pending

        read_csv_rows("orders.csv") -> [
            {"order_id": "1001", "customer_name": "Anna",
             "total_amount": "149.99", "status": "paid"},
            {"order_id": "1002", "customer_name": "Piotr",
             "total_amount": "89.50", "status": "pending"},
        ]

        read_csv_rows("nie_ma.csv") -> []

        Zwroc uwage: "149.99" to TEKST w cudzyslowie, nie liczba.

    Uwagi:
        - Wzorzec z notes, rozdzial 6. Klasa nazywa sie csv.DictReader.
        - Naglowek NIE jest wierszem danych - DictReader zjada go sam i robi
          z niego klucze. Nie musisz go pomijac recznie.
        - `list(reader)` zwija cala reszte do listy. UWAGA: ta linia musi byc
          W SRODKU bloku `with`, inaczej plik jest juz zamkniety.
        - Brak pliku: `except FileNotFoundError:` -> `return []`.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestReadCsvRows -v
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def get_headers(path) -> list[str]:
    """Zwroc same nazwy kolumn pliku CSV (bez danych).

    Dostajesz:
        path - sciezka do pliku CSV (TEKST albo Path).

    Zwracasz:
        Liste tekstow - nazwy kolumn z pierwszej linii pliku, w kolejnosci z pliku.
        Gdy plik NIE ISTNIEJE -> pusta lista [].
        Gdy plik jest PUSTY   -> pusta lista [].

    Przyklady:
        Plik o tresci:
            order_id,customer_name,total_amount,status
            1001,Anna,149.99,paid

        get_headers("orders.csv") -> ["order_id", "customer_name", "total_amount", "status"]

        Plik z SAMYM naglowkiem (zero wierszy danych):
        get_headers("puste_dane.csv") -> ["order_id", "customer_name"]
            (naglowek jest, wiec nazwy kolumn SA - mimo ze danych nie ma)

        get_headers("nie_ma.csv") -> []

    Uwagi:
        - Wzorzec z notes, rozdzial 8. DictReader trzyma naglowki w `.fieldnames`.
        - PULAPKA: dla calkowicie PUSTEGO pliku `.fieldnames` to None, nie [].
          Zabezpieczasz sie: `reader.fieldnames or []`.
          To ta sama truthiness, o ktora potknales sie w R2.
        - `.fieldnames` zwraca liste - opakuj w list(), zeby zwrocic zwykla liste.
        - DLACZEGO to osobna funkcja, a nie read_csv_rows(path)[0].keys()?
          Bo plik z samym naglowkiem ma nazwy kolumn, ale ZERO wierszy - wtedy
          rows[0] wybucha IndexError. .fieldnames dziala zawsze.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestGetHeaders -v
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return reader.fieldnames or []
    except FileNotFoundError:
        return []


def ensure_dir(path) -> Path:
    """Upewnij sie, ze katalog istnieje. Gdy go nie ma - utworz. Zwroc go jako Path.

    Maly klocek - uzyjesz go w write_csv_rows (#5).

    Dostajesz:
        path - sciezka do KATALOGU (TEKST albo Path). Moze byc zagniezdzona
               ("output/2026/sierpien") i moze jeszcze nie istniec.

    Zwracasz:
        Ten sam katalog jako obiekt Path.

    Zasady:
        - Gdy katalogu nie ma - tworzysz go, razem z brakujacymi katalogami po drodze.
        - Gdy katalog JUZ ISTNIEJE - nic sie nie dzieje, zadnego bledu.
          Funkcje mozna wolac ile razy chcesz (to sie nazywa IDEMPOTENCJA).

    Przyklady:
        ensure_dir("output")                  -> Path("output")        (utworzony)
        ensure_dir("output")                  -> Path("output")        (juz byl, OK)
        ensure_dir("output/2026/sierpien")    -> Path("output/2026/sierpien")
                                                 (utworzone WSZYSTKIE trzy poziomy)

    Uwagi:
        - Wzorzec z notes, rozdzial 10. Robiles to na dniu 20 w csv_utils.py.
        - Najpierw bramka wejsciowa: `path = Path(path)` - tekst albo Path -> zawsze Path.
        - Potem: `path.mkdir(parents=True, exist_ok=True)`.
            parents=True   -> utworz tez brakujace katalogi po drodze
            exist_ok=True  -> katalog juz istnieje? nie rob afery
          Te dwa argumenty ustawiasz ZAWSZE RAZEM.
        - Na koncu zwroc `path`.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestEnsureDir -v
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_csv_rows(path, rows: list[dict]) -> int:
    """Zapisz liste slownikow do pliku CSV. Zwroc liczbe zapisanych wierszy danych.

    Dostajesz:
        path - sciezka do pliku wynikowego (TEKST albo Path). Katalog moze jeszcze
               NIE ISTNIEC - masz go utworzyc.
        rows - lista slownikow. Kazdy slownik = jeden wiersz.

    Zwracasz:
        Liczbe zapisanych wierszy DANYCH (naglowka NIE liczysz).

    Zasady:
        - Nazwy kolumn bierzesz z kluczy PIERWSZEGO slownika, w jego kolejnosci.
        - Plik ma miec linie naglowka.
        - Gdy `rows` jest PUSTE -> zwracasz 0 i NIE TWORZYSZ zadnego pliku.
          (pusty plik CSV bez naglowka to smiec - lepiej go nie robic)
        - Katalog nadrzedny tworzysz, gdy go nie ma.

    Przyklady:
        write_csv_rows("output/wynik.csv", [
            {"order_id": "1001", "customer_name": "Anna"},
            {"order_id": "1002", "customer_name": "Piotr"},
        ]) -> 2

        Plik output/wynik.csv bedzie mial tresc:
            order_id,customer_name
            1001,Anna
            1002,Piotr

        write_csv_rows("output/pusty.csv", []) -> 0
            (plik output/pusty.csv NIE POWSTAJE)

    Uwagi:
        - Wzorzec z notes, rozdzial 9.
        - KOLEJNOSC MA ZNACZENIE:
            1. `if not rows: return 0`  - early return, zanim cokolwiek zrobisz
            2. utworz katalog nadrzedny (UZYJ ensure_dir z #4 - DRY!)
               interesuje Cie `Path(path).parent`, nie sam plik
            3. headers = list(rows[0].keys())
            4. otworz do zapisu i pisz
        - Otwarcie do zapisu: `open(path, "w", encoding="utf-8", newline="")`.
          newline="" jest OBOWIAZKOWE - bez niego na Windowsie dostaniesz puste
          linie miedzy wierszami.
        - `csv.DictWriter(file, fieldnames=headers)`, potem:
            writer.writeheader()      <- LATWO ZAPOMNIEC
            writer.writerows(rows)    <- liczba mnoga: cala lista naraz
        - Tryb "w" KASUJE dotychczasowa tresc pliku. Piszesz tylko tam, gdzie kaze test.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestWriteCsvRows -v
    """
    if not rows:
        return 0
    ensure_dir(Path(path).parent)
    headers = list(rows[0].keys())
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows) 


def copy_csv(src, dst) -> int:
    """Skopiuj plik CSV: wczytaj ze zrodla i zapisz w nowym miejscu. Zwroc liczbe wierszy.

    Pierwsze zadanie SKLADANE - nie piszesz tu zadnej nowej logiki plikowej.
    Wolasz dwie funkcje, ktore juz masz.

    Dostajesz:
        src - sciezka do pliku zrodlowego (TEKST albo Path)
        dst - sciezka do pliku docelowego (TEKST albo Path). Katalog moze nie istniec.

    Zwracasz:
        Liczbe skopiowanych wierszy DANYCH.

    Zasady:
        - Gdy plik zrodlowy NIE ISTNIEJE -> zwracasz 0 i NIE tworzysz pliku docelowego.
        - Gdy zrodlo ma zero wierszy danych -> zwracasz 0, pliku docelowego nie ma.
        - Wierszy NIE zmieniasz - kopiujesz w oryginalnej postaci.

    Przyklady:
        copy_csv("data/orders.csv", "output/kopia.csv")   -> 6
        copy_csv("nie_ma.csv", "output/kopia.csv")        -> 0   (kopia NIE powstaje)

    Uwagi:
        - DRY: `read_csv_rows(src)` (#2), potem `write_csv_rows(dst, rows)` (#5).
          To sa DWIE LINIE plus return. Jesli piszesz tu `with open(...)` albo
          `csv.DictReader` - robisz to zle i zobacze to na review.
        - Zwroc uwage, ze przypadki brzegowe zalatwiaja sie SAME: brak zrodla ->
          read_csv_rows zwraca [] -> write_csv_rows dostaje [] -> zwraca 0
          i nie tworzy pliku. Nie musisz ich obslugiwac osobno.
          TO JEST NAGRODA za porzadne napisanie #2 i #5.
        - Wynik write_csv_rows zapisz albo zwroc bezposrednio - nie licz niczego
          drugi raz (uwaga z R3 i R4).

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestCopyCsv -v
    """
    rows = read_csv_rows(src)
    return write_csv_rows(dst,rows)


def filter_csv_by_status(src, dst, status: str) -> int:
    """Wczytaj CSV, zostaw tylko wiersze o podanym statusie, zapisz do nowego pliku.

    To jest prawdziwy mini-ETL: EXTRACT (wczytaj) -> TRANSFORM (odfiltruj) -> LOAD (zapisz).
    Dokladnie to, co robi data engineer, tylko w miniaturze.

    Dostajesz:
        src    - sciezka do pliku zrodlowego CSV
        dst    - sciezka do pliku wynikowego CSV (katalog moze nie istniec)
        status - status do zostawienia, np. "paid"

    Zwracasz:
        Liczbe wierszy, ktore przeszly filtr i zostaly zapisane.

    Zasady:
        - Porownanie statusow jest ZNORMALIZOWANE po obu stronach:
          " PAID " w pliku i "paid" w argumencie to TEN SAM status.
          Normalizacja to .strip().lower() (znasz z R1 i R4).
        - Wiersz bez klucza "status" -> pomijasz.
        - Wiersze zapisujesz w ORYGINALNEJ POSTACI - niczego nie czyscisz.
          Normalizacja sluzy TYLKO do porownania, nie do zmiany danych.
        - Gdy zrodlo nie istnieje LUB zaden wiersz nie pasuje -> zwracasz 0
          i NIE tworzysz pliku wynikowego.

    Przyklady:
        Plik zrodlowy:
            order_id,status
            1001,paid
            1002,pending
            1003,PAID

        filter_csv_by_status("orders.csv", "output/paid.csv", "paid") -> 2

        Plik output/paid.csv:
            order_id,status
            1001,paid
            1003,PAID          <- ZAPISANY W ORYGINALNEJ POSTACI, wielkimi literami

        filter_csv_by_status("orders.csv", "output/x.csv", "refunded") -> 0
            (nic nie pasuje -> plik NIE POWSTAJE)

    Uwagi:
        - DRY: `read_csv_rows` (#2) na wejsciu, `write_csv_rows` (#5) na wyjsciu.
          W srodku Twoja petla filtrujaca z R3 (pusta lista -> .append() -> zwroc).
        - Znormalizuj argument `status` RAZ, przed petla - nie w kazdym obrocie.
          Nie licz tej samej rzeczy wiele razy (uwaga z R3 i R4).
        - KOLEJNOSC w petli: najpierw `row.get("status")`, sprawdz `is None`,
          DOPIERO POTEM .strip().lower() - bo None.strip() by wybuchlo.
          Ta sama kolejnosc co w count_statuses z R4.
        - Do listy dokladasz CALY oryginalny `row`, nie jego przerobiona wersje.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestFilterCsvByStatus -v
    """
    rows = read_csv_rows(src)
    normalized_status = status.strip().lower()

    filtered_rows = []

    for row in rows:
        row_status = row.get("status")

        if row_status is None:
            continue

        if row_status.strip().lower() == normalized_status:
            filtered_rows.append(row)
    return write_csv_rows(dst, filtered_rows)


def csv_summary(path) -> dict:
    """Zwroc krotki raport o pliku CSV: czy istnieje, ile wierszy, jakie kolumny.

    Zadanie integrujace - skladasz dwie wczesniejsze funkcje w jeden wynik.

    Dostajesz:
        path - sciezka do pliku CSV (TEKST albo Path).

    Zwracasz:
        Slownik z DOKLADNIE trzema kluczami:
            {
                "exists":  True / False,      # czy plik istnieje
                "rows":    liczba wierszy DANYCH (bez naglowka),
                "columns": lista nazw kolumn,
            }

    Przyklady:
        Plik o tresci:
            order_id,customer_name
            1001,Anna
            1002,Piotr

        csv_summary("orders.csv") -> {
            "exists": True,
            "rows": 2,
            "columns": ["order_id", "customer_name"],
        }

        Plik z SAMYM naglowkiem:
        csv_summary("puste_dane.csv") -> {
            "exists": True,
            "rows": 0,
            "columns": ["order_id", "customer_name"],
        }
            (plik istnieje, kolumny sa, danych brak - trzy rozne informacje)

        csv_summary("nie_ma.csv") -> {
            "exists": False,
            "rows": 0,
            "columns": [],
        }

    Uwagi:
        - DRY: `read_csv_rows` (#2) da Ci wiersze, `get_headers` (#3) da kolumny.
          Nie otwieraj tu pliku recznie.
        - Do sprawdzenia istnienia: `Path(path).exists()`.
          TUTAJ .exists() jest na miejscu - pytasz o istnienie jako INFORMACJE
          do raportu, a nie jako zabezpieczenie przed otwarciem pliku
          (tam lepszy jest try/except - patrz notes, rozdzial 11).
        - Liczba wierszy to po prostu len() z wyniku #2.
        - Zwroc uwage, dlaczego "rows" i "columns" musza pochodzic z DWOCH roznych
          funkcji: plik z samym naglowkiem ma 0 wierszy, ale MA kolumny.

    Testuj:  uv run pytest tests/test_powtorka_05.py::TestCsvSummary -v
    """
    csv_path = Path(path)

    rows = read_csv_rows(csv_path)
    columns = get_headers(csv_path)

    return {
        "exists": csv_path.exists(),
        "rows": len(rows),
        "columns": columns,
    }
