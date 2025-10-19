SELECT p.product_id, ROUND(IFNULL(sum(p.price * s.units) / SUM(s.units),0), 2) as average_price
FROM Prices as p
LEFT JOIN UnitsSold as s
ON p.product_id = s.product_id
AND s.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id


