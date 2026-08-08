# Powtórka R3 — Listy i pętle: filtrowanie, budowanie, walidacja

**Cel:** przetworzyć **wiele** rekordów naraz — przejść pętlą po liście, odsiać śmieci
i zbudować z tego nową, czystą listę. To jest codzienna robota data engineera: rzadko
masz jeden rekord, prawie zawsze masz ich tysiące.

Cztery klocki:
1. **budowanie nowej listy** — pusta lista + pętla + `.append()`,
2. **filtrowanie** — pętla + `if` — przepuszczasz tylko to, co spełnia warunek,
3. **try/except w pętli** — jeden zepsuty rekord nie może zabić całej pętli,
4. **walidacja** — sprawdzasz, czy rekord ma wszystko, czego wymagasz.

R3 stoi na R2. Kwoty wciąż konwertujesz i łapiesz wyjątki — tylko teraz robisz to
**dla każdego elementu listy po kolei.** `to_float` z R2 dostajesz gotowe na górze
pliku z zadaniami — **masz go używać, nie pisać od nowa** (pamiętasz DRY z R2).

---

## 1. Pętla `for` — robisz coś dla każdego elementu

```python
for liczba in [10, 20, 30]:
    print(liczba)      # 10, potem 20, potem 30
```

Czytasz to: „weź po kolei każdy element listy, nazwij go `liczba`, i wykonaj blok".
Zmienna `liczba` w każdym obrocie pętli trzyma **inny** element.

---

## 2. Budowanie nowej listy — wzorzec akumulatora

Najważniejszy wzorzec w tej pracy. Zaczynasz od **pustej listy** i **dokładasz** do niej:

```python
wynik = []                     # 1. pusta lista NA START
for liczba in [10, 20, 30]:
    wynik.append(liczba * 2)   # 2. dokładaj do niej w pętli
return wynik                   # 3. oddaj gotową listę -> [20, 40, 60]
```

Trzy kroki, zawsze te same: **pusta lista → pętla z `.append()` → return**.
`.append(x)` dokłada `x` na koniec listy. To Twój młotek na resztę R3.

**Uwaga na wcięcia:** `return wynik` jest na poziomie funkcji (poza pętlą). Gdyby
wpadło do środka pętli, funkcja skończyłaby się po pierwszym obrocie. Wcięcie decyduje.

---

## 3. Filtrowanie — przepuszczasz tylko to, co spełnia warunek

Dokładasz do listy **tylko wtedy**, gdy element przejdzie `if`:

```python
wynik = []
for liczba in [5, -3, 0, 10]:
    if liczba > 0:             # tylko dodatnie
        wynik.append(liczba)
return wynik                   # -> [5, 10]  (-3 i 0 odpadły)
```

To, co nie przejdzie `if`, **po prostu nie trafia** do wyniku. Nie zamieniasz go na
zero, nie zostawiasz dziury — go tam nie ma. Element `0` odpada, bo `0 > 0` to fałsz.

---

## 4. try/except w pętli — jeden zepsuty rekord nie zabija reszty

Dane są brudne (R2). W pętli po tysiącu kwot jedna będzie `"abc"`. Bez obsługi
wyjątku `float("abc")` wywala **całą** pętlę — i tracisz też 999 dobrych rekordów.

Masz gotowe `to_float` z R2 — zwraca liczbę albo `None` (zamiast wybuchać). Używasz go
tak, że **sprawdzasz wynik** i pomijasz `None`:

```python
wynik = []
for value in ["12.5", "abc", 30, None]:
    liczba = to_float(value)   # liczba ALBO None - nigdy nie wybucha
    if liczba is not None:     # udało się skonwertować?
        wynik.append(liczba)
return wynik                   # -> [12.5, 30.0]  ("abc" i None odpadły)
```

**`is not None`, nie `!= 0`.** Gdybyś napisał `if liczba:`, to prawidłowa kwota `0.0`
odpadłaby (bo `0.0` jest „fałszywe" — pamiętasz truthiness z R2). Rozróżniasz „nie dało
się skonwertować" (`None`) od „skonwertowało się na zero" (`0.0`). To dwie różne rzeczy.

---

## 5. Dwa warunki naraz

Kwota jest dobra, gdy **jednocześnie**: da się skonwertować **oraz** jest > 0.
Łączysz warunki słowem `and`:

```python
liczba = to_float(value)
if liczba is not None and liczba > 0:
    wynik.append(liczba)
```

Kolejność ma znaczenie: **najpierw** `is not None`, **potem** `> 0`. Gdyby `liczba`
było `None`, to `None > 0` by wybuchło. Ale Python sprawdza warunki od lewej i gdy
pierwszy jest fałszem (`None is not None` → fałsz), **drugiego już nie sprawdza**.
To się nazywa short-circuit. Dlatego bezpieczny warunek stawiasz jako pierwszy.

---

## 6. Walidacja słownika — wszystkie wymagane pola muszą być OK

Sprawdzasz, czy zamówienie ma komplet wymaganych pól. Reguła: **wystarczy, że JEDNO
pole zawiedzie, i całość jest niepoprawna.** Wzorzec „wszystkie muszą przejść":

```python
def is_valid_order(order, required_keys):
    for key in required_keys:
        if key not in order:          # brak klucza -> od razu źle
            return False
        value = order[key]
        if value is None:             # None -> źle
            return False
        if value.strip() == "":       # pusty lub same spacje -> źle
            return False
    return True                       # przeszły WSZYSTKIE -> dobre
```

Czytasz to: „lecę po wymaganych kluczach; przy pierwszym, który zawiedzie, **od razu**
zwracam `False` i wychodzę. Jeśli pętla doszła do końca bez wyjścia — znaczy, że
wszystkie przeszły, więc `True`".

**Znów kolejność:** najpierw sprawdzasz `key not in order` i `value is None`, a `.strip()`
wołasz **dopiero potem** — bo `None.strip()` by wybuchło. Bezpieczne sprawdzenia idą
przed tymi, które mogą paść na złej wartości.

---

## 7. Dwie listy naraz + zwracanie krotki

Czasem dzielisz dane na dwie kupki. Budujesz **dwie** listy i oddajesz **obie**:

```python
def split_valid_invalid(orders, required_keys):
    valid = []
    invalid = []
    for order in orders:
        if is_valid_order(order, required_keys):   # REUŻYWASZ #4, nie przepisujesz!
            valid.append(order)
        else:
            invalid.append(order)
    return valid, invalid          # dwie wartości naraz -> to jest krotka (tuple)
```

`return a, b` oddaje **krotkę** dwóch list. Wołający rozpakuje ją: `dobre, zle = split_...`.
Zauważ: nie przepisujesz tu logiki walidacji — wołasz `is_valid_order` z zadania #4.
**To jest DRY.** Zbudowałeś klocek → używasz klocka.

---

## 8. Demo — URUCHOM to najpierw

```
uv run python -m src.powtorka_03_listy_petle.demo
```

Zobaczysz na żywo budowanie listy, filtrowanie, try/except w pętli i walidację.
Kod dema jest w `src/powtorka_03_listy_petle/demo.py` — przeczytaj go.

---

## 9. Zadania

Plik: `src/powtorka_03_listy_petle/exercises.py`. Na górze masz **gotowe** `to_float`
(nie zmieniaj — używaj). Niżej pięć funkcji z `pass`. Jedna klasa naraz, od góry:

```
uv run pytest tests/test_powtorka_03.py::TestKeepPositive -v
```

| # | Funkcja | Co ćwiczy |
|---|---------|-----------|
| 1 | `keep_positive` | szkielet: pusta lista + pętla + `if` + `append` |
| 2 | `to_float_list` | konwersja w pętli, pomijanie `None` (**reuse `to_float`**) |
| 3 | `filter_valid_amounts` | payoff diag: konwersja **i** `> 0` razem |
| 4 | `is_valid_order` | walidacja jednego słownika: „wszystkie muszą przejść" |
| 5 | `split_valid_invalid` | payoff diag: dwie listy, krotka (**reuse `is_valid_order`**) |

**Reguła 20 minut** obowiązuje. **Test to prawda** — gdy docstring i test się różnią,
wierzysz testowi. **DRY** — jak piszesz drugi raz tę samą logikę, użyj funkcji z góry.

---

## Wyniki (wypełniaj na bieżąco)

| # | Funkcja | Bez pomocy? | Czas (min) | Co sprawiło problem |
|---|---------|-------------|------------|---------------------|
| 1 | `keep_positive` | | | |
| 2 | `to_float_list` | | | |
| 3 | `filter_valid_amounts` | | | |
| 4 | `is_valid_order` | | | | To zadanie sprawiło mi duże problemy, nei mogłem się skupić, wydaje mi się, że wcześniej robiłem to zupełenie inaczej w moich notatkach i zadanich. Tutaj jakby, nie mogłem troszkę tego pojąć. 
| 5 | `split_valid_invalid` | | | | No tutaj łatwe zadanie, ale to is_valid_order sprawiło mi trudności, chociaż wcześniej przychodziło mi zrobienie tego zadania łatwo. 

**Co wróciło od razu:**

**Co dalej sprawia problem:**

---

## Słowniczek (dopisz do `notes/english/glossary.md`)

| EN | PL | Gdzie to widzisz |
|----|----|------------------|
| to loop / to iterate | iterować, przechodzić w pętli | `for order in orders:` |
| to append | dołączyć na koniec | `wynik.append(x)` |
| to filter | filtrować, odsiewać | `if liczba > 0:` |
| to build a list | zbudować listę | pusta lista + `.append()` |
| to validate | walidować, sprawdzać poprawność | `is_valid_order(...)` |
| tuple | krotka | `return valid, invalid` |
| to skip | pominąć | element, który nie przeszedł `if` |
