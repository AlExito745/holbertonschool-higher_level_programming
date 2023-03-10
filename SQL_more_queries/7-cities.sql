-- Create a database and table on MySQL Server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
		`id` INT UNIQUE NOT NULL AUTO_INCREMENT,
		`state_id` INT NOT NULL,
		`name` VARCHAR(256) NOT NULL,
		PRIMARY KEY (`id`),
		FOREIGN KEY (`id`) REFERENCES states(`id`));
