import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class distancePublish(Node):

    def __init__(self):
        super().__init__('distance_publisher')
        self.distance_pub_ = self.create_publisher(Float32, "distance_of_robot", 10)
        self.timer_ = self.create_timer(1.0, self.publish_distance)
        self.get_logger().info("Distance Publisher Node started.")

    def publish_distance(self):
        msg = Float32()
        msg.data = round(random.uniform(0.2, 5.0), 2)
        self.get_logger().info("distance (publisher) is: " +str(msg.data) + " meters")
        self.distance_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = distancePublish()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
