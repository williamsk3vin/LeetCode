SELECT today.id
FROM Weather AS today
JOIN Weather AS yesterday
  ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;
