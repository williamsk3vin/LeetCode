Select V.customer_id, count(V.visit_id) as count_no_trans
FROM Visits as V
LEFT JOIN Transactions as T
ON V.visit_id = T.visit_id
WHERE T.visit_id IS NULL
GROUP BY V.customer_id
