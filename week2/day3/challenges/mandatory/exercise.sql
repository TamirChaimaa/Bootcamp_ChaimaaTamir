--Part I
--1
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,        
    first_name VARCHAR(100) NOT NULL, 
    last_name VARCHAR(100) NOT NULL 
);

CREATE TABLE Customer_profile (
    id SERIAL PRIMARY KEY,        
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT UNIQUE,        
    FOREIGN KEY (customer_id) REFERENCES Customer(id) 
);

--2

INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

--3
INSERT INTO Customer_profile (customer_id, isLoggedIn) VALUES
    ((SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe'), true),
    ((SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'), false);

--Part II
--1
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

--2
INSERT INTO Book (title, author)
VALUES
  ('Alice In Wonderland', 'Lewis Carroll'),
  ('Harry Potter', 'J.K. Rowling'),
  ('To Kill a Mockingbird', 'Harper Lee');

--3

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    CONSTRAINT age_check CHECK (age <= 15)
);

--4
INSERT INTO Student (name, age)
VALUES
  ('John', 12),
  ('Lera', 11),
  ('Patrick', 10),
  ('Bob', 14);
--5
CREATE TABLE Library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    CONSTRAINT fk_book FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_student FOREIGN KEY (student_fk_id) REFERENCES Student(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

--6
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES 
(
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
),
(
    (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
),
(
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
),
(
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

--7
SELECT * FROM Library;
 
SELECT 
    s.name,
    b.title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;
 
SELECT AVG(s.age)
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';
 
DELETE FROM Student WHERE name = 'Bob';