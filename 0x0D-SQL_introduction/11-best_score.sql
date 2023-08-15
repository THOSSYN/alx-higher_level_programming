-- list all records with score >= 10 in second_table
-- Should print score first
SELECT score, name FROM second_table
WHERE score >= 10
Order by score DESC;
