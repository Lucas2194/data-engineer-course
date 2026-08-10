"""Powtorka R4 - slowniki jako liczniki i agregatory. Zakres: .get(k,0)+1, .items().

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-04-slowniki-liczniki.md
    2. Uruchom demo:  uv run python -m src.powtorka_04_slowniki_liczniki.demo

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_04.py::TestCountItems -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.
DRY: gdy piszesz drugi raz te sama logike, uzyj funkcji, ktora juz masz wyzej.
"""


# ---------------------------------------------------------------------------
# GOTOWE - z R2. NIE zmieniaj tej funkcji. Masz jej UZYWAC w zadaniach nizej.
# ---------------------------------------------------------------------------
def to_float(value) -> float | None:
    """Zamien wartosc na float. Gdy sie nie da - zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def count_items(items: list) -> dict:
    """Policz, ile razy wystapil kazdy element listy. Zwroc slownik {element: ile}.

    Dostajesz:
        items - lista wartosci (tekstow), np. ["a", "b", "a", "a"]

    Zwracasz:
        Slownik: klucz = element, wartosc = ile razy wystapil.

    Przyklady:
        count_items(["a", "b", "a", "a"]) -> {"a": 3, "b": 1}
        count_items(["x"])                -> {"x": 1}
        count_items([])                   -> {}

    Uwagi:
        - Wzorzec z notes, rozdzial 1: pusty slownik -> liczniki.get(item, 0) + 1.
        - Nie normalizujesz i nic nie pomijasz - liczysz to, co dostajesz.

    Testuj:  uv run pytest tests/test_powtorka_04.py::TestCountItems -v
    """
    liczniki = {}
    for item in items:
        liczniki[item] = liczniki.get(item, 0) + 1
    return liczniki


def normalize_status(text: str) -> str:
    """Ujednolic status: obetnij spacje z brzegow i zamien na male litery.

    Dostajesz:
        text - tekst statusu, np. " PAID "

    Zwracasz:
        Tekst po .strip() i .lower().

    Przyklady:
        normalize_status(" PAID ")   -> "paid"
        normalize_status("Paid")     -> "paid"
        normalize_status("pending")  -> "pending"
        normalize_status("   ")      -> ""

    Uwagi:
        - Wzorzec z notes, rozdzial 2: laczysz .strip() i .lower() w lancuszek.
        - To maly klocek - uzyjesz go w count_statuses (#3).

    Testuj:  uv run pytest tests/test_powtorka_04.py::TestNormalizeStatus -v
    """
    return text.strip().lower()


def count_statuses(orders: list) -> dict:
    """Policz, ile razy wystapil kazdy status (znormalizowany). Payoff R4.

    To jest zadanie diagnostyczne. Laczy licznik (#1) z normalizacja (#2).

    Dostajesz:
        orders - lista slownikow, np. [{"status": "paid"}, {"status": " PAID "}]

    Zwracasz:
        Slownik: klucz = status znormalizowany, wartosc = ile razy wystapil.

    Normalizacja (uzyj normalize_status z #2):
        " PAID ", "Paid" i "paid" to TEN SAM status -> koszyk "paid".

    Pomijasz zamowienia, ktore:
        - nie maja klucza "status",
        - maja status pusty ("") lub z samych spacji ("   ").

    Przyklady:
        count_statuses([
            {"status": "paid"}, {"status": " PAID "},
            {"status": "pending"}, {"status": "Paid"},
        ]) -> {"paid": 3, "pending": 1}

        count_statuses([{"status": "paid"}, {}, {"status": ""}, {"status": "   "}])
            -> {"paid": 1}

        count_statuses([]) -> {}

    Uwagi:
        - Wzorzec z notes, rozdzial 3.
        - KOLEJNOSC: najpierw order.get("status") i sprawdz `is None`, DOPIERO POTEM
          normalize_status(...) - bo None.strip() by wybuchlo.
        - Po normalizacji sprawdz, czy status nie jest "" - jak jest, pomijasz (continue).
        - Do liczenia: licznik.get(status, 0) + 1 (jak #1).

    Testuj:  uv run pytest tests/test_powtorka_04.py::TestCountStatuses -v
    """
    liczniki = {}
    for order in orders:
        status = order.get("status")
        if status is None:
            continue
        status = normalize_status(status)
        if status == "":
            continue
        liczniki[status] = liczniki.get(status, 0) + 1
    return liczniki



def sum_by_customer(orders: list) -> dict:
    """Zsumuj kwoty zamowien per klient. Zwroc slownik {klient: suma}.

    Dostajesz:
        orders - lista slownikow z kluczami "customer_name" i "total_amount".
                 Kwota moze byc tekstem ("100"), liczba (50), smieciem ("abc"),
                 None albo moze jej brakowac.

    Zwracasz:
        Slownik: klucz = nazwa klienta (obcieta ze spacji), wartosc = suma jego kwot
        jako float.

    Zasady:
        - Nazwe klienta obcinasz ze spacji: " Anna " -> "Anna".
        - Klienta bez nazwy (pusta, same spacje albo brak klucza) POMIJASZ.
        - Kwote pobierasz BEZPIECZNIE przez to_float. Gdy sie nie da (smiec, None,
          brak klucza) - liczysz ja jako 0.0 (klient zostaje, kwota = 0).
        - Ten sam klient w kilku zamowieniach -> sumujesz jego kwoty.

    Przyklady:
        sum_by_customer([
            {"customer_name": "Anna",  "total_amount": "100"},
            {"customer_name": "Anna",  "total_amount": "50"},
            {"customer_name": "Piotr", "total_amount": "120"},
        ]) -> {"Anna": 150.0, "Piotr": 120.0}

        sum_by_customer([{"customer_name": " Ola ", "total_amount": "abc"}])
            -> {"Ola": 0.0}

        sum_by_customer([{"customer_name": "", "total_amount": "999"}]) -> {}
        sum_by_customer([]) -> {}

    Uwagi:
        - Wzorzec z notes, rozdzial 4: sumy.get(name, 0) + kwota (zamiast + 1).
        - UZYJ to_float z gory (DRY). Zapisz jego wynik do zmiennej i jej uzyj -
          nie wolaj float() drugi raz (uwaga z R3).
        - Nazwe pobierasz bezpiecznie: order.get("customer_name", "").strip().

    Testuj:  uv run pytest tests/test_powtorka_04.py::TestSumByCustomer -v
    """
    sumy = {}
    for order in orders:
        name = order.get("customer_name", "").strip()
        if name == "":
            continue
        kwota = to_float(order.get("total_amount"))
        if kwota is None:
            kwota = 0.0
        sumy[name] = sumy.get(name, 0) + kwota
    return sumy



def highest_spender(orders: list) -> tuple | None:
    """Znajdz klienta, ktory wydal najwiecej. Zwroc (nazwa, suma) albo None.

    Buduje na sum_by_customer z #4.

    Dostajesz:
        orders - lista slownikow (jak w sum_by_customer).

    Zwracasz:
        KROTKE (nazwa_klienta, jego_suma) - tego z NAJWYZSZA suma.
        None - gdy nie ma zadnego klienta z nazwa (pusty wynik sum_by_customer).

    Przyklady:
        highest_spender([
            {"customer_name": "Anna",  "total_amount": "100"},
            {"customer_name": "Anna",  "total_amount": "50"},
            {"customer_name": "Piotr", "total_amount": "120"},
        ]) -> ("Anna", 150.0)

        highest_spender([{"customer_name": "Piotr", "total_amount": "120"}])
            -> ("Piotr", 120.0)

        highest_spender([]) -> None
        highest_spender([{"customer_name": "", "total_amount": "999"}]) -> None

    Uwagi:
        - Wzorzec z notes, rozdzial 5-6: najpierw sum_by_customer(orders) (REUZYJ #4),
          potem chodzenie po .items() i pamietanie najlepszego.
        - Warunek: `if best_total is None or total > best_total:` - pierwszy klient
          zawsze zostaje zapisany, kazdy kolejny tylko gdy pobil rekord.
        - Gdy slownik sum jest pusty - petla nic nie zrobi, zwracasz None.
        - (Remisów tu nie testujemy - pelnym sortowaniem zajmie sie R6.)

    Testuj:  uv run pytest tests/test_powtorka_04.py::TestHighestSpender -v
    """

    
    best_name = None
    best_total = None
    sumy = sum_by_customer(orders)
    for name, total in sumy.items():
        if best_total is None or total > best_total:
            best_name = name
            best_total = total
    if best_total is None:
            return None
    return best_name, best_total
