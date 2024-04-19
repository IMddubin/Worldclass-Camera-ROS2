import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class FilteredStatus(Node):
    def __init__(self):
        super().__init__('filtered_status')
        self.sub_status = self.create_subscription(Image, '/camera', self.status_callback, 10)

    def status_callback(self, msg):
        print(msg)

def main():
    rclpy.init()
    node = FilteredStatus()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()