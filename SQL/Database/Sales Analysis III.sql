SELECT distinct s.product_id, p.product_name
FROM Product p
LEFT JOIN Sales s
ON p.product_id = s.product_id
WHERE s.sale_date between '2019-01-01' AND '2019-03-31'
AND p.product_id NOT IN (Select Distinct product_id from Sales where sale_date > '2019-03-31' OR sale_date < '2019-01-01' )
