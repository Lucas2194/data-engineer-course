"""Zadania diagnostyczne po przerwie. Zakres: dni 1-20.

ZANIM ZACZNIESZ: przeczytaj `notes/day-21-testy.md` i uruchom demo:
    uv run pytest tests/test_demo_pytest.py -v

Nie zmieniaj nazw funkcji ani ich parametrow - testy na nich polegaja.
Rozwiazania nie sa nigdzie zapisane. Masz testy - to jedyna informacja zwrotna.

Testy dla jednego zadania (tak pracuj - jedna klasa naraz):
    uv run pytest tests/test_day_21.py::TestFormatOrderSummary -v

Gdy opis i test sie roznia - WIERZYSZ TESTOWI. Test jest prawda.
"""


def format_order_summary(order_id: int, customer_name: str, total: float) -> str:
    """Zbuduj jednolinijkowe podsumowanie zamowienia.

    Dostajesz:
        order_id      - liczba, np. 1
        customer_name - tekst, moze miec zbedne spacje na brzegach, np. "  Piotr  "
        total         - liczba, np. 149.99 albo 149.5

    Zwracasz:
        Jeden STRING w dokladnie takim formacie:
        "Zamowienie #<id> | <imie i nazwisko> | <kwota> PLN"

    Przyklady:
        format_order_summary(1, "Anna Kowalska", 149.99)
            -> "Zamowienie #1 | Anna Kowalska | 149.99 PLN"

        format_order_summary(7, "Ewa", 149.5)
            -> "Zamowienie #7 | Ewa | 149.50 PLN"
               (uwaga: 149.5 ma sie wyswietlic jako 149.50 - ZAWSZE dwa miejsca)

        format_order_summary(2, "  Piotr  ", 89.0)
            -> "Zamowienie #2 | Piotr | 89.00 PLN"
               (uwaga: spacje wokol imienia znikaja)

    Uwagi:
        - Separator to spacja-pionowa kreska-spacja: " | "
        - Dwa miejsca po przecinku wymuszasz w f-stringu. Szukaj w dokumentacji
          hasla "Format Specification Mini-Language", sekcja o typie 'f'.
        - Spacje z brzegow tekstu obcina metoda .strip()

    Testuj:  uv run pytest tests/test_day_21.py::TestFormatOrderSummary -v
    """
    pass


def filter_valid_amounts(amounts: list) -> list[float]:
    """Odsiej z listy smieci i zostaw tylko sensowne kwoty.

    Dostajesz:
        amounts - lista MIESZANA. Moga w niej byc:
                  teksty z liczba ("12.50"), liczby (30), teksty-smieci ("abc"),
                  None, pusty tekst (""), liczby ujemne (-5), zero (0)

    Zwracasz:
        NOWA lista, zawierajaca tylko poprawne kwoty, KAZDA JAKO float.
        Kolejnosc taka jak w wejsciu.

    Kwota jest poprawna, gdy JEDNOCZESNIE:
        1. da sie ja zamienic na float, ORAZ
        2. jest wieksza od zera (0 i liczby ujemne odrzucamy)

    Przyklady:
        filter_valid_amounts(["12.50", 30, "abc", None, "", -5, 0, 7.25])
            -> [12.5, 30.0, 7.25]

        filter_valid_amounts([])            -> []
        filter_valid_amounts(["abc", None]) -> []

    Uwagi:
        - float("abc") rzuca ValueError. float(None) rzuca TypeError.
          Musisz to obsluzyc, zeby funkcja sie nie wywalila.
        - Elementow niepoprawnych nie zamieniasz na zero - po prostu ICH NIE MA w wyniku.

    Testuj:  uv run pytest tests/test_day_21.py::TestFilterValidAmounts -v
    """
    pass


def count_statuses(orders: list[dict]) -> dict[str, int]:
    """Policz, ile razy wystapil kazdy status zamowienia.

    Dostajesz:
        orders - lista slownikow, np. [{"status": "paid"}, {"status": " PAID "}]

    Zwracasz:
        Slownik: klucz = status (znormalizowany), wartosc = ile razy wystapil.

    Normalizacja statusu (wazne):
        - obcinasz biale znaki:      " PAID " -> "PAID"
        - zamieniasz na male litery: "PAID"   -> "paid"
        Czyli " PAID ", "Paid" i "paid" to TEN SAM status.

    Pomijasz zamowienia, ktore:
        - nie maja klucza "status"     -> {}
        - maja status pusty            -> {"status": ""}
        - maja status z samych spacji  -> {"status": "   "}

    Przyklady:
        count_statuses([
            {"status": "paid"}, {"status": " PAID "},
            {"status": "pending"}, {"status": "Paid"},
        ])
            -> {"paid": 3, "pending": 1}

        count_statuses([{"status": "paid"}, {}, {"status": ""}, {"status": "   "}])
            -> {"paid": 1}

        count_statuses([]) -> {}

    Uwagi:
        - Klasyczny wzorzec "licznik w slowniku": sprawdz, czy klucz juz jest;
          jesli tak - zwieksz o 1, jesli nie - ustaw na 1.
        - Do bezpiecznego siegania po klucz przydaje sie .get()

    Testuj:  uv run pytest tests/test_day_21.py::TestCountStatuses -v
    """
    pass


def safe_get_total(order: dict) -> float:
    """Wyciagnij kwote zamowienia tak, zeby NIGDY sie nie wywalilo.

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

    Funkcja NIE MOZE rzucic wyjatkiem. Nigdy. To jest cale zadanie.

    Przyklady:
        safe_get_total({"total_amount": "149.99"}) -> 149.99
        safe_get_total({"total_amount": 89})       -> 89.0
        safe_get_total({"total_amount": ""})       -> 0.0
        safe_get_total({"total_amount": None})     -> 0.0
        safe_get_total({"total_amount": "abc"})    -> 0.0
        safe_get_total({})                         -> 0.0

    Uwagi:
        - Dwie rzeczy moga pojsc nie tak: brak klucza ORAZ nieudana konwersja.
          Obie musisz obsluzyc.
        - W except lapiesz KONKRETNE wyjatki (ValueError, TypeError).
          Samo "except:" bez typu nie przejdzie u mnie przez code review -
          bo zjada tez bledy, o ktorych chcialbys wiedziec.
        - UWAGA: ta funkcja NIE odrzuca liczb ujemnych. -50 to poprawna liczba,
          wiec zwracasz -50.0. (Odrzucanie ujemnych to zadanie filter_valid_amounts.)

    Testuj:  uv run pytest tests/test_day_21.py::TestSafeGetTotal -v
    """
    pass


def split_valid_invalid(
    orders: list[dict], required_keys: list[str]
) -> tuple[list[dict], list[dict]]:
    """Podziel zamowienia na dwie kupki: poprawne i niepoprawne.

    Dostajesz:
        orders        - lista slownikow (zamowien)
        required_keys - lista nazw kluczy, ktore MUSZA byc wypelnione,
                        np. ["order_id", "customer_name"]

    Zwracasz:
        KROTKE dwoch list: (valid, invalid)
        Czyli: return poprawne, niepoprawne
        Kolejnosc zamowien w obu listach zachowana.

    Zamowienie jest POPRAWNE, gdy dla KAZDEGO klucza z required_keys:
        - klucz istnieje w slowniku, ORAZ
        - jego wartosc nie jest None, ORAZ
        - jego wartosc po obcieciu spacji nie jest pusta

    Wystarczy, ze JEDEN wymagany klucz zawiedzie -> cale zamowienie jest niepoprawne.

    Przyklad:
        orders = [
            {"order_id": "1", "customer_name": "Anna"},   # ok
            {"order_id": "2", "customer_name": ""},       # pusta nazwa   -> zle
            {"order_id": "3"},                            # brak klucza   -> zle
            {"order_id": "4", "customer_name": "  "},     # same spacje   -> zle
            {"order_id": "5", "customer_name": "Ewa"},    # ok
        ]
        split_valid_invalid(orders, ["order_id", "customer_name"])
            -> (
                 [{"order_id": "1", ...}, {"order_id": "5", ...}],   # valid
                 [{"order_id": "2", ...}, {"order_id": "3", ...}, {"order_id": "4", ...}],
               )

        Gdy required_keys jest pusta lista -> wszystko jest poprawne:
        split_valid_invalid([{"a": 1}, {}], []) -> ([{"a": 1}, {}], [])

    Uwagi:
        - Zaczynasz od dwoch pustych list i dokladasz do wlasciwej.
        - Przydaje sie druga petla (po required_keys) w srodku pierwszej (po orders).
        - Zwracanie dwoch wartosci naraz: `return lista_a, lista_b`

    Testuj:  uv run pytest tests/test_day_21.py::TestSplitValidInvalid -v
    """
    pass


def read_csv_rows(path) -> list[dict]:
    """Wczytaj plik CSV i zamien go na liste slownikow.

    Dostajesz:
        path - sciezka do pliku. Moze byc STRINGIEM ("dane/plik.csv")
               albo obiektem Path. Twoj kod musi radzic sobie z obydwoma.

    Zwracasz:
        Liste slownikow. Kazdy slownik = jeden wiersz.
        Klucze slownika = naglowki kolumn z pierwszej linii pliku.
        Wszystkie wartosci sa STRINGAMI (csv nie zamienia typow za Ciebie).

        Gdy plik NIE ISTNIEJE -> zwracasz pusta liste []. Bez wyjatku.

    Przyklad:
        Plik src/day_21_diagnostyka/data/orders_messy.csv zaczyna sie tak:

            order_id,customer_name,total_amount,status
            1,Anna Kowalska,149.99,paid

        read_csv_rows("src/day_21_diagnostyka/data/orders_messy.csv")
            -> [
                 {"order_id": "1", "customer_name": "Anna Kowalska",
                  "total_amount": "149.99", "status": "paid"},
                 ...  # razem 10 wierszy
               ]

        Zwroc uwage: "149.99" to TEKST, nie liczba.

    Uwagi:
        - Robiles to na dniu 20. Klasa nazywa sie csv.DictReader.
        - Plik otwieraj z encoding="utf-8".
        - Brak pliku: sprawdz istnienie ZANIM otworzysz (Path ma metode .exists())
          albo zlap FileNotFoundError. Obie drogi sa poprawne.

    Testuj:  uv run pytest tests/test_day_21.py::TestReadCsvRows -v
    """
    pass


def top_customers(orders: list[dict], n: int) -> list[tuple[str, float]]:
    """Znajdz n klientow, ktorzy wydali najwiecej. ZADANIE TRUDNIEJSZE.

    Dostajesz:
        orders - lista slownikow z kluczami "customer_name", "total_amount", "status"
        n      - ilu klientow zwrocic

    Zwracasz:
        Liste KROTEK (nazwa_klienta, suma_jego_zamowien),
        posortowana MALEJACO po sumie.
        Przy remisie (ta sama suma) - rosnaco alfabetycznie po nazwie.
        Gdy klientow jest mniej niz n - zwracasz tylu, ilu jest.

    Zasady liczenia:
        - Liczysz TYLKO zamowienia o statusie "paid" (po normalizacji -
          " PAID " tez sie liczy, patrz count_statuses).
        - Kwote pobierasz BEZPIECZNIE (patrz safe_get_total - smiec = 0.0).
        - Klientow bez nazwy (pusta / same spacje / brak klucza) POMIJASZ.
        - Nazwe klienta obcinasz ze spacji: " Piotr Nowak " -> "Piotr Nowak"

    Przyklad:
        orders = [
            {"customer_name": "Anna",  "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Anna",  "total_amount": "50.00",  "status": "PAID"},
            {"customer_name": "Anna",  "total_amount": "999.00", "status": "cancelled"},
            {"customer_name": "Piotr", "total_amount": "120.00", "status": "paid"},
            {"customer_name": "",      "total_amount": "500.00", "status": "paid"},
        ]
        top_customers(orders, 2)
            -> [("Anna", 150.0), ("Piotr", 120.0)]

        Dlaczego: Anna ma 100 + 50 = 150 (999 sie nie liczy, bo cancelled).
                  Piotr ma 120. Klient bez nazwy odpada.

    Uwagi:
        - Zrob to w DWOCH krokach: najpierw zbuduj slownik {klient: suma},
          potem zamien go na posortowana liste krotek.
        - Slownik ma metode .items(), ktora daje pary (klucz, wartosc).
        - sorted() przyjmuje argument key= (co porownujemy).
          Sortowanie malejaco po liczbie I rosnaco po tekscie naraz to trik:
          liczbe mozna odwrocic minusem.
        - Uzywaj funkcji, ktore juz napisales wyzej. Nie przepisuj ich.

    Testuj:  uv run pytest tests/test_day_21.py::TestTopCustomers -v
    """
    pass


def run_pipeline(input_path, output_dir) -> dict:
    """Mini-pipeline ETL. ZADANIE INTEGRUJACE - najtrudniejsze, rob je na koncu.

    To jest w miniaturze dokladnie to, co robi data engineer: wczytaj brudne dane,
    oddziel ziarno od plew, zapisz jedno i drugie, zdaj raport.

    Dostajesz:
        input_path - sciezka do pliku CSV z zamowieniami
        output_dir - KATALOG, do ktorego masz zapisac wyniki
                     (moze jeszcze nie istniec - masz go utworzyc)

    Masz zrobic:
        1. Wczytac CSV z input_path.
        2. Podzielic wiersze na poprawne i niepoprawne.
           Wiersz jest POPRAWNY, gdy JEDNOCZESNIE:
             - "order_id" jest niepusty, ORAZ
             - "customer_name" jest niepusty, ORAZ
             - "status" jest niepusty, ORAZ
             - "total_amount" da sie zamienic na liczbe WIEKSZA OD ZERA
               (uwaga: "-50.00" jest niepoprawny! "abc" i "" tez.)
        3. Zapisac:
             - poprawne  -> output_dir / "valid_orders.csv"
             - niepoprawne -> output_dir / "invalid_orders.csv"
           Naglowki kolumn takie same jak w pliku wejsciowym.
           Wiersze zapisujesz W ORYGINALNEJ POSTACI - niczego nie czyscisz,
           nie obcinasz spacji, nie zmieniasz wielkosci liter.
        4. Zwrocic slownik statystyk.

    Zwracasz:
        {
            "total": 10,            # ile wierszy bylo w pliku
            "valid": 6,             # ile poprawnych
            "invalid": 4,           # ile niepoprawnych
            "total_amount": 933.94, # suma kwot z POPRAWNYCH, zaokraglona do 2 miejsc
        }

    Gdy plik wejsciowy NIE ISTNIEJE:
        zwracasz {"total": 0, "valid": 0, "invalid": 0, "total_amount": 0.0}
        i NIE tworzysz zadnych plikow wyjsciowych.

    Uwagi:
        - Utworzenie katalogu (nawet zagniezdzonego): Path(...).mkdir(parents=True,
          exist_ok=True). Robiles to na dniu 20.
        - Do zapisu CSV ze slownikow: csv.DictWriter. Pamietaj o newline="" przy
          otwieraniu pliku do zapisu, inaczej na Windowsie dostaniesz puste linie.
        - Naglowki mozesz wziac z kluczy pierwszego wiersza.
        - NAJWAZNIEJSZE: uzyj funkcji, ktore napisales wyzej (read_csv_rows,
          safe_get_total...). Jesli przepisujesz te sama logike drugi raz -
          robisz to zle i zobacze to na code review.

    Testuj:  uv run pytest tests/test_day_21.py::TestRunPipeline -v
    """
    pass
