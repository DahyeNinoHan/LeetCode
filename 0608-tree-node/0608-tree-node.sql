# Write your MySQL query statement below

SELECT id
      ,CASE 
            WHEN p_id IS NULL THEN 'Root'
            WHEN id NOT IN (SELECT p_id FROM TREE WHERE p_id IS NOT NULL) THEN 'Leaf'
            ELSE 'Inner'
       END AS type
FROM Tree