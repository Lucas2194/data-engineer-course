"""DEMO R3 - listy i petle. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje sa juz napisane. Pokazuja cztery techniki:
    1. budowanie listy   -> pusta lista + petla + .append()
    2. filtrowanie       -> petla + if (przepuszczasz tylko to, co spelnia warunek)
    3. try/except w petli -> jeden zepsuty rekord nie zabija calej petli
    4. walidacja         -> wszystkie wymagane pola musza byc OK

Uruchom:
    uv run python -m src.powtorka_03_listy_petle.demo
"""


def to_float(value):
    """Z R2: zamien na float albo zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def demo_build(numbers: list) -> list:
    """Wzorzec akumulatora: pusta lista -> .append() w petli -> return."""
    wynik = []
    for liczba in numbers:
        wynik.append(liczba * 2)   # transformujesz kazdy element
    return wynik


def demo_filter(numbers: list) -> list:
    """Filtrowanie: dokladasz do wyniku TYLKO gdy element przejdzie if."""
    wynik = []
    for liczba in numbers:
        if liczba > 0:             # tylko dodatnie; 0 i ujemne odpadaja
            wynik.append(liczba)
    return wynik


def demo_convert_in_loop(values: list) -> list:
    """try/except w petli (przez to_float): pomijasz to, czego nie da sie skonwertowac."""
    wynik = []
    for value in values:
        liczba = to_float(value)   # liczba ALBO None - nigdy nie wybucha
        if liczba is not None:     # is not None, NIE 'if liczba' - bo 0.0 tez chcemy
            wynik.append(liczba)
    return wynik


def demo_validate(order: dict, required_keys: list) -> bool:
    """Walidacja: wystarczy, ze JEDNO wymagane pole zawiedzie -> caly rekord zly."""
    for key in required_keys:
        if key not in order:
            return False
        value = order[key]
        if value is None:
            return False
        if value.strip() == "":    # .strip() dopiero PO sprawdzeniu None
            return False
    return True                    # przeszly wszystkie


if __name__ == "__main__":
    print("=== 1. BUDOWANIE LISTY (pusta -> append -> return) ===")
    print(f"  demo_build([10, 20, 30]) = {demo_build([10, 20, 30])}")
    print()

    print("=== 2. FILTROWANIE (tylko to, co przejdzie if) ===")
    print(f"  demo_filter([5, -3, 0, 10, -1]) = {demo_filter([5, -3, 0, 10, -1])}")
    print("  (uwaga: 0 odpada, bo 0 > 0 to falsz)")
    print()

    print("=== 3. try/except W PETLI (przez to_float - pomijamy smieci) ===")
    dane = ["12.5", "abc", 30, None, "", 0]
    print(f"  wejscie:  {dane!r}")
    print(f"  wynik:    {demo_convert_in_loop(dane)}")
    print("  (uwaga: 0 ZOSTAJE - is not None; tylko 'abc', None, '' odpadaja)")
    print()

    print("=== 4. WALIDACJA SLOWNIKA (wszystkie pola musza byc OK) ===")
    req = ["order_id", "customer_name"]
    for order in (
        {"order_id": "1", "customer_name": "Anna"},   # ok
        {"order_id": "2", "customer_name": ""},        # pusta nazwa
        {"order_id": "3"},                             # brak klucza
        {"order_id": "4", "customer_name": "   "},     # same spacje
    ):
        print(f"  {order!r:<45} -> {demo_validate(order, req)}")
    print()

    print("Przeczytaj kod tego pliku, potem otworz exercises.py.")
