```sh
docker run --runtime nvidia -it --rm -v /home/boonkiat/Downloads:/pic --network=host dustynv/llava:r36.2.0
```

```sh
docker build . -t rag
docker build . -t my-ollama
```

```sh
docker run --runtime nvidia -it -v /home/boonkiat/Downloads/LLaVA2:/pic --network=host --name rag rag
docker run --runtime nvidia -it --network=host --name rag rag
docker run --runtime nvidia -it --name ollama-con my-ollama
docker run -d --runtime=nvidia -v ollama:/root/.ollama -p 11434:11434 --name ollama-con my-ollama
```

Exit the docker container, then use this line to transfer the test file to inside the docker.
```sh
docker cp predict.py rag:workspace/llava/predict.py
```

```sh
cp -r /home/boonkiat/Downloads/LLaVA2 rag:workspace/llava
```

```sh
docker cp  ~/Downloads/LLaVA2 rag:/workspace/llava
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

```sh
docker stop rag
docker rm rag
docker build . -t rag
```

```sh
docker stop ollama-con
docker rm ollama-con
docker build . -t my-ollama
```

```sh
docker run -d --runtime=nvidia -v ollama:/root/.ollama -p 11434:11434 --name ollama-con my-ollama
```

```sh
docker exec -it ollama-con bash
```

```sh
docker stop ollama-con3
docker rm ollama-con3
docker build . -t my-ollama3
```

```sh
docker cp ollama-con:/app/Images_and_Queries.xlsx .
```

qwen_SG_read_excel.py
```sh
docker cp ./qwen_SG_read_excel.py test-1-con:/app/qwen_SG_read_excel.py
```
```sh
docker stop test-4-con
docker rm test-4-con
docker build . -t test-4
```
```sh
docker run --runtime=nvidia -p 7860:7860 --name test-4-con test-4
```
