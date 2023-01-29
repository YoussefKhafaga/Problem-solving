# Write your MySQL query statement below
select firstName, lastName, city, state from Person left Join Address ON Person.personId = Address.personId;