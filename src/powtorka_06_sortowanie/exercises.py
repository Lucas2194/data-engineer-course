"""Powtorka R6 - CZESC A: sortowanie.

UWAGA: to NIE jest powtorka. sorted(), key=, lambda, reverse= i wycinek [:n]
       NIE wystepuja nigdzie w dniach 1-20 - sprawdzone greppem. Widzisz je
       pierwszy raz. Wolniejsze tempo jest tu normalne, nie jest regresem.

Zakres: sorted(), reverse=, key=, lambda, .items(), krotki, wycinek [:n].

ZANIM ZACZNIESZ:
    1. Przeczytaj notes/powtorka-06-sortowanie.md (rozdzialy 2-10)
    2. Uruchom demo:  uv run python -m src.powtorka_06_sortowanie.demo
    3. Przeczytaj kod dema - jest tam wszystko, czego potrzebujesz

Nie zmieniaj nazw funkcji ani parametrow - testy na nich polegaja.
Rozwiazan nigdzie nie ma. Testy sa jedyna informacja zwrotna.

Pracuj JEDNA klasa naraz:
    uv run pytest tests/test_powtorka_06.py::TestSortNames -v

Gdy docstring i test sie roznia - WIERZYSZ TESTOWI.

ZASADY TEGO BLOKU:
    - RUFF PRZED PYTESTEM. Zawsze:
        uv run ruff check src/powtorka_06_sortowanie/exercises.py
      W R5 zlapalby Ci 2 bledy z 5, zanim zobaczyles traceback. Darmowa runda.
    - DRY: #5 uzywa #3 i #4. Jesli przepisujesz tam sortowanie - robisz to zle.
    - Uzywasz `sorted()`, NIE `.sort()`. Wejscia nie wolno zmieniac.
    - Nazwy zmiennych PO ANGIELSKU.
    - Po zaliczeniu calej czesci A siadasz do PROJEKT.md (czesc B).
"""


# ---------------------------------------------------------------------------
# GOTOWE - z R2 i R4. NIE zmieniaj tych funkcji. Masz ich UZYWAC.
# ---------------------------------------------------------------------------
def to_float(value) -> float | None:
    """Zamien wartosc na float. Gdy sie nie da - zwroc None (zamiast wybuchac)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def normalize_status(value) -> str | None:
    """Obetnij spacje i zrob male litery. Nie-tekst / pusty tekst -> None."""
    if not isinstance(value, str):
        return None
    cleaned = value.strip().lower()
    return cleaned or None


def sort_names(names: list[str], descending: bool = False) -> list[str]:
    """Posortuj liste imion alfabetycznie. Rozgrzewka - goly sorted().

    Dostajesz:
        names      - lista tekstow.
        descending - gdy True, sortujesz OD KONCA alfabetu. Domyslnie False.
                     (to jest argument z wartoscia domyslna - wolajacy moze go pominac)

    Zwracasz:
        NOWA posortowana liste. Lista `names` ma zostac NIETKNIETA.
        Pusta lista -> pusta lista.

    Przyklady:
        sort_names(["Piotr", "Anna", "Marek"])                    -> ["Anna", "Marek", "Piotr"]
        sort_names(["Piotr", "Anna", "Marek"], descending=True)   -> ["Piotr", "Marek", "Anna"]
        sort_names([])                                            -> []

    Uwagi:
        - Notatka, rozdzial 2 i 4.
        - `sorted(x)` zwraca NOWA liste. `x.sort()` zmienia oryginal i zwraca None.
          Tutaj MUSISZ uzyc sorted() - jeden z testow sprawdza, czy wejscie zostalo
          nietkniete.
        - Kierunek ustawia argument `reverse=`. Zauwaz, ze Twoj parametr nazywa sie
          `descending`, a argument sorted() nazywa sie `reverse` - to nie ta sama nazwa,
          ale ta sama wartosc.
        - To jest zadanie na jedna linie. Jesli piszesz `if`, to prawie na pewno
          da sie krocej.

    Testuj:  uv run pytest tests/test_powtorka_06.py::TestSortNames -v
    """
    new_names = sorted(names, reverse=descending)
    return new_names


def sort_by_length(words: list[str]) -> list[str]:
    """Posortuj slowa od najkrotszego do najdluzszego. Pierwsze spotkanie z key=.

    Dostajesz:
        words - lista tekstow.

    Zwracasz:
        NOWA liste tych samych slow, uporzadkowana po DLUGOSCI rosnaco.
        Slowa tej samej dlugosci zachowuja kolejnosc z wejscia (patrz Uwagi).
        Pusta lista -> pusta lista.

    Przyklady:
        sort_by_length(["kot", "a", "abcd", "xy"])  -> ["a", "xy", "kot", "abcd"]
        sort_by_length(["bb", "aa", "c"])           -> ["c", "bb", "aa"]
                                                       ^^^^^^^^^^^^^^^^
                                          "bb" przed "aa", bo tak bylo w wejsciu
                                          (sortowanie jest STABILNE - rozdzial 11)

    Uwagi:
        - Notatka, rozdzial 5.
        - `key=` przyjmuje FUNKCJE, ktora z jednego elementu wyciaga wartosc
          do porownania. Dlugosc tekstu daje wbudowana funkcja `len`.
        - Przekazujesz `len` BEZ NAWIASOW. `key=len` to przepis do wykonania pozniej,
          `key=len()` to proba wywolania jej teraz -> TypeError.
          (To ta sama roznica co `writeheader` vs `writeheader()` z R5, tylko odwrotnie.)
        - Tu NIE potrzebujesz lambda. Bedzie w nastepnym zadaniu.
        - Zadanie na jedna linie.

    Testuj:  uv run pytest tests/test_powtorka_06.py::TestSortByLength -v
    """
    return sorted(words, key=len)


def sort_orders_by_amount(orders: list[dict]) -> list[dict]:
    """Posortuj zamowienia po kwocie, od najwyzszej. Pierwsza lambda.

    Dostajesz:
        orders - lista slownikow (wiersze z CSV). Kazdy MA klucz "total_amount",
                 ale jego wartosc to TEKST i moze byc smieciem ("abc", "", None).

    Zwracasz:
        NOWA liste tych samych slownikow, uporzadkowana po kwocie MALEJACO.
        Slownikow NIE zmieniasz - przestawiasz tylko ich kolejnosc.
        Wiersz, ktorego kwoty nie da sie zamienic na liczbe, traktujesz jak 0.0
        (ma wyladowac na koncu, nie wywalic programu).
        Pusta lista -> pusta lista.

    Przyklady:
        orders = [
            {"order_id": "1", "total_amount": "90.00"},
            {"order_id": "2", "total_amount": "1000.00"},
            {"order_id": "3", "total_amount": "abc"},
        ]
        sort_orders_by_amount(orders) -> [
            {"order_id": "2", "total_amount": "1000.00"},
            {"order_id": "1", "total_amount": "90.00"},
            {"order_id": "3", "total_amount": "abc"},
        ]

    Uwagi:
        - Notatka, rozdzialy 5 i 6.
        - Slownikow NIE da sie porownac wprost - `sorted(orders)` to TypeError.
          Musisz powiedziec, PO CZYM porownujesz, czyli podac key=.
        - PULAPKA, ktora kosztuje ludzi cale raporty: w CSV kwota jest TEKSTEM.
          Bez konwersji posortujesz alfabetycznie i "1000.00" wyladuje PRZED "90.00"
          (bo znak "1" jest przed "9"). Nic nie wybuchnie. Raport po prostu sklamie.
          Konwersje robisz WEWNATRZ key=.
        - Uzyj gotowego `to_float` z gory pliku. Zwraca None dla smiecia, a None
          nie da sie porownac z liczba - potrzebujesz wartosci zastepczej.
          Przypomnij sobie z R2, co robi `or` z wartoscia falszywa.
          UWAGA: `to_float("0") or 0.0` tez da 0.0 - i o to chodzi, bo 0.0 == 0.0.
        - Zadanie na jedna linie (dluga).

    Testuj:  uv run pytest tests/test_powtorka_06.py::TestSortOrdersByAmount -v
    """
    return sorted(orders, key=lambda order: to_float(order["total_amount"]) or 0.0, reverse=True)


def sorted_totals(totals: dict) -> list[tuple]:
    """Zamien slownik {klient: suma} na RANKING. To jest serce tego bloku.

    Dostajesz:
        totals - slownik {nazwa_klienta: suma_jego_zamowien}, np.
                 {"Anna": 250.0, "Piotr": 120.0}

    Zwracasz:
        Liste KROTEK (nazwa, suma), uporzadkowana:
            1. po sumie MALEJACO,
            2. przy REMISIE - po nazwie ROSNACO (alfabetycznie).
        Pusty slownik -> pusta lista.

    Przyklady:
        sorted_totals({"Anna": 250.0, "Marek": 120.0})
            -> [("Anna", 250.0), ("Marek", 120.0)]

        sorted_totals({"Zofia": 250.0, "Anna": 250.0, "Piotr": 250.0})
            -> [("Anna", 250.0), ("Piotr", 250.0), ("Zofia", 250.0)]
               (wszyscy maja tyle samo, wiec decyduje alfabet)

        sorted_totals({}) -> []

    Uwagi:
        - Notatka, rozdzialy 7, 8 i 9. Przeczytaj rozdzial 9 DWA RAZY.
        - Slownika nie sortujesz. Zamieniasz go na liste par przez `.items()`
          i sortujesz liste.
        - DWA KRYTERIA W PRZECIWNYCH KIERUNKACH: kwota malejaco, nazwa rosnaco.
          `reverse=True` tu NIE ZADZIALA - odwrocilby tez alfabet (Zofia przed Anna).
          Demo pokazuje ten bledny wynik obok poprawnego - uruchom je.
        - Trik: `key=` moze zwrocic KROTKE. Krotki porownuja sie po kolei od lewej:
          najpierw pierwsze elementy, a dopiero przy remisie drugie.
          Liczbe odwracasz MINUSEM. Tekstu minusem odwrocic sie nie da.
        - Jesli `pair` to jedna para, to `pair[0]` jest nazwa, a `pair[1]` suma.
        - Zadanie na jedna linie.

    Testuj:  uv run pytest tests/test_powtorka_06.py::TestSortedTotals -v
    """
    return sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))


def top_customers(orders: list[dict], n: int) -> list[tuple]:
    """Znajdz n klientow, ktorzy wydali najwiecej. PAYOFF - zadanie diagnostyczne #7.

    To jest dokladnie zadanie #7 z diagnostyki Dnia 21. Napiszesz je tutaj raz
    porzadnie i tam bedzie za darmo.

    Dostajesz:
        orders - lista slownikow z kluczami "customer_name", "total_amount", "status"
                 (klucze moga sie NIE POJAWIC w danym wierszu - uzywaj .get())
        n      - ilu klientow zwrocic

    Zwracasz:
        Liste KROTEK (nazwa_klienta, suma), posortowana jak w sorted_totals:
        malejaco po sumie, przy remisie alfabetycznie po nazwie.
        Gdy klientow jest MNIEJ niz n - zwracasz tylu, ilu jest (bez bledu).
        Gdy n <= 0 -> pusta lista.

    Zasady liczenia:
        - Liczysz TYLKO zamowienia o statusie "paid" PO NORMALIZACJI -
          czyli " PAID " tez sie liczy. Uzyj gotowego normalize_status.
        - Kwote pobierasz BEZPIECZNIE: smiec ("abc", "", brak klucza) -> 0.0.
        - Nazwe klienta obcinasz ze spacji: " Piotr " -> "Piotr".
        - Klientow BEZ NAZWY (pusta, same spacje, brak klucza) POMIJASZ calkiem.

    Przyklad:
        orders = [
            {"customer_name": "Anna",  "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Anna",  "total_amount": "50.00",  "status": " PAID "},
            {"customer_name": "Anna",  "total_amount": "999.00", "status": "cancelled"},
            {"customer_name": "Piotr", "total_amount": "120.00", "status": "paid"},
            {"customer_name": "",      "total_amount": "500.00", "status": "paid"},
        ]
        top_customers(orders, 2)  -> [("Anna", 150.0), ("Piotr", 120.0)]

        Dlaczego: Anna ma 100 + 50 = 150 (999 odpada, bo cancelled).
                  Piotr ma 120. Klient bez nazwy odpada calkiem.

    Uwagi:
        - Notatka, rozdzial 10. Rob to w DWOCH krokach:
            KROK 1: petla po orders -> zbuduj slownik {nazwa: suma}
                    (to jest agregacja z R4: `totals[name] = totals.get(name, 0.0) + kwota`)
            KROK 2: oddaj ten slownik do sorted_totals(#4) i wez pierwsze n
        - DRY: NIE przepisuj tu sortowania. Masz je gotowe w #4.
          Jesli widze tu `sorted(...)` albo `lambda`, to znaczy, ze robisz drugi raz
          to samo. Zobacze to na review.
        - Pierwsze n bierzesz WYCINKIEM `[:n]`, nie indeksem i nie petla.
          Wycinek nie wybucha, gdy klientow jest mniej niz n - dlatego przypadek
          "mniej niz n" zalatwia sie SAM. To nagroda za uzycie wlasciwego narzedzia.
        - ALE: wycinek z liczba UJEMNA zachowuje sie inaczej, niz myslisz.
          Sprawdz sam w konsoli (`uv run python`), co zwroci `["a", "b", "c"][:-1]`,
          i wyciagnij z tego wniosek dla przypadku n <= 0.
        - Przy budowaniu slownika pilnuj kolejnosci: najpierw ODRZUC wiersz
          (zly status / brak nazwy), potem dodawaj. Nie odwrotnie.

    Testuj:  uv run pytest tests/test_powtorka_06.py::TestTopCustomers -v
    """
    if n <= 0:
        return []

    totals = {}

    for order in orders:
        status = normalize_status(order.get("status"))

        if status != "paid":
            continue

        name = (order.get("customer_name") or "").strip()

        if not name:
            continue

        amount = to_float(order.get("total_amount")) or 0.0

        totals[name] = totals.get(name, 0.0) + amount

    return sorted_totals(totals)[:n]
