FROM ros:foxy

RUN apt-get update && apt-get install -y

#gazebo
RUN apt-get install -y ros-foxy-gazebo-*

#cartographer
RUN apt install -y ros-foxy-cartographer
RUN DEBIAN_FRONTEND=noninteractive apt install -y ros-foxy-cartographer-ros

#navigation
RUN apt install -y ros-foxy-navigation2
RUN apt install -y ros-foxy-nav2-bringup

#turtlebot
RUN apt install -y ros-foxy-dynamixel-sdk
RUN apt install -y ros-foxy-turtlebot3-msgs
RUN apt install -y  ros-foxy-turtlebot3

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