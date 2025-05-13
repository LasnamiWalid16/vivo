SELECT 
  date AS date, 
  SUM(prod_price * prod_qty) AS ventes
FROM 
  TRANSACTIONS
WHERE 
  date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
  1
ORDER BY 
  date ASC;
