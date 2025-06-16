FROM nvidia/cuda:12.6.2-devel-ubuntu22.04
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install torch
RUN git clone https://github.com/haotian-liu/LLaVA.git

RUN pip install git+https://github.com/huggingface/transformers accelerate
RUN pip install torchvision
RUN pip install -U transformers
RUN pip install autoawq
