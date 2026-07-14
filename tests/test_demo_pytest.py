"""DEMO - testy do przykladowej funkcji add_vat. Przeczytaj to powoli.

Test to zwykla funkcja Pythona, ktora:
  1. wywoluje Twoj kod,
  2. sprawdza slowem 'assert', czy wynik jest taki, jakiego oczekujemy.

'assert cos_tam' znaczy: "twierdze, ze to jest prawda".
Jesli jest prawda  -> test przechodzi (PASSED, zielony).
Jesli nie jest     -> test pada (FAILED, czerwony) i pytest pokazuje, co dostal.

Uruchom to tak:
    uv run pytest tests/test_demo_pytest.py -v
"""

from src.day_21_diagnostyka.demo_pytest import add_vat


def test_dolicza_vat_do_okraglej_kwoty():
    # 1. Przygotowanie danych wejsciowych
    cena_netto = 100.00

    # 2. Wywolanie funkcji, ktora testujemy
    wynik = add_vat(cena_netto)

    # 3. Sprawdzenie: czy wynik jest taki, jakiego oczekujemy?
    assert wynik == 123.00


def test_zaokragla_do_dwoch_miejsc():
    # 49.99 * 1.23 = 61.4877  -> po zaokragleniu 61.49
    assert add_vat(49.99) == 61.49


def test_zero_zostaje_zerem():
    assert add_vat(0) == 0.0


def test_ten_test_celowo_padnie():
    """Ten jeden test jest ZLY specjalnie - zebys zobaczyl, jak wyglada porazka.

    Twierdzimy (blednie), ze 100 zl netto to 150 zl brutto.
    Uruchom testy i przeczytaj UWAZNIE, co pytest wypisze pod tym testem.
    """
    assert add_vat(100.00) == 150.00
