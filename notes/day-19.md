## Dzień 19 - Python: ścieżki plików, pathlib i foldery 

## Cel dnia

Dzisiaj uczę się pracować ze ścieżkami do plików i folderów w Pythonie 

Po poprzednim dniu wiem jak zapisywać i odczytywać pliki tekstowe. Teraz uczę się robić to bardziej profesjonalnie. 

## Ścieżka względna 

Ścieżka względna jest liczona od aktualnego miejsca uruchomienia programu

Przykład 

```text

reporst/validation_report.txt

```

Taka ścieżka oznacza 

Folder reports a w nim plik validation_report.txt

Problem :

Jeśli uruchomię program z innego folderu, Python może szukać pliku w innym miejscu. 

## Ścieżka absolutna

Ścieżka absolutna to pełna ścieżka od początku dysku 

Na Windowsie może wyglądać tak : 

```text

C:\Users\Lukasz\data-engineer-course\src\day_19_paths\reports\validation_report.txt

```

Nie chce wpisywać takich ścieżek ręcznei w kodzie, bo u inncyh osób będą inne. 

## pathlib

To wbudowany moduł Pythona do pracy z ścieżkami 

import

```python

from pathlib import Path

```

Przykład

```python

file_path = Path("reports") / "validation_report.txt"

```

To lepsze niż ręczne sklejanie tekstów 

Czytam to jako - > folder `reports` a w nim plik `validation_report.txt`

## Akutalny folder roboczy 

Mogę sprwadzić skąd program został uruchomiony : 

```python

from pathlib import Path

print(Path.cwd())

```

cwd oznacza current working directory

## Folder akutalnego pliku 

Specjalna zmienna:

```python

__file__

```

pokazuję lokalizację aktualnego pliku .py

Folder akttualnego pliku mogę dostać tak

```python

BASE_DIR = Path(__file__).parent

```

To jest bardzo przydatne do budowanie stabilnych ścieżek 

## Foldery projektu dnia 

```python

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

NOTES_FILE = DATA_DIR / "notes.txt"
VALIDATION_REPORT_FILE = REPORTS_DIR / "validation_report.txt"

```

Dzięki temu ścieżki są czytelne i zdefiniowane w jednym miejscu. 

## Sprawdzanie czy plik istnieje 

```python

file_path.exists()

```

sprawdza, czy ścieżka istnieje.

```python

file_path.is_file()

```

Sprawdza czy ścieżka jest plikiem.

Sprawdzanie czy folder istnieje

```python

folder_path.exists()

# sprawdza czy ścieżka istnieje

folder_path.is_dir()

# sprawdza czy ścieżka jest folderem

```

## Tworzenie folderu

Prosty zapis

```python

folder_path.mkdir()

# Lepszy zapis 

folder_path.mkdir(parents = True, exist_ok = True)

```

Znaczenie 

parents = True - utwórz też brakujące foldery nadrzędne 
exist_ok = True - nie rób błędu, jeśli folder już istnieje

## Ulepsze write_text_to_file()

Funkja zapisująca tekst do pliku może najpierw utworzyć folder docelowy 

```python

def write_text_to_file(file_path, text):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents = True, exist_ok = True)

    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(text)

```

file_path.parent oznacza folder, w którym ma znaleźć się plik 

## Ulepszone append_text_to_file()

```python

def append_text_to_file(file_path, text):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents = True, exist_ok = True)

    with open(file_path, "a", encoding = "utf-8") as file:
        file.write(text)

```

Ta funkcja dopisuje tekst na końcu pliku i upewnia się, że folder istnieje

## Ulepszone read_text_from_file()

Przy odczycie pliku mogę obśłużyć brak pliku

```python

def read_text_from_file(file_path):

    file_path = Path(file_path)

    try:
        with open(file_path, "r", encoding = "utf-8") as file
        return file.read()
    except FileNotFoundError:
        return None
```

Jeśli plik nie istnieije, funkcja zwraca None 

## Dlaczego to ważne ? 

Ścieżki są bardzo ważne w Data Engineeringu, bo projekty często mają struukturę:

data/raw/
data/processed/
reports/
logs/
src/

Pipeline danych musi umieć zpaisywać i odczytywać pliki w przewidywalnych miejsach

## Najważniejsze rzeczy do zapamiętania 

- Ścieżka względna zależy od miejsca uruchomienia programu
- Ścieżka abolustna jest pełną lokalizacją pliku 
- pathlib pomaga pracować z plikami
- Path("folder") / "plik.txt" buduję ścieżkę
- Path.cwd() pokazuje akutalny folder roboczy 
- Path(__file__).parent pokazuje folder akutalnego pliku
- exists() sprawdza czy ścieżka istnieje
- is_file() sprawdza czy to plik 
- is_dir() sprawdza czy to folder
- mkdir(parents=True, exist_ok= True) tworzy bezpeiczne foldery
- file_path.parent oznacza folder nadrzędny pliku
- Dobre zarządzanie ścieżkami jset podstawą pracy z plikami CSV, JSON i pielineami




