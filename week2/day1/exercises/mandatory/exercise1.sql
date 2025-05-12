-- Database: public

CREATE DATABASE public;

    CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10, 2)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

--1 Add the following items to the items table:
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);


--2 Add 5 new customers to the customers table
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

--3 Add 5 new customers to the customers table

   --1 All the items
    SELECT * FROM items;

   --2 All the items with a price above 80 (80 not included).
    SELECT * FROM items WHERE price >80;
 
    --3 All the items with a price below 300. (300 included)
    SELECT * FROM items WHERE price <= 300;

    --4 All customers whose last name is ‘Smith’ (What will be your outcome?).
    SELECT  * From customers WHERE last_name = 'Smith';
    -- There is no customer with last name Smith, so the outcome will be an empty set.

    --5 All customers whose last name is ‘Jones’.
    SELECT * FROM customers WHERE last_name = 'Jones';

    --6 All customers whose firstname is not ‘Scott’.
    SELECT * FROM customers WHERE first_name <> 'Scott';

    

