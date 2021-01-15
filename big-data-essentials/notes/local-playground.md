# Local BigData Playground

Notes about working with Docker containers provided by `bigdatateam`:
* [bigdatateam/hysh-full](#bigdatatean-hysh-full)

## bigdatateam/hysh-full

**Link:** https://hub.docker.com/r/bigdatateam/hysh-full

#### Run

```
docker run -it --name hysh-full --rm -v $DATA_DIR:/home/jovyan/work -p 8080:80 -d bigdatateam/hysh-full:py3-c1
```