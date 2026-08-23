# Data Engineer Course

To jest moje repozytorium z intensywnego kursu Junior Data Engineer. Zapisuję
tutaj notatki z kolejnych dni nauki, ćwiczenia w Pythonie oraz rozwijane krok po
kroku mini-projekty związane z przetwarzaniem danych.

Aktualny etap: **dzień 24 - podstawy SQL**.

## Cele kursu

- nauczyć się pracy z terminalem, Git i GitHub,
- dobrze opanować Pythona,
- nauczyć się SQL,
- budować własne pipeline'y ETL,
- poznać Dockera i Airflow,
- stworzyć portfolio projektów Data Engineering.

## Czego nauczyłem się do tej pory

- podstaw Pythona: typów danych, pętli, funkcji i słowników,
- dzielenia programu na moduły,
- walidacji, filtrowania i transformowania danych,
- odczytu i zapisu plików tekstowych, CSV oraz JSON,
- pracy z danymi zagnieżdżonymi i agregacjami,
- obsługi wyjątków i kodów zakończenia programu,
- testowania pipeline'u na niepoprawnych danych wejściowych,
- podstawowych pojęć związanych z SQL i SQLite.

## Mini-projekty

### Pipeline CSV

Projekt [day_20_csv](src/day_20_csv/) zawiera modularny pipeline, który:

- odczytuje zamówienia z pliku CSV,
- sprawdza nagłówek i wymagane kolumny,
- rozdziela poprawne i błędne rekordy,
- transformuje poprawne dane,
- zapisuje pliki wynikowe i raport walidacji,
- obsługuje błędy wejścia w kontrolowany sposób,
- zapisuje dodatkowy raport `pipeline_error.txt` po krytycznym błędzie.

Folder `data/test_cases/` zawiera przypadki testowe dla pustego pliku, braku
kolumn, samego nagłówka oraz błędnego pojedynczego rekordu.

### JSON i agregacje

Projekt [day21-json](src/day21-json/) obejmuje odczyt i zapis JSON, filtrowanie
zamówień oraz pracę z danymi zagnieżdżonymi.

Projekt [day22-json-agregacja](src/day22-json-agregacja/) rozwija ten przykład o
liczenie i sumowanie zamówień według statusu oraz agregację metod dostawy.

## Struktura repozytorium

```text
.
|-- notes/                       # notatki z kolejnych dni nauki
|-- src/                         # ćwiczenia i mini-projekty w Pythonie
|   |-- day_20_csv/              # odporny pipeline CSV
|   |-- day21-json/              # przetwarzanie danych JSON
|   `-- day22-json-agregacja/    # agregacje danych JSON
`-- README.md
```

## Ostatnie notatki

- [Dzień 20 - pliki CSV](notes/day-20.md)
- [Dzień 21 - JSON](notes/day-21.md)
- [Dzień 22 - agregacje](notes/day-22.md)
- [Dzień 23 - obsługa błędów w pipeline CSV](notes/day-23.md)
- [Dzień 24 - podstawy SQL](notes/day-24.md)

## GitHub

Projekt został opublikowany na GitHubie jako moje repozytorium kursowe. Ćwiczę
tutaj pełny cykl pracy:

```text
zmiana pliku -> git add -> git commit -> git push
```
