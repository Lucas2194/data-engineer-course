# Powtórka R3 - listy i pętle : filtrowanie, budowania, walidacja

**Cel:** Przetwarzanie wiele rekordów naraz - przejść pętle po liście, odsiać niepotrzebne wartości, śmieci  zbudować z tego nową, czystą listę. To jest właśnie codzienna praca data engineera : prawie nigdy nie ma jednego rekordu, tylko tysiące 

Cztery klocki 

1. **budowanie nowej listy** - pusta lista + pętla + `.append()`,
2. **filtrowanie** - pętla + `if` - przepuszczenie tylko tych, co speniałają warunek
3. **try/except w pętli** - jeden zepsuty rekord nie może wywalić całej pętli
4. **walidacja** - sprwadzeanie czy rekord ma wszystko, czego wymaga

R3 stoi na R2. Ciągle konwertujesz kwoty, łapiesz wyjątki, tylko obecnie będziemy to robić dla każdego elementu listy pokolei

## Pętla `for` - robisz coś, dla każdego elementu 

```python

for liczba in [10,20,30]:
    print(liczba) # 10, potem 20, potem 30
```

Czytam to tak: weź po kolei każdy element listy, nazwij go `liczba` i wykonaj blok. Zmienna `liczba` trzyma w każdej iteracji **inny** element

---

## 2. Budowanie nowej listy - wzorzec akumulatora

Najważniejszy wzorzec w tej pracy. Zaczynasz od **pustej listy** i **dokładasz** do niej : 

```python

wynik = []

for liczba in [10,20,30]:
    wynik.append(liczba*2)
return wynik 
```

Trzy kroki, zawsze takie same : **pusta lista -> pętla z `append()` -> return ** 
`.append(x)` dokłada `x` na koniec listy

## 3. Filtorwanie - przepuszczenie tylko to, co spełnia warunek 

Dokładasz do listy **tylko wtedy** gdy element przejdzie `if`:

```python

wynik = []

for liczba in [5, -3, 0, 10]:
    if liczba > 0:
        wynik.append(liczba)
return wynik
```

To co nie przejdzie if, po prostu nie trafia do listy wynik. Czyli w tej liście będzie [5, 10]

## 4. try/except w pętli - jeden zepsuty rekord, nie wywali reszty.

Dane najczęściej są brudne. W pętli po tysiącu kwot jedna bęzie `"abc"`. Bez obłusgi wyjątku `float("abc")` wywala całą pętle i tracimy dobrych 1000 rekordów. 

```python

wynik = []

for value in ["12,5", "abc", 30, None]:
    liczba = to_float(value)
    if liczba is not None:
        wynik.append(liczba)
return wynik

```

**`is not None`** nie `!=0`** Gdybym napisał `if liczba:` to prawidłowa kwota `0.0` odpadałaby. 

## 5. Dwa warunki naraz 

Kwota jest dobra, gdy **jednocześnie** da się skonwertować **oraz** jest > 0. Łączymy warunki słowem `and`:

```python

liczba = to_float(Value)
if liczba is not None and liczba > 0:
    wynik.append(liczba)

```

Kolejność ma znaczenie, ponieważ gdybyśmy najpierw sprawdzili czy jest większe od 0, a byłoby None, to program by się wywalił ponieważ nie da się sprawdzić czy None jest większe od 0. Drugiego w takim wypadku już nie sprwadza. To się nazywa short-circuit. Dlatego bezpieczny warunek stawia się jako pierwszy. 

## Walidacja słownika - wszystkie wymagana pola muszą być OK 

Sprawdzamy czy zamówienie ma komplet wymaganych pól. Reguła **Wystarczy że JEDNO pole zawiedzie i całość jest niepoprawna** Wzorzec - > wszystkie muszą przejść : 

```python

def is_valid_order(order, required_keys):
    for key in required_keys:
        if key not in order:
            return False
        value = order[key]
        if value is None:
            return False
        if value.strip() = "":
            return False
    return True

```

Czytamy to tak : lecę po wymaganych kluczach, przy pierwszym który zawiedziec od razu zwracam `False` i wychodzę. Jeśli pętla doszła do końca bez wyjścia, znaczy że wszystkie przeszły więc zwraca `True`. 

**Znów kolejność jest ważna** - najpierw sprawdzamy czy klucz jest w wymaganych kluczach, następnie czy wartość jest , a następnie dopiero strip. 

---

## Dwie listy naraz - zwracanie krotki 

Czasami dzielimy dane na dwue kupki. Budujemy wtedy dwie listy i zwracamy obie 

```python

def split_valid_invalid(orders, required_keys):
    valid = []
    invalid = []

    for order in orders:
        if is_valid_order(order, required_keys):
            valid.append(order)
        else:
            invalid.append(order)
    return valid, invalid
```

`return a,b` - zwraca krotkę dwóch list. Należy ją później rozpakować. 