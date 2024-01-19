-- List all records with a score >= 10 in a table of database of MySQL Server.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC
LIMIT 10;
