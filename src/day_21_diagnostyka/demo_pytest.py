"""DEMO - to jest przyklad, ktory czytasz i uruchamiasz. Nie rozwiazujesz go.

Ta funkcja jest juz NAPISANA. Sluzy tylko do pokazania, jak dzialaja testy.
"""


def add_vat(net_price: float) -> float:
    """Doliczy VAT 23% do ceny netto i zaokragli wynik do 2 miejsc po przecinku.

    100.00 -> 123.00
    """
    return round(net_price * 1.23, 2)
