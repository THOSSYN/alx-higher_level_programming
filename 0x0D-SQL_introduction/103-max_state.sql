-- Displays the max temperature of each state
-- The order is by state name
SELECT city, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
