# Local BigData Playground

Notes about working with Docker containers provided by `bigdatateam`:
* [bigdatateam/hysh-full](#bigdatatean-hysh-full)

## bigdatateam/hysh-full

**Link:** https://hub.docker.com/r/bigdatateam/hysh-full

#### Run

```
docker run -it --name hysh-full --rm -v $(pwd):/home/vvlasov -p 8888:8888 -p 50070:50070 -d bigdatateam/hysh-full:py3-c1
```