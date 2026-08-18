"""Testy do powtorki R6 - CZESC A: sortowanie.

Kazda klasa = jedno zadanie z src/powtorka_06_sortowanie/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_06.py::TestSortNames -v

--------------------------------------------------------------------------------
CZESC B (PROJEKT.md) NIE MA TESTOW - i to jest celowe.
Tam sam decydujesz, jakie funkcje napisac, wiec nie ma czego z gory sprawdzic.
Weryfikacja czesci B: tabela kontrolna w PROJEKT.md + review coacha.
--------------------------------------------------------------------------------
"""

from src.powtorka_06_sortowanie.exercises import (
    sort_by_length,
    sort_names,
    sort_orders_by_amount,
    sorted_totals,
    top_customers,
)

# Dane wspolne dla kilku klas - wiersze jak z CSV (WSZYSTKO tekstem).
ORDERS = [
    {"customer_name": "Anna", "total_amount": "100.00", "status": "paid"},
    {"customer_name": "Anna", "total_amount": "50.00", "status": " PAID "},
    {"customer_name": "Anna", "total_amount": "999.00", "status": "cancelled"},
    {"customer_name": "Piotr", "total_amount": "120.00", "status": "paid"},
    {"customer_name": "", "total_amount": "500.00", "status": "paid"},
]


class TestSortNames:
    def test_sortuje_alfabetycznie(self):
        assert sort_names(["Piotr", "Anna", "Marek"]) == ["Anna", "Marek", "Piotr"]

    def test_malejaco_gdy_descending(self):
        assert sort_names(["Piotr", "Anna", "Marek"], descending=True) == [
            "Piotr",
            "Marek",
            "Anna",
        ]

    def test_domyslnie_rosnaco(self):
        # descending ma wartosc domyslna - wolajacy moze go pominac
        assert sort_names(["b", "a"]) == ["a", "b"]

    def test_pusta_lista(self):
        assert sort_names([]) == []

    def test_nie_zmienia_wejscia(self):
        # DLATEGO uzywasz sorted(), a nie .sort()
        names = ["Piotr", "Anna"]
        sort_names(names)
        assert names == ["Piotr", "Anna"]

    def test_zwraca_nowa_liste(self):
        names = ["Anna", "Piotr"]
        assert sort_names(names) is not names


class TestSortByLength:
    def test_sortuje_po_dlugosci(self):
        assert sort_by_length(["kot", "a", "abcd", "xy"]) == ["a", "xy", "kot", "abcd"]

    def test_rowna_dlugosc_zachowuje_kolejnosc(self):
        # sortowanie w Pythonie jest STABILNE - rozdzial 11 notatki
        assert sort_by_length(["bb", "aa", "c"]) == ["c", "bb", "aa"]

    def test_nie_sortuje_alfabetycznie(self):
        # gdyby ktos zapomnial o key=, wyszloby ['aaa', 'z']
        assert sort_by_length(["aaa", "z"]) == ["z", "aaa"]

    def test_pusta_lista(self):
        assert sort_by_length([]) == []

    def test_nie_zmienia_wejscia(self):
        words = ["abcd", "a"]
        sort_by_length(words)
        assert words == ["abcd", "a"]


class TestSortOrdersByAmount:
    def test_sortuje_malejaco_po_kwocie(self):
        orders = [
            {"order_id": "1", "total_amount": "90.00"},
            {"order_id": "2", "total_amount": "1000.00"},
        ]
        assert [row["order_id"] for row in sort_orders_by_amount(orders)] == ["2", "1"]

    def test_nie_sortuje_jak_tekst(self):
        # PULAPKA: bez float() "1000.00" wyladowaloby PRZED "90.00"
        orders = [
            {"order_id": "maly", "total_amount": "9.00"},
            {"order_id": "duzy", "total_amount": "1000.00"},
        ]
        assert sort_orders_by_amount(orders)[0]["order_id"] == "duzy"

    def test_smiec_traktowany_jak_zero(self):
        orders = [
            {"order_id": "1", "total_amount": "abc"},
            {"order_id": "2", "total_amount": "10.00"},
        ]
        assert [row["order_id"] for row in sort_orders_by_amount(orders)] == ["2", "1"]

    def test_pusty_tekst_traktowany_jak_zero(self):
        orders = [
            {"order_id": "1", "total_amount": ""},
            {"order_id": "2", "total_amount": "5.00"},
        ]
        assert [row["order_id"] for row in sort_orders_by_amount(orders)] == ["2", "1"]

    def test_ujemna_kwota_na_koncu(self):
        orders = [
            {"order_id": "1", "total_amount": "-40.00"},
            {"order_id": "2", "total_amount": "0.00"},
        ]
        assert [row["order_id"] for row in sort_orders_by_amount(orders)] == ["2", "1"]

    def test_pusta_lista(self):
        assert sort_orders_by_amount([]) == []

    def test_nie_zmienia_wejscia(self):
        orders = [
            {"order_id": "1", "total_amount": "1.00"},
            {"order_id": "2", "total_amount": "9.00"},
        ]
        sort_orders_by_amount(orders)
        assert [row["order_id"] for row in orders] == ["1", "2"]

    def test_nie_zmienia_slownikow(self):
        # przestawiasz kolejnosc, nie ruszasz zawartosci
        orders = [{"order_id": "1", "total_amount": "1.00"}]
        assert sort_orders_by_amount(orders)[0] == {"order_id": "1", "total_amount": "1.00"}


class TestSortedTotals:
    def test_sortuje_malejaco_po_sumie(self):
        assert sorted_totals({"Anna": 250.0, "Marek": 120.0}) == [
            ("Anna", 250.0),
            ("Marek", 120.0),
        ]

    def test_kolejnosc_wejscia_nie_ma_znaczenia(self):
        assert sorted_totals({"Marek": 120.0, "Anna": 250.0}) == [
            ("Anna", 250.0),
            ("Marek", 120.0),
        ]

    def test_remis_rozstrzyga_alfabet(self):
        # TU sie wywali reverse=True - dalby Zofia, Piotr, Anna
        assert sorted_totals({"Zofia": 250.0, "Anna": 250.0, "Piotr": 250.0}) == [
            ("Anna", 250.0),
            ("Piotr", 250.0),
            ("Zofia", 250.0),
        ]

    def test_remis_czesciowy(self):
        assert sorted_totals({"Zofia": 250.0, "Anna": 250.0, "Marek": 900.0}) == [
            ("Marek", 900.0),
            ("Anna", 250.0),
            ("Zofia", 250.0),
        ]

    def test_zwraca_krotki_nie_listy(self):
        wynik = sorted_totals({"Anna": 1.0})
        assert isinstance(wynik[0], tuple)

    def test_pusty_slownik(self):
        assert sorted_totals({}) == []

    def test_jeden_klient(self):
        assert sorted_totals({"Anna": 10.0}) == [("Anna", 10.0)]

    def test_wartosci_ujemne(self):
        assert sorted_totals({"Anna": -10.0, "Marek": 5.0}) == [
            ("Marek", 5.0),
            ("Anna", -10.0),
        ]


class TestTopCustomers:
    def test_przyklad_z_docstringa(self):
        assert top_customers(ORDERS, 2) == [("Anna", 150.0), ("Piotr", 120.0)]

    def test_liczy_tylko_paid(self):
        # 999.00 ma status cancelled - nie moze wejsc do sumy Anny
        assert top_customers(ORDERS, 1) == [("Anna", 150.0)]

    def test_status_normalizowany(self):
        orders = [{"customer_name": "Anna", "total_amount": "10.00", "status": "  PaId "}]
        assert top_customers(orders, 1) == [("Anna", 10.0)]

    def test_pomija_klienta_bez_nazwy(self):
        wynik = top_customers(ORDERS, 10)
        assert [name for name, _ in wynik] == ["Anna", "Piotr"]

    def test_pomija_same_spacje_jako_nazwe(self):
        orders = [{"customer_name": "   ", "total_amount": "10.00", "status": "paid"}]
        assert top_customers(orders, 5) == []

    def test_obcina_spacje_z_nazwy(self):
        orders = [
            {"customer_name": " Anna ", "total_amount": "10.00", "status": "paid"},
            {"customer_name": "Anna", "total_amount": "5.00", "status": "paid"},
        ]
        # po obcieciu spacji to JEDEN klient, nie dwoch
        assert top_customers(orders, 5) == [("Anna", 15.0)]

    def test_smiec_w_kwocie_liczony_jak_zero(self):
        orders = [
            {"customer_name": "Anna", "total_amount": "abc", "status": "paid"},
            {"customer_name": "Piotr", "total_amount": "5.00", "status": "paid"},
        ]
        assert top_customers(orders, 5) == [("Piotr", 5.0), ("Anna", 0.0)]

    def test_brakujace_klucze_nie_wywalaja(self):
        orders = [
            {"status": "paid"},
            {"customer_name": "Anna", "status": "paid"},
            {"customer_name": "Piotr", "total_amount": "5.00", "status": "paid"},
        ]
        assert top_customers(orders, 5) == [("Piotr", 5.0), ("Anna", 0.0)]

    def test_remis_rozstrzyga_alfabet(self):
        orders = [
            {"customer_name": "Zofia", "total_amount": "10.00", "status": "paid"},
            {"customer_name": "Anna", "total_amount": "10.00", "status": "paid"},
        ]
        assert top_customers(orders, 2) == [("Anna", 10.0), ("Zofia", 10.0)]

    def test_n_wieksze_niz_liczba_klientow(self):
        # wycinek NIE wybucha - dlatego ten przypadek zalatwia sie sam
        assert top_customers(ORDERS, 100) == [("Anna", 150.0), ("Piotr", 120.0)]

    def test_n_zero(self):
        assert top_customers(ORDERS, 0) == []

    def test_n_ujemne(self):
        assert top_customers(ORDERS, -1) == []

    def test_pusta_lista_zamowien(self):
        assert top_customers([], 5) == []

    def test_zaden_status_nie_jest_paid(self):
        orders = [{"customer_name": "Anna", "total_amount": "10.00", "status": "pending"}]
        assert top_customers(orders, 5) == []

    def test_nie_zmienia_wejscia(self):
        orders = [{"customer_name": " Anna ", "total_amount": "10.00", "status": "paid"}]
        top_customers(orders, 1)
        assert orders == [{"customer_name": " Anna ", "total_amount": "10.00", "status": "paid"}]
