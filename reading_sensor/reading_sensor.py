import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
import pandas as pd
import numpy as np
class Subscriber(Node):

    def __init__(self):
        super().__init__('sub_node')
        queue_size = 10
        self.subscriber1 = self.create_subscription(
            Vector3, 'micro_ros_arduino_node_publisher', self.sub_callback1, queue_size
        )
        self.subscriber2 = self.create_subscription(
            String, 'signal', self.sub_callback2, queue_size
        )


    def sub_callback1(self, msg):
        self.angle = msg.z
    def sub_callback2(self, msg):
        self.sign = msg.data
    angle = 0
    sign = ""

def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    
    
    theta = []
    while(True):
        rclpy.spin_once(subscriber)
        if subscriber.sign == "start":
            theta.append(subscriber.angle)
        elif subscriber.sign == "end":
            df = pd.DataFrame(theta, columns=['theta'])
            df.to_csv("~/ros2_ws/src/reading_sensor/measured/experiment.csv", index = False)
            break

    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()