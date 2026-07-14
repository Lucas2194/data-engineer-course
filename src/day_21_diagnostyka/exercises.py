"""Zadania diagnostyczne po przerwie. Zakres: dni 1-20.

Nie zmieniaj nazw funkcji ani ich parametrow - testy na nich polegaja.
Rozwiazania nie sa nigdzie zapisane. Masz testy - to jedyna informacja zwrotna.

Uruchomienie wszystkich testow:
    uv run pytest tests/test_day_21.py -v

Uruchomienie jednego zadania (przyklad):
    uv run pytest tests/test_day_21.py::TestSafeGetTotal -v
"""


def format_order_summary(order_id: int, customer_name: str, total: float) -> str:
    """Zwroc podsumowanie zamowienia w formacie:

        'Zamowienie #1 | Anna Kowalska | 149.99 PLN'

    Kwota ma miec ZAWSZE dwa miejsca po przecinku (149.5 -> '149.50').
    Nazwa klienta ma byc obcieta z bialych znakow z obu stron.
    """
    pass


def filter_valid_amounts(amounts: list) -> list[float]:
    """Zwroc nowa liste zawierajaca wylacznie poprawne kwoty jako float.

    Kwota jest poprawna, gdy: da sie ja zamienic na float ORAZ jest wieksza od zera.
    Wejscie moze zawierac stringi ('12.50'), None, puste stringi i smieci ('abc').
    Kolejnosc zachowana. Elementy niepoprawne po prostu pomijasz.
    """
    pass


def count_statuses(orders: list[dict]) -> dict[str, int]:
    """Policz, ile razy wystapil kazdy status.

    Statusy normalizujesz: obcinasz biale znaki i zamieniasz na male litery,
    czyli ' PAID ' i 'paid' to ten sam status.
    Zamowienia bez klucza 'status' lub z pustym statusem pomijasz.

    Przyklad zwrotu: {'paid': 3, 'pending': 1}
    """
    pass


def safe_get_total(order: dict) -> float:
    """Zwroc wartosc zamowienia jako float.

    Gdy klucza 'total_amount' brak, jest pusty, jest None albo nie da sie go
    zamienic na liczbe - zwroc 0.0. Funkcja NIE MOZE rzucic wyjatkiem.
    """
    pass


def split_valid_invalid(
    orders: list[dict], required_keys: list[str]
) -> tuple[list[dict], list[dict]]:
    """Podziel zamowienia na poprawne i niepoprawne.

    Zamowienie jest poprawne, gdy dla KAZDEGO klucza z required_keys:
    klucz istnieje, a jego wartosc nie jest None ani pustym stringiem
    (po obcieciu bialych znakow).

    Zwroc krotke (valid, invalid). Kolejnosc w obu listach zachowana.
    """
    pass


def read_csv_rows(path) -> list[dict]:
    """Wczytaj plik CSV i zwroc liste slownikow (klucze = naglowki kolumn).

    'path' moze byc stringiem albo obiektem Path. Kodowanie: utf-8.
    Gdy plik nie istnieje - zwroc pusta liste (bez wyjatku).
    """
    pass


def top_customers(orders: list[dict], n: int) -> list[tuple[str, float]]:
    """Zwroc n klientow o najwyzszej sumie wartosci zamowien.

    Liczysz TYLKO zamowienia o statusie 'paid' (po normalizacji - patrz count_statuses).
    Wartosc zamowienia pobierasz bezpiecznie (patrz safe_get_total).
    Klientow bez nazwy (pusta / brak klucza) pomijasz.
    Nazwe klienta obcinasz z bialych znakow.

    Zwrot: lista krotek (customer_name, suma) posortowana malejaco po sumie.
    Przy remisie - alfabetycznie po nazwie klienta.
    Gdy klientow jest mniej niz n - zwroc tylu, ilu jest.

    Przyklad: [('Anna Kowalska', 539.89), ('Sofia Rossi', 55.55)]
    """
    pass


def run_pipeline(input_path, output_dir) -> dict:
    """Mini-pipeline. Zadanie integrujace wszystko powyzej.

    1. Wczytaj CSV z input_path.
    2. Podziel wiersze na poprawne i niepoprawne. Wiersz jest poprawny, gdy ma
       niepuste 'order_id', 'customer_name', 'status' ORAZ 'total_amount' daje sie
       zamienic na liczbe wieksza od zera.
    3. Zapisz poprawne do output_dir/'valid_orders.csv',
       niepoprawne do output_dir/'invalid_orders.csv'.
       Katalog output_dir utworz, jesli nie istnieje.
       Naglowki kolumn takie same jak w pliku wejsciowym.
       Wiersze zapisujesz W ORYGINALNEJ POSTACI (bez czyszczenia).
    4. Zwroc slownik statystyk:
       {'total': int, 'valid': int, 'invalid': int, 'total_amount': float}
       gdzie 'total_amount' to suma kwot z poprawnych wierszy, zaokraglona do 2 miejsc.

    Gdy plik wejsciowy nie istnieje: zwroc
    {'total': 0, 'valid': 0, 'invalid': 0, 'total_amount': 0.0} i nie zapisuj nic.
    """
    pass
