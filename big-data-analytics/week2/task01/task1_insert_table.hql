USE stackoverflow_;

SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.error.on.empty.partition=true;

-- Filling managed posts table from external one

FROM posts_sample_external
INSERT OVERWRITE TABLE posts_sample
PARTITION (year, month)
SELECT id, year, month;
