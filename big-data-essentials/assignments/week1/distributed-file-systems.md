# Distributed File Systems

### Task 1

```
*Calculations:*

(1 PB / (64 MB * 3)) * 300 B = (1000000 GB / 0.192 GB) * 3e^-7 GB = 5208333.(3) GB * 3e^-7 GB = 1562500000 B ~ 1.56 GB

*Answer:*
1.56 GB
```

### Task 2

```
*Calculations:*

disk_speed = 60 MB/s
seek_time = 5 ms = 0.005 s
block_read_time = 200 * seek_time = 200 * 0.005 s = 1 s
block_size = block_read_time * disk_speed = 1 s * 60 MB/s = 60MB 

*Answer:*
60 MB
```

### Task 3

```
hdfs dfs -mkdir assignment1
hdfs dfs -put test.txt assignment1
hdfs dfs -ls assignment1/test.txt
hdfs dfs -chmod o-r assignment1/test.txt
hdfs dfs -cat assignment1/test.txt | head -10
hdfs dfs -mv assignment1/test.txt assignment1/test2.txt
```

### Task 4

```

```

### Task 5

```
total capacity: 2.14 TB
used space: 242.12 GB
total data nodes: 4
```