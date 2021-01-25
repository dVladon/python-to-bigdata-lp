USE stackoverflow_;

-- Create managed table posts_sample partitioned by year and month
CREATE TABLE posts_sample (
    id INT
)
PARTITIONED BY (year INT, month STRING);
