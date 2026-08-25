# Dzień 18 - pliki TXT i zapis raportu

## Najważniejsze

- Python może odczytywać i zapisywać pliki tekstowe.
- `with open(...)` bezpiecznie otwiera i zamyka plik.
- Tryb pliku decyduje, czy czytasz, nadpisujesz czy dopisujesz dane.
- Raport tekstowy jest prostym sposobem zapisania wyniku walidacji.

## Mini przykład

```python
with open("reports/log.txt", "w", encoding="utf-8") as file:
    file.write("Pipeline finished\n")
```

## Zapamiętaj

- `"r"` oznacza odczyt.
- `"w"` oznacza zapis z nadpisaniem pliku.
- `"a"` oznacza dopisywanie na końcu pliku.
- Folder docelowy musi istnieć przed zapisem pliku.
- `FileNotFoundError` oznacza, że ścieżka nie wskazuje istniejącego pliku.

## Pytania na rozmowę

### Pytanie: Dlaczego używamy `with open(...)`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Ponieważ plik zostanie automatycznie zamknięty po zakończeniu bloku, także wtedy, gdy wystąpi błąd.

</details>

### Pytanie: Czym różni się tryb `"w"` od `"a"`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `"w"` zapisuje plik od początku i usuwa jego poprzednią zawartość, a `"a"` dopisuje dane na końcu.

</details>

### Pytanie: Po co pipeline zapisuje raport?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby pozostawić informację o wyniku przetwarzania, błędach i odrzuconych rekordach do późniejszej analizy.

</details>
