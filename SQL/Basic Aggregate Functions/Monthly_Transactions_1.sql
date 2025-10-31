SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, 
    country, 
    COUNT(id) AS trans_count,
    sum(state = 'approved') as approved_count,
    sum(amount) as trans_total_amount,
    SUM(amount * (state = 'approved')) AS approved_total_amount
FROM Transactions
GROUP BY month, country
