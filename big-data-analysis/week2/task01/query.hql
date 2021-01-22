ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
USE stackoverflow_;

SELECT year, month, COUNT(*) as count 
FROM posts_sample 
GROUP BY year, month ORDER BY month;
