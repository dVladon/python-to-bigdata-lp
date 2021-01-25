# Big Data Analysis: Hive, Spark SQL, DataFrames and GraphFrames

### Assignments

* [Week 2](week2)
  * [Demo Task](week2/task00/Demo.ipynb)
  * [Hive DDL: Create Tables](week2/task01/CreateTables.ipynb)
  * [Hive DML: Find Most Popular Tags](week2/task02/FindMostPopularTags.ipynb)
  * [Honor Task 1: Calculate Amount of Posts per User Age](week2/task03/PostsPerUserAge.ipynb)
* [Week 4](week4)
  * [Counting number of the mutual friends](week4/task01/MutualFriends.ipynb)

### Local environment

Run `bigdatateam/hysh-full:py3-c2` Docker container with the following command:

```
docker run -it --name hysh-full --rm -v $DATA_DIR:/home/jovyan/work -p 8888:8888 -p 50070:50070 -p 8088:8088 -d bigdatateam/hysh-full:py3-c2
```

where

- `$DATA_DIR` - pre-defined environment variable with path to the directory to store all entities created during work on a task (e.g notebooks, compiled scripts, data samples)
- `-p 8888:8888` - for Jupyter Notebook UI
- `-p 50070:50070` - for HDFS UI
- `-p 8088:8088` - for YARN UI

