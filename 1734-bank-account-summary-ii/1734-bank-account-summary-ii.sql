# Write your MySQL query statement below
SELECT 
    U.name AS NAME, SUM(T.amount) AS BALANCE
FROM 
    Users U
JOIN 
    Transactions T ON T.account = U.account
GROUP BY 
    T.account
HAVING 
    BALANCE > 10000;