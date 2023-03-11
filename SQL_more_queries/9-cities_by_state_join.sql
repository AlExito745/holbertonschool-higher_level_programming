-- List all cities of a database in MySQL Server.
SELECT cities.`id`, cities.`name`, state.`name`
FROM `cities` AS c
INNER JOIN `states` AS s
ON cities.`state_id` = state.`id`
ORDER BY cities.`id`;
