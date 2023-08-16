-- Create table unique_id
-- id and name description
CREATE TABLE IF NOT EXISTS `unique_id` (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
