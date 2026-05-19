# Dzień 18 - Python: praca z plikami TXT i zapis raportu 

## Cel dnia 

Dzisiaj uczę się podstaw pracy z plikami tekstowymi w Pythonie 

W Data Engineeringu dane często pochodzą z plików albo są do plików zapisywane. Pliki mogą służyć jako:

- dane wejściowe,
- dane surowe,
- raporty,
- logi,
- wyniki przetwarzania,
- tymczasowe zbiory danych

Na początku przetwarzany zwykłe pliki `.txt`

## Plik tekstowy 

Plik `.txt` to prosty plik zawirający tekst. 

Może zaierać wiele linii, np.:

```text

Pierwsza linia
Druga linia
Trzecia linia

```

Python może ten plik: 

- odczytać
- zapisać od zera
- dopisaćna koncu

## Podstawy zapisu do pliku 

Przykład

```python

with open("reports/validation_report.txt", "w", encoding = "utf-8") as file:
    file.write("To jest raport walidacji")

```

- open() -> otwiera plik
- "w" -> oznacza tryb zapisu
- encoding = "utf-8" -> pomaga poprawie obsłużyć polskie znaki
- file.write() - > zapisuje tekst do pliku

## Dlaczego używam with open(...)?

with open(...) automatycznie zamyka plik po zakończonej pracy 

To jest lepsze niż ręczne:

file = open(...)
file.write(...)
file.close()

Na tym etapie warto używać zawsze:

```python

with open(...) as file:
    ...

```

## Tryb pracy z plikiem

Najważniejsze tryby: 

- "r" - > read, odczyt
- "w" - > write, zapis od zera
- "a" - > append, dopisywanie na końcu 

## tryb 'r'

Służy do oczytu pliku. 

```python

with open("data/notes.txt", "r", encoding = "utf-8") as file:
    content = file.read()

```

Jeśli plik nie istnieje, pojawi się ! FileNotFoundError

## Tryb "w" 

Służy do zapisu pliku od zera. 

```python

with open("reports/validation_report.txt", "w", encoding="utf-8") as file:
    file.write("Nowy raport")

```

Uwaga

tryb "w" nadpisuje istniejący plik.

Jeśli w pliku była wcześniejsza zawartość, zostanie usunięta. 

## Tryb "a"

Słuzy do dopisywanie tekstu na końcu pliku. 

```python

with open("reports/validation_report.txt", "a", encoding="utf-8") as file:
    file.write("\nKolejna linia")

```

Tryb "a" nie kasuje starej zawartości 

Znak nowej linie \n

Jeśli zapiszę 

```python

file.write("Pierwsza linia")
file.write("Druga linia")

```

tekst sklei się w jednej linii 

Dlatego używam \n

```python

file.write("Pierwsza linia \n")
file.write("Druga linia \n")

```

## Funkcja do zapisu tekstu 

Warto zrobić funkcję pomocniczą 

```python

def write_text_to_file(file_path, text):
    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(text)

```

Dzięki temu nie muszę potwarzać with open(...) w wielu miejsach

## Funckja do dopisywanie tekstu

```python

def append_text_to_file(file_path, text):
    with open(file_path, "a", encoding = "utf-8") as file:
        file.write(text)

```

## Funkcja do odczytu tekstu

```python

def read_text_from_file(file_path):
    with open(file_path, "r", encoding = "utf-8") as file:
        return file.read()

```

Funkcja zwraca cały tekst z pliku

## FileNotFoundError

Pojawia się wtwdy, gdy próbuję odczytać plik, który nie istnieje 
Bezpiecznie jest używać try/except 

```python

def read_text_from_file(file_path):
    try:
        with open(file_path, "r", encoding = "utf-8") as file:
            return file.read()
    except: FileNotFoundError:
        return None

```

## Folder musi istnieć 

Python może utworzyć nowy plik w trybie "w" ale folder musi już istnieć.

Jeśli zapisuje do - > reports/validation_report.txt 
to folder - > reports - > Musi istnieć 

## Funkcja budująca raport

Dobrze jest oddzielić 

- wypisywanie raport 
- budowanie tekstu raportu 

```python

def build_errors_report(errors):
    report = "! --- Raport walidacji --- !\n"

    if not errors:
        report += "Brak błędów\n"
    else:
        for error in errors:
            report += error + "\n"

    return report

```

Taka funkcja zwraca tekst, który można potem:

- wypisać w terminalu 
- zpaisać do pliku 
- uzyć dalej w programie

## Prosty przepływ programu 

```text

pobierz zamóienia 

\/ 

zwaliduj zamówienia 

\/

wypisz raport

\/ 

zapisz raport do pliku

To jest pierwszy prosty przepływ danych: 

data - > validation - > report - > file 

```

## Ścieżki względne 

Ścieżka - > report/validation_report.txt 

Jest liczna względem miejsca z któego uruchamiam program

Jeśli jestem w folderze:

src/day_18_files i uruchamiam - > main.py - > raport zapisze się do - > src/day_18_files/reports/validation_report.txt

## Najważniejsze rzeczy do zapamięania 

- Do pracy z plikami używam with open (...)
- Tryb 'r' służy od odczytu
- Tryb 'w' służy do zapisu od zera
- Tryb 'a' służy do dopisywania
- Tryb 'w' napisuje plik
- \n oznacza przejście do nowej lini
- encoding = "utf-8" pomaga przy polskich znakach
- Jeśli folder nie istnieje, zapis do pliku może się nie udać.
- FileNotFoundError oznacza brak pliku
- Warto miećfunkcję pomocnicze do zapisu i odczytu pliku
- Raport można zbudować jako tekst i zapisać do pliku
- Praca z plikami to fundament pod CSV, JSON i ETL
- 