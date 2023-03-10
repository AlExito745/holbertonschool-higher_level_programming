-- List the number of records with the same value in a table of a database of MySQL Server.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
ORDER BY `score` DESC
LIMIT 10;
