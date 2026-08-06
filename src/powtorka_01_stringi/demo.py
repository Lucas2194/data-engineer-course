"""DEMO R1 - stringi i formatowanie. Czytasz i uruchamiasz, NIE rozwiazujesz.

Wszystkie funkcje tutaj sa juz napisane. Sluza do pokazania trzech technik:
    1. f-string          -> sklejanie tekstu z wartosciami
    2. format spec :.2f  -> dwa miejsca po przecinku
    3. metody stringow   -> .strip(), .lower(), .upper()

Uruchom:
    uv run python -m src.powtorka_01_stringi.demo
"""


def demo_fstring(imie: str, wiek: int) -> str:
    """f-string sklaja tekst z wartosciami wprost w { }."""
    # W { } moze byc zmienna, ale tez wyrazenie, np. {wiek + 1}.
    return f"{imie} ma {wiek} lat, za rok bedzie mial {wiek + 1}."


def demo_format_spec(cena: float) -> str:
    """:.2f wymusza dokladnie dwa miejsca po przecinku (dokleja zera)."""
    # 149.5 -> "149.50", 89.0 -> "89.00". Bez :.2f dostalbys "149.5".
    return f"{cena:.2f} PLN"


def demo_metody(status: str) -> str:
    """Metody stringow ZWRACAJA nowy tekst - trzeba wynik przypisac/uzyc."""
    # Laczymy metody: obetnij spacje, potem zamien na male litery.
    return status.strip().lower()


if __name__ == "__main__":
    # Ten blok wykona sie tylko, gdy uruchomisz plik wprost (nie przy imporcie).
    print("=== 1. F-STRING ===")
    print(demo_fstring("Anna", 30))
    print()

    print("=== 2. FORMAT SPEC :.2f ===")
    for cena in (149.5, 89.0, 3.14159, 0):
        print(f"  {cena!r:>10}  ->  {demo_format_spec(cena)}")
    print()

    print("=== 3. METODY STRINGOW ===")
    for status in ("  PAID  ", "Paid", "pending", "   "):
        wynik = demo_metody(status)
        print(f"  {status!r:>10}  ->  {wynik!r}")
    print()

    print("Przeczytaj kod tego pliku, potem otworz exercises.py.")
