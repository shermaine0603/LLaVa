```sh
docker run --runtime nvidia -it --rm -v /home/boonkiat/Downloads:/pic --network=host dustynv/llava:r36.2.0
```

```sh
docker build . -t rag
```

```sh
docker run --runtime nvidia -it -v /home/boonkiat/Downloads/LLaVA2:/pic --network=host --name rag rag
```

Exit the docker container, then use this line to transfer the test file to inside the docker.
```sh
docker cp predict.py rag:workspace/llava/predict.py
```

```sh
cp -r /home/boonkiat/Downloads/LLaVA2 rag:workspace/llava
```

Get docker container id from:
```sh
docker ps -a
```

Start the container
```sh
docker start rag
```

```sh
docker exec -it rag bash
```
