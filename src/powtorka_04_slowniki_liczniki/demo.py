"""DEMO R4 - slowniki jako liczniki i agregatory. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje sa juz napisane. Pokazuja cztery techniki:
    1. slownik jako licznik   -> .get(k, 0) + 1
    2. normalizacja           -> .strip().lower() zanim policzysz
    3. slownik jako agregator -> dokladasz kwote do wartosci (suma per klucz)
    4. .items()               -> chodzenie po parach (klucz, wartosc)

Uruchom:
    uv run python -m src.powtorka_04_slowniki_liczniki.demo
"""


def to_float(value):
    """Z R2: zamien na float albo zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def demo_count(items: list) -> dict:
    """Slownik jako licznik: pusty slownik -> .get(k, 0) + 1 w petli."""
    liczniki = {}
    for item in items:
        liczniki[item] = liczniki.get(item, 0) + 1
    return liczniki


def demo_count_normalized(statuses: list) -> dict:
    """Licznik + normalizacja: ' PAID ', 'Paid', 'paid' trafiaja do JEDNEGO koszyka."""
    liczniki = {}
    for status in statuses:
        status = status.strip().lower()    # normalizacja PRZED liczeniem
        liczniki[status] = liczniki.get(status, 0) + 1
    return liczniki


def demo_sum(orders: list) -> dict:
    """Slownik jako agregator: dokladasz kwote do sumy klienta (zamiast + 1)."""
    sumy = {}
    for order in orders:
        name = order.get("customer_name", "").strip()
        if name == "":
            continue
        kwota = to_float(order.get("total_amount"))
        if kwota is None:
            kwota = 0.0
        sumy[name] = sumy.get(name, 0) + kwota
    return sumy


if __name__ == "__main__":
    print("=== 1. SLOWNIK JAKO LICZNIK (.get(k, 0) + 1) ===")
    print(f"  demo_count(['a', 'b', 'a', 'a']) = {demo_count(['a', 'b', 'a', 'a'])}")
    print()

    print("=== 2. LICZNIK + NORMALIZACJA (jeden koszyk mimo roznej pisowni) ===")
    dane = ["paid", " PAID ", "Paid", "pending"]
    print(f"  wejscie: {dane!r}")
    print(f"  wynik:   {demo_count_normalized(dane)}")
    print("  (uwaga: 3x 'paid' mimo ze pisane inaczej)")
    print()

    print("=== 3. SLOWNIK JAKO AGREGATOR (suma kwot per klient) ===")
    orders = [
        {"customer_name": "Anna", "total_amount": "100"},
        {"customer_name": "Anna", "total_amount": "50"},
        {"customer_name": "Piotr", "total_amount": "120"},
        {"customer_name": "", "total_amount": "999"},      # bez nazwy -> pomijamy
        {"customer_name": "Ola", "total_amount": "abc"},   # smiec -> 0.0
    ]
    sumy = demo_sum(orders)
    print(f"  demo_sum(...) = {sumy}")
    print()

    print("=== 4. .items() - CHODZENIE PO PARACH (klucz, wartosc) ===")
    for name, total in sumy.items():
        print(f"  {name:<8} wydal {total}")
    print()

    print("Przeczytaj kod tego pliku, potem otworz exercises.py.")
