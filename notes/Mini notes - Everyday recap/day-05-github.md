# Dzień 5 - GitHub

## Najważniejsze

- Git działa lokalnie, a GitHub przechowuje repozytorium zdalnie.
- `push` wysyła lokalne commity na GitHub.
- `pull` pobiera zmiany z repozytorium zdalnego.
- Repozytorium zdalne ułatwia backup i współpracę.

## Mini przykład

```bash
git status
git add .
git commit -m "Update notes"
git push
```

## Zapamiętaj

- Commit zapisuje zmianę lokalnie.
- Push wysyła commity do GitHuba.
- GitHub nie zastępuje Gita, tylko działa jako zdalne miejsce na repozytorium.
- Warto pushować regularnie po sensownych commitach.

## Pytania na rozmowę

### Pytanie: Czym różni się commit od push?

<details>
<summary>Przykładowa odpowiedź</summary>

> Commit zapisuje zmiany lokalnie w historii Git, a push wysyła lokalne commity do zdalnego repozytorium.

</details>

### Pytanie: Po co używać GitHuba?

<details>
<summary>Przykładowa odpowiedź</summary>

> GitHub przechowuje zdalną kopię repozytorium oraz ułatwia współpracę, przegląd zmian i udostępnianie projektu.

</details>

### Pytanie: Co robi `git pull`?

<details>
<summary>Przykładowa odpowiedź</summary>

> Pobiera zmiany ze zdalnego repozytorium i łączy je z aktualną lokalną gałęzią.

</details>
