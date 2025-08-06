# Write your MySQL query statement below
SELECT C.class FROM 
(SELECT class, COUNT(student) AS student_count 
    FROM Courses 
    GROUP BY class
    HAVING student_count >=5
) AS C;