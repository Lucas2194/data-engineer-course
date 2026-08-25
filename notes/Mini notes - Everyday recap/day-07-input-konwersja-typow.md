# Dzień 7 - input i konwersja typów

## Najważniejsze

- `input()` pobiera dane od użytkownika jako tekst.
- Jeżeli chcesz pracować na liczbach, musisz wykonać konwersję typu.
- Konwersja zmienia reprezentację wartości, np. z tekstu na liczbę.

## Mini przykład

```python
age_text = input("Podaj wiek: ")
age = int(age_text)

print(age + 1)
```

## Zapamiętaj

- Wynik `input()` zawsze jest typu `str`.
- `int()` zamienia wartość na liczbę całkowitą.
- `float()` zamienia wartość na liczbę dziesiętną.
- Nie każdy tekst da się bezpiecznie zamienić na liczbę.

## Pytania na rozmowę

### Pytanie: Dlaczego `input()` zwraca tekst?

<details>
<summary>Przykładowa odpowiedź</summary>

> Python nie wie, jaki rodzaj danych wpisze użytkownik, dlatego `input()` zawsze zwraca wartość typu `str`.

</details>

### Pytanie: Kiedy użyjesz `int()`, a kiedy `float()`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `int()` użyjesz dla liczb całkowitych, a `float()` dla liczb zawierających część dziesiętną.

</details>

### Pytanie: Co może pójść źle przy konwersji typu?

<details>
<summary>Przykładowa odpowiedź</summary>

> Tekst może nie mieć poprawnego formatu, np. `int("abc")` zgłosi `ValueError`.

</details>
