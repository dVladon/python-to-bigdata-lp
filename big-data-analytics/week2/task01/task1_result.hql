USE stackoverflow_;

-- Count posts by months
SELECT year, month, COUNT(*) as count 
FROM posts_sample 
GROUP BY year, month ORDER BY month
LIMIT 2,1;
