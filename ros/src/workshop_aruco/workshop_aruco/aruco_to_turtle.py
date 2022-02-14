import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
from cv2 import aruco
from cv_bridge import CvBridge, CvBridgeError

class ArucoToTurtle(Node):
    def __init__(self):
        super().__init__('aruco_to_turtle')
        self.get_logger().info('STARTING ARUCO TO TURTLE')
        self.bridge = CvBridge()
        self.subscription_ = self.create_subscription(Image, 'topic/image', self.listener_callback, 2)
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 2)


    def listener_callback(self, msg):
        
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()

        _, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        if not ids is None:
            self.get_logger().info("Marker id: %d" % ids[0])
            
            # Convert to velocity command
            switcher = {
                6: (1.0, 0.0),  # UP
                2: (0.0, -1.0), # RIGHT
                4: (-1.0, 0.0), # DOWN
                5: (0.0, 1.0)   # LEFT
            }
            linear_, angular_ = switcher.get(int(ids[0]),(0., 0.))
        
            cmd = Twist()
            cmd.linear.x = linear_
            cmd.angular.z = angular_
            self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    aruco_to_turtle = ArucoToTurtle()

    rclpy.spin(aruco_to_turtle)
    
    aruco_to_turtle.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
