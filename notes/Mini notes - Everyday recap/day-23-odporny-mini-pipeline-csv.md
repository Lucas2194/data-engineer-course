# Dzień 23 - odporny mini-pipeline CSV

## Najważniejsze

- Pipeline musi radzić sobie nie tylko z idealnymi danymi.
- Inaczej traktujemy błąd techniczny, błąd struktury pliku i błąd pojedynczego rekordu.
- Wyjątek przerywa normalny przepływ programu.
- Błąd walidacji może być zapisany do raportu bez zatrzymywania całego pipeline'u.

## Mini przykład

```python
required_columns = ["order_id", "customer_name", "total_amount", "status"]

missing_columns = [
    column for column in required_columns
    if column not in fieldnames
]
```

## Zapamiętaj

- `raise` zgłasza wyjątek.
- Fail fast oznacza szybkie zatrzymanie programu przy błędzie, który uniemożliwia dalszą pracę.
- Pusty plik to coś innego niż plik z nagłówkiem, ale bez rekordów.
- Błąd najlepiej obsługiwać na poziomie, który potrafi sensownie zdecydować, co dalej.
- Kody zakończenia pomagają zrozumieć, czy program zakończył się sukcesem.

## Pytania na rozmowę

### Pytanie: Czym różni się wyjątek od błędu walidacji?

<details>
<summary>Przykładowa odpowiedź</summary>

> Wyjątek przerywa normalny przebieg kodu, a błąd walidacji może być oczekiwanym wynikiem sprawdzenia rekordu i zostać zapisany bez zatrzymywania całości.

</details>

### Pytanie: Kiedy pipeline powinien zatrzymać się od razu?

<details>
<summary>Przykładowa odpowiedź</summary>

> Gdy dalsze przetwarzanie nie ma sensu lub byłoby niebezpieczne, np. plik nie istnieje albo brakuje wymaganych kolumn.

</details>

### Pytanie: Po co sprawdzać `fieldnames` w CSV?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby przed przetwarzaniem rekordów upewnić się, że plik zawiera wymagane kolumny.

</details>
