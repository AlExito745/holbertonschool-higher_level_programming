-- List all cities of a database in MySQL Server.
SELECT `id`, `name`
FROM `cities` AND SELECT (
		`name`
		FROM `states`)
ORDER BY `id`;
