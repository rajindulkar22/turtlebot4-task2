from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to turtlebot4_navigation package
    tb4_nav_dir = get_package_share_directory('turtlebot4_navigation')

    # Paths to map and nav2 config
    map_file = '/home/raj/maps/test1_map.yaml'
    params_file = '/home/raj/ros2_ws/config/my_nav2.yaml'

    # Path to RViz config
    rviz_config = os.path.join(
        tb4_nav_dir, 'rviz', 'nav2_default_view.rviz'
    )

    return LaunchDescription([
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(tb4_nav_dir, 'launch', 'localization.launch.py')),
            launch_arguments={
                'map': map_file,
                'params_file': params_file,
                'rviz': 'false'  # we'll launch rviz separately
            }.items()
        ),

        # Start RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        ),

        # Start region_reporter
        Node(
            package='region_reporter',
            executable='region_reporter',
            output='screen'
        )
    ])
