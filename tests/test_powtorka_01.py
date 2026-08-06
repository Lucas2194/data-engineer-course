"""Testy do powtorki R1 - stringi i formatowanie.

Kazda klasa = jedno zadanie z src/powtorka_01_stringi/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_01.py::TestCleanText -v
"""

from src.powtorka_01_stringi.exercises import (
    clean_text,
    format_amount,
    format_order_line,
    initials,
    normalize_status,
)


class TestCleanText:
    def test_obcina_z_obu_stron(self):
        assert clean_text("  Anna  ") == "Anna"

    def test_bez_spacji_bez_zmian(self):
        assert clean_text("Piotr") == "Piotr"

    def test_zostawia_spacje_w_srodku(self):
        assert clean_text("Jan Nowak") == "Jan Nowak"

    def test_same_spacje_daja_pusto(self):
        assert clean_text("   ") == ""

    def test_pusty_tekst(self):
        assert clean_text("") == ""


class TestNormalizeStatus:
    def test_obcina_i_zmniejsza(self):
        assert normalize_status(" PAID ") == "paid"

    def test_mieszana_wielkosc(self):
        assert normalize_status("Paid") == "paid"

    def test_juz_male(self):
        assert normalize_status("shipped") == "shipped"

    def test_slowo_z_wielka_litera(self):
        assert normalize_status("Pending") == "pending"

    def test_same_spacje(self):
        assert normalize_status("   ") == ""


class TestFormatAmount:
    def test_dokleja_zero(self):
        assert format_amount(149.5) == "149.50"

    def test_cala_liczba(self):
        assert format_amount(89.0) == "89.00"

    def test_obcina_do_dwoch(self):
        assert format_amount(3.14159) == "3.14"

    def test_zero(self):
        assert format_amount(0) == "0.00"

    def test_wieksza_liczba(self):
        assert format_amount(1234.5) == "1234.50"


class TestFormatOrderLine:
    def test_basic(self):
        assert (
            format_order_line(1, "Anna Kowalska", 149.99)
            == "Zamowienie #1 | Anna Kowalska | 149.99 PLN"
        )

    def test_dopelnia_kwote(self):
        assert format_order_line(7, "Ewa", 149.5) == "Zamowienie #7 | Ewa | 149.50 PLN"

    def test_obcina_imie(self):
        assert format_order_line(2, "  Piotr  ", 89.0) == "Zamowienie #2 | Piotr | 89.00 PLN"


class TestInitials:
    def test_imie_i_nazwisko(self):
        assert initials("Anna Kowalska") == "AK"

    def test_male_litery_na_wejsciu(self):
        assert initials("piotr nowak") == "PN"

    def test_trzy_slowa(self):
        assert initials("Jan Maria Rokita") == "JMR"

    def test_jedno_slowo_ze_spacjami(self):
        assert initials("  Ewa  ") == "E"

    def test_pusty_tekst(self):
        assert initials("") == ""
