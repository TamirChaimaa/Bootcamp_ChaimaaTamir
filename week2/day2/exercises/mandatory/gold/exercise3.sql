-- =============================
-- PART I: Create and insert into the purchases table
-- =============================

-- 1. Create the purchases table
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    item_id INT REFERENCES items(id),
    quantity_purchased INT
);

-- 2. Insert purchases using subqueries

-- Scott Scott bought 1 fan
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
    (SELECT id FROM items WHERE name ILIKE '%fan%'),
    1
);

-- Melanie Johnson bought 10 large desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
    (SELECT id FROM items WHERE name ILIKE '%large desk%'),
    10
);

-- Greg Jones bought 2 small desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
    (SELECT id FROM items WHERE name ILIKE '%small desk%'),
    2
);

-- =============================
-- PART II: Queries
-- =============================

-- 1. Get all purchases
SELECT * FROM purchases;

-- 2. Get all purchases with customer information
SELECT p.*, c.first_name, c.last_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id;

-- 3. Get all purchases made by the customer with ID = 5
SELECT * FROM purchases
WHERE customer_id = 5;

-- 4. Get all purchases of a large desk AND a small desk
SELECT * FROM purchases
WHERE item_id IN (
    SELECT id FROM items WHERE name ILIKE '%large desk%' OR name ILIKE '%small desk%'
);

-- 5. Show all customers who have made a purchase, including item name
SELECT c.first_name, c.last_name, i.name AS item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id
JOIN items i ON p.item_id = i.id;

-- 6. Insert a row with a valid customer_id but no item_id
-- This will only work if item_id accepts NULL values

-- Try to insert a row with NULL item_id
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 3);

-- Note: If item_id is NOT NULL, the above insert will fail with an error:
-- ERROR: null value in column "item_id" violates not-null constraint

-- If needed, you can allow NULL values in item_id like this:
-- ALTER TABLE purchases ALTER COLUMN item_id DROP NOT NULL;
