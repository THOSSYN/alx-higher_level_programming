-- Lists all cities in hbtn_0d_usa
-- Should have 3 columns
SELECT c.id, c.name, s.state
FROM cities AS c
	INNER JOIN states AS s
	ON c.state_id = s.id
ORDER BY c.id ASC;
