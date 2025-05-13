SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC, first_name ASC
LIMIT 2 OFFSET (
  SELECT COUNT(*) - 2 FROM customers
);

DELETE FROM purchases
WHERE customer_id = (
  SELECT id FROM customers WHERE first_name = 'Scott'
);

SELECT * FROM customers
WHERE first_name = 'Scott';

SELECT p.id AS purchase_id,
       c.first_name,
       c.last_name
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.id;

SELECT p.id AS purchase_id,
       c.first_name,
       c.last_name
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.id;
