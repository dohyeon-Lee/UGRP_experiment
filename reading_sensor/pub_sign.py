import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Sign_Publisher(Node):

    def __init__(self):
        super().__init__('signal_pub_node')
        # publisher를 생성하는 부분입니다. 하단에 추가 설명이 있습니다.
        self.publisher = self.create_publisher(String, "signal", 10)

        # 어느정도의 주기로 publish 할 것인지를 선택합니다.
        # 지금의 경우 0.5초의 간격으로 publish_callback 함수를 반복 실행합니다.
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.publish_callback)
    
    def publish_callback(self):
        sign_msg = String()
        if self.key == "s" or self.key == "S":
            sign_msg.data = "start"
        elif self.key == "e" or self.key == "E":
            sign_msg.data = "end"
        else:
            sign_msg.data = "waiting.."
        self.publisher.publish(sign_msg)
    
    key = ""

def main(args=None):
    rclpy.init(args=args)

    sign_publisher = Sign_Publisher()

    while (True):
        key = input('s (start) or e (end) : ')
        Sign_Publisher.key = key
        rclpy.spin_once(sign_publisher)
    
    sign_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()