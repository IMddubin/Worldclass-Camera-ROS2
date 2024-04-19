import cv2
import datetime

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from world_class_msg.srv import CaptureImage
# from world_class_msg.srv import RecordStart


class ImgScreenshot(Node):
    def __init__(self):
        super().__init__('img_screenshot')

        self.declare_parameter('camera_topic', '/camera')
        self.cv_bridge = CvBridge()
        self.img = None

        self.img_subscriber = self.create_subscription(Image, 'camera', self.image_callback, 10)
        self.capture_server = self.create_service(CaptureImage, 'capture_image', self.capture_image_callback)
        

    def image_callback(self, msg):
        self.img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def capture_image_callback(self, request, response):
        if self.img is not None:
            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = now + ".png"
            path = "/home/subin/worldclass_ros/src/world_class_cam/world_class_cam/album/"
        
            cv2.imwrite(path + filename, self.img)

            response.success = True
            response.message = 'Image captured and saved as {}'.format(filename)
            response.filename = filename
        else:
            response.success = False
            response.message = 'Failed to capture and save image'
            response.filename = ''
    
        return response

def main() :
    rclpy.init()
    node = ImgScreenshot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()