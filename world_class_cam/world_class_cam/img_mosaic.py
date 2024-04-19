import cv2
import numpy

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImgEdge(Node):
    def __init__(self):
        super().__init__('img_mosaic')

        self.declare_parameter('camera_topic', '/camera')
        self.declare_parameter('mosaic_value', 15)

        # self.width = 480
        # self.length = 320
        self.declare_parameter('width', 640)
        self.width = self.get_parameter('width').value
        self.declare_parameter('length', 480)
        self.length = self.get_parameter('length').value
        output_msg = "Video Width : " + str(self.width) + "\n\r"
        output_msg = output_msg + "Video Length : " + str(self.length)    

        self.mosaic_value = self.get_parameter('mosaic_value').value

        self.img_subscriber = self.create_subscription(
            Image,
            '/camera', 
            self.image_callback,
            10
        )

        self.img_mosaic = self.create_publisher(Image, '/img_mosaic', 10)
        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        mosaic_img = self.mosaic(img, self.mosaic_value)

        pub_img = self.cv_bridge.cv2_to_imgmsg(mosaic_img, "bgr8")
        self.img_mosaic.publish(pub_img)

    def mosaic(self, img, mosaic_value):

        mosaic_img = cv2.resize(img, (self.width // int(mosaic_value+1), self.length // int(mosaic_value+1)))
        mosaic_img = cv2.resize(mosaic_img, (self.width, self.length), interpolation=cv2.INTER_NEAREST)

        return mosaic_img


def main():
    rclpy.init()
    node = ImgEdge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()