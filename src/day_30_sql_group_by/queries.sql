-- Zadanie do poprzedniej lekcji - 5 pytań biznesowych 

-- 1 Ile zamówień z statusem paid pochodzi z Gdańska albo Gdynii

SELECT COUNT(*) AS paid_orders
FROM orders
WHERE status = 'paid' AND city IN('Gdańsk', 'Gdynia'); 

-- 2 Jaka jest łączna wartość zamówień 

SELECT SUM(total_amount) AS sum_total_amount
FROM orders 
WHERE status != 'cancelled' AND total_amount BETWEEN 100 AND 300;

-- 3 Jaka jest średnia wartość zamówień ze statusem paid, z Kartuz lub Sopotu. 

SELECT ROUND(AVG(total_amount), 2) AS average_amount
FROM orders
WHERE status = 'paid' AND city IN ('Kartuzy', 'Sopot');

-- 4 Jaka jest najniższa wartość zamówienia z statusem pending pochodzącego z Gdańska lub Gdynii

SELECT MIN(total_amount) AS min_order
FROM orders
WHERE status = 'pending' AND city IN ('Gdańsk', 'Gdynia');

-- 5 Jaka jest najwyższa wartość zamówienai które, ma status pending albo cancelled, pochodzi z Kartuz albo Sopotu, ma wartość od 50 do 350 włącznie

SELECT MAX(total_amount) AS max_order
FROM orders
WHERE status IN ('pending', 'cancelled') AND city IN ('Kartuzy', 'Sopot') AND total_amount BETWEEN 50 AND 350;

-- Zadanie 1 właściwe

SELECT *
FROM orders
ORDER BY order_id ASC;

-- Liczba rekordów 12, Liczba kolumn 5, paid, cancelled, pending, Gdańsk Gdynia Kartuzy Sopot, no już nie bedę rećznie liczył.

-- Zadanie 2 

SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY status ASC;

-- Wynik ma 3 wiersze, ponieważ są trzy statusy, i zliczamy po tych 3 statusach COUNTEM ile jest w naszym orders tych statusów
-- Jeden wiersz reprezentuje status i ile razy ten status jest w naszej tabeli orders
-- Bo każdy ma status.  

-- Zadanie 3 

SELECT
    status,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC, status;

-- Pending jest przed cancelled, bo ma wyższą wartość zamówień, a sortujemy po wartości zamówień. 
-- Nie wpływa 

-- Zadanie 4 

SELECT
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount,
    MIN(total_amount) AS minimum_amount,
    MAX(total_amount) AS maximum_amount
FROM orders
GROUP BY status
ORDER BY status;

-- Każda agregacja widzi inny zbiór, bo jest robiona najpierw GROUP BY. 

-- Zadanie 5 

SELECT
    city,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount
FROM orders
GROUP BY city
ORDER BY average_amount DESC, city ASC;

-- Nie musi mieć najwyżeszej średniej, licza się zamówienia dzielone przez ich ilość a nie liczba zamówień. 

-- Zadanie 6 

SELECT 
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
WHERE total_amount >= 100
GROUP BY status 
ORDER BY status;

-- Rekordy z mniejszą kwotą zamówienia od 100. Bo w każdym z tych statusów jest przynajmniej jedno zamówienie z wartością powyżej 100
-- Nie, Where wykonuje się pierwsze

-- Zadanie 7 

SELECT
    city,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount
FROM orders
WHERE city IN ('Gdańsk', 'Gdynia')
GROUP BY city
ORDER BY city;

-- Ponieważ zrobiliśmy where gdzie wskazaliśmy konkretne miasta w których chcemy używać. Następnie robimy GROUP BY , a następnie agregacje. Na końcu sortujemy

-- Zadanie 8 

SELECT
    city,
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY city, status
ORDER BY status, city;

-- Bo taka nie istnieje, najwyraźniej nie istnieje taki przypadek że w Gdańsku anulowano zamówienie. 
-- Bo tworzy pary, muszą być identyczne. paid Kartuzy , to nie to samo co paid Gdańsk 
-- Reprezentuje pasujące do siebie statusy i miasta. Ile razy występuję określona para w orders. 

-- Zadanie 9 

SELECT 
    status,
    city,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount,
    MIN(total_amount) AS minimum_amount,
    MAX(total_amount) AS maximum_amount
FROM orders
WHERE status IN ('paid', 'pending') AND total_amount BETWEEN 100 AND 500 AND city != 'Kartuzy'
GROUP BY status, city
ORDER BY status, city;

-- 6 rekordów dało 4 wiersze bo tyle jest par, które spełniają warunek
-- Nie wystepuję, bo najwyraźniej nie pasuje do warunku. Kwota poniżej 100 jak teraz patrzę.
-- Widziały grupy pasujące do najpierw WHERE a potem GROUP BY, także widziały inne pary. 

-- Zadanie 10 

SELECT
    customer_name,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount
FROM orders
GROUP BY customer_name
ORDER BY total_revenue DESC, customer_name ASC;

-- Wynik ma 9 wierszy, bo powtarzają się imiona, a grupujemy po imieniu
-- Niekoniecznie, jakbyśmy mieli klienta z jednym zamówieniem za 1000 zł, a drugiego z dwudziestoma po 100 zł, a ten z dwudziestoma miałby największą sumę
-- Bo imiona mogą w prawdziwym życiu się powtarzać, nawet bardzo często. Co zepsuje wyniki. 

-- Zadanie 11

SELECT
    customer_name,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY customer_name
ORDER BY total_revenue DESC, customer_name ASC
LIMIT 3;

-- rekordów wejściowcyh grupowanie widziało wszystkie czyli 12
-- Tyle ile imion, czyli chyba 9 z tego co kojarzę z poprzednich zadań
-- 3
-- Wykonuje się na końcu po grupowaniu, where i sortowaniu 

-- Zadanie 12 

SELECT COUNT(*) AS order_count
FROM orders;

SELECT SUM(total_amount) AS total_revenue
FROM orders;

-- Wszystko się zgadza
-- Brak zgodności może oznaczać że jakieś wartości są puste
-- To samo ^ 

-- Zadanie 13 - zrobię je jutro razem z Pandas

-- Zadania dodatkowe 

-- A: wejście 12; grupy 3; wynik 3x2; pierwsza paid, ostatnia cancelled.
-- Jeden wiersz = status i liczba jego zamówień. Tabela bez zmian.

-- B: wejście 7; grupy 4; wynik 4x2; pierwsza Gdańsk, ostatnia Sopot.
-- Jeden wiersz = miasto i suma opłaconych zamówień. Tabela bez zmian.

-- C: wejście 4; grupy 4; wynik 4x3.
-- Pierwsza grupa: cancelled + Kartuzy; ostatnia: pending + Kartuzy.
-- Jeden wiersz = para status-miasto i liczba zamówień. Tabela bez zmian.

-- D: wejście 12; grupy 9; po LIMIT wynik 2x2.
-- Pierwszy Tomasz, ostatni Piotr.
-- Jeden wiersz = klient i jego największe zamówienie. Tabela bez zmian.

-- E: wejście 12; grupy 3; wynik 3x2; pierwsza cancelled, ostatnia pending.
-- Jeden wiersz = status i liczba niepustych kwot. Tabela bez zmian.

-- Po uruchomieniu: brak różnic względem przewidywań. 

-- 1. SQLite wykona zapytanie i zwróci 1 wiersz.
-- COUNT policzy wszystkie zamówienia, a status będzie przypadkowy.
-- Wynik biznesowo błędny. Należy grupować po statusie.

-- 2. SQLite wykona zapytanie i zwróci 3 wiersze.
-- Liczby dla statusów będą poprawne, ale customer_name będzie przypadkowy.
-- Należy usunąć customer_name albo dodać go do GROUP BY.

-- 3. SQLite nie wykona zapytania; wynik 0 wierszy.
-- WHERE jest w złym miejscu. Musi znajdować się przed GROUP BY.

-- 4. SQLite nie wykona zapytania; wynik 0 wierszy.
-- WHERE nie służy do filtrowania wyników agregacji.
-- Warunek z COUNT(*) należy umieścić w HAVING.

-- 5. SQLite nie wykona zapytania; wynik 0 wierszy.
-- Funkcji agregującej nie można używać w GROUP BY.
-- Należy grupować po zwykłej kolumnie, np. statusie.

-- 6. SQLite wykona zapytanie i zwróci 2 wiersze.
-- Wynik poprawnie pokazuje dwa najliczniejsze statusy.
-- COUNT analizuje wszystkie zamówienia, a LIMIT ogranicza gotowe grupy.

-- 7. SQLite wykona zapytanie i zwróci 9 wierszy.
-- Jeden wiersz oznacza parę status-miasto.
-- Wynik jest poprawny, ale dla pełnego porządku warto sortować też po city.

-- 8. SQLite wykona zapytanie i zwróci 4 wiersze.
-- Suma dla miasta będzie poprawna, ale status może być przypadkowy.
-- Należy usunąć status albo grupować jednocześnie po city i status.

-- Quiz 

-- 1. C
-- 2. customer-name 
-- 3. C
-- 4. B
-- 5. B

