-- list the number of records with same value
SELECT score,
COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
