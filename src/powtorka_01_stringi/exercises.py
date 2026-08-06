"""Powtorka R1 - stringi i formatowanie. Zakres: f-string, :.2f, metody stringow.

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-01-stringi.md
    2. Uruchom demo:  uv run python -m src.powtorka_01_stringi.demo

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_01.py::TestCleanText -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.
"""


def clean_text(text: str) -> str:
    """Obetnij biale znaki (spacje) z obu brzegow tekstu.

    Dostajesz:
        text - tekst, moze miec zbedne spacje na brzegach, np. "  Anna  "

    Zwracasz:
        Ten sam tekst bez spacji na brzegach. Srodek zostaje nietkniety.

    Przyklady:
        clean_text("  Anna  ")   -> "Anna"
        clean_text("Piotr")      -> "Piotr"
        clean_text("Jan Nowak")  -> "Jan Nowak"   (spacja w srodku ZOSTAJE)
        clean_text("   ")        -> ""            (same spacje -> pusty tekst)
        clean_text("")           -> ""

    Uwagi:
        - Jedna metoda stringa zalatwia cale zadanie. Szukaj w notes, rozdzial 3.

    Testuj:  uv run pytest tests/test_powtorka_01.py::TestCleanText -v
    """
    return text.strip()


def normalize_status(status: str) -> str:
    """Znormalizuj status: obetnij spacje ORAZ zamien na male litery.

    Po co: " PAID ", "Paid" i "paid" maja byc traktowane jako TEN SAM status.
    Ta funkcja sprowadza je wszystkie do jednej postaci: "paid".

    Dostajesz:
        status - tekst statusu, np. " PAID ", "Pending", "shipped"

    Zwracasz:
        Status obciety ze spacji i zamieniony na male litery.

    Przyklady:
        normalize_status(" PAID ")   -> "paid"
        normalize_status("Paid")     -> "paid"
        normalize_status("Pending")  -> "pending"
        normalize_status("shipped")  -> "shipped"
        normalize_status("   ")      -> ""

    Uwagi:
        - Dwie metody stringa jedna po drugiej. Kolejnosc nie ma tu znaczenia,
          ale klasycznie: najpierw obcinasz, potem zmniejszasz litery.
        - Metody stringow ZWRACAJA nowy tekst - pamietaj, ze wynik trzeba zwrocic.

    Testuj:  uv run pytest tests/test_powtorka_01.py::TestNormalizeStatus -v
    """
    return status.strip().lower()


def format_amount(amount: float) -> str:
    """Sformatuj kwote jako tekst z DOKLADNIE dwoma miejscami po przecinku.

    Dostajesz:
        amount - liczba, np. 149.5, 89.0, 3.14159, 0

    Zwracasz:
        STRING z dwoma miejscami po przecinku. Bez waluty, bez spacji - sama liczba.

    Przyklady:
        format_amount(149.5)    -> "149.50"   (doklejone zero)
        format_amount(89.0)     -> "89.00"
        format_amount(3.14159)  -> "3.14"     (obciete do dwoch miejsc)
        format_amount(0)        -> "0.00"
        format_amount(1234.5)   -> "1234.50"

    Uwagi:
        - To jest format spec :.2f w f-stringu. Notes, rozdzial 2.
        - Nie uzywaj round() - round(149.5, 2) da 149.5, a Ty potrzebujesz "149.50".

    Testuj:  uv run pytest tests/test_powtorka_01.py::TestFormatAmount -v
    """
    return f"{amount:.2f}"


def format_order_line(order_id: int, customer_name: str, amount: float) -> str:
    """Zbuduj jedna linie podsumowania zamowienia. Zlozenie trzech poprzednich klockow.

    To jest dokladnie zadanie #1 z diagnostyki (format_order_summary). Tym razem
    umiesz juz kazdy kawalek osobno - teraz sklej je razem.

    Dostajesz:
        order_id      - liczba, np. 1
        customer_name - tekst, moze miec zbedne spacje na brzegach, np. "  Piotr  "
        amount        - liczba, np. 149.99 albo 149.5

    Zwracasz:
        Jeden STRING w dokladnie takim formacie:
        "Zamowienie #<id> | <imie> | <kwota> PLN"

    Przyklady:
        format_order_line(1, "Anna Kowalska", 149.99)
            -> "Zamowienie #1 | Anna Kowalska | 149.99 PLN"

        format_order_line(7, "Ewa", 149.5)
            -> "Zamowienie #7 | Ewa | 149.50 PLN"       (kwota z dwoma miejscami)

        format_order_line(2, "  Piotr  ", 89.0)
            -> "Zamowienie #2 | Piotr | 89.00 PLN"      (spacje wokol imienia znikaja)

    Uwagi:
        - Separator to spacja-kreska-spacja: " | "
        - Imie: obcinasz spacje (jak w clean_text).
        - Kwota: dwa miejsca po przecinku (jak w format_amount).
        - Wszystko zmiesci sie w jednym f-stringu.

    Testuj:  uv run pytest tests/test_powtorka_01.py::TestFormatOrderLine -v
    """
    return f"Zamowienie #{order_id} | {customer_name.strip()} | {amount:.2f} PLN"


def initials(full_name: str) -> str:
    """Zbuduj inicjaly z imienia i nazwiska (ZADANIE STRETCH).

    Dostajesz:
        full_name - imie i (opcjonalnie) nazwisko, np. "Anna Kowalska".
                    Moze miec zbedne spacje, moze byc jedno slowo, moze byc puste.

    Zwracasz:
        Pierwsze litery kazdego slowa, WIELKIMI literami, sklejone razem.

    Przyklady:
        initials("Anna Kowalska")     -> "AK"
        initials("piotr nowak")       -> "PN"
        initials("Jan Maria Rokita")  -> "JMR"
        initials("  Ewa  ")           -> "E"     (jedno slowo -> jedna litera)
        initials("")                  -> ""      (pusto -> pusto)

    Uwagi:
        - Rozbicie tekstu na slowa: metoda .split() bez argumentu dzieli po spacjach
          i sama radzi sobie z wieloma spacjami oraz spacjami na brzegach.
        - Pierwsza litera slowa: slowo[0]. Wielka litera: .upper().
        - Zbierasz litery w petli albo skladasz je - dowolna droga jest dobra.

    Testuj:  uv run pytest tests/test_powtorka_01.py::TestInitials -v
    """
    tekst = full_name.strip()
    slowa = tekst.split()
    initials = ""

    for slowo in slowa:
        initials = initials + slowo[0]

    return initials.upper()

     
