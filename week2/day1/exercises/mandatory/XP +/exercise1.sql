CREATE TABLE IF NOT EXISTS students2 (
  id SERIAL PRIMARY KEY,      -- Unique student ID, automatically increments
  first_name VARCHAR(50) NOT NULL,        -- First name of the student
  last_name VARCHAR(50) NOT NULL,         -- Last name of the student
  birth_date DATE NOT NULL                -- Birth date of the student
);

