#!/bin/bash

model=Qwen/Qwen2.5-1.5B-Instruct
volume=$PWD/data

if docker ps -a --format "{{.Names}}" | grep -q "^tgi_container$"; then
    docker start tgi_container
    echo "Inference up"
else
    docker run -d --gpus all --shm-size 1g -p 8080:80 -v $volume:/data --name tgi_container \
        ghcr.io/huggingface/text-generation-inference:3.0.0 \
        --model-id $model
    echo "Docker container tgi_container is built"
fi