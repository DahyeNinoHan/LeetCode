# Write your MySQL query statement below

SELECT P.product_name
      ,S.year
      ,S.price
FROM Sales as S JOIN 
     Product as P   
     ON S.Product_id = P.product.id
