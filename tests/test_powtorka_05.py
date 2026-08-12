"""Testy do powtorki R5 - pliki: CSV, sciezki i brak pliku.

Kazda klasa = jedno zadanie z src/powtorka_05_pliki_csv/exercises.py.
Czytaj testy jak specyfikacje: kazdy assert to jedno wymaganie.

Jedno zadanie naraz:
    uv run pytest tests/test_powtorka_05.py::TestReadTextLines -v

--------------------------------------------------------------------------------
NOWOSC W TYM BLOKU: tmp_path
--------------------------------------------------------------------------------
Testy plikow potrzebuja plikow. Nie tworzymy ich w repo - pytest daje nam
KATALOG TYMCZASOWY. Wystarczy wpisac `tmp_path` jako argument funkcji testowej:

    def test_cos(tmp_path):
        plik = tmp_path / "orders.csv"              # tmp_path to Path do pustego katalogu
        plik.write_text("a,b\\n1,2\\n", encoding="utf-8")
        assert read_csv_rows(plik) == [{"a": "1", "b": "2"}]

pytest widzi nazwe `tmp_path`, tworzy SWIEZY pusty katalog dla KAZDEGO testu
i sam po nim sprzata. To sie nazywa FIXTURE. Nic nie importujesz.

Dwa skroty Path uzywane nizej:
    plik.write_text(tekst, encoding="utf-8")   # zapisz tekst   (skrot na with open)
    plik.read_text(encoding="utf-8")           # wczytaj tekst  (skrot na with open)
--------------------------------------------------------------------------------
"""

from pathlib import Path

from src.powtorka_05_pliki_csv.exercises import (
    copy_csv,
    csv_summary,
    ensure_dir,
    filter_csv_by_status,
    get_headers,
    read_csv_rows,
    read_text_lines,
    write_csv_rows,
)

CSV_TRESC = (
    "order_id,customer_name,total_amount,status\n"
    "1001,Anna,149.99,paid\n"
    "1002,Piotr,89.50,pending\n"
)

WIERSZ_1 = {
    "order_id": "1001",
    "customer_name": "Anna",
    "total_amount": "149.99",
    "status": "paid",
}
WIERSZ_2 = {
    "order_id": "1002",
    "customer_name": "Piotr",
    "total_amount": "89.50",
    "status": "pending",
}


def zrob_csv(tmp_path, nazwa="orders.csv", tresc=CSV_TRESC):
    """Pomocnik: tworzy plik CSV w katalogu tymczasowym i zwraca sciezke do niego."""
    plik = tmp_path / nazwa
    plik.write_text(tresc, encoding="utf-8")
    return plik


class TestReadTextLines:
    def test_czyta_linie(self, tmp_path):
        plik = tmp_path / "ludzie.txt"
        plik.write_text("Anna\nPiotr\nOla\n", encoding="utf-8")
        assert read_text_lines(plik) == ["Anna", "Piotr", "Ola"]

    def test_obcina_znak_konca_linii(self, tmp_path):
        plik = tmp_path / "jedna.txt"
        plik.write_text("Anna\n", encoding="utf-8")
        assert read_text_lines(plik) == ["Anna"]      # NIE ["Anna\n"]

    def test_nie_obcina_spacji_w_srodku_linii(self, tmp_path):
        plik = tmp_path / "spacje.txt"
        plik.write_text("  Anna  \n", encoding="utf-8")
        # .rstrip("\n") zdejmuje TYLKO znak konca linii - spacje zostaja.
        # Gdybys uzyl .strip(), ten test bylby czerwony.
        assert read_text_lines(plik) == ["  Anna  "]

    def test_zachowuje_puste_linie_w_srodku(self, tmp_path):
        plik = tmp_path / "przerwa.txt"
        plik.write_text("Anna\n\nPiotr\n", encoding="utf-8")
        assert read_text_lines(plik) == ["Anna", "", "Piotr"]

    def test_polskie_znaki(self, tmp_path):
        plik = tmp_path / "pl.txt"
        plik.write_text("Łódź\nŻółw\n", encoding="utf-8")
        # to przechodzi tylko z encoding="utf-8" przy odczycie
        assert read_text_lines(plik) == ["Łódź", "Żółw"]

    def test_pusty_plik(self, tmp_path):
        plik = tmp_path / "pusty.txt"
        plik.write_text("", encoding="utf-8")
        assert read_text_lines(plik) == []

    def test_brak_pliku_daje_pusta_liste(self, tmp_path):
        assert read_text_lines(tmp_path / "nie_ma_takiego.txt") == []

    def test_sciezka_jako_tekst(self, tmp_path):
        plik = tmp_path / "tekstowa.txt"
        plik.write_text("Anna\n", encoding="utf-8")
        assert read_text_lines(str(plik)) == ["Anna"]      # str, nie Path


class TestReadCsvRows:
    def test_czyta_wiersze_jako_slowniki(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert read_csv_rows(plik) == [WIERSZ_1, WIERSZ_2]

    def test_wartosci_sa_tekstami(self, tmp_path):
        plik = zrob_csv(tmp_path)
        rows = read_csv_rows(plik)
        assert rows[0]["total_amount"] == "149.99"        # TEKST
        assert rows[0]["total_amount"] != 149.99          # NIE liczba
        assert isinstance(rows[0]["total_amount"], str)

    def test_naglowek_nie_jest_wierszem(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert len(read_csv_rows(plik)) == 2              # 3 linie w pliku, 2 wiersze danych

    def test_sam_naglowek_daje_pusta_liste(self, tmp_path):
        plik = zrob_csv(tmp_path, tresc="order_id,customer_name\n")
        assert read_csv_rows(plik) == []

    def test_puste_pole_zostaje_pustym_tekstem(self, tmp_path):
        plik = zrob_csv(tmp_path, tresc="order_id,total_amount\n1001,\n")
        assert read_csv_rows(plik) == [{"order_id": "1001", "total_amount": ""}]

    def test_przecinek_w_cudzyslowie(self, tmp_path):
        # csv.DictReader rozumie cudzyslowy - .split(",") by tego nie ogarnal
        plik = zrob_csv(tmp_path, tresc='order_id,customer_name\n1001,"Kowalska, Anna"\n')
        assert read_csv_rows(plik) == [{"order_id": "1001", "customer_name": "Kowalska, Anna"}]

    def test_brak_pliku_daje_pusta_liste(self, tmp_path):
        assert read_csv_rows(tmp_path / "nie_ma_takiego.csv") == []

    def test_sciezka_jako_tekst(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert read_csv_rows(str(plik)) == [WIERSZ_1, WIERSZ_2]


class TestGetHeaders:
    def test_zwraca_nazwy_kolumn(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert get_headers(plik) == ["order_id", "customer_name", "total_amount", "status"]

    def test_zachowuje_kolejnosc_z_pliku(self, tmp_path):
        plik = zrob_csv(tmp_path, tresc="status,order_id,customer_name\npaid,1001,Anna\n")
        assert get_headers(plik) == ["status", "order_id", "customer_name"]

    def test_sam_naglowek_bez_danych(self, tmp_path):
        # kluczowy przypadek: danych nie ma, ale KOLUMNY SA
        plik = zrob_csv(tmp_path, tresc="order_id,customer_name\n")
        assert get_headers(plik) == ["order_id", "customer_name"]

    def test_pusty_plik_daje_pusta_liste(self, tmp_path):
        # tu .fieldnames to None - stad `or []`
        plik = zrob_csv(tmp_path, tresc="")
        assert get_headers(plik) == []

    def test_brak_pliku_daje_pusta_liste(self, tmp_path):
        assert get_headers(tmp_path / "nie_ma_takiego.csv") == []


class TestEnsureDir:
    def test_tworzy_katalog(self, tmp_path):
        cel = tmp_path / "output"
        assert cel.exists() is False
        ensure_dir(cel)
        assert cel.exists() is True
        assert cel.is_dir() is True

    def test_tworzy_zagniezdzone_katalogi(self, tmp_path):
        cel = tmp_path / "output" / "2026" / "sierpien"
        ensure_dir(cel)
        assert cel.exists() is True              # to jest zasluga parents=True

    def test_istniejacy_katalog_nie_wybucha(self, tmp_path):
        cel = tmp_path / "output"
        ensure_dir(cel)
        ensure_dir(cel)                          # drugi raz - to jest zasluga exist_ok=True
        ensure_dir(cel)                          # i trzeci. IDEMPOTENCJA.
        assert cel.exists() is True

    def test_zwraca_sciezke(self, tmp_path):
        cel = tmp_path / "output"
        wynik = ensure_dir(cel)
        assert wynik == cel

    def test_zwraca_obiekt_path_nawet_dla_tekstu(self, tmp_path):
        wynik = ensure_dir(str(tmp_path / "output"))
        assert isinstance(wynik, Path)           # dostal str, ma zwrocic Path


class TestWriteCsvRows:
    def test_zwraca_liczbe_wierszy(self, tmp_path):
        assert write_csv_rows(tmp_path / "out.csv", [WIERSZ_1, WIERSZ_2]) == 2

    def test_tworzy_plik(self, tmp_path):
        cel = tmp_path / "out.csv"
        write_csv_rows(cel, [WIERSZ_1])
        assert cel.exists() is True

    def test_tresc_pliku_z_naglowkiem(self, tmp_path):
        cel = tmp_path / "out.csv"
        write_csv_rows(cel, [{"order_id": "1001", "customer_name": "Anna"}])
        assert cel.read_text(encoding="utf-8").splitlines() == [
            "order_id,customer_name",            # naglowek - zasluga writeheader()
            "1001,Anna",
        ]

    def test_bez_pustych_linii_miedzy_wierszami(self, tmp_path):
        # ten test lapie brak newline="" przy otwieraniu pliku do zapisu
        cel = tmp_path / "out.csv"
        write_csv_rows(cel, [{"a": "1"}, {"a": "2"}, {"a": "3"}])
        assert cel.read_text(encoding="utf-8").splitlines() == ["a", "1", "2", "3"]

    def test_kolejnosc_kolumn_z_pierwszego_wiersza(self, tmp_path):
        cel = tmp_path / "out.csv"
        write_csv_rows(cel, [{"status": "paid", "order_id": "1001"}])
        assert cel.read_text(encoding="utf-8").splitlines()[0] == "status,order_id"

    def test_tworzy_brakujacy_katalog(self, tmp_path):
        cel = tmp_path / "output" / "2026" / "out.csv"
        assert write_csv_rows(cel, [WIERSZ_1]) == 1
        assert cel.exists() is True

    def test_pusta_lista_zwraca_zero(self, tmp_path):
        assert write_csv_rows(tmp_path / "out.csv", []) == 0

    def test_pusta_lista_nie_tworzy_pliku(self, tmp_path):
        cel = tmp_path / "out.csv"
        write_csv_rows(cel, [])
        assert cel.exists() is False

    def test_sciezka_jako_tekst(self, tmp_path):
        cel = tmp_path / "out.csv"
        assert write_csv_rows(str(cel), [WIERSZ_1]) == 1
        assert cel.exists() is True


class TestCopyCsv:
    def test_kopiuje_wiersze(self, tmp_path):
        zrodlo = zrob_csv(tmp_path)
        cel = tmp_path / "kopia.csv"
        assert copy_csv(zrodlo, cel) == 2
        assert read_csv_rows(cel) == [WIERSZ_1, WIERSZ_2]

    def test_kopia_ma_te_sama_tresc(self, tmp_path):
        zrodlo = zrob_csv(tmp_path)
        cel = tmp_path / "kopia.csv"
        copy_csv(zrodlo, cel)
        assert cel.read_text(encoding="utf-8") == zrodlo.read_text(encoding="utf-8")

    def test_tworzy_brakujacy_katalog(self, tmp_path):
        zrodlo = zrob_csv(tmp_path)
        cel = tmp_path / "output" / "kopia.csv"
        assert copy_csv(zrodlo, cel) == 2
        assert cel.exists() is True

    def test_brak_zrodla_zwraca_zero(self, tmp_path):
        assert copy_csv(tmp_path / "nie_ma.csv", tmp_path / "kopia.csv") == 0

    def test_brak_zrodla_nie_tworzy_celu(self, tmp_path):
        cel = tmp_path / "kopia.csv"
        copy_csv(tmp_path / "nie_ma.csv", cel)
        assert cel.exists() is False

    def test_zrodlo_bez_danych_nie_tworzy_celu(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc="order_id,customer_name\n")
        cel = tmp_path / "kopia.csv"
        assert copy_csv(zrodlo, cel) == 0
        assert cel.exists() is False


class TestFilterCsvByStatus:
    TRESC = (
        "order_id,customer_name,status\n"
        "1001,Anna,paid\n"
        "1002,Piotr,pending\n"
        "1003,Ola,PAID\n"
        "1004,Marek, paid \n"
        "1005,Kasia,cancelled\n"
    )

    def test_zwraca_liczbe_pasujacych(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        assert filter_csv_by_status(zrodlo, tmp_path / "paid.csv", "paid") == 3

    def test_normalizuje_status_z_pliku(self, tmp_path):
        # "PAID" i " paid " maja wpasc do tego samego koszyka co "paid"
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        cel = tmp_path / "paid.csv"
        filter_csv_by_status(zrodlo, cel, "paid")
        assert [row["order_id"] for row in read_csv_rows(cel)] == ["1001", "1003", "1004"]

    def test_normalizuje_takze_argument(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        assert filter_csv_by_status(zrodlo, tmp_path / "paid.csv", "  PAID  ") == 3

    def test_zapisuje_wiersze_w_oryginalnej_postaci(self, tmp_path):
        # normalizacja sluzy TYLKO do porownania - danych nie czyscimy
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        cel = tmp_path / "paid.csv"
        filter_csv_by_status(zrodlo, cel, "paid")
        statusy = [row["status"] for row in read_csv_rows(cel)]
        assert statusy == ["paid", "PAID", " paid "]

    def test_zachowuje_wszystkie_kolumny(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        cel = tmp_path / "paid.csv"
        filter_csv_by_status(zrodlo, cel, "paid")
        assert get_headers(cel) == ["order_id", "customer_name", "status"]

    def test_tworzy_brakujacy_katalog(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        cel = tmp_path / "output" / "paid.csv"
        filter_csv_by_status(zrodlo, cel, "paid")
        assert cel.exists() is True

    def test_pomija_wiersz_bez_klucza_status(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc="order_id\n1001\n")
        assert filter_csv_by_status(zrodlo, tmp_path / "paid.csv", "paid") == 0

    def test_brak_dopasowan_zwraca_zero(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        assert filter_csv_by_status(zrodlo, tmp_path / "x.csv", "refunded") == 0

    def test_brak_dopasowan_nie_tworzy_pliku(self, tmp_path):
        zrodlo = zrob_csv(tmp_path, tresc=self.TRESC)
        cel = tmp_path / "x.csv"
        filter_csv_by_status(zrodlo, cel, "refunded")
        assert cel.exists() is False

    def test_brak_zrodla_zwraca_zero(self, tmp_path):
        assert filter_csv_by_status(tmp_path / "nie_ma.csv", tmp_path / "x.csv", "paid") == 0


class TestCsvSummary:
    def test_raport_dla_normalnego_pliku(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert csv_summary(plik) == {
            "exists": True,
            "rows": 2,
            "columns": ["order_id", "customer_name", "total_amount", "status"],
        }

    def test_plik_z_samym_naglowkiem(self, tmp_path):
        # zero wierszy, ale kolumny SA - dlatego "rows" i "columns" licza sie osobno
        plik = zrob_csv(tmp_path, tresc="order_id,customer_name\n")
        assert csv_summary(plik) == {
            "exists": True,
            "rows": 0,
            "columns": ["order_id", "customer_name"],
        }

    def test_pusty_plik(self, tmp_path):
        plik = zrob_csv(tmp_path, tresc="")
        assert csv_summary(plik) == {"exists": True, "rows": 0, "columns": []}

    def test_brak_pliku(self, tmp_path):
        assert csv_summary(tmp_path / "nie_ma.csv") == {
            "exists": False,
            "rows": 0,
            "columns": [],
        }

    def test_ma_dokladnie_trzy_klucze(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert sorted(csv_summary(plik).keys()) == ["columns", "exists", "rows"]

    def test_sciezka_jako_tekst(self, tmp_path):
        plik = zrob_csv(tmp_path)
        assert csv_summary(str(plik))["exists"] is True
