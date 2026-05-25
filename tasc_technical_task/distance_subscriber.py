import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class distanceSubscribe(Node):

    def __init__(self):
        super().__init__('distance_subscriber')
        self.distance_sub_ = self.create_subscription(Float32, "distance_of_robot", self.distance_callback, 10)
        self.get_logger().info("Distance Subscriber Node has been started.")

    def distance_callback(self, msg):
        self.get_logger().info("distance (subscriber) is: " +str(msg.data) + " meters")

def main(args=None):
    rclpy.init(args=args)
    node = distanceSubscribe()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

