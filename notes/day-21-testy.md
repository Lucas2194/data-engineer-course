# Dzień 21 — Teoria: czym są testy i jak je czytać

**To jest blok, który wczoraj pominąłem. Przeczytaj go przed zadaniami.**

---

## 1. Po co w ogóle testy

Do tej pory sprawdzałeś swój kod tak: uruchamiałeś `main.py`, patrzyłeś na wydruk
i oceniałeś okiem, czy wygląda dobrze. To działa przy dziesięciu wierszach danych.
Przestaje działać, gdy masz ich milion, a pipeline uruchamia się o 3:00 w nocy,
kiedy śpisz.

**Test to zapisane raz, uruchamiane zawsze pytanie: „czy mój kod nadal robi to,
co ma robić?"**

W pracy data engineera to nie jest ozdobnik. Zmieniasz jedną linijkę w transformacji,
uruchamiasz testy i w dwie sekundy wiesz, czy nie zepsułeś czegoś, o czym zapomniałeś.
Bez testów dowiadujesz się o tym od analityka, trzy dni później, gdy raport dla zarządu
pokazuje bzdury.

---

## 2. Anatomia testu

Test to **zwykła funkcja Pythona**. Nic magicznego. Ma tylko dwie cechy:

1. Jej nazwa zaczyna się od `test_` — po tym pytest ją rozpoznaje.
2. W środku jest słowo **`assert`**.

`assert` znaczy dosłownie: **„twierdzę, że to jest prawda"**.

```python
assert 2 + 2 == 4     # prawda -> nic sie nie dzieje, idziemy dalej
assert 2 + 2 == 5     # falsz  -> Python rzuca AssertionError, test PADA
```

Cały test wygląda tak (masz to w `tests/test_demo_pytest.py`):

```python
def test_dolicza_vat_do_okraglej_kwoty():
    cena_netto = 100.00          # 1. przygotowanie danych
    wynik = add_vat(cena_netto)  # 2. wywolanie testowanej funkcji
    assert wynik == 123.00       # 3. sprawdzenie oczekiwania
```

Trzy kroki: **przygotuj → wywołaj → sprawdź**. Każdy test na świecie tak wygląda.

---

## 3. Jak czytać wynik

Uruchom sam i porównaj:

    uv run pytest tests/test_demo_pytest.py -v

Zobaczysz:

```
tests/test_demo_pytest.py::test_dolicza_vat_do_okraglej_kwoty PASSED     [ 25%]
tests/test_demo_pytest.py::test_zaokragla_do_dwoch_miejsc PASSED         [ 50%]
tests/test_demo_pytest.py::test_zero_zostaje_zerem PASSED                [ 75%]
tests/test_demo_pytest.py::test_ten_test_celowo_padnie FAILED            [100%]
```

**PASSED** (zielony) = Twój kod zrobił to, czego test oczekiwał.
**FAILED** (czerwony) = nie zrobił. I teraz najważniejsze — pytest **mówi Ci, dlaczego**:

```
>       assert add_vat(100.00) == 150.00
E       assert 123.0 == 150.0
E        +  where 123.0 = add_vat(100.0)
```

Czytasz to tak:

- Linia z `>` — **która asercja** padła.
- Linia `E assert 123.0 == 150.0` — **co dostaliśmy** (123.0) kontra **czego oczekiwano** (150.0).
  Po lewej zawsze wynik Twojej funkcji, po prawej oczekiwanie.
- Linia `where 123.0 = add_vat(100.0)` — **skąd wzięło się 123.0**.

Nie zgadujesz. Nie dodajesz `print()` w dziesięciu miejscach. **Czytasz komunikat.**
To jest umiejętność, którą będziesz stosował codziennie przez resztę kariery — i dlatego
zaczynamy od niej, a nie od Airflow.

---

## 4. Test jest instrukcją zadania

Tu jest sedno, którego wczoraj nie wyjaśniłem.

**Testy w `tests/test_day_21.py` nie są egzaminatorem. Są specyfikacją.**
Nie musisz się domyślać, czego chcę — **wystarczy, że przeczytasz test.**

Otwórz `tests/test_day_21.py` i popatrz na pierwszą klasę:

```python
class TestFormatOrderSummary:
    def test_basic(self):
        assert (
            format_order_summary(1, "Anna Kowalska", 149.99)
            == "Zamowienie #1 | Anna Kowalska | 149.99 PLN"
        )

    def test_dopelnia_do_dwoch_miejsc(self):
        assert format_order_summary(7, "Ewa", 149.5) == "Zamowienie #7 | Ewa | 149.50 PLN"

    def test_obcina_biale_znaki(self):
        assert format_order_summary(2, "  Piotr  ", 89.0) == "Zamowienie #2 | Piotr | 89.00 PLN"
```

Przeczytaj to jak zdanie po polsku:

- „Gdy dostaniesz `1`, `"Anna Kowalska"`, `149.99` → masz zwrócić dokładnie
  `"Zamowienie #1 | Anna Kowalska | 149.99 PLN"`."
- „Gdy dostaniesz `149.5` → masz zwrócić `149.50`, a nie `149.5`." (stąd wiesz, że
  trzeba wymusić dwa miejsca po przecinku)
- „Gdy dostaniesz `"  Piotr  "` ze spacjami → masz zwrócić `"Piotr"` bez spacji."
  (stąd wiesz, że trzeba obciąć białe znaki)

**Trzy testy = trzy wymagania.** Wszystko, co musisz wiedzieć, żeby napisać tę funkcję,
jest tutaj. Gdy nie wiesz, co zrobić — **czytasz test**, nie zgadujesz.

To jest też odpowiedź na Twoje „nie rozumiem opisów zadań": docstring to streszczenie,
a **test to prawda**. Gdy się różnią, wierzysz testowi.

---

## 5. Jak z tym pracować w praktyce

Nie uruchamiaj wszystkich 26 testów naraz — zaleje Cię czerwień i nic z tego nie wyniesiesz.
**Bierzesz jedną klasę, zielenisz, przechodzisz do następnej.**

    uv run pytest tests/test_day_21.py::TestFormatOrderSummary -v

Pętla, w której będziesz siedział przez najbliższe miesiące (i w pracy też):

1. Uruchom testy jednej klasy. Zobacz czerwone.
2. Przeczytaj **pierwszy** komunikat błędu. Tylko pierwszy.
3. Napisz kod, który go naprawia.
4. Uruchom ponownie. Powtarzaj, aż wszystko zielone.
5. Następna klasa.

Gdy funkcja nie jest napisana i zwraca `None` (bo w środku jest `pass`), komunikat
wygląda tak:

```
E       assert None == 'Zamowienie #1 | Anna Kowalska | 149.99 PLN'
```

To znaczy dokładnie: „Twoja funkcja nie zwróciła nic". Normalny start. Nie panikuj.

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| assert | twierdzić, zapewniać | `assert wynik == 123.00` |
| to pass | przejść, zaliczyć | `PASSED` — test zielony |
| to fail | nie przejść, paść | `FAILED` — test czerwony |
| expected | oczekiwany | „expected 150.0" |
| assertion error | błąd twierdzenia | `AssertionError` |
