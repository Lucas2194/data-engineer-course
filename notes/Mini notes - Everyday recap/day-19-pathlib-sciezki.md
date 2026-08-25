# Dzień 19 - `pathlib`, ścieżki i foldery

## Najważniejsze

- Ścieżka mówi, gdzie znajduje się plik lub folder.
- Ścieżka względna zależy od aktualnego folderu roboczego.
- Ścieżka absolutna wskazuje pełną lokalizację.
- `pathlib.Path` ułatwia budowanie ścieżek w Pythonie.

## Mini przykład

```python
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "orders.csv"
```

## Zapamiętaj

- `Path(__file__).parent` wskazuje folder aktualnego pliku.
- Operator `/` w `pathlib` łączy części ścieżki.
- `path.exists()` sprawdza, czy ścieżka istnieje.
- `path.is_file()` sprawdza, czy ścieżka jest plikiem.
- `mkdir(parents=True, exist_ok=True)` tworzy foldery bez błędu, gdy już istnieją.

## Pytania na rozmowę

### Pytanie: Czym różni się ścieżka względna od absolutnej?

<details>
<summary>Przykładowa odpowiedź</summary>

> Ścieżka względna jest liczona od aktualnego folderu roboczego, a absolutna wskazuje pełną lokalizację w systemie.

</details>

### Pytanie: Po co używać `pathlib`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Pozwala czytelnie i przenośnie budować ścieżki oraz wykonywać typowe operacje na plikach i folderach.

</details>

### Pytanie: Dlaczego aktualny folder roboczy może powodować błędy?

<details>
<summary>Przykładowa odpowiedź</summary>

> Ta sama ścieżka względna może wskazywać inne miejsce zależnie od folderu, z którego uruchomiono program.

</details>
