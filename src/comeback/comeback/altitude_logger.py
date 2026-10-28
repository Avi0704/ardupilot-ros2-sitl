import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import PoseStamped


class AltitudeLogger(Node):
    def __init__(self):
        super().__init__('altitude_logger')
        self.altitude = None
        self.create_subscription(
            PoseStamped,
            '/ap/pose/filtered',
            self.pose_callback,
            qos_profile_sensor_data)
        self.create_timer(1.0, self.report)

    def pose_callback(self, msg):
        self.altitude = msg.pose.position.z

    def report(self):
        if self.altitude is None:
            self.get_logger().info('No pose received yet')
        else:
            self.get_logger().info(f'Altitude: {self.altitude:.2f} m')


def main(args=None):
    rclpy.init(args=args)
    node = AltitudeLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()