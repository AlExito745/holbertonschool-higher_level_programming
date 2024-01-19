-- List all records of a table in a database of MySQL Server.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC
LIMIT 10;
