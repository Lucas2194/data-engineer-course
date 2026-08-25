# Dzień 4 - Git głębiej

## Najważniejsze

- Git śledzi zmiany w plikach projektu.
- `git status` pokazuje aktualny stan repozytorium.
- Staging area to miejsce, do którego dodajesz zmiany przed commitem.
- Commit zapisuje konkretny punkt historii projektu.

## Mini przykład

```bash
git status
git add notes/day-04.md
git commit -m "Add day 4 notes"
```

## Zapamiętaj

- `git add` przygotowuje zmiany do commita.
- `git commit` zapisuje przygotowane zmiany w historii.
- Dobry commit opisuje jedną logiczną zmianę.
- Przed commitem zawsze warto użyć `git status`.

## Pytania na rozmowę

### Pytanie: Czym jest staging?

<details>
<summary>Przykładowa odpowiedź</summary>

> Staging area to miejsce, w którym przygotowujesz wybrane zmiany do następnego commita.

</details>

### Pytanie: Jaka jest różnica między `git add` i `git commit`?

<details>
<summary>Przykładowa odpowiedź</summary>

> `git add` dodaje zmiany do staging area, a `git commit` zapisuje przygotowany zestaw zmian w historii repozytorium.

</details>

### Pytanie: Po co sprawdzać `git status`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Żeby zobaczyć, które pliki zmieniono, które są przygotowane do commita i czego Git jeszcze nie śledzi.

</details>
