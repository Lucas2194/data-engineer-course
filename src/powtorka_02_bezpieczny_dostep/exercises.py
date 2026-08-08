"""Powtorka R2 - bezpieczny dostep i konwersje. Zakres: dict.get(), try/except, float().

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-02-bezpieczny-dostep.md
    2. Uruchom demo:  uv run python -m src.powtorka_02_bezpieczny_dostep.demo

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_02.py::TestGetField -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.
"""


def get_field(data: dict, key: str, default):
    """Siegnij po klucz w slowniku, a gdy go nie ma - zwroc wartosc domyslna.

    Dostajesz:
        data    - slownik, np. {"status": "paid"}
        key     - nazwa klucza, ktorego szukasz, np. "status"
        default - co zwrocic, gdy klucza NIE MA

    Zwracasz:
        Wartosc spod klucza, gdy klucz istnieje.
        default, gdy klucza nie ma.

    Przyklady:
        get_field({"status": "paid"}, "status", "unknown")  -> "paid"
        get_field({}, "status", "unknown")                  -> "unknown"
        get_field({"status": "paid"}, "total", 0)           -> 0
        get_field({"total": 149.99}, "total", 0)            -> 149.99

    Uwagi:
        - To jest dokladnie to, co robi metoda dict.get(). Notes, rozdzial 2.
        - NIE uzywaj data[key] - to wybucha przy braku klucza (KeyError).

    Testuj:  uv run pytest tests/test_powtorka_02.py::TestGetField -v
    """
    return data.get(key, default)


def to_float(value) -> float | None:
    """Zamien wartosc na float. Gdy sie nie da - zwroc None (zamiast wybuchac).

    Dostajesz:
        value - cokolwiek: tekst z liczba ("149.99"), liczbe (89), tekst-smiec
                ("abc"), pusty tekst (""), None.

    Zwracasz:
        float - gdy konwersja sie udala.
        None  - gdy konwersja by wybuchla (ValueError albo TypeError).

    Funkcja NIE MOZE rzucic wyjatkiem.

    Przyklady:
        to_float("149.99")  -> 149.99
        to_float("89")      -> 89.0
        to_float(89)        -> 89.0
        to_float("abc")     -> None
        to_float("")        -> None
        to_float(None)      -> None

    Uwagi:
        - Wzorzec z notes, rozdzial 4: try wokol float(value), except lapie
          KONKRETNE typy (ValueError, TypeError).
        - Samo "except:" bez typu nie przejdzie na review.

    Testuj:  uv run pytest tests/test_powtorka_02.py::TestToFloat -v
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def is_convertible_to_float(value) -> bool:
    """Sprawdz, czy wartosc DA SIE zamienic na float. Zwroc True albo False.

    To ten sam wzorzec try/except co wyzej, ale zamiast liczby zwracasz odpowiedz
    tak/nie. Pokazuje, ze try/except to narzedzie, ktore ksztaltujesz pod potrzebe.

    Dostajesz:
        value - cokolwiek (jak w to_float).

    Zwracasz:
        True  - gdy float(value) by sie udalo.
        False - gdy by wybuchlo.

    Przyklady:
        is_convertible_to_float("12.5")  -> True
        is_convertible_to_float("7")     -> True
        is_convertible_to_float(7)       -> True
        is_convertible_to_float("abc")   -> False
        is_convertible_to_float("")      -> False
        is_convertible_to_float(None)    -> False

    Uwagi:
        - try: zrob float(value), potem return True.
          except (ValueError, TypeError): return False.

    Testuj:  uv run pytest tests/test_powtorka_02.py::TestIsConvertible -v
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False



def safe_get_total(order: dict) -> float:
    """Wyciagnij kwote zamowienia tak, zeby NIGDY sie nie wywalilo. Zlozenie R2.

    To jest dokladnie zadanie #2 z diagnostyki. Tym razem umiesz juz kazdy klocek.

    Dostajesz:
        order - slownik jednego zamowienia. Klucz "total_amount" moze:
                istniec i byc poprawny ("149.99" albo 89),
                istniec i byc pusty (""),
                istniec i byc None,
                istniec i byc smieciem ("abc"),
                albo w ogole nie istniec.

    Zwracasz:
        float - kwote, gdy da sie ja odczytac.
        0.0   - w KAZDYM innym przypadku.

    Funkcja NIE MOZE rzucic wyjatkiem. To jest cale zadanie.

    Przyklady:
        safe_get_total({"total_amount": "149.99"}) -> 149.99
        safe_get_total({"total_amount": 89})       -> 89.0
        safe_get_total({"total_amount": ""})       -> 0.0
        safe_get_total({"total_amount": None})     -> 0.0
        safe_get_total({"total_amount": "abc"})    -> 0.0
        safe_get_total({})                         -> 0.0
        safe_get_total({"total_amount": -50})      -> -50.0

    Uwagi:
        - Schemat masz w notes, rozdzial 5: najpierw .get("total_amount"),
          potem try/except wokol float().
        - UWAGA: ta funkcja NIE odrzuca liczb ujemnych. -50 to poprawna liczba,
          wiec zwracasz -50.0.
        - Mozesz uzyc to_float, ktore napisales wyzej. Nie przepisuj tej logiki.

    Testuj:  uv run pytest tests/test_powtorka_02.py::TestSafeGetTotal -v
    """
    value = order.get("total_amount")

    try:
        return float(value)
    except(ValueError, TypeError):
        return 0.0


def format_total(order: dict) -> str:
    """Zwroc kwote zamowienia jako ladny tekst albo informacje o braku (STRETCH).

    Laczy R2 (bezpieczny odczyt) z R1 (formatowanie :.2f).

    Dostajesz:
        order - slownik zamowienia (jak w safe_get_total).

    Zwracasz:
        "<kwota z dwoma miejscami> PLN" - gdy kwote da sie odczytac.
        "brak danych"                   - gdy klucza nie ma, jest pusty,
                                          None albo smiec.

    Przyklady:
        format_total({"total_amount": "149.5"}) -> "149.50 PLN"
        format_total({"total_amount": 89})      -> "89.00 PLN"
        format_total({"total_amount": "abc"})   -> "brak danych"
        format_total({"total_amount": ""})      -> "brak danych"
        format_total({})                        -> "brak danych"

    Uwagi:
        - "Da sie odczytac" znaczy: to_float(...) zwrocilo cos innego niz None.
          Rozroznienie None vs liczba: `if wynik is None:`
        - Formatowanie kwoty to :.2f (R1, format_amount).
        - Zwroc uwage: tu ROZROZNIASZ brak danych od prawdziwego zera - dlatego
          patrzysz na None, a nie na to, czy kwota == 0.

    Testuj:  uv run pytest tests/test_powtorka_02.py::TestFormatTotal -v
    """
    value = order.get("total_amount")

    try:
        return f'{float(value):.2f} PLN'
    except(ValueError, TypeError):
        return "brak danych"