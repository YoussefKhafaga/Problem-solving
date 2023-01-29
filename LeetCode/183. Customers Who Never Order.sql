# Write your MySQL query statement below
SELECT name as Customers from Customers where Customers.id not in ( select Customers.id from Customers, Orders where Customers.id = Orders.customerId);