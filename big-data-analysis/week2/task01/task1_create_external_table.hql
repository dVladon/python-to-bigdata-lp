ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-serde.jar;

USE stackoverflow_;

-- Create external table posts_sample_external with suitable values
DROP TABLE IF EXISTS posts_sample_external;

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
