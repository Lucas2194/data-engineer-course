"""Testy do powtorki R3 - listy i petle.

Kazda klasa = jedno zadanie z src/powtorka_03_listy_petle/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_03.py::TestKeepPositive -v
"""

from src.powtorka_03_listy_petle.exercises import (
    filter_valid_amounts,
    is_valid_order,
    keep_positive,
    split_valid_invalid,
    to_float_list,
)


class TestKeepPositive:
    def test_mieszane_zostaja_dodatnie(self):
        assert keep_positive([5, -3, 0, 10, -1]) == [5, 10]

    def test_wszystkie_dodatnie(self):
        assert keep_positive([1, 2, 3]) == [1, 2, 3]

    def test_zero_odpada(self):
        assert keep_positive([-5, 0]) == []

    def test_pusta_lista(self):
        assert keep_positive([]) == []

    def test_nie_zmienia_wejscia(self):
        dane = [1, -2, 3]
        keep_positive(dane)
        assert dane == [1, -2, 3]


class TestToFloatList:
    def test_pomija_smieci(self):
        assert to_float_list(["12.5", "abc", 30, None, ""]) == [12.5, 30.0]

    def test_same_dobre(self):
        assert to_float_list(["1", "2", "3"]) == [1.0, 2.0, 3.0]

    def test_zero_zostaje(self):
        assert to_float_list([0, "0"]) == [0.0, 0.0]

    def test_ujemne_zostaja(self):
        assert to_float_list(["-5", -3]) == [-5.0, -3.0]

    def test_same_smieci(self):
        assert to_float_list(["abc", None]) == []

    def test_pusta_lista(self):
        assert to_float_list([]) == []


class TestFilterValidAmounts:
    def test_mieszane(self):
        assert filter_valid_amounts(["12.50", 30, "abc", None, "", -5, 0, 7.25]) == [
            12.5,
            30.0,
            7.25,
        ]

    def test_zero_i_ujemne_odpadaja(self):
        assert filter_valid_amounts([-5, 0, "-3"]) == []

    def test_same_smieci(self):
        assert filter_valid_amounts(["abc", None]) == []

    def test_pusta_lista(self):
        assert filter_valid_amounts([]) == []

    def test_zwraca_floaty(self):
        assert filter_valid_amounts(["30"]) == [30.0]


class TestIsValidOrder:
    def test_komplet_pol(self):
        assert is_valid_order(
            {"order_id": "1", "customer_name": "Anna"}, ["order_id", "customer_name"]
        ) is True

    def test_pusta_wartosc(self):
        assert is_valid_order(
            {"order_id": "2", "customer_name": ""}, ["order_id", "customer_name"]
        ) is False

    def test_brak_klucza(self):
        assert is_valid_order(
            {"order_id": "3"}, ["order_id", "customer_name"]
        ) is False

    def test_same_spacje(self):
        assert is_valid_order(
            {"order_id": "4", "customer_name": "   "}, ["order_id", "customer_name"]
        ) is False

    def test_brak_wymagan_daje_true(self):
        assert is_valid_order({"cokolwiek": "x"}, []) is True


class TestSplitValidInvalid:
    def test_dzieli_na_dwie_kupki(self):
        orders = [
            {"order_id": "1", "customer_name": "Anna"},
            {"order_id": "2", "customer_name": ""},
            {"order_id": "3"},
            {"order_id": "5", "customer_name": "Ewa"},
        ]
        valid, invalid = split_valid_invalid(orders, ["order_id", "customer_name"])
        assert valid == [
            {"order_id": "1", "customer_name": "Anna"},
            {"order_id": "5", "customer_name": "Ewa"},
        ]
        assert invalid == [
            {"order_id": "2", "customer_name": ""},
            {"order_id": "3"},
        ]

    def test_zwraca_krotke(self):
        wynik = split_valid_invalid([], ["order_id"])
        assert wynik == ([], [])
        assert isinstance(wynik, tuple)

    def test_brak_wymagan_wszystko_valid(self):
        assert split_valid_invalid([{"a": 1}, {}], []) == ([{"a": 1}, {}], [])
