-- Zadanie 1 

SELECT *
FROM orders
ORDER BY order_id ASC;

-- Liczba wierszy - 12 , liczba kolumn 5, pierwszy order id - 1001, ostatni - 1012, paid, pending, cancelled

-- Zadanie 2 

SELECT COUNT(*) AS order_count
FROM orders; 

-- Przewiduje liczbę wierszy - 1, wartość 12 
-- Właśnie dlatego pokazuje 1 wiersz z wartością 12. COUNT(*) zlicza rekordy

-- Zadanie 3 

SELECT COUNT(*) AS paid_order_count
FROM orders
WHERE status = 'paid';

-- FROM -> WHERE -> COUNT 

-- Zadanie 4

SELECT COUNT(*) AS unfinished_or_cancelled_count
FROM orders
WHERE status IN('pending', 'cancelled');

-- Zadanie 5 

SELECT COUNT(*) AS selected_order_count
FROM orders
WHERE status IN('paid', 'pending') AND total_amount BETWEEN 100 AND 500 AND city != 'Kartuzy';

-- Zadanie 6

SELECT SUM(total_amount) AS total_revenue
FROM orders;

-- 1 - Nie możemy z wszystkich kolumn policzyć sumy, jedynie z tych liczbowych. Nie miałoby to sensu. SUM() nie zmienia danych w tabeli. 3 - 12

-- Zadanie 7 

SELECT SUM(total_amount) AS paid_revenue
FROM orders
WHERE status = 'paid';

-- Wynik jest mniejszych od wszystkich, ponieważ są inne statusy które podbijają cenę. A my sumujemy jedynie opłacone. 

-- Zadanie 8 - A 

SELECT AVG(total_amount) AS raw_average_amount
FROM orders;

-- Zadanie 8 - B 

SELECT ROUND(AVG(total_amount), 2) AS average_amount
FROM orders;

-- 1 - Agregację wynikuje funkcja AVG() , 2 - ROUND() , 3- Nie zmienia

-- Zadanie 9 

SELECT ROUND(AVG(total_amount), 2) AS pending_average_amount
FROM orders 
WHERE status = 'pending';

-- Zadanie 10 

SELECT MIN(total_amount) AS minimum_amount, MAX(total_amount) AS maximum_amount
FROM orders;

-- Nie mówi, jedynie najmniejsza i największa wartość

-- Zadanie 11 

SELECT 
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue, 
    ROUND(AVG(total_amount), 2) AS average_amount,
    MIN(total_amount) AS minimum_amount,
    MAX(total_amount) AS maximum_amount
FROM orders;

-- Zadanie 12 

SELECT 
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount,
    MIN(total_amount) AS minimum_amount,
    MAX(total_amount) AS maximum_amoun
FROM orders
WHERE status IN ('pending', 'paid') AND total_amount BETWEEN 100 AND 500 AND city != 'Kartuzy';

-- 5 - tyle co funkcji agregujących, Jeden wiersz bo to podsumowania - funkcje agregujące - Tak, wszystkie widziały ten sam zbiór 

-- Zadanie 13 

SELECT 
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_amount,
    MIN(total_amount) AS minimum_amount,
    MAX(total_amount) AS maximum_amoun
FROM orders
WHERE status = 'returned';

-- Bo nie znalazł żadnych danych. Bo to nadal funkcje agregujące. Bo nie da się zsumować danych których nie ma. Tak. 0 to 0. NULL to tak jakby brak. 

-- Zadanie 14

SELECT COUNT(*) as all_row_count, COUNT(total_amount) AS known_amount_count
FROM orders;

-- Bo nie ma żadnej wartości NULL w pliku orders.csv, różniłby się, jakby jakaś wartość miała NULL

-- Zadanie 15

SELECT COUNT(*) as paid_orders
FROM orders
WHERE status = 'paid';

SELECT COUNT(*) as pending_orders
FROM orders
WHERE status = 'pending';

SELECT COUNT(*) as cancelled_orders
FROM orders
WHERE status = 'cancelled';

-- Zadanie 16

SELECT SUM(total_amount) as sum_paid_orders
FROM orders
WHERE status = 'paid';

SELECT SUM(total_amount) as sum_pending_orders
FROM orders
WHERE status = 'pending';

SELECT SUM(total_amount) as sum_cancelled_orders
FROM orders
WHERE status = 'cancelled';

-- Własne biznesowo ułoże już jutro, przed jutrzejszą lekcją, dzisiaj trochę już zmęczony, się zaraz kładę spać. 

-- Zadanie dodatkowe 

-- A - Agregując
-- B - SELECT - WHERE 
-- C - Agregująca
-- D - SELECT - ORDER BY - LIMIT
-- E - Agregująca 
-- F - SELECT - WHERE - ORDER BY - LIMIT 

-- Zadanie dodatkowe kolejne - przewidywanie wyniku 

-- A - 1, 1, row_count, 12, nie 
-- B - 1, 1, total_amount, suma zamówień o statusie cancelled, nie 
-- C - 1, 2 , minimum_amount, maximum_amount, Najmniejsza i największa wartość zamówień, z miast Gdańska i Gdynii, Nie
-- D - 1,1, average_amount, średnia wartość z zamówień gdzie ich wartość jest pomiędzy 100 i 300 włącznie , nie
-- E - 1, 2, row_count, total_amount, Liczba zamówień i suma wartości gdzie status jest unknown, tutaj akurat wiem że takiego statusu nie ma, także wynik będzie 0 i NULL, NIe

-- Wyzwanie diagnostyczne 

-- 1 - Brak nawiasów przy count, powinno być (*) , albo (nazwa kolumny)
-- 2 - SUM nie może być z (*), bo to funkcja agregująca licząca, trzeba wskazać kolumnę liczbową aby mogła dokonać obliczenia
-- 3 - brak przecinka 
-- 4 - nie dajemy nazwy kolumny i funkcji agregującej przy SELECT
-- 5 - Jest to bez sensu i marnotrastwo bo wynik i tak będzie zawsze jednym wierszem. Źle twierdzi. 
-- 6 -  ORDER BY nie jest konieczne, również jest marnotrastwem 
-- 7 - Zwróci, tylko zwróci NULL - nie dało się policzyć. 
-- 8 - Niestety nie jest, nie można jak wyżej wspomniałem łączyć w SELECT nazw kolumn i funkcji agregującej w ten sposób. 

-- QUIZ 

-- 1 - B
-- 2 - C 
-- 3 - C 
-- 4 - B 
-- 5 - C 

