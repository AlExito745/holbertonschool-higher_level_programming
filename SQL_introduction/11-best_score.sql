-- List all records with a score >= 10 in a table of database of MySQL Server.
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC
WHERE `score` >= 10
LIMIT 10;
