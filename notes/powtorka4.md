# Powtórka R4 - czyli słowniki jako liczniki i agregatory 

**Cel** Zmienić wiele rekordów, w jedno podsumowanie - ile czego jest, ile kto wydał, co się powtarza. To jest w Pythonie to samo, co `GROUP BY` w SQL. Grupujesz dane i coś dla każej grupy liczysz. Codzienna robota data enginerra. 

Cztery klocki 

1. **słownik jako licznik** - `{klucz: ile_razy}` wzorzec `.get(k,0) + 1`
2. **normalizacja przed liczeniem** - żeby `"  PAID  "` , `"Paid"`, `"paid"` było JEDNYM koszykiem.
3. **słownik jako agregator** `{klucz:suma}` - dokłdasz do wartośći, zamiast liczyc
4. **`.items()`** - chodzenie po parach (klucz, wartość) żeby coś z gotowego słownika odczytać.

r4 stoi na r2 i r3. Kwoty konwertujesz bezpieczenie (`to_float` z R2 jest gotowe) a pętle i pomijanie brudnych rekordów znasz z R3. Nowością będzie to, że wynikiem jest słownik, nie lista. 

## 1. Słownik jako licznik - wzorzec `.get(k, 0) + 1`

Jeśli chcesz policzyć, ile razy pojawia się każda wartość, zaczynamy od pustego słownika i dla każdego elementu podbijasz jego licznik o 1: 

```python

licznik = {}

for item in ["a", "b", "a", "a"]:
    licznik[item] = licznik.get(item,0) + 1
return licznik
```

Sedno to `licznik.get(item, 0) + 1`. Czytam to: weź obecny licznik dla `item` ( a jak go jeszcze nie ma, potraktuj jak `0`), dodaj 1 i zapisz z powrotem.
`.get(item, 0)` to funkcja, bezpiecznego dostępu przypomniena sobie z R2. Dzięki `0` jako domyślnej, nie wybuchnie przy pierwszym wystąpieniu klucza.

## 2. Normalizacja przed liczeniem

Dane są brudne. Status `"paid"`, `"  PAID  "` i `"Paid"` to **ten sam** status, ale dla Pythona, to trzy różne tekstu, więc policzy je, jako trzy osobne koszyki. Zanim je zliczymy, trzeba je ujednolicić.

```python

def normalize_status(text):
    return text.strip().lower()

```

`.strip()` obcina spacje z brzegów, `.lower()` daje małe litery. 

## 3. Pomijanie brudnych rekordów. 

Niektóre zamówienia nie mają statusu w ogóle, albo mają pusty. Takie trzeba **pomijać** 

```python

liczniki = {}
for order in orders:
    status = order.get("status")
    if status is None:        # brak klucza -> pomijamy 
        continue
    status = normalize_status(status)
    if status == "":    # pusty albo same spacje - > pomijamy
        continue
    licznik[status] = licznik.get(status, 0) + 1
return liczniki

```

**Kolejność** - najpierw `status is None`, dopiero potem `normalize_status(status)` bo `None.strip()` by wybuchło. 
**`continue`** mówi, pomiń ten element i skocz następnego obrotu pętli 

---

## 4. Słownik jako agregator - sumowanie zamisat liczenia

licznik dodaje ` +1 `. Agregator dodaje **wartość** - np. sumujesz kwoty per klient

```python
sumy = {}
for order in orders:
    name = order.get("customer_name", "").strip()
    if name == "":                     # klient bez nazwy -> pomijamy
        continue
    kwota = to_float(order.get("total_amount"))
    if kwota is None:
        kwota = 0.0                   # śmiec trakujemy jako 0
    sumy[name] = sumy.get(name, 0) + kwota # Dokładasz kwotę do dotychczasowej sumy {"Anna":150.0, "Piotr":120.0}
return sumy
```

To ten sam szkielet co licznik tylko `+1` zmieniasz na `+kwota`. 
`sumy.get(name,0)`, daje dotychczasową sumę klienta (albo `0`, gdy widzisz go pierwszy raz).

## 5. `.items()` - chodzenie po parach (klucz, wartość)

Gdy mam gotowy słownik i chce przejść przez wszystkie pary w tym słowniku używam `.items()`. Rozpakowuje pary na dwie zmienne : 

```python
sumy = {"Anna": 150.0, "Piotr":120.0}
for name, total in sumy.items():
    print(f"{name} wydał {total:.2f}")
```

`for name, total in sumy.items():` - w każdym obrocie `name` to klucz, `total` to wartość. To Twoje okno odczytu słownika. 

## 6. Znalezienie maksimum przez `.items()`

Chcesz klienta z najwyższą sumą. Idziesz po `.items()` i zapisuje najwyższą do tej pory 

```python
best_name = None
best_total = None 
for name, total in sumy.items():
    if best_total is None or total > best_total:
        best_name = name
        best_total = total 
return best_name, best_total
```

Warunek `best_total is None or total > best_total` : jako pierwszy klient zostaje zapisany bo `best_total` jest jeszcze `None`, a każdy kolejny - tylko gdy jest większy pod poprzedniego. Gdy słownik jest pusty, pętla nic nie zrobi i `best_name` pozostanie `None`. 

---