# Big Data Analysis: Hive, Spark SQL, DataFrames and GraphFrames

### Assignments

* [Week 2](week2)
  * [Demo Task](week2/task00/Demo.ipynb)

### Local environment

Run `bigdatateam/hysh-full:py3-c2` Docker container with the following command:

```
docker run -it --name hysh-full --rm -v $DATA_DIR:/home/jovyan/work -p 8888:8888 -p 50070:50070 -p 8088:8088 -d -e "LOCAL_MODE=true" bigdatateam/hysh-full:py3-c2
```

where

- `$DATA_DIR` - pre-defined environment variable with path to the directory to store all entities created during work on a task (e.g notebooks, compiled scripts, data samples)
- `-e "LOCAL_MODE=true"` - allows to run some command which are restricted when run a Notebook in the course' (e.g database creation)
- `-p 8888:8888` - for Jupyter Notebook UI
- `-p 50070:50070` - for HDFS UI
- `-p 8088:8088` - for YARN UI

