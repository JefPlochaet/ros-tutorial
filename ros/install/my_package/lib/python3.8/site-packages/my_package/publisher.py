import rclpy
from rclpy.node import Node
from std_msgs.msg import String
# These lines represent the dependencies
# Don't forget to add these to package.xml

class MinimalPublisher(Node):
    def __init__(self):
        # Super calls the Node class constructor
        super().__init__('minimal_publisher') # Argument is name of node
        # Declares that node publishes messages of type String, over a topic
        # named topic and the queue size is 10 (QoS)
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        """ Creates a message with the counter value appended and 
            publishes it to the console with the get_logger().info
            function.
        """
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    """ Initializes rclpy, then creates the node. Then spins the node so its
        callbacks are called.
    """
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - eotherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
