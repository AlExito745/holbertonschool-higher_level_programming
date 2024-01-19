-- List the number of records with the same value in a table of a database of MySQL Server.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
