"""Powtorka R3 - listy i petle. Zakres: for, .append(), filtrowanie, walidacja.

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-03-listy-i-petle.md
    2. Uruchom demo:  uv run python -m src.powtorka_03_listy_petle.demo

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_03.py::TestKeepPositive -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.
DRY: gdy piszesz drugi raz te sama logike, uzyj funkcji, ktora juz masz wyzej.
"""


# ---------------------------------------------------------------------------
# GOTOWE - z R2. NIE zmieniaj tej funkcji. Masz jej UZYWAC w zadaniach nizej.
# ---------------------------------------------------------------------------
def to_float(value) -> float | None:
    """Zamien wartosc na float. Gdy sie nie da - zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def keep_positive(numbers: list) -> list:
    """Zostaw z listy tylko liczby DODATNIE (wieksze od zera). Zbuduj nowa liste.

    Dostajesz:
        numbers - lista liczb (int/float), np. [5, -3, 0, 10]

    Zwracasz:
        NOWA lista z samymi liczbami > 0. Kolejnosc jak w wejsciu.

    Przyklady:
        keep_positive([5, -3, 0, 10, -1]) -> [5, 10]
        keep_positive([1, 2, 3])          -> [1, 2, 3]
        keep_positive([-5, 0])            -> []
        keep_positive([])                 -> []

    Uwagi:
        - Wzorzec z notes, rozdzial 2-3: pusta lista -> petla z if i .append() -> return.
        - 0 NIE jest dodatnie (0 > 0 to falsz), wiec odpada.
        - Nie zmieniasz wejsciowej listy - budujesz NOWA.

    Testuj:  uv run pytest tests/test_powtorka_03.py::TestKeepPositive -v
    """

    positive = []

    for number in numbers:
        if number > 0:
            positive.append(number)

    return positive


def to_float_list(values: list) -> list[float]:
    """Zamien kazdy element na float, a te, ktorych sie nie da - POMIN.

    Dostajesz:
        values - lista MIESZANA: teksty z liczba ("12.5"), liczby (30),
                 smieci ("abc"), None, pusty tekst ("").

    Zwracasz:
        NOWA lista floatow - tylko z tych elementow, ktore udalo sie skonwertowac.
        Kolejnosc jak w wejsciu.

    Przyklady:
        to_float_list(["12.5", "abc", 30, None, ""]) -> [12.5, 30.0]
        to_float_list(["1", "2", "3"])               -> [1.0, 2.0, 3.0]
        to_float_list([0, "0"])                       -> [0.0, 0.0]
        to_float_list(["abc", None])                  -> []
        to_float_list([])                             -> []

    Uwagi:
        - Wzorzec z notes, rozdzial 4. UZYJ gotowego to_float z gory pliku -
          nie pisz try/except drugi raz (DRY).
        - to_float zwraca None, gdy sie nie da. Pomijasz element, gdy wynik JEST None.
        - Sprawdzasz `is not None`, NIE `if liczba` - bo 0.0 ma zostac (patrz przyklad
          [0, "0"] -> [0.0, 0.0]).

    Testuj:  uv run pytest tests/test_powtorka_03.py::TestToFloatList -v
    """
    valid_values = []

    for value in values:
        if to_float(value) is not None:
            valid_values.append(float(value))
    return valid_values


def filter_valid_amounts(amounts: list) -> list[float]:
    """Odsiej z listy smieci i zostaw tylko sensowne kwoty (float, > 0). Payoff R3.

    To jest zadanie diagnostyczne. Laczy konwersje (R2) z filtrowaniem (R3).

    Dostajesz:
        amounts - lista MIESZANA: teksty z liczba ("12.50"), liczby (30), smieci
                  ("abc"), None, pusty tekst (""), liczby ujemne (-5), zero (0).

    Zwracasz:
        NOWA lista poprawnych kwot, KAZDA JAKO float. Kolejnosc jak w wejsciu.

    Kwota jest poprawna, gdy JEDNOCZESNIE:
        1. da sie ja zamienic na float, ORAZ
        2. jest wieksza od zera (0 i liczby ujemne ODRZUCASZ).

    Przyklady:
        filter_valid_amounts(["12.50", 30, "abc", None, "", -5, 0, 7.25])
            -> [12.5, 30.0, 7.25]
        filter_valid_amounts([])            -> []
        filter_valid_amounts(["abc", None]) -> []
        filter_valid_amounts([-5, 0, "-3"]) -> []

    Uwagi:
        - Wzorzec z notes, rozdzial 5: dwa warunki naraz przez `and`.
        - UZYJ to_float z gory (DRY). Warunek: `if liczba is not None and liczba > 0`.
        - Kolejnosc w warunku wazna: najpierw `is not None`, potem `> 0` - inaczej
          `None > 0` by wybuchlo (short-circuit z notes).
        - UWAGA: tu, w odroznieniu od safe_get_total z R2, ODRZUCASZ zero i ujemne.

    Testuj:  uv run pytest tests/test_powtorka_03.py::TestFilterValidAmounts -v
    """
    valid_list = []

    for amount in amounts:
        if to_float(amount) is not None and float(amount) > 0:
            valid_list.append(float(amount))
    return valid_list


def is_valid_order(order: dict, required_keys: list) -> bool:
    """Sprawdz, czy zamowienie ma KOMPLET wymaganych, niepustych pol. Zwroc True/False.

    Dostajesz:
        order         - slownik jednego zamowienia, np. {"order_id": "1", ...}
        required_keys - lista nazw kluczy, ktore MUSZA byc wypelnione,
                        np. ["order_id", "customer_name"]

    Zwracasz:
        True  - gdy dla KAZDEGO klucza z required_keys jednoczesnie:
                  * klucz istnieje w slowniku, ORAZ
                  * jego wartosc nie jest None, ORAZ
                  * jego wartosc po obcieciu spacji (.strip()) nie jest pusta.
        False - gdy CHOC JEDEN wymagany klucz zawiedzie.

    Wystarczy jeden zly klucz, zeby caly rekord byl niepoprawny.

    Przyklady:
        is_valid_order({"order_id": "1", "customer_name": "Anna"},
                       ["order_id", "customer_name"])                 -> True
        is_valid_order({"order_id": "2", "customer_name": ""},
                       ["order_id", "customer_name"])                 -> False  (pusta nazwa)
        is_valid_order({"order_id": "3"},
                       ["order_id", "customer_name"])                 -> False  (brak klucza)
        is_valid_order({"order_id": "4", "customer_name": "   "},
                       ["order_id", "customer_name"])                 -> False  (same spacje)
        is_valid_order({"cokolwiek": "x"}, [])                        -> True   (brak wymagan)

    Uwagi:
        - Wzorzec z notes, rozdzial 6: petla po required_keys, przy pierwszym bledzie
          `return False`; jesli petla dojdzie do konca - `return True`.
        - Kolejnosc sprawdzen wazna: najpierw `key not in order` i `value is None`,
          DOPIERO POTEM `value.strip()` - bo None.strip() by wybuchlo.
        - Pusta required_keys -> petla nic nie sprawdza -> zwracasz True.
        - Zakladasz, ze wartosci sa tekstem (jak w danych z CSV).

    Testuj:  uv run pytest tests/test_powtorka_03.py::TestIsValidOrder -v
    """
    for key in required_keys:
        if key not in order:
            return False
        value = order[key]
        if value is None:
            return False
        if value.strip() == "":
            return False
    return True
    



def split_valid_invalid(orders: list, required_keys: list) -> tuple[list, list]:
    """Podziel zamowienia na dwie kupki: poprawne i niepoprawne. Payoff R3.

    To jest zadanie diagnostyczne. Buduje na is_valid_order z zadania #4.

    Dostajesz:
        orders        - lista slownikow (zamowien)
        required_keys - lista wymaganych kluczy (jak w is_valid_order)

    Zwracasz:
        KROTKE dwoch list: (valid, invalid)
        Czyli:  return poprawne, niepoprawne
        Kolejnosc zamowien w obu listach zachowana.

    Zamowienie trafia do 'valid', gdy is_valid_order(...) daje True. W przeciwnym
    razie trafia do 'invalid'. Kazde zamowienie laduje w DOKLADNIE jednej liscie.

    Przyklady:
        orders = [
            {"order_id": "1", "customer_name": "Anna"},   # ok
            {"order_id": "2", "customer_name": ""},       # pusta nazwa -> zle
            {"order_id": "3"},                            # brak klucza -> zle
            {"order_id": "5", "customer_name": "Ewa"},    # ok
        ]
        split_valid_invalid(orders, ["order_id", "customer_name"])
            -> (
                 [{"order_id": "1", ...}, {"order_id": "5", ...}],   # valid
                 [{"order_id": "2", ...}, {"order_id": "3", ...}],   # invalid
               )

        split_valid_invalid([], ["order_id"])   -> ([], [])
        split_valid_invalid([{"a": 1}, {}], [])  -> ([{"a": 1}, {}], [])

    Uwagi:
        - Wzorzec z notes, rozdzial 7: DWIE puste listy, petla, dokladasz do wlasciwej,
          `return valid, invalid`.
        - UZYJ is_valid_order z zadania #4 (DRY). NIE przepisuj logiki walidacji tutaj.

    Testuj:  uv run pytest tests/test_powtorka_03.py::TestSplitValidInvalid -v
    """

    valid = []
    invalid = []

    for order in orders:
        if is_valid_order(order, required_keys):
            valid.append(order)
        else:
            invalid.append(order)
    return valid, invalid
