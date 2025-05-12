--CREATE DATABASE Hollywood;

CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt','Damon','1970-10-08', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('George','Clooney','1961-05-06', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
('Leonardo', 'DiCaprio', '1974-11-11', 1),
('Tom', 'Hanks', '1956-07-09', 2),
('Brad', 'Pitt', '1963-12-18', 2);

--1. Count how many actors are in the table.
SELECT COUNT(*) FROM actors;

--2 Try to add a new actor with some blank fields. What do you think the outcome will be ?
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('', '', NULL, NULL);
-- The outcome will be an error because the first_name and last_name fields cannot be blank or NULL due to the NOT NULL constraint.