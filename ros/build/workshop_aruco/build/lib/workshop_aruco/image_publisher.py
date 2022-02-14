import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError


class ImagePublisher(Node):
    def __init__(self, path):
        super().__init__('image_publisher')
        self.get_logger().info('STARTING IMAGE PUBLISHER')
        self.publisher_ = self.create_publisher(Image, 'topic/image', 2)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(path)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        _, frame = self.cap.read()
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='passthrough')
        self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher('/root/_data/Turtle_control.webm')

    rclpy.spin(image_publisher)
    
    image_publisher.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
