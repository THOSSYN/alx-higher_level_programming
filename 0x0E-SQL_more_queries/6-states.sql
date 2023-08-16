-- Creates the database hbtn_0d_usa and table state
-- state is created inside hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	PRMARY KEY(`id`),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
