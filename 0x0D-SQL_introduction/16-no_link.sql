-- List all records of second_table
-- List row and name
SELECT score, name FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
