--Exercise 1
--Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?

SELECT *
FROM rental
WHERE return_date IS NULL;

--Get a list of all customers who have not returned their rentals. Make sure to group your results.
SELECT customer_id, COUNT(*) AS rental_count
FROM rental
WHERE return_date IS NULL
GROUP BY customer_id;

SELECT f.film_id, f.title 
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
AND c.name = 'Action';
 
CREATE VIEW action_films_with_joe_swank AS 
SELECT f.film_id, f.title 
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
AND c.name = 'Action';
 
SELECT * FROM action_films_with_joe_swank;