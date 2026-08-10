# Tor powtórkowy R1–R6 (przed powrotem do diagnostyki Dnia 21)

**Data:** 2026-08-08 (spisany; tor ruszył 2026-08-06)
**Uczestnik:** Łukasz
**Status:** w trakcie — R1–R3 zaliczone, R4 zbudowany (czeka na rozwiązanie), R5–R6 do zbudowania

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

### R4 — słowniki jako liczniki/agregatory 🔨 ZBUDOWANY, czeka na ucznia
- [x] Zbudowany i zweryfikowany (wzorcówka 21/21, ruff czysty, stuby przywrócone).
- [ ] **[UCZEŃ]** Rozwiąż `src/powtorka_04_slowniki_liczniki/exercises.py`
      (`count_items` → `normalize_status` → `count_statuses` → `sum_by_customer`
      → `highest_spender`). DRY: #3 użyj #2, #5 użyj #4; zapisz wynik `to_float`.
- [ ] **[COACH]** Senior-review po zgłoszeniu gotowości.

### R5 — pliki: CSV + pathlib ⬜ DO ZBUDOWANIA
- [ ] **[COACH]** Zbuduj blok (notes/demo/exercises/tests) w stałym formacie.
      Zakres: `csv.DictReader`/`DictWriter`, `Path`, `encoding="utf-8"`,
      `newline=""` przy zapisie, obsługa braku pliku (`Path.exists()` /
      `FileNotFoundError` → `[]`). Payoff: `read_csv_rows`.
      Drabinka wstępna: `read_rows(path)` → `write_rows(path, rows, headers)` →
      `read_or_empty(path)` (brak pliku → `[]`) → mały round-trip zapis+odczyt.
- [ ] **[UCZEŃ]** Rozwiąż. → **[COACH]** review.

### R6 — sortowanie + integracja ⬜ DO ZBUDOWANIA (ostatni blok)
- [ ] **[COACH]** Zbuduj blok. Zakres: `sorted(key=...)`, sortowanie malejące +
      remis alfabetyczny (trik: `key=lambda x: (-x[1], x[0])`), `.items()` → lista
      krotek, składanie wcześniejszych funkcji. Payoff: pełny `top_customers`
      (z filtrem `paid` i sortowaniem) oraz szkielet `run_pipeline`.
- [ ] **[UCZEŃ]** Rozwiąż. → **[COACH]** review.

### Wyjście z toru — powrót do diagnostyki
- [ ] Po R6: uczeń wraca do `src/day_21_diagnostyka/exercises.py` i rozwiązuje 8 zadań
      — teraz każdy klocek jest przećwiczony. To zamyka Fazę 0 (Task 3 z planu Fazy 0).
- [ ] Następnie Task 6 z planu Fazy 0: code review diagnostyki, mapa braków, plan Fazy 1.

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
