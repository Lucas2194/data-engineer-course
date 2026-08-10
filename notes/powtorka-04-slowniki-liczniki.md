# Powtórka R4 — Słowniki jako liczniki i agregatory (`.items()`)

**Cel:** zamienić **wiele rekordów** w jedno **podsumowanie** — ile czego jest,
ile kto wydał, co się powtarza. To jest w Pythonie to samo, co `GROUP BY` w SQL:
grupujesz dane i coś dla każdej grupy liczysz. Codzienna robota data engineera.

Cztery klocki:
1. **słownik jako licznik** — `{klucz: ile razy}`, wzorzec `.get(k, 0) + 1`,
2. **normalizacja przed liczeniem** — żeby `" PAID "`, `"Paid"`, `"paid"` był JEDNYM koszykiem,
3. **słownik jako agregator** — `{klucz: suma}`, dokładasz do wartości zamiast liczyć,
4. **`.items()`** — chodzenie po parach (klucz, wartość), żeby coś z gotowego słownika odczytać.

R4 stoi na R2 i R3. Kwoty konwertujesz bezpiecznie (`to_float` z R2 masz gotowe na górze
pliku), a pętle i pomijanie brudnych rekordów znasz z R3. Nowość: **wynikiem jest słownik**,
nie lista.

---

## 1. Słownik jako licznik — wzorzec `.get(k, 0) + 1`

Chcesz policzyć, ile razy pojawia się każda wartość. Zaczynasz od **pustego słownika**
i dla każdego elementu podbijasz jego licznik o 1:

```python
liczniki = {}                              # 1. pusty slownik NA START
for item in ["a", "b", "a", "a"]:
    liczniki[item] = liczniki.get(item, 0) + 1   # 2. podbij licznik o 1
return liczniki                            # -> {"a": 3, "b": 1}
```

Sedno to `liczniki.get(item, 0) + 1`. Czytasz to: „weź obecny licznik dla `item`
(a jak go jeszcze nie ma — potraktuj jak `0`), dodaj 1, i zapisz z powrotem".
`.get(item, 0)` to Twój bezpieczny dostęp z R2 — dzięki `0` jako domyślnej nie
wybuchniesz przy pierwszym wystąpieniu klucza.

---

## 2. Normalizacja przed liczeniem

Dane są brudne (R2). Status `"paid"`, `" PAID "` i `"Paid"` to **ten sam** status —
ale dla Pythona to trzy różne teksty, więc policzyłby je jako trzy osobne koszyki.
Zanim policzysz, musisz je **ujednolicić**:

```python
def normalize_status(text):
    return text.strip().lower()     # " PAID " -> "paid",  "Paid" -> "paid"
```

`.strip()` obcina spacje z brzegów (R1), `.lower()` daje małe litery (R1). Łączysz je
w łańcuszek: najpierw `.strip()`, potem na wyniku `.lower()`. Dopiero **znormalizowany**
tekst wrzucasz do licznika — inaczej podsumowanie jest błędne.

---

## 3. Pomijanie brudnych rekordów

Niektóre zamówienia nie mają statusu w ogóle, albo mają pusty. Takie **pomijasz**
(jak w R3 — po prostu nie trafiają do wyniku):

```python
liczniki = {}
for order in orders:
    status = order.get("status")        # None, gdy klucza nie ma
    if status is None:                  # brak klucza -> pomijamy
        continue
    status = normalize_status(status)   # .strip().lower()  (REUŻYWASZ #2)
    if status == "":                    # pusty lub same spacje -> pomijamy
        continue
    liczniki[status] = liczniki.get(status, 0) + 1
return liczniki
```

**Znów kolejność (jak w R3):** najpierw `status is None`, DOPIERO POTEM
`normalize_status(status)` — bo `None.strip()` by wybuchło. `continue` mówi „pomiń ten
element i skocz do następnego obrotu pętli".

---

## 4. Słownik jako agregator — sumowanie zamiast liczenia

Licznik dodaje `+ 1`. Agregator dodaje **wartość** — np. sumujesz kwoty per klient:

```python
sumy = {}
for order in orders:
    name = order.get("customer_name", "").strip()
    if name == "":                      # klient bez nazwy -> pomijamy
        continue
    kwota = to_float(order.get("total_amount"))   # bezpiecznie (R2); None gdy smiec
    if kwota is None:
        kwota = 0.0                     # smiec traktujemy jak 0
    sumy[name] = sumy.get(name, 0) + kwota   # DOKLADASZ kwote do dotychczasowej sumy
return sumy                             # -> {"Anna": 150.0, "Piotr": 120.0}
```

To ten sam szkielet co licznik, tylko `+ 1` zamieniasz na `+ kwota`.
`sumy.get(name, 0)` daje dotychczasową sumę klienta (albo `0`, gdy widzisz go pierwszy raz).

---

## 5. `.items()` — chodzenie po parach (klucz, wartość)

Gdy masz gotowy słownik i chcesz go **przeczytać** — przejść po wszystkich parach —
używasz `.items()`. Rozpakowujesz parę na dwie zmienne:

```python
sumy = {"Anna": 150.0, "Piotr": 120.0}
for name, total in sumy.items():        # name = klucz, total = wartosc
    print(f"{name} wydal {total}")
```

`for name, total in sumy.items():` — w każdym obrocie `name` to klucz, `total` to wartość.
To Twoje okno do odczytu słownika.

---

## 6. Znalezienie maksimum przez `.items()`

Chcesz klienta z najwyższą sumą. Idziesz po `.items()` i **pamiętasz najlepszego
do tej pory**:

```python
best_name = None
best_total = None
for name, total in sumy.items():
    if best_total is None or total > best_total:   # pierwszy ALBO lepszy
        best_name = name
        best_total = total
return best_name, best_total            # krotka (name, total)
```

Warunek `best_total is None or total > best_total`: pierwszy klient zawsze zostaje
zapisany (bo `best_total` jest jeszcze `None`), a każdy kolejny — tylko gdy pobił rekord.
Gdy słownik był pusty, pętla nic nie zrobi i `best_name` zostanie `None`.

---

## 7. Demo — URUCHOM to najpierw

```
uv run python -m src.powtorka_04_slowniki_liczniki.demo
```

Zobaczysz na żywo licznik, normalizację, agregator sum i chodzenie po `.items()`.
Kod dema jest w `src/powtorka_04_slowniki_liczniki/demo.py` — przeczytaj go.

---

## 8. Zadania

Plik: `src/powtorka_04_slowniki_liczniki/exercises.py`. Na górze masz **gotowe**
`to_float` (nie zmieniaj — używaj). Niżej pięć funkcji z `pass`. Jedna klasa naraz:

```
uv run pytest tests/test_powtorka_04.py::TestCountItems -v
```

| # | Funkcja | Co ćwiczy |
|---|---------|-----------|
| 1 | `count_items` | słownik jako licznik: `.get(k, 0) + 1` |
| 2 | `normalize_status` | helper: `.strip().lower()` |
| 3 | `count_statuses` | payoff diag: licznik + normalizacja + pomijanie (**reuse #2**) |
| 4 | `sum_by_customer` | słownik jako agregator: sumy per klient (**reuse `to_float`**) |
| 5 | `highest_spender` | `.items()` + znalezienie maksimum (**reuse #4**) |

**Reguła 20 minut** obowiązuje. **Test to prawda**. **DRY** — #3 użyj #2, #5 użyj #4,
w #4 użyj `to_float`. Zapisuj wynik konwersji do zmiennej i jej używaj — nie licz dwa razy
(pamiętasz uwagę z R3).

---

## Wyniki (wypełniaj na bieżąco)

| # | Funkcja | Bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|-------------|------------|---------------------|
| 1 | `count_items` | | | |
| 2 | `normalize_status` | | | |
| 3 | `count_statuses` | | | |
| 4 | `sum_by_customer` | | | |
| 5 | `highest_spender` | | | |

**Co wróciło od razu:**

**Co dalej sprawia problem:**

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| to count | liczyć (wystąpienia) | `licznik.get(k, 0) + 1` |
| to aggregate / aggregation | agregować, agregacja | sumowanie kwot per klient |
| to normalize | znormalizować, ujednolicić | `.strip().lower()` |
| to sum up | zsumować | `suma = suma + kwota` |
| key-value pair | para klucz-wartość | `for k, v in d.items():` |
| counter | licznik | `{"paid": 3, "pending": 1}` |
| to skip | pominąć | `continue` przy brudnym rekordzie |
