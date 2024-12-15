model=Qwen/Qwen2.5-1.5B-Instruct
volume=$PWD/data

docker run --gpus all \
    --shm-size 1g \
    -p 8080:80 \
    -v $volume:/data ghcr.io/huggingface/text-generation-inference:3.0.0 \
    --model-id $model