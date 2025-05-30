--EXERCISE 1
--Get a list of all the languages, from the language table.
select * from language

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT
    film.title,
    film.description,
    language.name AS language_name
FROM
    film
JOIN
    language ON film.language_id = language.language_id;

--Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

SELECT
    film.title,
    film.description,
    language.name AS language_name
FROM
    language
LEFT JOIN
    film ON language.language_id = film.language_id;


--Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE  new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO new_film (name) VALUES ('Film 1');
INSERT INTO new_film (name) VALUES ('Film 2');
INSERT INTO new_film (name) VALUES ('Film 3');
INSERT INTO new_film (name) VALUES ('Film 4');

--Create a new table called customer_review, which will contain film reviews that customers will make.Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.It should have the following columns:
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    language_id INT NOT NULL,
    title VARCHAR(255),
    score SMALLINT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id)
);
--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES (1, 1, 'Great Movie', 9, 'I really enjoyed this film. The plot was engaging and the characters were well-developed.');
INSERT INTO customer_review (film_id, language_id, title, score, review_text)    
VALUES (2, 2, 'Good Movie', 8, 'I liked this film. The plot was interesting and the characters were well-crafted.');


--Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;

--When this runs, the review for id = 1 will be automatically deleted from customer_review due to the ON DELETE CASCADE constraint. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Exercise 2 : DVD Rental

--Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film 
SET language_id = 2 
WHERE film_id IN (1, 2, 3)
AND EXISTS (SELECT 1 FROM language WHERE language_id = 2);



---- The foreign keys defined for the customer table are (store_id - address_id).
---When inserting into the customer table, we must ensure that all foreign key values already exist in the referenced tables to maintain referential integrity. 



---We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;
---Dropping the customer_review table may seem like a simple step, but it can require extra checking if the table is referenced by foreign keys in other tables or contains important data that should be backed up before deletion.

--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) 
FROM rental 
WHERE return_date IS NULL;
 
--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

SELECT DISTINCT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' 
AND a.last_name = 'Monroe'
AND f.description ILIKE '%sumo wrestler%';

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Documentary'
AND f.rating = 'R'
AND f.length < 60;
 
--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT DISTINCT f.title
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN payment p ON r.rental_id = p.rental_id
WHERE c.first_name = 'Matthew' 
AND c.last_name = 'Mahan'
AND p.amount > 4.00
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';
 
--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace
SELECT DISTINCT f.title, f.description,f.replacement_cost
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' 
  AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;

 