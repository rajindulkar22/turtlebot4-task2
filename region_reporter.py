#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from shapely.geometry import Point, Polygon
import yaml

class RegionReporter(Node):
    def __init__(self, map_yaml_path):
        super().__init__('region_reporter')

        # Load YAML file (map info + regions)
        with open(map_yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        self.regions = data.get('regions', {})
        self.get_logger().info(f"Loaded regions: {list(self.regions.keys())}")

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

        found = False
        for name, region in self.regions.items():
            # Polygon-based region
            if "polygon" in region:
                poly = Polygon(region["polygon"])
                if poly.contains(p):
                    self.get_logger().info(f" Robot is in: {name}")
                    found = True
                    break

        if not found:
            self.get_logger().info(f" Robot at ({x:.2f}, {y:.2f}) not in any labeled region")

def main(args=None):
    rclpy.init(args=args)
    node = RegionReporter("/home/raj/test.yaml")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
