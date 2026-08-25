# Dzień 15 - Python: import i moduły

## Najważniejsze

- Moduł to plik `.py`, z którego można importować kod.
- Import pozwala używać funkcji z innych plików.
- Podział na moduły porządkuje projekt.
- `main.py` często jest głównym miejscem uruchomienia programu.

## Mini przykład

```python
from validator import is_valid_status

if is_valid_status("paid"):
    print("OK")
```

## Zapamiętaj

- `from module import function` importuje konkretną funkcję.
- `import module` importuje cały moduł.
- Dane, walidację i raportowanie warto trzymać w osobnych plikach.
- Blok `if __name__ == "__main__":` chroni kod przed uruchomieniem przy imporcie.

## Pytania na rozmowę

### Pytanie: Czym jest moduł?

<details>
<summary>Przykładowa odpowiedź</summary>

> Moduł to plik `.py` zawierający kod, który można importować do innych plików.

</details>

### Pytanie: Po co dzielić projekt na kilka plików?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby rozdzielić odpowiedzialności, ułatwić nawigację po kodzie i ponownie wykorzystywać funkcje.

</details>

### Pytanie: Do czego służy `if __name__ == "__main__":`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Uruchamia wskazany kod tylko wtedy, gdy plik wykonujemy bezpośrednio, a nie gdy go importujemy.

</details>
