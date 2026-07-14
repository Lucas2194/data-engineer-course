import csv

import pytest

from src.day_21_diagnostyka.exercises import (
    count_statuses,
    filter_valid_amounts,
    format_order_summary,
    read_csv_rows,
    run_pipeline,
    safe_get_total,
    split_valid_invalid,
    top_customers,
)

MESSY_CSV = "src/day_21_diagnostyka/data/orders_messy.csv"


class TestFormatOrderSummary:
    def test_basic(self):
        assert (
            format_order_summary(1, "Anna Kowalska", 149.99)
            == "Zamowienie #1 | Anna Kowalska | 149.99 PLN"
        )

    def test_dopelnia_do_dwoch_miejsc(self):
        assert format_order_summary(7, "Ewa", 149.5) == "Zamowienie #7 | Ewa | 149.50 PLN"

    def test_obcina_biale_znaki(self):
        assert format_order_summary(2, "  Piotr  ", 89.0) == "Zamowienie #2 | Piotr | 89.00 PLN"


class TestFilterValidAmounts:
    def test_odsiewa_smieci(self):
        assert filter_valid_amounts(["12.50", 30, "abc", None, "", -5, 0, 7.25]) == [
            12.5,
            30.0,
            7.25,
        ]

    def test_pusta_lista(self):
        assert filter_valid_amounts([]) == []

    def test_wszystko_niepoprawne(self):
        assert filter_valid_amounts(["abc", None, -1, 0]) == []


class TestCountStatuses:
    def test_normalizuje_wielkosc_liter(self):
        orders = [
            {"status": "paid"},
            {"status": " PAID "},
            {"status": "pending"},
            {"status": "Paid"},
        ]
        assert count_statuses(orders) == {"paid": 3, "pending": 1}

    def test_pomija_braki(self):
        orders = [{"status": "paid"}, {}, {"status": ""}, {"status": "   "}]
        assert count_statuses(orders) == {"paid": 1}

    def test_pusta_lista(self):
        assert count_statuses([]) == {}


class TestSafeGetTotal:
    @pytest.mark.parametrize(
        "order,expected",
        [
            ({"total_amount": "149.99"}, 149.99),
            ({"total_amount": 89}, 89.0),
            ({"total_amount": ""}, 0.0),
            ({"total_amount": None}, 0.0),
            ({"total_amount": "abc"}, 0.0),
            ({}, 0.0),
        ],
    )
    def test_zwraca_float_lub_zero(self, order, expected):
        assert safe_get_total(order) == expected


class TestSplitValidInvalid:
    def test_dzieli_poprawnie(self):
        orders = [
            {"order_id": "1", "customer_name": "Anna"},
            {"order_id": "2", "customer_name": ""},
            {"order_id": "3"},
            {"order_id": "4", "customer_name": "  "},
            {"order_id": "5", "customer_name": "Ewa"},
        ]
        valid, invalid = split_valid_invalid(orders, ["order_id", "customer_name"])
        assert [o["order_id"] for o in valid] == ["1", "5"]
        assert [o["order_id"] for o in invalid] == ["2", "3", "4"]

    def test_brak_wymagan_wszystko_poprawne(self):
        orders = [{"a": 1}, {}]
        valid, invalid = split_valid_invalid(orders, [])
        assert len(valid) == 2
        assert invalid == []


class TestReadCsvRows:
    def test_wczytuje_plik(self):
        rows = read_csv_rows(MESSY_CSV)
        assert len(rows) == 10
        assert rows[0]["customer_name"] == "Anna Kowalska"
        assert rows[0]["total_amount"] == "149.99"

    def test_brak_pliku_zwraca_pusta_liste(self, tmp_path):
        assert read_csv_rows(tmp_path / "nie_ma.csv") == []


class TestTopCustomers:
    def test_sumuje_tylko_paid(self):
        orders = [
            {"customer_name": "Anna", "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Anna", "total_amount": "50.00", "status": "PAID"},
            {"customer_name": "Anna", "total_amount": "999.00", "status": "cancelled"},
            {"customer_name": "Piotr", "total_amount": "120.00", "status": "paid"},
            {"customer_name": "", "total_amount": "500.00", "status": "paid"},
        ]
        assert top_customers(orders, 2) == [("Anna", 150.0), ("Piotr", 120.0)]

    def test_remis_alfabetycznie(self):
        orders = [
            {"customer_name": "Zofia", "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Adam", "total_amount": "100.00", "status": "paid"},
        ]
        assert top_customers(orders, 2) == [("Adam", 100.0), ("Zofia", 100.0)]

    def test_n_wieksze_niz_liczba_klientow(self):
        orders = [{"customer_name": "Anna", "total_amount": "10.00", "status": "paid"}]
        assert top_customers(orders, 5) == [("Anna", 10.0)]

    def test_na_prawdziwych_danych(self):
        rows = read_csv_rows(MESSY_CSV)
        assert top_customers(rows, 2) == [("Anna Kowalska", 229.89), ("Piotr Nowak", 89.0)]


class TestRunPipeline:
    def test_pelny_przebieg(self, tmp_path):
        stats = run_pipeline(MESSY_CSV, tmp_path)

        assert stats["total"] == 10
        assert stats["valid"] == 6
        assert stats["invalid"] == 4
        assert stats["total_amount"] == 933.94

        with open(tmp_path / "valid_orders.csv", encoding="utf-8") as f:
            valid_rows = list(csv.DictReader(f))
        assert len(valid_rows) == 6
        assert [r["order_id"] for r in valid_rows] == ["1", "2", "5", "6", "9", "10"]

        with open(tmp_path / "invalid_orders.csv", encoding="utf-8") as f:
            invalid_rows = list(csv.DictReader(f))
        assert [r["order_id"] for r in invalid_rows] == ["3", "4", "7", "8"]

    def test_tworzy_katalog_wyjsciowy(self, tmp_path):
        out = tmp_path / "glebiej" / "output"
        run_pipeline(MESSY_CSV, out)
        assert (out / "valid_orders.csv").exists()

    def test_brak_pliku_wejsciowego(self, tmp_path):
        stats = run_pipeline(tmp_path / "nie_ma.csv", tmp_path / "out")
        assert stats == {"total": 0, "valid": 0, "invalid": 0, "total_amount": 0.0}
        assert not (tmp_path / "out" / "valid_orders.csv").exists()
