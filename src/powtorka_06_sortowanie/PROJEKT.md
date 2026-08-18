# R6 — Część B: projekt bez testów

> **Do tej części siadasz dopiero po zaliczeniu części A** (`exercises.py`, 42 testy).
> Będziesz z niej korzystał.

---

## Czym to się różni od wszystkiego, co robiłeś do tej pory

Przez pięć bloków dostawałeś gotowe sygnatury funkcji, docstringi z przykładami i testy,
które mówiły dokładnie, czego brakuje. Wypełniałeś środek.

Tutaj dostajesz **pusty plik i opis tego, co program ma robić**.

Nie ma stubów. Nie ma testów. Nie ma podanych nazw funkcji, argumentów ani typów zwracanych.
**Sam decydujesz, na jakie funkcje podzielić program, co każda przyjmuje i co zwraca.**

To jest ta sama zmiana, która czeka Cię w pierwszej pracy: nikt nie da Ci docstringa.
Dostaniesz zdanie na Slacku — *„potrzebujemy raportu top klientów z tego CSV-ki"* — i tyle.

---

## Zadanie

Napisz program, który bierze surowy plik z zamówieniami, oddziela dane poprawne
od śmieci, zapisuje jedno i drugie osobno i produkuje czytelny raport tekstowy.

To jest w miniaturze dokładnie to, co robi data engineer.

**Plik do napisania:** `src/powtorka_06_sortowanie/raport.py`

**Dane wejściowe:** `src/powtorka_06_sortowanie/data/orders.csv` (16 wierszy, celowo brudny)

**Uruchomienie:**
```
uv run python -m src.powtorka_06_sortowanie.raport
```

---

## Wymagania

### 1. Ścieżki

- Wszystkie ścieżki liczone **od położenia pliku `.py`**, nie od katalogu, z którego
  uruchamiasz program. Ma działać niezależnie od tego, gdzie stoisz w terminalu.
- Ścieżki jako **stałe WIELKIMI literami na górze modułu**. Nigdzie w kodzie nie ma
  ścieżki wpisanej z palca w środku funkcji.
- Katalog wyjściowy `output/` może nie istnieć — program ma go utworzyć.

### 2. Wczytanie i podział

Wczytaj CSV i podziel wiersze na **poprawne** i **niepoprawne**.

Wiersz jest **POPRAWNY**, gdy spełnia **jednocześnie wszystkie** warunki:

| Warunek | Uwaga |
|---------|-------|
| `order_id` niepusty | po obcięciu spacji |
| `customer_name` niepusty | po obcięciu spacji |
| `status` niepusty | po obcięciu spacji |
| `total_amount` daje się zamienić na liczbę **większą od zera** | `"abc"`, `""`, `"-40.00"`, `"0.00"` są **nie**poprawne |

Wierszy **nie czyścisz** — zapisujesz je w oryginalnej postaci, ze spacjami i wielkimi
literami, tak jak przyszły z pliku. Walidacja tylko **decyduje**, do której kupki wiersz trafia.

### 3. Zapis dwóch plików CSV

- `output/valid_orders.csv` — wiersze poprawne
- `output/invalid_orders.csv` — wiersze niepoprawne

Kolumny takie same jak w pliku wejściowym, w tej samej kolejności, z nagłówkiem.

### 4. Raport tekstowy

`output/raport.txt`. Ma zawierać co najmniej:

- nazwę pliku źródłowego i liczbę wczytanych wierszy,
- liczbę poprawnych i niepoprawnych,
- sumę kwot z wierszy **poprawnych**, sformatowaną do dwóch miejsc po przecinku,
- **TOP 3 klientów** wg sumy zamówień — liczone tak jak w `top_customers` z części A
  (tylko `paid`, klienci bez nazwy pomijani), numerowane 1–3,
- **liczbę zamówień w każdym statusie**, posortowaną malejąco (przy remisie alfabetycznie).
  Status pusty pokazuj jako `(brak)`.

Statusy i ranking liczysz z **wszystkich** wierszy pliku, nie tylko z poprawnych.

Raport ma być czytelny dla człowieka, który nie zna Twojego kodu. Formatowanie
(`f-string`, `:.2f`, wyrównanie kolumn) masz z R1 — użyj go.

### 5. Podsumowanie na ekranie

Po wykonaniu program wypisuje krótkie podsumowanie: ile wierszy, ile poprawnych,
ile niepoprawnych i gdzie zapisał wyniki. Trzy–pięć linii. To ma być informacja
dla człowieka, który właśnie uruchomił program, a nie zrzut wszystkiego.

### 6. Struktura

- Program podzielony na **funkcje**. Jedna funkcja = jedna odpowiedzialność.
- Na dole `if __name__ == "__main__":` i wywołanie funkcji startowej.
- **DRY — to jest oceniane najostrzej.** Masz gotowe i przetestowane:

  ```python
  from src.powtorka_05_pliki_csv.exercises import ensure_dir, read_csv_rows, write_csv_rows
  from src.powtorka_06_sortowanie.exercises import top_customers
  ```

  Jeśli zobaczę w `raport.py` własne `csv.DictReader`, `csv.DictWriter` albo `sorted()`
  z `lambda`, to znaczy, że napisałeś drugi raz coś, co już masz. **To jest główne
  kryterium tego zadania.** Pisz tylko to, czego jeszcze nie masz: walidację wiersza,
  liczenie statusów, składanie tekstu raportu i sklejenie całości.

---

## Tabela kontrolna — tym się sprawdzisz

Nie ma testów, więc weryfikujesz się sam. Uruchomiłem wzorcową implementację na tym
pliku i to są liczby, które muszą Ci wyjść:

| Co | Ile |
|----|-----|
| wierszy wczytanych | **16** |
| poprawnych | **10** |
| niepoprawnych | **6** |
| suma kwot z poprawnych | **2254.50** |

**Niepoprawne wiersze to dokładnie te `order_id`:**
`3008`, `3009`, `3010`, `3011`, `3014`, `3016`

Jeśli masz inny zestaw — masz błąd w walidacji. Otwórz te wiersze w pliku i sprawdź,
który warunek każdy z nich łamie. Umiesz to uzasadnić dla każdego z sześciu? Dobrze.

**TOP 3 klientów:**

| # | Klient | Suma |
|---|--------|------|
| 1 | Anna Kowalska | 250.00 |
| 2 | Piotr Nowak | 250.00 |
| 3 | Zielińska, Maria | 250.00 |

Trzy razy 250.00 to nie przypadek — plik jest tak zbudowany celowo, żeby sprawdzić,
czy Twoje rozstrzyganie remisu działa. Kolejność alfabetyczna jest tu jedynym poprawnym
wynikiem. Gdyby wyszło `Zielińska, Piotr, Anna` — masz `reverse=True` zamiast minusa.

**Statusy:**

| Status | Ile |
|--------|-----|
| paid | 12 |
| (brak) | 1 |
| cancelled | 1 |
| pending | 1 |
| shipped | 1 |

Zwróć uwagę na kolejność: `paid` ma najwięcej, a cztery pozostałe mają po 1 i są
ułożone alfabetycznie. `(brak)` przed `cancelled`, bo nawias ma niższy kod niż litera.

---

## Jak w ogóle zacząć, gdy plik jest pusty

Nie zaczynaj od pisania kodu. To jest najczęstszy błąd i kosztuje najwięcej czasu.

**Krok 1 — wypisz na kartce przepływ danych.** Dosłownie strzałkami:

```
orders.csv -> wczytaj -> podziel na dwie kupki -> zapisz dwa CSV
                             |
                             +-> policz statusy -> zbuduj tekst -> zapisz raport.txt
```

**Krok 2 — z każdej strzałki zrób jedną funkcję.** Nazwij ją i zapisz, co przyjmuje
i co zwraca. Nadal na kartce, nadal bez kodu.

**Krok 3 — napisz szkielet z samymi `pass`** i wywołaniami w funkcji startowej.
Uruchom. Ma się wykonać i nic nie zrobić — ale bez błędu.

**Krok 4 — wypełniaj po jednej funkcji, uruchamiając po każdej.** Nie pisz całości
i nie odpalaj na końcu. Pisz najmniejszy kawałek, który da się sprawdzić, i sprawdzaj.

**Krok 5 — po każdej funkcji zerknij do tabeli kontrolnej.** Wypisz liczbę na ekran
i porównaj. To jest Twój zamiennik `pytest` w tym zadaniu.

To nie jest ceremoniał dla początkujących. Tak się pisze programy, których kształtu
się jeszcze nie zna — a to jest większość programów.

---

## Jak to ocenię

Nie ma testów, więc podaję kryteria z góry. Review będzie po tych punktach:

| Kryterium | Co sprawdzam |
|-----------|--------------|
| **DRY** | czy wołasz funkcje z R5 i R6, zamiast pisać je drugi raz |
| **Poprawność** | czy liczby zgadzają się z tabelą kontrolną |
| **Podział na funkcje** | czy jedna funkcja robi jedną rzecz i da się ją zrozumieć bez czytania reszty |
| **Ścieżki** | stałe na górze, liczone od `__file__`, `output/` tworzony automatycznie |
| **Nazwy** | po angielsku, mówiące co to jest (`valid_orders`, nie `lista2`) |
| **Czystość** | `ruff check` przechodzi, brak spacji na końcach linii, brak martwego kodu |
| **Raport** | czy człowiek, który nie zna kodu, zrozumie wynik |

Czego **nie** oceniam: czy wybrałeś te same nazwy funkcji co ja, czy podzieliłeś to na
cztery funkcje czy siedem. To są Twoje decyzje i różne odpowiedzi są dobre.

---

## Checklista przed zgłoszeniem

- [ ] `uv run python -m src.powtorka_06_sortowanie.raport` działa z katalogu głównego repo
- [ ] działa też, gdy uruchomisz go stojąc w innym katalogu
- [ ] `output/valid_orders.csv` — 10 wierszy danych + nagłówek
- [ ] `output/invalid_orders.csv` — 6 wierszy danych + nagłówek
- [ ] `output/raport.txt` — czytelny, z TOP 3 i statusami
- [ ] wszystkie liczby zgadzają się z tabelą kontrolną
- [ ] otworzyłeś oba CSV i raport **oczami** i sprawdziłeś, czy wygląda sensownie
- [ ] `uv run ruff check src/powtorka_06_sortowanie/` przechodzi
- [ ] w `raport.py` nie ma ani jednego `csv.DictReader`, `csv.DictWriter` ani `sorted(`
- [ ] wypełniona tabela „Część B" w `notes/powtorka-06-sortowanie.md`

---

## Jeśli utkniesz

Reguła 20 minut obowiązuje tak samo jak przy zadaniach z testami — **z jedną różnicą**:
zanim zapytasz, napisz mi, **na czym dokładnie stoisz**. Nie „nie działa", tylko
„mam podział na funkcje taki i taki, utknąłem na tym, jak przekazać X do Y".

Tu nie ma czerwonego testu, który powie za Ciebie, co jest nie tak. Umiejętność
nazwania własnego problemu jest częścią tego zadania — i szczerze mówiąc, jest
jedną z rzeczy, które najbardziej widać na rozmowie o pracę.
