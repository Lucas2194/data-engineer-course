"""DEMO R6 - sortowanie i skladanie funkcji. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje sa juz napisane. Pokazuja siedem technik:
    1. sorted()                -> nowa posortowana lista (oryginal nietkniety)
    2. sorted() vs .sort()     -> zwraca nowa liste vs zwraca None
    3. reverse=True            -> malejaco
    4. key=<funkcja>           -> po CZYM porownujemy
    5. lambda                  -> funkcja bez nazwy, w miejscu
    6. .items() + krotka       -> slownik -> posortowana lista par
    7. wycinek [:n]            -> pierwsze n, bez IndexError

Demo NICZEGO nie zapisuje na dysk - tylko czyta data/orders.csv i drukuje.

Uruchom:
    uv run python -m src.powtorka_06_sortowanie.demo
"""

import csv
from pathlib import Path

# Sciezka liczona OD TEGO PLIKU, nie od katalogu, z ktorego uruchamiasz program.
DATA_FILE = Path(__file__).parent / "data" / "orders.csv"


# ---------------------------------------------------------------------------
# Klocki z poprzednich blokow. Nie o nich jest ten blok - sa tu, zeby demo
# mialo na czym pracowac.
# ---------------------------------------------------------------------------
def to_float(value) -> float | None:
    """Z R2: zamien na float albo zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def normalize_status(value) -> str | None:
    """Z R4: obetnij spacje i zrob male litery. Smiec -> None."""
    if not isinstance(value, str):
        return None
    cleaned = value.strip().lower()
    return cleaned or None


def read_csv_rows(path) -> list[dict]:
    """Z R5: wczytaj CSV jako liste slownikow."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


# ---------------------------------------------------------------------------
# 1-3. sorted(), .sort() i reverse=
# ---------------------------------------------------------------------------
def demo_sorted_vs_sort() -> None:
    """sorted() zwraca NOWA liste. .sort() zmienia w miejscu i zwraca None."""
    original = [5, 1, 4, 2]

    new_list = sorted(original)
    print(f"  sorted(original)   -> {new_list}")
    print(f"  original po sorted -> {original}       <- NIETKNIETY")

    copy = original.copy()              # kopia, zeby nie zepsuc `original`
    result = copy.sort()                # <- .sort() zwraca None!
    print(f"  copy.sort() zwrocilo -> {result}          <- None, nie lista")
    print(f"  ale `copy` jest teraz -> {copy}")

    print(f"  sorted(original, reverse=True) -> {sorted(original, reverse=True)}")


# ---------------------------------------------------------------------------
# 4. key= z GOTOWA funkcja (bez lambda)
# ---------------------------------------------------------------------------
def demo_key_with_function() -> None:
    """key= przyjmuje FUNKCJE. Przekazujesz jej nazwe BEZ nawiasow."""
    words = ["kot", "a", "abcd", "xy"]

    print(f"  sorted(words)          -> {sorted(words)}   <- alfabetycznie")
    print(f"  sorted(words, key=len) -> {sorted(words, key=len)}   <- po dlugosci")
    #                          ^^^ BEZ nawiasow: dajesz przepis, nie wynik

    # key= moze byc dowolna funkcja - takze Twoja wlasna:
    print(f"  sorted(words, key=str.upper) -> {sorted(words, key=str.upper)}")


# ---------------------------------------------------------------------------
# 5. key=lambda - na slownikach z CSV
# ---------------------------------------------------------------------------
def demo_key_with_lambda(rows: list[dict]) -> None:
    """Slownikow nie da sie porownac wprost - key= mowi, PO CZYM sortowac."""
    # sorted(rows) -> TypeError: '<' not supported between instances of 'dict'

    # PULAPKA: bez konwersji sortujesz TEKSTY, wiec "1000" wypada przed "90".
    by_text = sorted(rows, key=lambda row: row["total_amount"])
    print("  BEZ konwersji (alfabetycznie, ZLE):")
    for row in by_text[:4]:
        print(f"    {row['total_amount']:>8}  {row['customer_name']}")

    # DOBRZE: konwersja WEWNATRZ key=. `or 0.0` ratuje smieci ("abc", "").
    by_number = sorted(rows, key=lambda row: to_float(row["total_amount"]) or 0.0, reverse=True)
    print("  Z konwersja i malejaco (DOBRZE):")
    for row in by_number[:4]:
        print(f"    {row['total_amount']:>8}  {row['customer_name']}")


# ---------------------------------------------------------------------------
# 6. .items() + krotka jako key -> dwa kryteria naraz
# ---------------------------------------------------------------------------
def demo_sorted_pairs(rows: list[dict]) -> list[tuple]:
    """Slownika sie nie sortuje. Zamieniasz go na liste par i sortujesz liste."""
    # Agregacja z R4: {klient: suma jego zamowien "paid"}
    totals: dict[str, float] = {}
    for row in rows:
        if normalize_status(row.get("status")) != "paid":
            continue
        name = (row.get("customer_name") or "").strip()
        if not name:
            continue
        totals[name] = totals.get(name, 0.0) + (to_float(row.get("total_amount")) or 0.0)

    print(f"  slownik z agregacji: {totals}")
    print(f"  .items() daje pary:  {list(totals.items())}")

    # ZLE - reverse=True odwraca TEZ alfabet przy remisie:
    wrong = sorted(totals.items(), key=lambda pair: (pair[1], pair[0]), reverse=True)
    print(f"  reverse=True (ZLE):  {wrong}")

    # DOBRZE - minus odwraca TYLKO kwote, nazwa zostaje rosnaco:
    right = sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))
    print(f"  minus w krotce (OK): {right}")

    # Krotki porownuja sie po kolei, od lewej - stad dziala rozstrzyganie remisu:
    print(f"  (1, 'b') < (2, 'a') -> {(1, 'b') < (2, 'a')}   <- decyduje pierwszy")
    print(f"  (1, 'a') < (1, 'b') -> {(1, 'a') < (1, 'b')}   <- remis, decyduje drugi")

    return right


# ---------------------------------------------------------------------------
# 7. Wycinek [:n] - top N bez IndexError
# ---------------------------------------------------------------------------
def demo_slice(pairs: list[tuple]) -> None:
    """Wycinek nie wybucha, nawet gdy prosisz o wiecej, niz jest."""
    print(f"  pairs[:2]   -> {pairs[:2]}")
    print(f"  pairs[:100] -> {pairs[:100]}")
    print("                 <- 100 zadane, tyle ile jest zwrocone. ZERO bledu.")
    print(f"  [][:5]      -> {[][:5]}")

    # Rozpakowanie krotki w petli - czytelniejsze niz pair[0] / pair[1]:
    print("  ranking:")
    for position, (name, total) in enumerate(pairs[:3], start=1):
        print(f"    {position}. {name:<20} {total:>8.2f} zl")


def main() -> None:
    rows = read_csv_rows(DATA_FILE)

    print("=" * 70)
    print(f"DEMO R6 - sortowanie.  Plik: {DATA_FILE.name}, wierszy: {len(rows)}")
    print("=" * 70)

    print("\n[1-3] sorted() vs .sort() vs reverse=")
    demo_sorted_vs_sort()

    print("\n[4] key= z gotowa funkcja")
    demo_key_with_function()

    print("\n[5] key=lambda na danych z CSV")
    demo_key_with_lambda(rows)

    print("\n[6] .items() + krotka jako key")
    pairs = demo_sorted_pairs(rows)

    print("\n[7] wycinek [:n]")
    demo_slice(pairs)

    print("\n" + "=" * 70)
    print("Przeczytales kod tego pliku? Jesli nie - wroc na gore. Tam jest wszystko,")
    print("czego potrzebujesz do zadan.")
    print("=" * 70)


if __name__ == "__main__":
    main()
