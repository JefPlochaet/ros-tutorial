from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='workshop_aruco', executable='image_publisher', output='screen',
            name=['image_publisher']),
        launch_ros.actions.Node(
            package='workshop_aruco', executable='aruco_to_turtle', output='screen',
            name=['aruco_to_turtle']),
        launch_ros.actions.Node(
            package='turtlesim', executable='turtlesim_node', output='screen',
            name=['turtlesim']),
        ])