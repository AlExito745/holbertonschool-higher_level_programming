-- List all cities of a State on database of MySQL Server.
SELECT `id`,`name`
FROM `cities`
WHERE `state_id` IN (
		SELECT `id`
		FROM `states`
		WHERE `name` = "California")
ORDER BY `id`;
