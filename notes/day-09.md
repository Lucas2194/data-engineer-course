# Dzień 9 — Python: `and`, `or`, `not`

## 1. Cel dnia

Dzisiaj uczę się operatorów logicznych:

- `and`
- `or`
- `not`

Dzięki nim mogę łączyć kilka warunków w jednym `if`.

W poprzednim dniu sprawdzałem proste warunki, np.:

```python
if age >= 18:
    print("Pełnoletni")

Dzisiaj mogę sprawdzać kilka rzeczy naraz:

if age >= 18 and has_ticket:
    print("Możesz wejść")


## Po co są operatory logiczne 


Operatory logiczne pozwalają tworzyć bardziej realistyczne decyzje.

Przykłady:

użytkownik może wejść, jeśli ma 18 lat i ma bilet,
zamówienie ma darmową dostawę, jeśli wartość jest powyżej 200 zł lub użytkownik ma kod,
program pokazuje ostrzeżenie, jeśli konto nie jest aktywne,
plik danych można przetwarzać, jeśli ma więcej niż 0 wierszy i ma mało błędów.

## 3. Operator and

and oznacza „i” albo „oraz”.

Warunek z and jest prawdziwy tylko wtedy, gdy wszystkie części warunku są prawdziwe.

Przykład:

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Możesz wejść.")
else:
    print("Nie możesz wejść.")

W tym przykładzie program sprawdza dwie rzeczy:

Czy age >= 18?
Czy has_ticket jest True?

Tylko jeśli oba warunki są prawdziwe, cały warunek jest prawdziwy.

4. Tabela prawdy dla and
Warunek A	Warunek B	A and B
True	True	True
True	False	False
False	True	False
False	False	False

Wniosek:

Przy and wszystko musi być prawdziwe.

5. Przykład and w danych
rows_count = 1000
error_percent = 2.5

if rows_count > 0 and error_percent <= 5:
    print("Plik można przetwarzać.")
else:
    print("Plik wymaga sprawdzenia.")

Znaczenie:

Plik można przetwarzać tylko wtedy, gdy:

ma więcej niż 0 wierszy,
procent błędów jest mniejszy lub równy 5.
6. Operator or

or oznacza „lub”.

Warunek z or jest prawdziwy wtedy, gdy przynajmniej jedna część warunku jest prawdziwa.

Przykład:

order_value = 250
has_free_shipping_code = False

if order_value >= 200 or has_free_shipping_code:
    print("Darmowa dostawa.")
else:
    print("Dostawa płatna.")

W tym przykładzie darmowa dostawa przysługuje, jeśli:

zamówienie ma wartość co najmniej 200 zł,
lub użytkownik ma kod darmowej dostawy.

Wystarczy jeden prawdziwy warunek.

7. Tabela prawdy dla or
Warunek A	Warunek B	A or B
True	True	True
True	False	True
False	True	True
False	False	False

Wniosek:

Przy or wystarczy jedna prawda.

8. Operator not

not oznacza „nie”.

Odwraca wartość logiczną.

not True

daje:

False

A:

not False

daje:

True

Przykład:

is_active = False

if not is_active:
    print("Konto jest nieaktywne.")
else:
    print("Konto jest aktywne.")

Znaczenie:

Jeśli konto nie jest aktywne, pokaż komunikat.

9. Tabela prawdy dla not
Wartość	not Wartość
True	False
False	True

Wniosek:

not odwraca warunek.

10. Łączenie kilku warunków

Można łączyć więcej niż dwa warunki.

Przykład:

rows_count = 1000
error_percent = 2.5
file_name = "orders.csv"

if rows_count > 0 and error_percent <= 5 and file_name != "":
    print("Plik wygląda poprawnie.")
else:
    print("Plik wymaga sprawdzenia.")

Znaczenie:

Plik wygląda poprawnie, jeśli:

ma więcej niż 0 wierszy,
ma maksymalnie 5% błędów,
ma nazwę pliku.
11. Czytelność warunków

Długie warunki mogą być trudne do czytania.

Mniej czytelnie:

if rows_count > 0 and error_percent <= 5 and file_name != "":
    print("OK")

Czytelniej:

has_rows = rows_count > 0
has_acceptable_errors = error_percent <= 5
has_file_name = file_name != ""

if has_rows and has_acceptable_errors and has_file_name:
    print("OK")

To jest dobra praktyka, bo nazwy zmiennych tłumaczą logikę programu.

12. Nawiasy w warunkach

Nawiasy pomagają jasno pokazać, jak ma być rozumiany warunek.

Przykład:

if (order_value >= 200 or has_free_shipping_code) and is_paid:
    print("Zamówienie może mieć darmową dostawę.")

Znaczenie:

Darmowa dostawa jest możliwa, jeśli:

zamówienie ma wartość co najmniej 200 zł lub użytkownik ma kod,
oraz zamówienie jest opłacone.

Nawiasy pomagają uniknąć pomyłek.

13. Różnica między and i or

and wymaga, żeby wszystko było prawdziwe.

or wymaga, żeby przynajmniej jedna rzecz była prawdziwa.

Przykład z and:

if is_paid and has_valid_address:
    print("Można wysłać.")

Zamówienie można wysłać tylko wtedy, gdy jest opłacone i ma poprawny adres.

Przykład z or:

if order_value >= 200 or has_discount_code:
    print("Darmowa dostawa.")

Darmowa dostawa jest wtedy, gdy zamówienie jest wystarczająco drogie albo użytkownik ma kod.

14. Zastosowanie w Data Engineeringu

Operatory logiczne są bardzo przydatne przy walidacji danych.

Przykłady:

Jeśli plik ma więcej niż 0 wierszy i procent błędów jest niski, można go przetwarzać.

Jeśli status zamówienia to "paid" albo "refunded", zamówienie ma rozliczony status płatności.

Jeśli rekord nie ma poprawnej ceny, trzeba go oznaczyć jako błędny.

Jeśli cena jest większa od 0 i status jest znany, rekord może przejść dalej.

Typowe kontrole danych:

czy plik nie jest pusty,
czy liczba błędów nie jest zbyt duża,
czy status jest jednym z dozwolonych,
czy cena nie jest ujemna,
czy wymagane pole nie jest puste,
czy rekord może zostać załadowany do bazy.

## 17. Najważniejsze rzeczy do zapamiętania
and oznacza, że wszystkie warunki muszą być prawdziwe.
or oznacza, że przynajmniej jeden warunek musi być prawdziwy.
not odwraca wartość logiczną.
Długie warunki warto rozbijać na mniejsze zmienne.
Przy or każde porównanie trzeba zapisać osobno.
Nawiasy poprawiają czytelność złożonych warunków.
Operatory logiczne są bardzo ważne przy walidacji danych.