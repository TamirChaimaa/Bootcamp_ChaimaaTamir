-- ====================
-- SELECT QUERIES CONTINUATION
-- ====================

-- 1. Fetch the first four students, ordered alphabetically by last name
SELECT first_name, last_name, birth_date FROM students
ORDER BY last_name
LIMIT 4;

-- 2. Fetch the details of the youngest student (youngest based on birth_date)
SELECT first_name, last_name, birth_date FROM students
ORDER BY birth_date DESC
LIMIT 1;

-- 3. Fetch three students, skipping the first two students (using OFFSET and LIMIT)
SELECT first_name, last_name, birth_date FROM students
ORDER BY last_name
LIMIT 3 OFFSET 2;