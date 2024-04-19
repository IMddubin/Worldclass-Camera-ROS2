import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from world_class_msg.srv import RecordStart


class RecordVideoNode(Node):
    def __init__(self):
        super().__init__('record_video_node')
        self.bridge = CvBridge()
        self.img_subscriber = self.create_subscription(Image, '/camera', self.image_callback, 10)

        self.recording = False
        self.video_writer = None
        self.save_service = self.create_service(RecordStart, 'record_start', self.recording_callback)
        self.save_path = "/home/subin/worldclass_ros/src/world_class_cam/world_class_cam/album/"
        self.filename = None

    def image_callback(self, msg):
        if self.recording:
            try:
                cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
                if self.video_writer is None:
                    height, width, _ = cv_image.shape
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    filename = self.save_path + self.filename + ".mp4"
                    self.video_writer = cv2.VideoWriter(filename, fourcc, 30, (width, height))
                self.video_writer.write(cv_image)
            except CvBridge.CvBridgeError as e:
                print(e)

    def recording_callback(self, request, response):
        self.filename = request.filename
        if request.start:
            self.recording = True
            response.success = True
            response.message = "Recording started."
            response.filename = request.filename
        else:
            self.recording = False
            if self.video_writer is not None:
                self.video_writer.release()
                self.video_writer = None
            response.success = True
            response.message = "Recording stopped and video saved."
            response.filename = request.filename
        return response

def main():
    rclpy.init()
    node = RecordVideoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
