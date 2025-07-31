# Write your MySQL query statement below
SELECT c.name AS 'Customers'
FROM Customers c
LEFT JOIN Orders ON Orders.customerId = c.Id
WHERE Orders.customerId IS NULL;