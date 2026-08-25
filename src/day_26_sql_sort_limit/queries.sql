-- Zadanie 1 

SELECT order_id, customer_name, total_amount
FROM orders
ORDER BY total_amount ASC;

-- Dlaczego pierwszy rekord ma 1005? Ponieważ ma najmniejszą wartość, a ASC - czyli idziemy od najmniejszego. 

-- Zadanie 2 

SELECT order_id, customer_name, total_amount
FROM orders
ORDER BY total_amount DESC; 

-- Zadanie 3 

SELECT order_id, customer_name, city, total_amount
FROM orders
ORDER BY city, total_amount DESC, order_id;

-- Kryterium główne to City, pierwszy remis rozstrzyga total_amount od najwyższej wartości 

-- Zadanie 4 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE status = 'paid'
ORDER BY total_amount DESC;

-- Zadanie 5 

SELECT order_id, customer_name, total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;

-- Zadanie 6 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE status = 'paid'
ORDER BY total_amount
LIMIT 4;

-- Zadanie 7 

SELECT order_id, customer_name, city, total_amount
FROM orders
WHERE city IN ('Gdańsk', 'Gdynia')
ORDER BY city, order_id;

-- Zadanie 8

SELECT order_id, customer_name, status, total_amount
FROM orders
WHERE status IN ('pending', 'cancelled')
ORDER BY total_amount DESC;

-- Dłuższy warunek wyglądałoby tak, że musiałbym użyć dwa razy słowa status - status = '...' OR status = '...' 

-- Zadanie 9 

SELECT order_id, customer_name, city
FROM orders 
WHERE city NOT IN ('Kartuzy', 'SOPOT')
ORDER BY order_id;

-- Zadanie 10

SELECT order_id, customer_name, total_amount
FROM orders
WHERE total_amount BETWEEN 120 AND 260
ORDER BY total_amount;

-- Zadanie 11 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE total_amount NOT BETWEEN 100 AND 300
ORDER BY total_amount;

-- Zadanie 12 

SELECT order_id, customer_name, total_amount, status, city 
FROM orders
WHERE status IN ('paid', 'pending') AND total_amount BETWEEN 100 AND 500 AND city NOT IN ('Kartuzy')
ORDER BY total_amount DESC
LIMIT 4;

-- Zadanie 13 Własne pytania 

-- 1 

SELECT order_id, customer_name, total_amount
FROM orders
WHERE status IN ('cancelled')
ORDER BY order_id, total_amount DESC;
LIMIT 5;

-- 2 

SELECT order_id, customer_name, city, status
FROM orders
WHERE status NOT IN ('paid') AND city NOT IN ('Kartuzy')
ORDER BY customer_name
LIMIT 3;

-- 3 

SELECT order_id, status, total_amount
FROM orders 
WHERE status NOT IN ('pending') AND total_amount BETWEEN 250 AND 500
ORDER BY order_id, total_amount DESC, status DESC;

-- Zadanie dodatkowe 

-- A - Będą 3 wiersze. Kolumny order_id, customer_name, total_amount, 3 najniższe kwoty

-- B - Kolumny - order_id, status, total_amount - Zamówienia będą z statuem paid i cancelled oraz z kwotami powyżej 200 do 400 włącznie. Będą posegregowane malejąco, od najniższej 

-- C Kolumny - order_id, customer_name, city - Zamówienia będą takie, której nie mają Gdańska i Gdyni w city, posegregowane rosnąco po mieście, w przypadku remisu, po numerze zamówienia malejąca, będą 4 wiersze

-- D - Kolumny - order_id, customer_name, total_amount, Zamówienia gdzie ich wartość będzie do 100 włącznie oraz powyżej 400. Posegrewgowane według kwoty malejąco. 

-- Nie chce mi się dokładnie rozpisywać i sprawdzać w orders.csv dokładnie pokolei jka to będzie wyglądać, ale łapię regułę. 

-- Wyzawania diagnostyczne 

-- 1 

-- Błędna kolejność, WHERE powinno być nad ORDER BY

-- 2 

-- Błędna kolejność, LIMIT powinna być na samym końcu 

-- 3 

-- Brakuje nawiasu ('electronics', 'books')

-- 4 

-- BETWEEN jest źle zadeklarowane, BETWEEN musi być od mniejszej do większej. 

-- 5 

-- Chyba nie wiem ? Przyda się również numer zamówienia ? 