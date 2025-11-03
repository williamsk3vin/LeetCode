SELECT 
  ROUND(
    (
      (SELECT COUNT(*) 
       FROM Delivery
       WHERE (customer_id, order_date) IN (
               SELECT customer_id, MIN(order_date)
               FROM Delivery
               GROUP BY customer_id
             )
         AND order_date = customer_pref_delivery_date)
      /
      (SELECT COUNT(DISTINCT customer_id)
       FROM Delivery)
    ) * 100
  , 2) AS immediate_percentage;
