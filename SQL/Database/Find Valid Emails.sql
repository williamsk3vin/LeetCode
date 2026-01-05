SELECT user_id, email
FROM Users
WHERE email REGEXP '^[A-za-z0-9]+@[A-Za-z]+\\.com$'
ORDER BY user_id ASC
