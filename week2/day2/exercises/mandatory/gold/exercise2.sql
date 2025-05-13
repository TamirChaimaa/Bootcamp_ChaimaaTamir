-- ========================
-- UPDATE
-- ========================
UPDATE students
SET birth_date = '1998-11-02'
WHERE (first_name = 'Lea' AND last_name = 'Benichou')
   OR (first_name = 'Marc' AND last_name = 'Benichou');

UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

-- ========================
-- DELETE
-- ========================
DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- ========================
-- COUNT
-- ========================
-- Total number of students
SELECT COUNT(*) AS total_students FROM students;

-- Students born after 1/01/2000
SELECT COUNT(*) AS born_after_2000
FROM students
WHERE birth_date > '2000-01-01';

-- ========================
-- INSERT / ALTER
-- ========================
-- Add math_grade column (only once; if it already exists, skip this)
ALTER TABLE students ADD COLUMN math_grade INT;

-- Update math grades
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id IN (2, 4);
UPDATE students SET math_grade = 40 WHERE id = 6;

-- Count how many students have grade > 83
SELECT COUNT(*) AS students_above_83
FROM students
WHERE math_grade > 83;

-- Insert another Omer Simpson with same birth_date as existing
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT 'Omer', 'Simpson', birth_date, 70
FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;

-- ========================
-- BONUS: Count grades per student
-- ========================
SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

-- ========================
-- SUM of grades
-- ========================
SELECT SUM(math_grade) AS total_sum_math_grade
FROM students;
