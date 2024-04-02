#!/bin/bash

path=`pwd ..`
parent=$(dirname "$path")

docker_name=python_tool_hub
docker stop $docker_name
docker rm $docker_name
docker run -dt --name $docker_name -it  \
-v ${parent}:/workspace \
-p 9122:22 \
--ulimit core=-1 --security-opt seccomp=unconfined \
python_tools:v1 \
/bin/bash
