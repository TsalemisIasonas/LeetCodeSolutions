# Write your MySQL query statement below
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    Employee e
JOIN
    Department d ON e.departmentId = d.id
JOIN
    (SELECT departmentId, MAX(salary) AS max_salary
     FROM Employee
     GROUP BY departmentId) AS MaxSalaries
     ON e.departmentId = MaxSalaries.departmentId
     AND e.salary = MaxSalaries.max_salary;