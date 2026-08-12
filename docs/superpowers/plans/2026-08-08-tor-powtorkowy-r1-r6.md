# Tor powtórkowy R1–R6 (przed powrotem do diagnostyki Dnia 21)

**Data:** 2026-08-08 (spisany; tor ruszył 2026-08-06)
**Uczestnik:** Łukasz
**Status:** w trakcie — R1–R4 zaliczone, R5 zbudowany (czeka na rozwiązanie), R6 do zbudowania
**Ostatnia aktualizacja:** 2026-08-12 (zmiana formatu zadań od R6 — patrz sekcja niżej)

> **Dla agentów:** WYMAGANY SUB-SKILL: `superpowers:subagent-driven-development` lub
> `superpowers:executing-plans`. Tryb pracy z ucznia: [[jak-uczyc-lukasza]] w pamięci coacha.

---

## Dlaczego ten tor istnieje (kontekst)

Po ~7-tygodniowej przerwie (ostatni commit merytoryczny dni 1–20: **2026-05-25**) Łukasz
wrócił 2026-08-06. Diagnostyka Dnia 21 (`src/day_21_diagnostyka/`, 8 funkcji naraz,
zadania 7–8 celowo trudne) okazała się za dużym progiem na wejście po przerwie —
zaciął się na zadaniu #2 (`safe_get_total`).

**Decyzja (2026-08-06):** zamiast męczyć diagnostykę, robimy **ustrukturyzowaną powtórkę**
materiału z dni 1–20, rozbitą na 6 małych bloków R1–R6. Każdy blok domyka konkretne
zadania diagnostyczne, więc po R6 diagnostyka Dnia 21 ma być już łatwa. Ten tor jest
**wstawką** między Fazę 0 (środowisko + diagnostyka) a Fazę 1 — nie zmienia specyfikacji
kursu (`../specs/2026-07-14-junior-data-engineer-course-design.md`), tylko łagodzi próg
powrotu.

---

## Format każdego bloku (stały — zgodny ze specyfikacją §3.4)

Każdy blok R to cztery pliki w tej samej konwencji:

- `notes/powtorka-0X-<temat>.md` — teoria po polsku + tabela wyników + słowniczek EN,
- `src/powtorka_0X_<temat>/demo.py` — działający kod do przeczytania i uruchomienia,
- `src/powtorka_0X_<temat>/exercises.py` — sygnatury + docstringi + `pass` (bez rozwiązań),
- `tests/test_powtorka_0X.py` — testy, które uczeń zazielenia.

**Zasady (jak w specyfikacji):** demo obowiązkowe przed zadaniami; jedna klasa testów
naraz; reguła 20 minut; „test to prawda"; `except` łapie konkretny typ; **DRY** —
reużywasz własnych funkcji, nie przepisujesz logiki. Namespace `powtorka_*` celowo
oddzielony od liniowego toru `day_*`. Rozwiązań nie ma w repo.

**Weryfikacja bloku przed oddaniem (coach):** wzorcowe rozwiązanie → wszystkie testy
zielone + `ruff` czysty → przywrócenie stubów → potwierdzenie stanu czerwonego.

---

## Mapa bloków → zadania diagnostyczne

| Blok | Temat | Domyka w diagnostyce (Dzień 21) |
|------|-------|--------------------------------|
| R1 | stringi i formatowanie (`f-string`, `:.2f`, `.strip/.lower`) | `format_order_summary` |
| R2 | bezpieczny dostęp i konwersje (`.get()`, `try/except`, `float()`) | `safe_get_total` |
| R3 | listy i pętle (filtrowanie, budowanie, walidacja) | `filter_valid_amounts`, `split_valid_invalid` |
| R4 | słowniki jako liczniki/agregatory (`.items()`) | `count_statuses` (część `top_customers`) |
| R5 | pliki: CSV + `pathlib` (`DictReader/Writer`, `Path`, brak pliku) | `read_csv_rows` |
| R6 | sortowanie (`sorted(key=)`) + integracja (składanie funkcji) | `top_customers`, `run_pipeline` |

---

## Stan i zadania

### R1 — stringi i formatowanie ✅ ZALICZONY (2026-08-06)
- [x] Zbudowany (`src/powtorka_01_stringi/`, `tests/test_powtorka_01.py`).
- [x] Rozwiązany samodzielnie (23/23). Commit + push przez ucznia.
- Uwagi z review: nazwa funkcji vs parametr (`clean_text.strip()`), polskie znaki
  (`ó` != `o`), `.strip()` vs `.split()`, czytanie diffa pytest.

### R2 — bezpieczny dostęp i konwersje ✅ ZALICZONY (2026-08-08)
- [x] Zbudowany, rozwiązany (28/28). Payoff: `safe_get_total`.
- Uwagi z review: literal-tekst vs zmienna, truthiness (`0.0` jest „fałszywe"),
  **DRY** — nie przepisuj `try/except` z `to_float` w kółko.

### R3 — listy i pętle ✅ ZALICZONY (2026-08-08)
- [x] Zbudowany, rozwiązany (24/24). Commit + push.
- Uwagi z review: `=` vs `==` (błąd składni); `is_valid_order` był progiem pojęciowym;
  w #2/#3 wołał `float()` ponownie zamiast użyć wyniku `to_float` (DRY do domknięcia).

### R4 — słowniki jako liczniki/agregatory ✅ ZALICZONY (2026-08-10)
- [x] Zbudowany i zweryfikowany (wzorcówka 21/21, ruff czysty, stuby przywrócone).
- [x] Rozwiązany (21/21, ruff czysty). Commit + push przez ucznia.
- ⚠️ **Poza zakresem powtórki — patrz sekcja „DŁUG DO SPŁACENIA" niżej. Do powtórzenia
  jako lekcja nowego materiału.**
- Uwagi z review: **DRY trafione we wszystkich trzech miejscach** (#3→#2, #4→`to_float`,
  #5→#4) — dług z R2/R3 spłacony, wynik `to_float` zapisany do zmiennej.
  `count_items`, `normalize_status` bezbłędnie za pierwszym razem.
  Do poprawy: wcięcie 12 spacji zamiast 8 w `highest_spender`; puste linie ze spacjami
  na starcie funkcji; `sumy.get(name, 0)` → `0.0` (spójność typów w agregatorze float).
- Błędy po drodze: `order.get(status)` bez cudzysłowów (zmienna zamiast literału — ta sama
  oś co w R2, odwrócona); `orders.items()` na liście zamiast na wyniku `sum_by_customer`;
  `return best_name, best_total` zwracające `(None, None)` zamiast `None`; **`if` wstawiony
  DO ŚRODKA pętli zamiast za nią** (pusta pętla przeskakuje całe wnętrze). #5 finalnie
  podane jako rozwiązanie na wyraźną prośbę.
- **Uwaga o pracy:** dwie rundy stracone, bo uczeń czytał połowę wiadomości i działał
  z pamięci zamiast porównać literalnie z podpowiedzią na ekranie.
- Zalecenie od R5: **nazwy zmiennych po angielsku** (`counts`, `totals`, `amount`) —
  repo jest portfolio, a angielski i tak jest na liście braków.

### R5 — pliki: CSV + pathlib 🔨 ZBUDOWANY (2026-08-10), czeka na ucznia
Blok **celowo najobszerniejszy** — na prośbę ucznia (najtrudniejszy temat w torze).

- [x] Zbudowany: `notes/powtorka-05-pliki-csv.md` (16 rozdziałów + tabela pułapek
      + słowniczek EN na 22 pozycje), `src/powtorka_05_pliki_csv/demo.py` (9 sekcji),
      `.../data/orders.csv`, `.../exercises.py` (8 zadań), `tests/test_powtorka_05.py`
      (57 testów).
- [x] Zweryfikowany protokołem: wzorcówka **57/57 zielone**, `ruff` czysty →
      stuby przywrócone → **54 failed / 3 passed**. Trzy zielone na stubie to testy
      „NIE tworzy pliku" (asercja na nieistnienie przechodzi trywialnie) — celowo
      zostawione jako kolejna lekcja **„zielony ≠ zrobione"** (jak w R3/R4).
- [x] Demo uruchomione i sprawdzone: pisze do katalogu tymczasowego, repo nie brudzi.
- **Drabinka (8 zadań):** `read_text_lines` → `read_csv_rows` (**payoff diag #6**) →
  `get_headers` → `ensure_dir` → `write_csv_rows` (reuse #4) → `copy_csv` (reuse #2+#5)
  → `filter_csv_by_status` (reuse #2+#5, mini-ETL) → `csv_summary` (reuse #2+#3).
- **Nowość oznaczona jawnie w teorii:** fixture `tmp_path` w pytest (rozdział 13,
  nagłówek `[NOWE]`) — pierwszy raz, bo bez niego nie da się testować plików.
  Reszta bloku to potwierdzona powtórka dni 18 i 20.
- **Zmiana w `pyproject.toml`:** dodane `ignore = ["UP015"]` w `[tool.ruff.lint]`.
  UP015 każe usuwać domyślny tryb `"r"` z `open()`; w repo edukacyjnym piszemy tryb
  jawnie, żeby `"r"` obok `"w"` uczyło, że tryb jest wyborem. Przy okazji znika
  10 istniejących ostrzeżeń w kodzie ucznia z dni 18/20.
- [ ] **[UCZEŃ]** Rozwiąż. → **[COACH]** review.

### R6 — sortowanie + integracja ⬜ DO ZBUDOWANIA (ostatni blok)
> ⚠️ **R6 ma NOWY FORMAT** — patrz sekcja „Zmiana formatu od R6" niżej. To pierwszy blok
> hybrydowy: krótki drill z testami + zadanie projektowe bez testów.

- [ ] **[COACH]** Zbuduj blok. Zakres: `sorted(key=...)`, sortowanie malejące +
      remis alfabetyczny (trik: `key=lambda x: (-x[1], x[0])`), `.items()` → lista
      krotek, składanie wcześniejszych funkcji. Payoff: pełny `top_customers`
      (z filtrem `paid` i sortowaniem) oraz szkielet `run_pipeline`.
- [ ] **[COACH]** Część A (drill, z testami): 2–3 funkcje na samą mechanikę `sorted(key=)`.
      Tam istnieje jedna poprawna odpowiedź, więc testy są właściwym narzędziem.
- [ ] **[COACH]** Część B (projekt, BEZ testów): sama treść zadania. Uczeń pisze cały plik
      od zera — sam projektuje sygnatury, sam podłącza, sam uruchamia, sam ogląda
      artefakty w `reports/`. Weryfikacja: review coacha na commicie, nie pytest.
- [ ] **[UCZEŃ]** Rozwiąż. → **[COACH]** review.

### Wyjście z toru — powrót do diagnostyki
- [ ] Po R6: uczeń wraca do `src/day_21_diagnostyka/exercises.py` i rozwiązuje 8 zadań
      — teraz każdy klocek jest przećwiczony. To zamyka Fazę 0 (Task 3 z planu Fazy 0).
- [ ] Następnie Task 6 z planu Fazy 0: code review diagnostyki, mapa braków, plan Fazy 1.

---

## Zmiana formatu zadań od R6 (decyzja ucznia, 2026-08-12)

**Zgłoszone przez Łukasza:** chce zadań w formie samej treści, do których pisze cały kod
sam — zamiast stubów sprawdzanych testami.

**Diagnoza coacha.** Sam format stub+test ma realną lukę: uczeń nigdy nie projektuje
sygnatury, nie pisze pliku od zera i nie staje przed pustym ekranem — a **to właśnie
zatrzymało go w diagnostyce Dnia 21**, nie brak wiedzy o `.get()`. Drugi argument:
`exercises.py` nie jest portfolio, działający pipeline jest — a kawa z rekruterem
jest we wrześniu 2026.
Kontrargument, który zostaje w mocy: bez testów jedyną weryfikacją jest oko, a cichy
błąd w danych jest z definicji niewidoczny dla oka.

**Decyzja: format hybrydowy, nie zamiana.**

| Blok | Format |
|------|--------|
| R5 | **bez zmian** — stary format (zbudowany i zweryfikowany, 57 testów) |
| R6 | drill z testami (mechanika `sorted(key=)`) + **zadanie projektowe bez testów** |
| Faza 1 i dalej | domyślnie: krótki drill z testami na nową mechanikę (3–5 funkcji, ~30 min) + zadanie projektowe na repo ucznia |

**Etap trzeci — do wprowadzenia po zamknięciu toru R1–R6:** uczeń **sam pisze testy**.
Nie „dostaję testy", nie „testów nie ma". To ruch odróżniający juniora od kogoś,
kogo się zatrudnia. Nie teraz — za dużo naraz.

Zapisane też w pamięci coacha: [[jak-uczyc-lukasza]].

---

## ⚠️ DŁUG DO SPŁACENIA — R4 wykroczyło poza zakres dni 1–20

**Zgłoszone przez ucznia 2026-08-10, zweryfikowane przez coacha tego samego dnia.**

Łukasz zgłosił, że materiału z R4 nigdy wcześniej nie miał, a powtórka miała obejmować
**wyłącznie** dni/lekcje obecne w repo. Weryfikacja greppem potwierdza zarzut:

| Szukane | `src/day_*` | `notes/day-*.md` |
|---------|-------------|------------------|
| `.items()` | 0 trafień | 0 trafień |
| licznik `.get(k, 0) + 1` | 0 trafień | 0 trafień |
| agregator `{klucz: suma}` | 0 trafień | 0 trafień |

`notes/day-12-dict.md` uczy słowników (tworzenie, dostęp po kluczu), ale **nie** `.items()`,
**nie** wzorca licznika i **nie** agregacji.

**Przyczyna źródłowa (ważniejsza niż sam R4):** blok R4 był projektowany „pod diagnostykę",
a nie „pod dni 1–20". Diagnostyka `src/day_21_diagnostyka/exercises.py` deklaruje w linii 1
*„Zakres: dni 1-20"*, ale zadanie #3 `count_statuses` wymaga wzorca licznika, a #7
`top_customers` wymaga `.items()`. **To diagnostyka wykracza poza swój zadeklarowany zakres**
— R4 tylko odziedziczyło ten błąd. Coach nie zweryfikował pokrycia przed budową bloku.

**Konsekwencja dla ucznia:** trudność R4 nie była luką w pamięci Łukasza — to był materiał
widziany pierwszy raz. Nie interpretować tego jako regresu.

### Do zrobienia (po zamknięciu toru R1–R6, przed Fazą 1)
- [ ] **[COACH]** Zweryfikować pokrycie diagnostyki Dnia 21: dla każdego z 8 zadań sprawdzić
      greppem, czy wymagana technika występuje w dniach 1–20. Spisać listę rozbieżności.
- [ ] **[COACH]** Zdecydować z uczniem: albo dopisać brakujące tematy do toru liniowego jako
      pełnoprawne lekcje (`day-22+`), albo poprawić nagłówek diagnostyki, żeby nie kłamał
      o zakresie.
- [ ] **[COACH]** Wrócić do R4 jako **lekcji nowego materiału**, nie powtórki — uczeń przerobił
      go „na zimno" i zasługuje na drugie podejście z pełną teorią (`.items()`, licznik,
      agregator, `Counter` z `collections` jako dopełnienie).
- [ ] **[COACH]** Reguła na przyszłość: **przed zbudowaniem bloku powtórkowego zawsze grep po
      `src/day_*` i `notes/day-*.md`**, czy technika faktycznie występuje. Blok powtórkowy
      zawierający nowy materiał musi go oznaczyć jako nowy — jawnie, w teorii.

### Weryfikacja pokrycia R5 (wykonana 2026-08-10 — czysto)
`src/day_20_csv/csv_utils.py` (kod ucznia z dnia 20) zawiera `from pathlib import Path`,
`Path(file_path)`, `.parent.mkdir(parents=True, exist_ok=True)`, `csv.DictReader`,
`csv.DictWriter`, `newline=""`, `encoding="utf-8"`. Dzień 18 pokrywa `open()`,
`with` i `FileNotFoundError`. **R5 jest prawdziwą powtórką.** Jedyna luka: `notes/day-20.md`
nie opisuje `Path` (kod był, notatka nie) — teoria R5 to uzupełnia.
Nowość świadomie oznaczona w teorii R5: fixture `tmp_path` w pytest.

---

## Czego ten tor NIE obejmuje (świadomie)

Powtórka dotyczy **wyłącznie toru Python (dni 1–20)**. Nie rusza:
- **toru SQL** — wg specyfikacji §3.1 miał być codziennym nawykiem od dnia 1; **nadal
  nie wystartował** (brak `sql/`, `docker/`). To osobna, otwarta decyzja — patrz niżej.
- **Dockera/Postgresa** (Task 2 planu Fazy 0 — niezrobiony).
- **toru angielskiego** poza istniejącym `notes/english/glossary.md` (zasiany, nierozwijany).

Te braki są realne i rosną w miarę zbliżania się kawy (wrzesień 2026).

**Decyzja ucznia (2026-08-08):** najpierw dokończyć tor Python (powtórki R4–R6 +
diagnostyka Dnia 21), **dopiero potem** startować SQL — jeden temat naraz, mniejsze
obciążenie wieczorem. Świadomy koszt: tor SQL rusza realnie za 1–2 tygodnie, bliżej kawy.
Coach ma o tym przypomnieć **natychmiast po zamknięciu diagnostyki Dnia 21** (to jest
moment startu SQL), a nie później. Docker/Postgres = pierwszy krok tego startu.
