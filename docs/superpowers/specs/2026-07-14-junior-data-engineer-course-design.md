# Kurs Junior Data Engineer — projekt programu

**Data:** 2026-07-14
**Uczestnik:** Łukasz (obecnie: produkcja — grawerowanie upominków)
**Cel:** stanowisko Junior Data Engineer
**Status:** zatwierdzony, gotowy do rozpisania planu

---

## 1. Punkt startowy

**Stan repo (audyt z 2026-07-14):**

- 20 dni nauki, ostatni commit **2026-05-25** → przerwa ~7 tygodni.
- Opanowane: Git (podstawy + GitHub), Python — zmienne, typy, warunki, pętle, listy,
  słowniki, funkcje, moduły, `try/except`, `pathlib`, moduł `csv`.
- Jakość kodu: powyżej średniej dla 20. dnia. `src/day_20_csv/` to projekt rozbity na
  moduły (`main` / `validators` / `transformers` / `reports` / `csv_utils`) — świadczy
  o rozumieniu separacji odpowiedzialności.
- Słabości kodu: niespójne formatowanie (`parents = True`), brak testów, brak
  type hintów, brak logowania.

**Czego brakuje całkowicie:** SQL, bazy danych, pandas, API/`requests`, Docker,
chmura, testy, CI.

**Budżet czasu:** 2–3h dziennie, okno 17:00–19:30 (praca 7:00–15:00). ≈15–18h/tydzień.

**Angielski:** słaby — zidentyfikowany jako **największe pojedyncze ryzyko rekrutacyjne**.
Polskie ogłoszenia juniorskie niemal zawsze wymagają dobrego angielskiego.

**Kontekst „rozmowy we wrześniu":** nieformalna kawa ze znajomym rekrutującym w firmie
danowej. Nie jest to egzamin techniczny. Cel: wiarygodnie opowiedzieć o tym, co się
zbudowało, i zostać zapamiętanym jako kandydat.

---

## 2. Wyniki researchu rynku (lipiec 2026)

Ustalenia, które kształtują program:

1. **Screen SQL-owy na juniora jest przewidywalny:** ~25 min, trzy pytania —
   `WHERE`+`GROUP BY`, JOIN+agregacja, **funkcja okienkowa**. Rozróżnienie
   `RANK`/`DENSE_RANK`/`ROW_NUMBER` przy remisach to typowy filtr.
2. **Modelowanie danych to sygnał jakości.** Star schema, fakty vs wymiary.
   Odpowiedź „zrobię jedną wielką tabelę" dyskwalifikuje.
3. **Idempotencja pipeline'ów** — stałe pytanie („co, jeśli uruchomi się dwa razy?").
4. **Rdzeń stacku 2026:** Python + SQL + dbt + Airflow + jedna hurtownia.
   Kafka/Kubernetes — poza zakresem juniora.
5. **Polski rynek:** minimum to Python + SQL (poziom średni) + Git; **bardzo dobry
   angielski** jako twardy filtr w większości ofert.
6. **Nowoczesne narzędzia warte dołożenia:** DuckDB (analityczny warsztat),
   dlt (ingestia), Parquet; Iceberg — świadomościowo.
7. **Pandas** pozostaje standardem rynkowym; **Polars** jako alternatywa do pokazania.

---

## 3. Decyzje projektowe

### 3.1 Dwutorowość (wariant A)

SQL **nie jest etapem** — jest codziennym nawykiem od dnia 1 do końca kursu.
Uzasadnienie: SQL to umiejętność mięśniowa. Zrozumienie JOIN-a zajmuje godzinę;
pisanie zapytań odruchowo, pod presją, wymaga miesięcy powtórek. Odłożenie SQL-a
na „po Pythonie" (plan pierwotny) oznaczałoby zerową znajomość SQL-a we wrześniu.

### 3.2 Odrzucone alternatywy

- **Sekwencyjnie (Python → potem SQL):** prostsze w prowadzeniu, ale we wrześniu
  bez SQL-a. Odrzucone.
- **„Projekt najpierw":** motywujące, ale zostawia dziury w fundamentach, które
  wychodzą na rozmowie technicznej. Odrzucone.

### 3.3 Zmiany wobec planu pierwotnego (GPT)

| Zmiana | Uzasadnienie |
|---|---|
| PySpark: 6 tygodni → **1 tydzień** | Na juniora to „nice to have". 5 tygodni przeniesione na SQL, jakość danych i portfolio. |
| SQL: etap 8-tygodniowy → **codzienny tor przez cały kurs** | Umiejętność mięśniowa, wymaga rozłożenia w czasie. |
| Testy (`pytest`) i CI: etap 11 → **faza 1** | Testy są mechanizmem samodzielnej weryfikacji — fundamentem trybu pracy. |
| Docker: etap 6 → **narzędziowo w fazie 0**, teoria w fazie 4 | Postgres potrzebny natychmiast, żeby ruszyć z SQL-em. |
| **Dodano:** DuckDB, dlt, Parquet, `uv`, `ruff`, WSL2, angielski techniczny | Zgodnie z researchem 2026. |
| **Zachowano:** GCP/BigQuery, pandas, brak Kafki/K8s | Trafne decyzje pierwotne. |

### 3.4 Tryb pracy (zatwierdzony wariant A)

Cykl jak w prawdziwym zespole:

1. Coach generuje `notes/day-XX.md` (teoria + przykłady do uruchomienia).
2. Coach generuje zadania: sygnatury funkcji + docstringi + `pass`, **bez rozwiązań**.
3. Coach generuje `tests/test_day_XX.py` — testy, które uczeń musi zazielenić.
4. Uczeń koduje samodzielnie. Zielone testy = obiektywna informacja zwrotna bez coacha.
5. Uczeń zgłasza gotowość → **code review na poziomie seniora**: konkretne błędy,
   bez pochwał na wyrost.
6. Commit + wpis do dziennika nauki.

**Zasady:**

- Rozwiązania **nie są** podawane z góry. Przy utknięciu: wskazówka → mocniejsza
  wskazówka → rozwiązanie tylko na wyraźną prośbę.
- **Reguła 20 minut:** 20 min walki z jednym problemem, potem pytanie. Bez bohaterstwa.
- **Reguła minimum 20 minut:** w najgorszy dzień — same drille SQL + commit.
  Ciągłość jest ważniejsza niż objętość.

---

## 4. Struktura dnia (2h35, 17:00–19:35)

| Blok | Czas | Treść |
|---|---|---|
| 1. Teoria + demo | 25 min | `notes/day-XX.md`, przykłady kodu do uruchomienia |
| 2. Zadania | 65 min | Od rozgrzewki do jednego trudnego. Testy muszą przejść. |
| 3. SQL | 40 min | Nowy temat + **drille** (2–3 zapytania ze starych dni) |
| 4. Angielski techniczny | 15 min | Dokumentacja, glosariusz, później: mówienie |
| 5. Domknięcie | 15 min | Commit, dziennik nauki, review |

**Ciężkie rzeczy na początku sesji** (świeża głowa po pracy fizycznej), mechaniczne
na końcu (drille SQL, notatki).

**Higiena:** jeden lekki dzień w tygodniu (45 min: drille + angielski);
co 6 tygodni jeden dzień całkiem wolny.

---

## 5. Oś czasu

Start: 2026-07-14. Kawa: początek września 2026. Koniec: przełom XI/XII 2026.

| Faza | Termin | Tor główny | Tor SQL |
|---|---|---|---|
| **0. Diagnostyka** | 14–16 lipca | Zadania sprawdzające dni 1–20; Postgres + DuckDB w Dockerze; `uv`, `ruff`, `pytest` | pierwsze `SELECT`-y |
| **1. Fundamenty** | tyg. 1–3 (→3 sierpnia) | Łatanie luk wg diagnostyki; pliki, JSON, `requests`/API, `pytest`, `logging`, pandas, WSL2 | `WHERE`, `ORDER BY`, agregacje, `GROUP BY`/`HAVING`, JOIN-y |
| **2. Pierwszy pipeline** | tyg. 4–6 (→24 sierpnia) | **API → raw → Postgres (raw/staging/mart) → raport**; idempotencja, logowanie, testy; dlt na koniec | CTE, funkcje okienkowe, star schema |
| **3. Tydzień rozmowy** | tyg. 7 (→31 sierpnia) | README, diagram architektury, porządki w repo, **trening narracji o projekcie (PL + EN)** | powtórka pod screen: `GROUP BY`, JOIN, okienkowe |
| ☕ **KAWA** | wrzesień | | |
| **4. Docker + Airflow** | tyg. 8–11 | Docker od podstaw; cały stack w Compose; pipeline przeniesiony na DAG-i; retry, backfill | indeksy, `EXPLAIN`, optymalizacja |
| **5. dbt + hurtownia** | tyg. 12–14 | Modele, sources, testy, dokumentacja, lineage, modele inkrementalne; OLTP vs OLAP | modelowanie wymiarowe |
| **6. Chmura (GCP)** | tyg. 15–17 | IAM, Cloud Storage → BigQuery → dbt; partycjonowanie, koszty | SQL w BigQuery |
| **7. Profesjonalizacja** | tyg. 18–19 | Jakość danych, CI (GitHub Actions), monitoring; **PySpark w pigułce (1 tydz.)** | powtórki |
| **8. Portfolio i aplikacje** | tyg. 20–21 | 3 projekty dopięte, CV, LinkedIn, rozmowy próbne | drille rekrutacyjne |

---

## 6. Stack narzędziowy

**Od fazy 0:** Python 3.13, `uv` (zamiast pip), `ruff` (lint + format), `pytest`,
Docker Desktop, PostgreSQL (w kontenerze), DBeaver, DuckDB, Git/GitHub.

**Faza 1:** WSL2/Ubuntu (podstawy terminala), pandas, `requests`, `logging`.

**Faza 2+:** dlt, Parquet, Airflow, dbt (`dbt-postgres`, potem `dbt-bigquery`),
GitHub Actions, GCP (Cloud Storage, BigQuery), PySpark.

**Świadomościowo (bez wdrażania):** Iceberg, Polars, Kafka, Snowflake/Databricks.

---

## 7. Portfolio (produkt końcowy)

Każdy projekt wyrasta z poprzedniego. Żaden nie jest tutorialem.

**Projekt 1 — SQL Analytics** (koniec fazy 2)
Model danych sklepu, ~40 zapytań analitycznych, star schema.
*Pokazuje:* SQL, JOIN-y, CTE, funkcje okienkowe, modelowanie.

**Projekt 2 — ETL Pipeline** (faza 2; **główny projekt na kawę we wrześniu**)
API → raw (JSON) → Postgres → staging → mart → raport.
*Pokazuje:* Python, API, pandas, PostgreSQL, walidacja, idempotencja, logowanie,
testy, README z diagramem.

**Projekt 3 — End-to-End** (fazy 4–7; **projekt przypięty na GitHubie**)
Ten sam pipeline: Docker Compose + Airflow + dbt + testy jakości danych + CI +
wersja na BigQuery.
*Pokazuje:* pełny warsztat data engineera.

---

## 8. Angielski techniczny

Traktowany jako osobny tor, 15 min dziennie, podporządkowany celowi rekrutacyjnemu.

- **Faza 1–2:** czytanie dokumentacji w oryginale; `notes/english/glossary.md` —
  słownictwo techniczne (`row`, `query`, `schema`, `retry`, `stale data`, `to deploy`).
- **Faza 3:** opowiedzenie **własnego projektu po angielsku** — 90 sekund, płynnie.
- **Faza 4+:** typowe pytania rekrutacyjne po angielsku, odpowiedzi na głos, korekta.

Notatki i teoria: **po polsku**. Terminologia i dokumentacja: **po angielsku**.

---

## 9. Ryzyka

| Ryzyko | Przeciwdziałanie |
|---|---|
| **Wypalenie** (2,5h nauki po 8h pracy fizycznej) | Lekki dzień w tygodniu; wolny dzień co 6 tygodni; trudne rzeczy na początku sesji |
| **Kolejna długa przerwa** (już wystąpiła: 7 tyg.) | Reguła „minimum 20 minut"; ciągłość > objętość |
| **Angielski** | Osobny tor 15 min/dzień od dnia 1 |
| **Iluzja postępu** („przerobiłem tutorial") | Testy jako obiektywna weryfikacja; code review bez taryfy ulgowej |
| **Rozproszenie na zbyt wiele technologii** | Świadome cięcia: PySpark do 1 tyg.; brak Kafki, K8s, Terraform, ML, BI |

---

## 10. Kryterium sukcesu

Po ukończeniu kursu uczestnik potrafi powiedzieć — i **udowodnić kodem na GitHubie**:

> „Potrafię zbudować pipeline danych od źródła (API/plik), przez warstwy raw i staging,
> do tabel analitycznych. Uruchamiam go lokalnie w Dockerze, orkiestruję w Airflow,
> transformacje piszę w dbt, mam testy jakości danych i CI. Projekt jest
> udokumentowany i umiem o nim opowiedzieć — również po angielsku."

**Kamienie milowe:**

- **31 sierpnia:** działający Projekt 2 + umiejętność opowiedzenia o nim → gotowość na kawę.
- **Przełom XI/XII 2026:** trzy projekty, CV, gotowość do aplikowania.
