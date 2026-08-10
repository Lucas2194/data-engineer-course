"""Testy do powtorki R4 - slowniki jako liczniki i agregatory.

Kazda klasa = jedno zadanie z src/powtorka_04_slowniki_liczniki/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_04.py::TestCountItems -v
"""

from src.powtorka_04_slowniki_liczniki.exercises import (
    count_items,
    count_statuses,
    highest_spender,
    normalize_status,
    sum_by_customer,
)


class TestCountItems:
    def test_liczy_powtorzenia(self):
        assert count_items(["a", "b", "a", "a"]) == {"a": 3, "b": 1}

    def test_jeden_element(self):
        assert count_items(["x"]) == {"x": 1}

    def test_pusta_lista(self):
        assert count_items([]) == {}

    def test_wszystkie_rozne(self):
        assert count_items(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


class TestNormalizeStatus:
    def test_spacje_i_wielkosc(self):
        assert normalize_status(" PAID ") == "paid"

    def test_wielka_litera(self):
        assert normalize_status("Paid") == "paid"

    def test_juz_dobry(self):
        assert normalize_status("pending") == "pending"

    def test_same_spacje_daje_pusty(self):
        assert normalize_status("   ") == ""


class TestCountStatuses:
    def test_normalizuje_i_liczy(self):
        assert count_statuses(
            [
                {"status": "paid"},
                {"status": " PAID "},
                {"status": "pending"},
                {"status": "Paid"},
            ]
        ) == {"paid": 3, "pending": 1}

    def test_pomija_brak_i_pusty(self):
        assert count_statuses(
            [{"status": "paid"}, {}, {"status": ""}, {"status": "   "}]
        ) == {"paid": 1}

    def test_pusta_lista(self):
        assert count_statuses([]) == {}


class TestSumByCustomer:
    def test_sumuje_per_klient(self):
        assert sum_by_customer(
            [
                {"customer_name": "Anna", "total_amount": "100"},
                {"customer_name": "Anna", "total_amount": "50"},
                {"customer_name": "Piotr", "total_amount": "120"},
            ]
        ) == {"Anna": 150.0, "Piotr": 120.0}

    def test_obcina_spacje_w_nazwie(self):
        assert sum_by_customer(
            [{"customer_name": " Ola ", "total_amount": "30"}]
        ) == {"Ola": 30.0}

    def test_smiec_liczy_jako_zero(self):
        assert sum_by_customer(
            [{"customer_name": "Ola", "total_amount": "abc"}]
        ) == {"Ola": 0.0}

    def test_pomija_bez_nazwy(self):
        assert sum_by_customer([{"customer_name": "", "total_amount": "999"}]) == {}

    def test_brak_klucza_nazwy(self):
        assert sum_by_customer([{"total_amount": "50"}]) == {}

    def test_pusta_lista(self):
        assert sum_by_customer([]) == {}


class TestHighestSpender:
    def test_zwraca_najwiekszego(self):
        assert highest_spender(
            [
                {"customer_name": "Anna", "total_amount": "100"},
                {"customer_name": "Anna", "total_amount": "50"},
                {"customer_name": "Piotr", "total_amount": "120"},
            ]
        ) == ("Anna", 150.0)

    def test_jeden_klient(self):
        assert highest_spender(
            [{"customer_name": "Piotr", "total_amount": "120"}]
        ) == ("Piotr", 120.0)

    def test_pusta_lista_daje_none(self):
        assert highest_spender([]) is None

    def test_sami_bez_nazwy_daje_none(self):
        assert highest_spender([{"customer_name": "", "total_amount": "999"}]) is None
