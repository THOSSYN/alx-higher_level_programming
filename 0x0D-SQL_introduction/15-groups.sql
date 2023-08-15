-- Lists the number of records with same score in the second_table
-- The result should display the score
SELECT score, COUNT(1) AS number
FROM second_table
GROUP BY SCORE
ORDER BY number DESC;
