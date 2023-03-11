-- List all cities of a State on database of MySQL Server.
SELECT `name`
FROM `states`
WHERE `name` = "California"
ORDER BY cities.id ASC
LIMIT 10;
