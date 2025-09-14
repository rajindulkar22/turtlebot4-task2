#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from shapely.geometry import Point, Polygon
from std_msgs.msg import String
import yaml

class RegionReporter(Node):
    def __init__(self, map_yaml_path):
        super().__init__('region_reporter')

        # Load YAML file (map info + regions)
        with open(map_yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        self.regions = data.get('regions', {})
        self.get_logger().info(f"Loaded regions: {list(self.regions.keys())}")

        # Publisher for current region
        self.pub = self.create_publisher(String, "/current_region", 10)

        # Subscribe to AMCL pose
        self.sub = self.create_subscription(
            PoseWithCovarianceStamped,
            "/amcl_pose",
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        # Current robot pose
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        p = Point(x, y)

        region_msg = String()
        region_msg.data = "none"   # default

        for name, region in self.regions.items():
            if "polygon" in region:
                poly = Polygon(region["polygon"])
                if poly.contains(p):
                    region_msg.data = name     # <-- assign region name
                    break

        self.pub.publish(region_msg)
        self.get_logger().info(f" Current region: {region_msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = RegionReporter("/home/raj/maps/test1_map.yaml")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
