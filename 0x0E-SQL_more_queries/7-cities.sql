-- Creates hbtn_0d_usa and cities
-- cities should have id, state_id, name description
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY(id),
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id)
	REFERENCES `hbtn_0d_usa`.`cities`(id)
);
