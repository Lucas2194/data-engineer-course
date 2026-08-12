"""DEMO R5 - pliki: CSV, sciezki i brak pliku. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje sa juz napisane. Pokazuja siedem technik:
    1. with open()            -> otwieranie i automatyczne zamykanie
    2. petla po pliku         -> czytanie linia po linii
    3. csv.DictReader         -> wiersz CSV jako slownik
    4. .fieldnames            -> nazwy kolumn (i pulapka None)
    5. Path + mkdir           -> budowanie sciezek i tworzenie katalogow
    6. csv.DictWriter         -> zapis listy slownikow do CSV
    7. try/except             -> brak pliku nie wywala programu

Demo pisze WYLACZNIE do katalogu tymczasowego systemu - niczego Ci nie zasmieci.

Uruchom:
    uv run python -m src.powtorka_05_pliki_csv.demo
"""

import csv
import tempfile
from pathlib import Path

# Sciezka do pliku z danymi, liczona OD TEGO PLIKU (__file__), nie od katalogu,
# z ktorego uruchamiasz program. Dzieki temu demo dziala z kazdego miejsca.
DATA_FILE = Path(__file__).parent / "data" / "orders.csv"


def to_float(value):
    """Z R2: zamien na float albo zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def demo_read_lines(path) -> list[str]:
    """Czytanie pliku tekstowego linia po linii. Brak pliku -> pusta lista."""
    lines = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:                 # plik chodzi sie petla, jak liste
                lines.append(line.rstrip("\n"))   # obetnij znak konca linii
    except FileNotFoundError:
        return []                             # brak pliku -> pusty wynik, bez wybuchu
    return lines


def demo_read_csv(path) -> list[dict]:
    """csv.DictReader: kazdy wiersz jako slownik {kolumna: wartosc}."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)               # UWAGA: W SRODKU with, nie poza!
    except FileNotFoundError:
        return []


def demo_headers(path) -> list[str]:
    """Same nazwy kolumn. Pusty plik daje .fieldnames == None - stad `or []`."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader.fieldnames or [])
    except FileNotFoundError:
        return []


def demo_write_csv(path, rows: list[dict]) -> int:
    """csv.DictWriter: lista slownikow -> plik CSV. Zwraca liczbe zapisanych wierszy."""
    if not rows:
        return 0                              # nie ma czego zapisac, nie tworzymy pliku

    path = Path(path)                         # bramka: tekst albo Path -> zawsze Path
    path.parent.mkdir(parents=True, exist_ok=True)   # katalog MUSI istniec przed zapisem

    headers = list(rows[0].keys())            # kolejnosc kolumn z pierwszego wiersza
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()                  # linia naglowka - latwo zapomniec!
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    print("=== 0. PLIK ZRODLOWY ===")
    print(f"  sciezka:  {DATA_FILE}")
    print(f"  istnieje: {DATA_FILE.exists()}")
    print(f"  nazwa:    {DATA_FILE.name}   bez rozszerzenia: {DATA_FILE.stem}")
    print(f"  katalog:  {DATA_FILE.parent}")
    print()

    print("=== 1. PLIK JAKO ZWYKLY TEKST (linia po linii) ===")
    for line in demo_read_lines(DATA_FILE):
        print(f"  {line!r}")
    print("  (pierwsza linia to naglowek - dla zwyklego tekstu to nic specjalnego)")
    print()

    print("=== 2. TEN SAM PLIK PRZEZ csv.DictReader ===")
    rows = demo_read_csv(DATA_FILE)
    for row in rows:
        print(f"  {row}")
    print(f"  liczba wierszy DANYCH: {len(rows)}  (naglowek NIE jest wierszem)")
    print()

    print("=== 3. NAGLOWKI ===")
    print(f"  demo_headers(...) = {demo_headers(DATA_FILE)}")
    print()

    print("=== 4. WSZYSTKO JEST TEKSTEM ===")
    first = rows[0]
    raw = first["total_amount"]
    print(f"  first['total_amount'] = {raw!r}   typ: {type(raw).__name__}")
    print(f"  to_float(...)         = {to_float(raw)!r}   typ: float")
    print("  wiersz z PUSTA kwota (1006):")
    empty = rows[-1]["total_amount"]
    print(f"    wartosc {empty!r} -> to_float -> {to_float(empty)!r}  (None, nie wybuch)")
    print()

    print("=== 5. WCZESNIEJSZE BLOKI DZIALAJA NA TYCH WIERSZACH ===")
    counts = {}
    for row in rows:                          # licznik z R4 + normalizacja z R1
        status = row.get("status")
        if status is None:
            continue
        status = status.strip().lower()
        if status == "":
            continue
        counts[status] = counts.get(status, 0) + 1
    print(f"  count_statuses(z pliku) = {counts}")
    print("  (zwroc uwage: 'PAID' z wiersza 1003 wpadlo do koszyka 'paid')")
    print()

    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp) / "output" / "2026"     # katalog jeszcze NIE istnieje
        out_file = out_dir / "paid_orders.csv"      # sciezki sklejasz ukosnikiem /

        print("=== 6. Path + mkdir - katalog trzeba utworzyc SAMEMU ===")
        print(f"  cel:              {out_file}")
        print(f"  katalog istnieje: {out_dir.exists()}   <- jeszcze nie")

        paid = [row for row in rows if row.get("status", "").strip().lower() == "paid"]

        print()
        print("=== 7. ZAPIS PRZEZ csv.DictWriter ===")
        written = demo_write_csv(out_file, paid)
        print(f"  zapisano wierszy: {written}")
        print(f"  katalog istnieje: {out_dir.exists()}   <- mkdir go utworzyl")
        print(f"  plik istnieje:    {out_file.exists()}")
        print()
        print("  --- surowa tresc zapisanego pliku ---")
        for line in out_file.read_text(encoding="utf-8").splitlines():
            print(f"  | {line}")
        print("  (zadnych pustych linii miedzy wierszami - to zasluga newline='')")
        print()

        print("=== 8. ROUND-TRIP: zapisz -> odczytaj -> porownaj ===")
        again = demo_read_csv(out_file)
        print(f"  wczytane z powrotem: {len(again)} wierszy")
        print(f"  identyczne z tym, co zapisalem? {again == paid}")
        print()

    print("=== 9. BRAK PLIKU NIE WYWALA PROGRAMU ===")
    missing = Path("nie") / "ma" / "takiego.csv"
    print(f"  sciezka:              {missing}")
    print(f"  .exists()             -> {missing.exists()}")
    print(f"  demo_read_csv(...)    -> {demo_read_csv(missing)}")
    print(f"  demo_read_lines(...)  -> {demo_read_lines(missing)}")
    print("  (pusty wynik zamiast FileNotFoundError - pipeline jedzie dalej)")
    print()

    print("Przeczytaj kod tego pliku, potem otworz exercises.py.")
