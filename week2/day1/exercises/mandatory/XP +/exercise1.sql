-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS bootcamp;

-- Select the database to use
USE bootcamp;

-- Create the students table if it doesn't already exist
CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique student ID, automatically increments
  first_name VARCHAR(50) NOT NULL,        -- First name of the student
  last_name VARCHAR(50) NOT NULL,         -- Last name of the student
  birth_date DATE NOT NULL                -- Birth date of the student
);

-- Insert data into the students table
INSERT INTO students (first_name, last_name, birth_date)
VALUES 
  ('Marc', 'Benichou', '1998-11-02'),
  ('Yoan', 'Cohen', '2010-12-03'),
  ('Lea', 'Benichou', '1987-07-27'),
  ('Amelia', 'Dux', '1996-04-07'),
  ('David', 'Grez', '2003-06-14'),
  ('Omer', 'Simpson', '1980-10-03'),
  --   personal entry 
  ('Chaimaa', 'Tamir', '2001-04-13');

-- ====================
-- SELECT QUERIES
-- ====================

-- 1. Retrieve all data from the students table
SELECT * FROM students;

-- 2. Retrieve only first names and last names of all students
SELECT first_name, last_name FROM students;

-- 3. Retrieve the student whose id is 2
SELECT first_name, last_name FROM students WHERE id = 2;

-- 4. Retrieve the student named Marc Benichou
SELECT first_name, last_name FROM students 
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- 5. Retrieve students with the last name Benichou or the first name Marc
SELECT first_name, last_name FROM students 
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- 6. Retrieve students whose first name contains the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a%';

-- 7. Retrieve students whose first name starts with the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name LIKE 'a%';

-- 8. Retrieve students whose first name ends with the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a';

-- 9. Retrieve students whose second-to-last letter of the first name is 'a'
SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a_';

-- 10. Retrieve students whose id is either 1 or 3
SELECT first_name, last_name FROM students 
WHERE id IN (1, 3);

-- 11. Retrieve students born on or after January 1, 2000
SELECT * FROM students 
WHERE birth_date >= '2000-01-01';
