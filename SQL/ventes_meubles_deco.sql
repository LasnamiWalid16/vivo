SELECT 
    client_id,
    SUM(CASE WHEN P.product_type LIKE 'MEUBLE' THEN prod_price * prod_qty ELSE 0)  AS ventes_meuble,
    SUM(CASE WHEN P.product_type LIKE 'DECO' THEN prod_price * prod_qty ELSE 0)   AS ventes_deco
FROM 
    TRANSACTIONS T INNER JOIN PRODUCT_NOMENCLATURE P ON T.prop_id = P.prop_id
WHERE 
     P.product_type IN ('MEUBLE','DECO')
GROUP BY  
    client_id