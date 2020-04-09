USE sakila;
select * from actor;
select first_name,last_name from actor;
---q2--
select CONCAT(`first_name`,' ', `last_name`) AS 'Actor Name'  FROM actor;
---q3---
select actor_id,first_name,last_name from actor
where first_name = 'Joe';
----q3---

select * from actor
where last_name LIKE '%GEN%';

---q4--
select * from actor
where last_name LIKE '%LI%';
order by last_name,first_name;

---q5--
select * from country
where country in ('Afghanistan', 'Bangladesh','China');

---4a---
select last_name , count(last_name) from actor
group by last_name;

---4b---
select last_name , count(last_name) from actor
group by last_name
having count(last_name)>1;

--6a--
select * from staff;
select * from address;

select staff.first_name,staff.last_name,address.address_id
from adress
inner join staff
where staff.address_id = address.address_id;

--6b--
select * from staff ; 
select * from payment ; 
select staff.first_name,staff.last_name,sum(payment.amount)
from staff
inner join payment
where staff.staff_id = payment.staff_id and payment_date like '2005-08%';

--6c--
select * from film;
select * from film_actor;
select film.title , count(film_actor.actor_id) as 'total number'
from film
inner join film_actor
where film.film_id = film_actor.film_id
group by film.title;

---6d--
select * from film;
select * from inventory;
