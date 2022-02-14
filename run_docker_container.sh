xhost +local:docker

docker run -it --rm \
	-e DISPLAY=${DISPLAY} \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
	-v ${PWD}/ros:/root/dev_ws/ \
    --name 'ros' ros