# Faza 0 — Diagnostyka i środowisko (dni 21–23)

> **Dla agentów:** WYMAGANY SUB-SKILL: `superpowers:subagent-driven-development` lub
> `superpowers:executing-plans`. Kroki mają checkboxy (`- [ ]`).

**Cel:** Postawić środowisko pracy (uv, ruff, pytest, Postgres w Dockerze, DuckDB),
zmierzyć realne ubytki wiedzy po 7-tygodniowej przerwie i uruchomić tor SQL oraz tor
angielskiego — tak, żeby plan Fazy 1 opierał się na danych, a nie na zgadywaniu.

**Architektura:** Repo zostaje w obecnej konwencji (`notes/day-XX.md`, `src/day_XX/`),
numeracja dni jest kontynuowana od 21. Dochodzą trzy nowe tory: `sql/` (tor SQL
z systemem drilli), `tests/` (pytest — mechanizm samodzielnej weryfikacji ucznia),
`notes/english/` (tor angielskiego). Postgres i Adminer działają w Dockerze; DuckDB
lokalnie jako plik.

**Stack:** Python 3.13, uv, ruff, pytest, Docker Compose, PostgreSQL 17, DuckDB, Git.

## Global Constraints

- **Rozwiązań nie umieszczamy w repo.** Zadania to sygnatury + docstringi + `pass`.
  Uczeń dostaje testy, nie odpowiedzi.
- **Notatki i docstringi po polsku.** Nazwy funkcji, zmiennych, commitów, terminologia — po angielsku.
- **Numeracja dni kontynuowana:** następny dzień to **21**.
- **Struktura istniejącego repo zostaje.** Nie przenosimy `src/day_XX/`.
- **Każdy commit w konwencji:** `feat:` / `docs:` / `chore:` / `test:`.
- **Python >= 3.13**, zarządzany przez `uv`. Bez globalnego `pip install`.
- **ruff** jest jedynym źródłem prawdy o formatowaniu — uczeń nie formatuje ręcznie.
- **Baza demo:** PostgreSQL, użytkownik `de_user`, hasło `de_pass`, baza `de_shop`, port `5432`.

---

## Struktura plików

**Nowe:**
- `pyproject.toml` — zależności (uv), konfiguracja ruff i pytest
- `docker/docker-compose.yml` — Postgres 17 + Adminer
- `docker/init/01_schema.sql` — schemat sklepu (raw dane do SQL-a)
- `docker/init/02_seed.sql` — dane demo
- `.env.example` — wzorzec zmiennych środowiskowych
- `src/day_21_diagnostyka/exercises.py` — 8 zadań diagnostycznych (stuby)
- `src/day_21_diagnostyka/data/orders_messy.csv` — brudne dane wejściowe
- `tests/test_day_21.py` — testy diagnostyczne (uczeń musi zazielenić)
- `notes/day-21.md` — instrukcja diagnostyki
- `notes/day-22.md` — Docker + Postgres + DuckDB
- `notes/day-23.md` — pierwszy SQL + omówienie wyników
- `sql/README.md` — zasady toru SQL i systemu drilli
- `sql/day-21_select.sql` — pierwsze zadania SQL
- `sql/drills/drills.md` — rejestr drilli do codziennych powtórek
- `notes/english/glossary.md` — słownik techniczny

**Modyfikowane:**
- `.gitignore` — dodać `.venv/`, `*.duckdb`, `.env`
- `README.md` — sekcja „Jak uruchomić projekt"

---

### Task 1: Środowisko Pythona (uv, ruff, pytest)

**Files:**
- Create: `pyproject.toml`
- Create: `.env.example`
- Modify: `.gitignore`

**Interfaces:**
- Produces: działające `uv run pytest` i `uv run ruff check .`; wszystkie kolejne
  zadania uruchamiane przez `uv run`.

- [ ] **Krok 1: Zainstaluj uv**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Zamknij i otwórz terminal ponownie. Weryfikacja: `uv --version` → wypisze wersję.

- [ ] **Krok 2: Utwórz `pyproject.toml`**

```toml
[project]
name = "data-engineer-course"
version = "0.1.0"
description = "Kurs Junior Data Engineer - repozytorium nauki"
requires-python = ">=3.13"
dependencies = [
    "duckdb>=1.5",
    "psycopg[binary]>=3.2",
    "python-dotenv>=1.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.9",
]

[tool.ruff]
line-length = 100
target-version = "py313"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
```

- [ ] **Krok 3: Zainstaluj zależności**

```powershell
uv sync
```

Oczekiwane: powstaje `.venv/` i `uv.lock`, instalują się duckdb, psycopg, pytest, ruff.

- [ ] **Krok 4: Utwórz `.env.example`**

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=de_shop
POSTGRES_USER=de_user
POSTGRES_PASSWORD=de_pass
```

- [ ] **Krok 5: Uzupełnij `.gitignore`**

Dopisz na końcu pliku:

```
# Środowisko i sekrety
.venv/
.env

# Bazy lokalne
*.duckdb
*.duckdb.wal

# Cache narzędzi
.pytest_cache/
.ruff_cache/
```

- [ ] **Krok 6: Zweryfikuj, że narzędzia działają**

```powershell
uv run ruff check .
uv run pytest --collect-only
```

Oczekiwane: ruff kończy się bez błędów krytycznych (może zgłosić uwagi do starego kodu
w `src/` — to normalne, na razie je ignorujemy). pytest wypisze „no tests collected" —
to poprawne, testów jeszcze nie ma.

- [ ] **Krok 7: Commit**

```powershell
git add pyproject.toml uv.lock .env.example .gitignore
git commit -m "chore: add uv, ruff and pytest tooling"
```

---

### Task 2: Postgres i DuckDB w Dockerze (dzień 22)

**Files:**
- Create: `docker/docker-compose.yml`
- Create: `docker/init/01_schema.sql`
- Create: `docker/init/02_seed.sql`
- Create: `notes/day-22.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: `.env.example` z Taska 1.
- Produces: działająca baza `de_shop` na `localhost:5432` z tabelami
  `customers`, `products`, `orders`, `order_items` — źródło danych dla całego toru SQL.

- [ ] **Krok 1: Zainstaluj Docker Desktop**

Pobierz z https://www.docker.com/products/docker-desktop/, zainstaluj, uruchom.
Weryfikacja: `docker --version` → wypisze wersję.

- [ ] **Krok 2: Utwórz `docker/docker-compose.yml`**

```yaml
services:
  postgres:
    image: postgres:17
    container_name: de_postgres
    environment:
      POSTGRES_USER: de_user
      POSTGRES_PASSWORD: de_pass
      POSTGRES_DB: de_shop
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U de_user -d de_shop"]
      interval: 5s
      retries: 5

  adminer:
    image: adminer:latest
    container_name: de_adminer
    ports:
      - "8080:8080"
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  pgdata:
```

- [ ] **Krok 3: Utwórz `docker/init/01_schema.sql`**

```sql
-- Schemat sklepu internetowego. Baza dla całego toru SQL.

CREATE TABLE customers (
    customer_id   SERIAL PRIMARY KEY,
    first_name    TEXT NOT NULL,
    last_name     TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    city          TEXT,
    country       TEXT NOT NULL,
    created_at    DATE NOT NULL
);

CREATE TABLE products (
    product_id    SERIAL PRIMARY KEY,
    product_name  TEXT NOT NULL,
    category      TEXT NOT NULL,
    unit_price    NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE orders (
    order_id      SERIAL PRIMARY KEY,
    customer_id   INTEGER NOT NULL REFERENCES customers (customer_id),
    order_date    DATE NOT NULL,
    status        TEXT NOT NULL CHECK (status IN ('paid', 'pending', 'cancelled', 'refunded'))
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id      INTEGER NOT NULL REFERENCES orders (order_id),
    product_id    INTEGER NOT NULL REFERENCES products (product_id),
    quantity      INTEGER NOT NULL CHECK (quantity > 0),
    unit_price    NUMERIC(10, 2) NOT NULL
);
```

- [ ] **Krok 4: Utwórz `docker/init/02_seed.sql`**

```sql
INSERT INTO customers (first_name, last_name, email, city, country, created_at) VALUES
('Anna',   'Kowalska',   'anna.kowalska@example.com',   'Warszawa', 'PL', '2025-01-15'),
('Piotr',  'Nowak',      'piotr.nowak@example.com',     'Kraków',   'PL', '2025-02-03'),
('Maria',  'Wisniewska', 'maria.wis@example.com',       'Gdansk',   'PL', '2025-02-20'),
('Tomasz', 'Wojcik',     'tomasz.wojcik@example.com',   'Wroclaw',  'PL', '2025-03-11'),
('Ewa',    'Kaminska',   'ewa.kaminska@example.com',    NULL,       'PL', '2025-04-02'),
('John',   'Smith',      'john.smith@example.com',      'Berlin',   'DE', '2025-04-18'),
('Lukas',  'Muller',     'lukas.muller@example.com',    'Munich',   'DE', '2025-05-09'),
('Sofia',  'Rossi',      'sofia.rossi@example.com',     'Milan',    'IT', '2025-05-30');

INSERT INTO products (product_name, category, unit_price) VALUES
('Grawerowany kubek',      'gifts',       49.99),
('Deska do krojenia',      'kitchen',     89.00),
('Breloczek stalowy',      'gifts',       19.50),
('Zestaw noży',            'kitchen',    249.00),
('Lampka nocna',           'home',       129.90),
('Ramka na zdjecia',       'home',        39.00),
('Karafka szklana',        'kitchen',    159.00),
('Pudelko na herbate',     'gifts',       69.90);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2025-06-01', 'paid'),
(1, '2025-06-15', 'paid'),
(2, '2025-06-03', 'cancelled'),
(2, '2025-07-01', 'paid'),
(3, '2025-06-20', 'pending'),
(4, '2025-06-22', 'paid'),
(4, '2025-07-05', 'refunded'),
(5, '2025-07-08', 'paid'),
(6, '2025-06-11', 'paid'),
(6, '2025-07-12', 'paid'),
(7, '2025-07-14', 'pending'),
(1, '2025-07-20', 'paid');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 2,  49.99), (1, 3, 1,  19.50),
(2, 4, 1, 249.00),
(3, 2, 1,  89.00),
(4, 5, 2, 129.90), (4, 6, 3,  39.00),
(5, 1, 1,  49.99),
(6, 7, 1, 159.00), (6, 8, 2,  69.90),
(7, 4, 1, 249.00),
(8, 3, 5,  19.50),
(9, 2, 1,  89.00), (9, 5, 1, 129.90),
(10, 8, 1, 69.90),
(11, 6, 2, 39.00),
(12, 1, 3, 49.99), (12, 7, 1, 159.00);
```

- [ ] **Krok 5: Uruchom bazę**

```powershell
docker compose -f docker/docker-compose.yml up -d
```

Oczekiwane: dwa kontenery wstają (`de_postgres`, `de_adminer`).
Weryfikacja: `docker ps` → obie usługi ze statusem `Up`.

- [ ] **Krok 6: Sprawdź, że dane się załadowały**

```powershell
docker exec -it de_postgres psql -U de_user -d de_shop -c "SELECT count(*) FROM orders;"
```

Oczekiwane: `12`.

Jeśli wychodzi błąd „relation does not exist": skrypty z `init/` uruchamiają się
**tylko przy pierwszym** starcie pustego wolumenu. Napraw tak:

```powershell
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
```

- [ ] **Krok 7: Wejdź do Adminera przez przeglądarkę**

Otwórz http://localhost:8080. System: `PostgreSQL`, serwer: `postgres`,
użytkownik: `de_user`, hasło: `de_pass`, baza: `de_shop`.
Oczekiwane: widzisz cztery tabele.

- [ ] **Krok 8: Napisz `notes/day-22.md`**

Notatka musi zawierać: czym jest obraz, czym kontener, czym wolumen (i dlaczego
`down -v` kasuje dane); co robi `docker compose up -d`; jak wejść do bazy przez
`docker exec`; dane połączenia do Adminera; oraz sekcję „Co poszło nie tak i jak
naprawiłem" — uzupełniana na bieżąco.

- [ ] **Krok 9: Dopisz do `README.md` sekcję „Jak uruchomić projekt"**

```markdown
## Jak uruchomić projekt

Wymagania: Python 3.13+, uv, Docker Desktop.

    uv sync                                              # zależności
    docker compose -f docker/docker-compose.yml up -d    # baza + Adminer
    uv run pytest                                        # testy

Baza: `localhost:5432`, db `de_shop`, user `de_user`. Adminer: http://localhost:8080
```

- [ ] **Krok 10: Commit**

```powershell
git add docker/ notes/day-22.md README.md
git commit -m "feat: add Postgres and Adminer via Docker Compose with shop schema"
```

---

### Task 3: Zadania diagnostyczne — Python (dzień 21)

**Files:**
- Create: `src/day_21_diagnostyka/exercises.py`
- Create: `src/day_21_diagnostyka/data/orders_messy.csv`
- Create: `tests/test_day_21.py`
- Create: `notes/day-21.md`

**Interfaces:**
- Produces: 8 funkcji, których zieloność mierzy stan wiedzy z dni 1–20.
  Sygnatury (dokładnie te nazwy — testy na nich polegają):
  - `format_order_summary(order_id: int, customer_name: str, total: float) -> str`
  - `filter_valid_amounts(amounts: list) -> list[float]`
  - `count_statuses(orders: list[dict]) -> dict[str, int]`
  - `safe_get_total(order: dict) -> float`
  - `split_valid_invalid(orders: list[dict], required_keys: list[str]) -> tuple[list[dict], list[dict]]`
  - `read_csv_rows(path) -> list[dict]`
  - `top_customers(orders: list[dict], n: int) -> list[tuple[str, float]]`
  - `run_pipeline(input_path, output_dir) -> dict`

- [ ] **Krok 1: Utwórz brudne dane `src/day_21_diagnostyka/data/orders_messy.csv`**

```csv
order_id,customer_name,total_amount,status
1,Anna Kowalska,149.99,paid
2, Piotr Nowak ,89.00,PAID
3,Maria Wisniewska,,pending
4,Tomasz Wojcik,-50.00,paid
5,Ewa Kaminska,249.50,cancelled
6,Anna Kowalska,79.90,paid
7,,120.00,paid
8,Piotr Nowak,abc,paid
9,Anna Kowalska,310.00,PENDING
10,Sofia Rossi,55.55,paid
```

- [ ] **Krok 2: Utwórz stuby `src/day_21_diagnostyka/exercises.py`**

```python
"""Zadania diagnostyczne po przerwie. Zakres: dni 1-20.

Nie zmieniaj nazw funkcji ani ich parametrow - testy na nich polegaja.
Rozwiazania nie sa nigdzie zapisane. Masz testy - to jedyna informacja zwrotna.
"""

import csv
from pathlib import Path


def format_order_summary(order_id: int, customer_name: str, total: float) -> str:
    """Zwroc podsumowanie zamowienia w formacie:

        'Zamowienie #1 | Anna Kowalska | 149.99 PLN'

    Kwota ma miec ZAWSZE dwa miejsca po przecinku (149.5 -> '149.50').
    Nazwa klienta ma byc obcieta z bialych znakow z obu stron.
    """
    pass


def filter_valid_amounts(amounts: list) -> list[float]:
    """Zwroc nowa liste zawierajaca wylacznie poprawne kwoty jako float.

    Kwota jest poprawna, gdy: da sie ja zamienic na float ORAZ jest wieksza od zera.
    Wejscie moze zawierac stringi ('12.50'), None, puste stringi i smieci ('abc').
    Kolejnosc zachowana. Elementy niepoprawne po prostu pomijasz.
    """
    pass


def count_statuses(orders: list[dict]) -> dict[str, int]:
    """Policz, ile razy wystapil kazdy status.

    Statusy normalizujesz: obcinasz biale znaki i zamieniasz na male litery,
    czyli ' PAID ' i 'paid' to ten sam status.
    Zamowienia bez klucza 'status' lub z pustym statusem pomijasz.

    Przyklad zwrotu: {'paid': 3, 'pending': 1}
    """
    pass


def safe_get_total(order: dict) -> float:
    """Zwroc wartosc zamowienia jako float.

    Gdy klucza 'total_amount' brak, jest pusty, jest None albo nie da sie go
    zamienic na liczbe - zwroc 0.0. Funkcja NIE MOZE rzucic wyjatkiem.
    """
    pass


def split_valid_invalid(
    orders: list[dict], required_keys: list[str]
) -> tuple[list[dict], list[dict]]:
    """Podziel zamowienia na poprawne i niepoprawne.

    Zamowienie jest poprawne, gdy dla KAZDEGO klucza z required_keys:
    klucz istnieje, a jego wartosc nie jest None ani pustym stringiem
    (po obcieciu bialych znakow).

    Zwroc krotke (valid, invalid). Kolejnosc w obu listach zachowana.
    """
    pass


def read_csv_rows(path) -> list[dict]:
    """Wczytaj plik CSV i zwroc liste slownikow (klucze = naglowki kolumn).

    'path' moze byc stringiem albo obiektem Path. Kodowanie: utf-8.
    Gdy plik nie istnieje - zwroc pusta liste (bez wyjatku).
    """
    pass


def top_customers(orders: list[dict], n: int) -> list[tuple[str, float]]:
    """Zwroc n klientow o najwyzszej sumie wartosci zamowien.

    Liczysz TYLKO zamowienia o statusie 'paid' (po normalizacji - patrz count_statuses).
    Wartosc zamowienia pobierasz bezpiecznie (patrz safe_get_total).
    Klientow bez nazwy (pusta / brak klucza) pomijasz.

    Zwrot: lista krotek (customer_name, suma) posortowana malejaco po sumie.
    Przy remisie - alfabetycznie po nazwie klienta.
    Gdy klientow jest mniej niz n - zwroc tylu, ilu jest.

    Przyklad: [('Anna Kowalska', 539.89), ('Sofia Rossi', 55.55)]
    """
    pass


def run_pipeline(input_path, output_dir) -> dict:
    """Mini-pipeline. Zadanie integrujace wszystko powyzej.

    1. Wczytaj CSV z input_path.
    2. Podziel wiersze na poprawne i niepoprawne. Wiersz jest poprawny, gdy ma
       niepuste 'order_id', 'customer_name', 'status' ORAZ 'total_amount' daje sie
       zamienic na liczbe wieksza od zera.
    3. Zapisz poprawne do output_dir/'valid_orders.csv',
       niepoprawne do output_dir/'invalid_orders.csv'.
       Katalog output_dir utworz, jesli nie istnieje.
       Naglowki kolumn takie same jak w pliku wejsciowym.
    4. Zwroc slownik statystyk:
       {'total': int, 'valid': int, 'invalid': int, 'total_amount': float}
       gdzie 'total_amount' to suma kwot z poprawnych wierszy, zaokraglona do 2 miejsc.

    Gdy plik wejsciowy nie istnieje: zwroc
    {'total': 0, 'valid': 0, 'invalid': 0, 'total_amount': 0.0} i nie zapisuj nic.
    """
    pass
```

- [ ] **Krok 3: Utwórz testy `tests/test_day_21.py`**

```python
import csv

import pytest

from src.day_21_diagnostyka.exercises import (
    count_statuses,
    filter_valid_amounts,
    format_order_summary,
    read_csv_rows,
    run_pipeline,
    safe_get_total,
    split_valid_invalid,
    top_customers,
)

MESSY_CSV = "src/day_21_diagnostyka/data/orders_messy.csv"


class TestFormatOrderSummary:
    def test_basic(self):
        assert format_order_summary(1, "Anna Kowalska", 149.99) == (
            "Zamowienie #1 | Anna Kowalska | 149.99 PLN"
        )

    def test_dopelnia_do_dwoch_miejsc(self):
        assert format_order_summary(7, "Ewa", 149.5) == "Zamowienie #7 | Ewa | 149.50 PLN"

    def test_obcina_biale_znaki(self):
        assert format_order_summary(2, "  Piotr  ", 89.0) == "Zamowienie #2 | Piotr | 89.00 PLN"


class TestFilterValidAmounts:
    def test_odsiewa_smieci(self):
        assert filter_valid_amounts(["12.50", 30, "abc", None, "", -5, 0, 7.25]) == [
            12.5,
            30.0,
            7.25,
        ]

    def test_pusta_lista(self):
        assert filter_valid_amounts([]) == []

    def test_wszystko_niepoprawne(self):
        assert filter_valid_amounts(["abc", None, -1, 0]) == []


class TestCountStatuses:
    def test_normalizuje_wielkosc_liter(self):
        orders = [
            {"status": "paid"},
            {"status": " PAID "},
            {"status": "pending"},
            {"status": "Paid"},
        ]
        assert count_statuses(orders) == {"paid": 3, "pending": 1}

    def test_pomija_braki(self):
        orders = [{"status": "paid"}, {}, {"status": ""}, {"status": "   "}]
        assert count_statuses(orders) == {"paid": 1}

    def test_pusta_lista(self):
        assert count_statuses([]) == {}


class TestSafeGetTotal:
    @pytest.mark.parametrize(
        "order,expected",
        [
            ({"total_amount": "149.99"}, 149.99),
            ({"total_amount": 89}, 89.0),
            ({"total_amount": ""}, 0.0),
            ({"total_amount": None}, 0.0),
            ({"total_amount": "abc"}, 0.0),
            ({}, 0.0),
        ],
    )
    def test_zwraca_float_lub_zero(self, order, expected):
        assert safe_get_total(order) == expected


class TestSplitValidInvalid:
    def test_dzieli_poprawnie(self):
        orders = [
            {"order_id": "1", "customer_name": "Anna"},
            {"order_id": "2", "customer_name": ""},
            {"order_id": "3"},
            {"order_id": "4", "customer_name": "  "},
            {"order_id": "5", "customer_name": "Ewa"},
        ]
        valid, invalid = split_valid_invalid(orders, ["order_id", "customer_name"])
        assert [o["order_id"] for o in valid] == ["1", "5"]
        assert [o["order_id"] for o in invalid] == ["2", "3", "4"]

    def test_brak_wymagan_wszystko_poprawne(self):
        orders = [{"a": 1}, {}]
        valid, invalid = split_valid_invalid(orders, [])
        assert len(valid) == 2
        assert invalid == []


class TestReadCsvRows:
    def test_wczytuje_plik(self):
        rows = read_csv_rows(MESSY_CSV)
        assert len(rows) == 10
        assert rows[0]["customer_name"] == "Anna Kowalska"
        assert rows[0]["total_amount"] == "149.99"

    def test_brak_pliku_zwraca_pusta_liste(self, tmp_path):
        assert read_csv_rows(tmp_path / "nie_ma.csv") == []


class TestTopCustomers:
    def test_sumuje_tylko_paid(self):
        orders = [
            {"customer_name": "Anna", "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Anna", "total_amount": "50.00", "status": "PAID"},
            {"customer_name": "Anna", "total_amount": "999.00", "status": "cancelled"},
            {"customer_name": "Piotr", "total_amount": "120.00", "status": "paid"},
            {"customer_name": "", "total_amount": "500.00", "status": "paid"},
        ]
        assert top_customers(orders, 2) == [("Anna", 150.0), ("Piotr", 120.0)]

    def test_remis_alfabetycznie(self):
        orders = [
            {"customer_name": "Zofia", "total_amount": "100.00", "status": "paid"},
            {"customer_name": "Adam", "total_amount": "100.00", "status": "paid"},
        ]
        assert top_customers(orders, 2) == [("Adam", 100.0), ("Zofia", 100.0)]

    def test_n_wieksze_niz_liczba_klientow(self):
        orders = [{"customer_name": "Anna", "total_amount": "10.00", "status": "paid"}]
        assert top_customers(orders, 5) == [("Anna", 10.0)]


class TestRunPipeline:
    def test_pelny_przebieg(self, tmp_path):
        stats = run_pipeline(MESSY_CSV, tmp_path)

        assert stats["total"] == 10
        assert stats["valid"] == 6
        assert stats["invalid"] == 4
        assert stats["total_amount"] == 933.94

        with open(tmp_path / "valid_orders.csv", encoding="utf-8") as f:
            valid_rows = list(csv.DictReader(f))
        assert len(valid_rows) == 6
        assert [r["order_id"] for r in valid_rows] == ["1", "2", "5", "6", "9", "10"]

        with open(tmp_path / "invalid_orders.csv", encoding="utf-8") as f:
            invalid_rows = list(csv.DictReader(f))
        assert [r["order_id"] for r in invalid_rows] == ["3", "4", "7", "8"]

    def test_tworzy_katalog_wyjsciowy(self, tmp_path):
        out = tmp_path / "glebiej" / "output"
        run_pipeline(MESSY_CSV, out)
        assert (out / "valid_orders.csv").exists()

    def test_brak_pliku_wejsciowego(self, tmp_path):
        stats = run_pipeline(tmp_path / "nie_ma.csv", tmp_path / "out")
        assert stats == {"total": 0, "valid": 0, "invalid": 0, "total_amount": 0.0}
        assert not (tmp_path / "out" / "valid_orders.csv").exists()
```

- [ ] **Krok 4: Uruchom testy i potwierdź, że WSZYSTKIE padają**

```powershell
uv run pytest tests/test_day_21.py -v
```

Oczekiwane: komplet FAILED (funkcje zwracają `None`). To jest punkt startowy —
czerwone testy są celem do zazielenienia, nie błędem.

- [ ] **Krok 5: Napisz `notes/day-21.md`**

Notatka zawiera: zasady diagnostyki (limit 20 minut na jedno zadanie, potem pytasz;
zadania robisz **bez zaglądania do starego kodu w `src/day_*/`** — chodzi o zmierzenie,
co pamiętasz, a nie co potrafisz skopiować); komendę uruchamiania pojedynczego testu
(`uv run pytest tests/test_day_21.py::TestSafeGetTotal -v`); oraz tabelę do wypełnienia:
zadanie | czy zrobione bez pomocy | ile minut | co sprawiło problem.

- [ ] **Krok 6: Commit (materiały, przed rozwiązywaniem)**

```powershell
git add src/day_21_diagnostyka/ tests/test_day_21.py notes/day-21.md
git commit -m "test: add day 21 diagnostic exercises covering days 1-20"
```

- [ ] **Krok 7: [UCZEŃ] Rozwiąż zadania**

Wypełniasz `exercises.py`. Cel: `uv run pytest tests/test_day_21.py` na zielono.
Kolejność od najprostszego: `format_order_summary` → `safe_get_total` →
`filter_valid_amounts` → `count_statuses` → `split_valid_invalid` → `read_csv_rows`
→ `top_customers` → `run_pipeline`.

Wypełniaj tabelę w `notes/day-21.md` na bieżąco — **to ona jest właściwym produktem
tego dnia**, nie zielone testy.

- [ ] **Krok 8: [UCZEŃ] Sformatuj kod i commituj**

```powershell
uv run ruff check --fix .
uv run ruff format src/day_21_diagnostyka/
uv run pytest tests/test_day_21.py -v
git add -A
git commit -m "feat: solve day 21 diagnostic exercises"
```

---

### Task 4: Tor SQL — start (dzień 23)

**Files:**
- Create: `sql/README.md`
- Create: `sql/day-21_select.sql`
- Create: `sql/drills/drills.md`
- Create: `notes/day-23.md`

**Interfaces:**
- Consumes: baza `de_shop` z Taska 2.
- Produces: system drilli — od tego dnia **każda sesja zaczyna się od 2–3 drilli**.

- [ ] **Krok 1: Utwórz `sql/README.md`**

Opisz: jak połączyć się z bazą (`docker exec -it de_postgres psql -U de_user -d de_shop`
albo Adminer na http://localhost:8080); konwencję plików (`sql/day-XX_temat.sql`);
oraz **zasadę drilli**: każdą sesję zaczynasz od 2–3 zapytań z `sql/drills/drills.md`,
pisanych **z pamięci, bez podglądania**. Drill, który się nie udał, wraca do puli
na kolejny dzień.

- [ ] **Krok 2: Utwórz `sql/day-21_select.sql`** — zadania, bez rozwiązań

```sql
-- Dzien 21 (tor SQL): SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
-- Baza: de_shop. Pod kazdym zadaniem napisz zapytanie i uruchom je.
-- Rozwiazan nie ma. Sprawdzian: czy wynik ma sens. Liczby w nawiasach to
-- oczekiwana liczba wierszy - jesli sie nie zgadza, zapytanie jest zle.

-- Z1. Wypisz wszystkie kolumny z tabeli customers. (8 wierszy)

-- Z2. Wypisz imie, nazwisko i miasto klientow z Polski. (5 wierszy)

-- Z3. Wypisz klientow, ktorzy NIE maja podanego miasta. (1 wiersz)

-- Z4. Wypisz produkty drozsze niz 100 PLN, od najdrozszego. (3 wiersze)

-- Z5. Wypisz 3 najtansze produkty. (3 wiersze)

-- Z6. Wypisz unikalne kategorie produktow. (3 wiersze)

-- Z7. Wypisz unikalne statusy wystepujace w zamowieniach. (4 wiersze)

-- Z8. Wypisz zamowienia zlozone w lipcu 2025, od najnowszego. (6 wierszy)

-- Z9. Wypisz zamowienia o statusie 'paid' LUB 'pending', posortowane po dacie. (10 wierszy)

-- Z10. Wypisz produkty z kategorii 'gifts' w cenie od 20 do 70 PLN. (2 wiersze)

-- Z11 (trudniejsze). Wypisz email i date rejestracji klientow zarejestrowanych
--     w pierwszym kwartale 2025, posortowanych od najstarszego. Kolumne z data
--     nazwij 'registered_on' (uzyj aliasu). (4 wiersze)
```

- [ ] **Krok 3: Utwórz `sql/drills/drills.md`**

```markdown
# Drille SQL

Zasada: kazda sesje zaczynasz od 2-3 drilli. Piszesz Z PAMIECI, bez podgladania.
Drill zaliczony = poprawny wynik za pierwszym razem. Drill niezaliczony wraca na jutro.

Legenda: [ ] do zrobienia | [x] zaliczony (data)

## Pula aktywna

- [ ] D1. Klienci z Niemiec, posortowani po nazwisku.
- [ ] D2. Trzy najdrozsze produkty.
- [ ] D3. Unikalne kategorie produktow.
- [ ] D4. Zamowienia ze statusem innym niz 'paid'.
- [ ] D5. Klienci bez podanego miasta.
- [ ] D6. Zamowienia z czerwca 2025, od najnowszego.

## Dziennik

| Data | Drille | Zaliczone | Uwagi |
|------|--------|-----------|-------|
|      |        |           |       |
```

- [ ] **Krok 4: Napisz `notes/day-23.md`**

Teoria (po polsku, z przykładami do uruchomienia na `de_shop`): czym jest tabela,
wiersz, kolumna; klucz główny i obcy (pokaż na `orders.customer_id` → `customers`);
kolejność wykonania `SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT`;
`DISTINCT`; aliasy (`AS`); `NULL` i dlaczego `= NULL` nie działa, a `IS NULL` działa —
to jest klasyczne pytanie rekrutacyjne.

- [ ] **Krok 5: [UCZEŃ] Rozwiąż zadania z `sql/day-21_select.sql`**

Zapytania wpisujesz pod komentarzami, w tym samym pliku. Uruchamiasz w Adminerze
lub `psql`. Weryfikacja: liczba wierszy zgadza się z liczbą w nawiasie.

- [ ] **Krok 6: Commit**

```powershell
git add sql/ notes/day-23.md
git commit -m "feat: start SQL track with SELECT exercises and drill system"
```

---

### Task 5: Tor angielskiego — start

**Files:**
- Create: `notes/english/glossary.md`

**Interfaces:**
- Produces: rutyna 15 min/dzień; glosariusz rośnie codziennie o 3–5 haseł.

- [ ] **Krok 1: Utwórz `notes/english/glossary.md`**

```markdown
# Slownik techniczny EN -> PL

Zasada: kazdego dnia dopisujesz 3-5 hasel, ktore realnie spotkales w dokumentacji
albo w komunikacie bledu. Nie przepisujesz slownika - notujesz to, co Cie zablokowalo.

Kolumna "Zdanie" jest obowiazkowa - slowo bez kontekstu nie zostaje w glowie.

| EN | PL | Zdanie, w ktorym to spotkalem |
|----|----|-------------------------------|
| row | wiersz | "The query returned 12 rows." |
| query | zapytanie | "Run the query against the database." |
| schema | schemat (struktura danych) | "The table schema defines column types." |
| to fail | nie powiesc sie, wywalic sie | "The test failed with an assertion error." |
| missing | brakujacy | "Missing required column: customer_name." |

## Zadanie na dzis

Przeczytaj po angielsku sekcje "Basic Usage" w dokumentacji pytest:
https://docs.pytest.org/en/stable/how-to/assert.html

Nie tlumacz zdanie po zdaniu. Cel: zrozumiec, o co chodzi, i wyciagnac 5 nowych hasel
do tabeli powyzej.
```

- [ ] **Krok 2: Commit**

```powershell
git add notes/english/
git commit -m "docs: start technical English track with glossary"
```

---

### Task 6: Raport diagnostyczny i zakres Fazy 1

**Files:**
- Create: `docs/superpowers/plans/2026-07-17-faza-1-fundamenty.md` (produkt tego taska)

**Interfaces:**
- Consumes: tabela wyników z `notes/day-21.md`, kod ucznia w `exercises.py`,
  rozwiązania z `sql/day-21_select.sql`.
- Produces: plan Fazy 1 dopasowany do realnych braków.

- [ ] **Krok 1: [COACH] Code review rozwiązań ucznia**

Przejrzyj `src/day_21_diagnostyka/exercises.py`. Oceń nie „czy zielone", ale:
czy `try/except` łapie konkretne wyjątki, czy wszystko po kolei; czy nie ma
duplikacji logiki, którą dało się wydzielić; czy `run_pipeline` używa wcześniejszych
funkcji, czy przepisuje je od zera; czy nazwy zmiennych coś znaczą.
Feedback konkretny, bez pochwał na wyrost.

- [ ] **Krok 2: [COACH] Zbuduj mapę braków**

Zestaw tabelę: temat (dni 1–20) → status (`umie` / `chwieje się` / `nie pamięta`),
na podstawie czasu rozwiązania i liczby proszonych wskazówek. Zapisz w `notes/day-21.md`
w sekcji „Wyniki diagnostyki".

- [ ] **Krok 3: [COACH] Napisz plan Fazy 1**

Dni, które trafiają do planu Fazy 1, wybierasz **wyłącznie** na podstawie mapy braków.
Tematy oznaczone `umie` **pomijasz całkowicie**. Stałe elementy niezależne od
diagnostyki: `pytest` i pisanie własnych testów, `logging`, `requests`/API, pandas,
WSL2, JSON — plus tor SQL (agregacje → `GROUP BY` → JOIN-y) i tor angielskiego.

- [ ] **Krok 4: Commit**

```powershell
git add docs/superpowers/plans/ notes/day-21.md
git commit -m "docs: add diagnostic results and Phase 1 plan"
```

---

## Kolejność wykonania

| Dzień | Data | Taski |
|---|---|---|
| **21** | wt 14 lipca | Task 1 (środowisko) + Task 3 (diagnostyka Python) + Task 5 (angielski) |
| **22** | śr 15 lipca | Task 2 (Docker + Postgres) + dokończenie diagnostyki |
| **23** | czw 16 lipca | Task 4 (start SQL) + Task 6 (raport i plan Fazy 1) |

Task 1 musi poprzedzić Task 3 (pytest). Task 2 musi poprzedzić Task 4 (baza).
Task 6 wymaga ukończonych Tasków 3 i 4.
