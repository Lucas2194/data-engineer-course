-- Zadanie 1 

SELECT *
FROM orders; 

-- Zadanie 2 

SELECT order_id, customer_name, status
FROM orders;

-- Zadanie 3 

SELECT * 
FROM orders
WHERE status = 'paid';

-- Zadanie 4 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE total_amount > 200;

-- Zadanie 5

SELECT customer_name, city, status
FROM orders
WHERE city = 'Gdańsk';

-- Zadanie 6 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE status = 'paid' AND total_amount > 150;

-- Zadanie 7 

SELECT order_id, customer_name, status
FROM orders
WHERE status = 'pending' OR status = 'cancelled';

-- Zadanie 8 

SELECT order_id, customer_name, city
FROM orders
WHERE city != 'Kartuzy';

-- Zadanie 9 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE total_amount > 100 AND total_amount <= 300 ;

--

SELECT order_id, customer_name
FROM orders 
WHERE customer_name = 'Anna';

-- 

SELECT order_id, customer_name, status 
FROM orders 
WHERE status = 'paid' AND customer_name != 'Anna'

-- Zadanie dodatkowe

-- A - kolumny customer_name, total_amount, 4 wiersze 
-- B - Kolumny order_id, status, 1 wiersz, 
-- C - kolumny customer_name, city, 5 wierszy 