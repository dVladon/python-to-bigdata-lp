ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-serde.jar;

USE stackoverflow_;
DROP TABLE IF EXISTS posts_sample_external;
DROP TABLE IF EXISTS posts_sample;

-- Create 'posts_sample_external' table with post id, post creation year and post creation month
CREATE EXTERNAL TABLE posts_sample_external (
    id INT,
    year INT,
    month STRING
)
ROW FORMAT
    SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
    WITH SERDEPROPERTIES (
        "input.regex" = ".*?(?=\\bId=\"(\\d+)\").*(?=.*\\bCreationDate=\"(\\d{4}).*)(?=.*\\bCreationDate=\"(\\d{4}-\\d{2}).*).*$"
    )
LOCATION '/data/stackexchange1000/posts'
TBLPROPERTIES (
    "skip.header.line.count"="1"
);

-- Create and fill managed table 'posts_sample' with partitioning
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.error.on.empty.partition=true;

CREATE TABLE posts_sample (
    id INT
)
PARTITIONED BY (year INT, month STRING);

FROM posts_sample_external
INSERT OVERWRITE TABLE posts_sample
PARTITION (year, month)
SELECT id, year, month;






--
