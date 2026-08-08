"""DEMO R2 - bezpieczny dostep i konwersje. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje sa juz napisane. Pokazuja trzy techniki:
    1. dict.get()   -> siegniecie po klucz, ktory moze nie istniec
    2. float()      -> konwersja tekstu na liczbe (i kiedy wybucha)
    3. try/except   -> zlapanie wybuchu, zeby program szedl dalej

Uruchom:
    uv run python -m src.powtorka_02_bezpieczny_dostep.demo
"""


def demo_get(order: dict) -> str:
    """dict.get(klucz, domyslne) - zwraca domyslne, gdy klucza nie ma. BEZ bledu."""
    # order["status"] wybuchloby przy braku klucza. .get() nie.
    return order.get("status", "unknown")


def demo_try_except(value) -> float:
    """try/except - probujemy konwersji, a gdy wybuchnie, dajemy plan B (0.0)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        # value bylo "abc" (ValueError) albo None (TypeError) - nie padamy, dajemy 0.0
        return 0.0


if __name__ == "__main__":
    print("=== 1. dict.get() Z DOMYSLNA WARTOSCIA ===")
    for order in ({"status": "paid"}, {"status": "pending"}, {}):
        print(f"  {order!r:<24} -> get('status', 'unknown') = {demo_get(order)!r}")
    print()

    print("=== 2. float() - CO DZIALA, CO WYBUCHA ===")
    for value in ("149.99", "89", 89, "abc", "", None):
        try:
            wynik = repr(float(value))
        except (ValueError, TypeError) as blad:
            wynik = f"WYBUCH: {type(blad).__name__}"
        print(f"  float({value!r:<8}) -> {wynik}")
    print()

    print("=== 3. try/except - LAPIEMY WYBUCH, DAJEMY 0.0 ===")
    for value in ("149.99", 89, "abc", None, ""):
        print(f"  demo_try_except({value!r:<8}) -> {demo_try_except(value)}")
    print()

    print("Przeczytaj kod tego pliku, potem otworz exercises.py.")
