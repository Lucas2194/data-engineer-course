# Powtórka R1 — Stringi i formatowanie

**Cel:** odświeżyć trzy mechaniczne umiejętności, na których stoi zadanie #1 z diagnostyki
(`format_order_summary`) i normalizacja z zadania #4 (`count_statuses`):

1. **f-string** — sklejanie tekstu z wartościami,
2. **format spec `:.2f`** — wymuszenie dwóch miejsc po przecinku,
3. **metody stringów** — `.strip()`, `.lower()`, `.upper()`.

To są klocki. Gdy każdy z osobna wejdzie w palce, `format_order_summary` przestanie być
"trudnym zadaniem" i stanie się złożeniem trzech rzeczy, które znasz.

---

## 1. F-string — sklejanie tekstu z wartościami

Do tej pory pewnie sklejałeś tekst plusem:

```python
imie = "Anna"
print("Czesc, " + imie + "!")     # dziala, ale meczace przy wielu wartosciach
```

**F-string** to ten sam efekt, czytelniej. Stawiasz literę `f` przed cudzysłowem,
a wartości wkładasz w `{ }` **wprost w tekście**:

```python
imie = "Anna"
print(f"Czesc, {imie}!")          # Czesc, Anna!
```

W `{ }` może być nie tylko zmienna — może być **wyrażenie**:

```python
a = 2
b = 3
print(f"{a} + {b} = {a + b}")     # 2 + 3 = 5
```

To jest sposób, którego będziesz używał codziennie: budowanie komunikatów, ścieżek,
linii raportu. Zapomnij o sklejaniu plusem.

---

## 2. Format spec `:.2f` — dwa miejsca po przecinku ZAWSZE

Problem, który Cię ugryzł w diagnostyce: liczba `149.5` wyświetla się jako `149.5`,
a Ty potrzebujesz `149.50`. Python domyślnie nie dokleja zer na końcu.

Rozwiązanie: wewnątrz `{ }` po **dwukropku** podajesz *jak* sformatować wartość.
Zapis `:.2f` znaczy: "pokaż jako liczbę zmiennoprzecinkową (`f`) z dokładnie dwoma
miejscami po przecinku (`.2`)".

```python
cena = 149.5
print(f"{cena:.2f}")              # 149.50   <- dopchnięte zero
print(f"{89.0:.2f}")             # 89.00
print(f"{3.14159:.2f}")          # 3.14     <- obcięte do dwóch miejsc (zaokrągla)
```

Sam dwukropek `:` mówi: "teraz podam instrukcję formatowania". To, co po nim,
nazywa się **Format Specification Mini-Language** — to jest to hasło, którego
kazałem Ci szukać w dokumentacji. Na razie potrzebujesz tylko `:.2f`.

> **Pułapka:** `:.2f` to nie to samo co `round()`. `round(149.5, 2)` da liczbę `149.5`
> (bez doklejonego zera). `:.2f` daje **tekst** `"149.50"`. Do wyświetlania — format spec.

---

## 3. Metody stringów — `.strip()`, `.lower()`, `.upper()`

Metoda to funkcja "przyklejona" do wartości, wołasz ją kropką: `tekst.metoda()`.

**`.strip()`** — obcina białe znaki (spacje, tabulatory) z **obu brzegów**.
Środka nie rusza.

```python
"  Piotr  ".strip()              # "Piotr"
"Anna".strip()                    # "Anna"   (nie ma co obcinać — bez zmian)
"   ".strip()                     # ""       (same spacje -> pusty tekst)
```

**`.lower()` / `.upper()`** — zamieniają wielkość liter.

```python
"PAID".lower()                    # "paid"
"paid".upper()                    # "PAID"
"Pending".lower()                 # "pending"
```

**Kluczowa własność:** metody stringów **niczego nie zmieniają w miejscu** — one
**zwracają nowy tekst**. String w Pythonie jest niezmienny. Dlatego to nie działa:

```python
tekst = "  PAID  "
tekst.strip()                     # wynik wyrzucony w powietrze!
print(tekst)                      # nadal "  PAID  "

tekst = tekst.strip()             # <- TAK. Przypisujesz wynik z powrotem.
```

**Łączenie metod** (bardzo częste — normalizacja statusu z zadania #4):

```python
" PAID ".strip().lower()          # "paid"
```

Czytasz od lewej: weź `" PAID "`, obetnij spacje → `"PAID"`, zamień na małe → `"paid"`.
Dokładnie to znaczy zdanie z diagnostyki: *" PAID ", "Paid" i "paid" to TEN SAM status*.

---

## 4. Wszystko razem — jak powstaje linia zamówienia

Zadanie #1 z diagnostyki to złożenie trzech powyższych klocków:

```python
order_id = 2
name = "  Piotr Nowak  "
amount = 89.0

linia = f"Zamowienie #{order_id} | {name.strip()} | {amount:.2f} PLN"
#          |            |          |                 |
#          tekst        wartość    metoda w {}       format spec w {}
# -> "Zamowienie #2 | Piotr Nowak | 89.00 PLN"
```

Zwróć uwagę: `name.strip()` i `amount:.2f` **dzieją się wprost w f-stringu**.
Nie musisz robić tego w osobnych linijkach (choć możesz, jeśli tak czytelniej).

---

## 5. Demo — URUCHOM to najpierw

Zanim ruszysz zadania, odpal gotowy, działający przykład i **przeczytaj go powoli**:

```
uv run python -m src.powtorka_01_stringi.demo
```

Zobaczysz wydruk krok po kroku: f-stringi, `:.2f` i metody stringów w akcji.
Kod tego dema jest w `src/powtorka_01_stringi/demo.py` — zajrzyj, jest cały napisany
i skomentowany. Niczego w nim nie rozwiązujesz.

---

## 6. Zadania

Plik: `src/powtorka_01_stringi/exercises.py` — pięć funkcji, każda z `pass` w środku.
Twoja robota: zamień `pass` na kod, aż testy zzielenieją.

Pracuj **jedną klasą naraz**, od góry:

```
uv run pytest tests/test_powtorka_01.py::TestCleanText -v
```

Wszystkie naraz (dopiero na koniec, do sprawdzenia):

```
uv run pytest tests/test_powtorka_01.py -v
```

Kolejność (łatwe → trudniejsze):

| # | Funkcja | Co ćwiczy |
|---|---------|-----------|
| 1 | `clean_text` | `.strip()` |
| 2 | `normalize_status` | `.strip().lower()` (łączenie metod) |
| 3 | `format_amount` | format spec `:.2f` |
| 4 | `format_order_line` | złożenie wszystkiego (to jest zadanie #1 z diagnostyki) |
| 5 | `initials` | `.split()`, indeksowanie, `.upper()` (stretch) |

**Reguła 20 minut** dalej obowiązuje: zacinasz się dłużej → pytasz. I jak zawsze —
**gdy docstring i test się różnią, wierzysz testowi.**

---

## Wyniki (wypełniaj na bieżąco)

| # | Funkcja | Bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|-------------|------------|---------------------|
| 1 | `clean_text` | TAK | | |
| 2 | `normalize_status` | | | |
| 3 | `format_amount` | | | |                  Odniosę się do wszystkich. Dałem radę, z lekką pomocą Claude. 
| 4 | `format_order_line` | | | |
| 5 | `initials` | | | |

**Co wróciło od razu:**

**Co dalej sprawia problem:**

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| f-string / formatted string literal | dosłowny łańcuch formatowany | `f"{x}"` |
| format specifier | specyfikator formatu | `:.2f` |
| to strip | obcinać (białe znaki) | `.strip()` |
| lowercase / uppercase | małe / wielkie litery | `.lower()` / `.upper()` |
| immutable | niezmienny | string nie zmienia się w miejscu |
| to trim whitespace | przyciąć białe znaki | to samo co `.strip()` |
