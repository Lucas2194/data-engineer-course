"""Testy do powtorki R2 - bezpieczny dostep i konwersje.

Kazda klasa = jedno zadanie z src/powtorka_02_bezpieczny_dostep/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_02.py::TestGetField -v
"""

from src.powtorka_02_bezpieczny_dostep.exercises import (
    format_total,
    get_field,
    is_convertible_to_float,
    safe_get_total,
    to_float,
)


class TestGetField:
    def test_klucz_istnieje(self):
        assert get_field({"status": "paid"}, "status", "unknown") == "paid"

    def test_klucza_brak_daje_default(self):
        assert get_field({}, "status", "unknown") == "unknown"

    def test_inny_klucz_brak_daje_default(self):
        assert get_field({"status": "paid"}, "total", 0) == 0

    def test_zwraca_liczbe_spod_klucza(self):
        assert get_field({"total": 149.99}, "total", 0) == 149.99


class TestToFloat:
    def test_tekst_z_liczba(self):
        assert to_float("149.99") == 149.99

    def test_int_owy_tekst(self):
        assert to_float("89") == 89.0

    def test_liczba(self):
        assert to_float(89) == 89.0

    def test_smiec_daje_none(self):
        assert to_float("abc") is None

    def test_pusty_daje_none(self):
        assert to_float("") is None

    def test_none_daje_none(self):
        assert to_float(None) is None


class TestIsConvertible:
    def test_liczba_w_tekscie(self):
        assert is_convertible_to_float("12.5") is True

    def test_int_owy_tekst(self):
        assert is_convertible_to_float("7") is True

    def test_liczba(self):
        assert is_convertible_to_float(7) is True

    def test_smiec(self):
        assert is_convertible_to_float("abc") is False

    def test_pusty(self):
        assert is_convertible_to_float("") is False

    def test_none(self):
        assert is_convertible_to_float(None) is False


class TestSafeGetTotal:
    def test_tekst_z_kwota(self):
        assert safe_get_total({"total_amount": "149.99"}) == 149.99

    def test_liczba(self):
        assert safe_get_total({"total_amount": 89}) == 89.0

    def test_pusty_daje_zero(self):
        assert safe_get_total({"total_amount": ""}) == 0.0

    def test_none_daje_zero(self):
        assert safe_get_total({"total_amount": None}) == 0.0

    def test_smiec_daje_zero(self):
        assert safe_get_total({"total_amount": "abc"}) == 0.0

    def test_brak_klucza_daje_zero(self):
        assert safe_get_total({}) == 0.0

    def test_ujemna_zostaje(self):
        assert safe_get_total({"total_amount": -50}) == -50.0


class TestFormatTotal:
    def test_kwota_z_tekstu(self):
        assert format_total({"total_amount": "149.5"}) == "149.50 PLN"

    def test_kwota_z_liczby(self):
        assert format_total({"total_amount": 89}) == "89.00 PLN"

    def test_smiec_daje_brak(self):
        assert format_total({"total_amount": "abc"}) == "brak danych"

    def test_pusty_daje_brak(self):
        assert format_total({"total_amount": ""}) == "brak danych"

    def test_brak_klucza_daje_brak(self):
        assert format_total({}) == "brak danych"
