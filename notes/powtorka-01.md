# Zaczynamy małą powtórkę 

## Format spec `:.2f` - dwa miejsca po przecinku ZAWSZE

```python

cena = 149.50

print(f"{cena:.2f}")    # < - Dopchnięte zero 149.50
print(f"{89.0:.2f}")    # <- To samo 89.00
print(f"{3.14159:.2f}") # <- Obcięcie dwóch miejsc ( zaokrągla) 3.14

```

Sam dwukropek `:` mówi: "Teraz podam instrukcję formatowania". To co po nim, nazywa się **Format Specification Mini-Language** - `:.2f` 

> **Pułapka:** `:.2f` to nie to samo co `round()`. `round(148.5, 2)` da liczbę `148.5` bez doklejonego zera. 
> `:.2f` daje -> `149.50`. Do wyświetlania - format spec

## Metody stringów - `.strip()`, `lower()`, `upper()`

Metoda to funkcja przyklejona do wartości, wywołuja się ją kropką: `tekst.metoda()`.

** `.strip()` ** - obcina białe znaki (spacje, tabulatory) z **obu brzegów**. Środka nie rusza 

```python

"  Piotr ".strip() # "Piotr"
"Anna".strip() # "Anna" nie ma co obcinać, pozostaje bez zmian 
"   ".strip() # "" - pozostwia pusty string 
```
**`.lower()` / `.upper()`** - zmiają wielkość liter.

```python

"PAID".lower() # "paid"
"paid".upper() # "PAID"
"Pending".lower() #"pending 
```

**Kluczowa własność** metody stringów **niczego nie zmieniają w miejscu** - one **zwracają nowy tekst**.String w Pythonie jest niezmienny. Dlatego to nie działa:

```python

tekst = "  PAID  " 
tekst.strip() # Wynik wyrzucony w powietrze! 
print(tekst) # nadal "  PAID  "

tekst = tekst.strip*() # <- TAK. Przypisujesz wynik z powrotem 

```

**Łączenie metod** (bardzo często - normalizacja statusu z zadani #4):

```python

"  PAID  ".strip().lower()    #"paid"
```

Czytasz od lewej: weź `"  PAID  "`, obetnij spacje, zmień na małe

## Wszystko razem  

```python 

order_id = 2