FROM ros:foxy

RUN apt-get update -y

RUN apt install -y vim

#turtlesim
RUN apt install -y ros-foxy-turtlesim

#rqt
RUN apt install -y ~nros-foxy-rqt*

#configure environment
RUN echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
RUN echo 'source /opt/ros/foxy/setup.bash' >> ~/.bashrc

COPY _data /root/_data

WORKDIR /root/

CMD /bin/bash