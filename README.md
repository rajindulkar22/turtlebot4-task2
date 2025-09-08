# turtlebot4-task2
 launch file :- ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py nav2:=true slam:=false localization:=true rviz:=true map:=/home/raj/test.yaml						
slam :- ros2 launch turtlebot4_navigation slam.launch.py		                       

 launch rviz :- ros2 launch turtlebot4_viz view_robot.launch.py
 
 ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py nav2:=true slam:=false localization:=true rviz:=true map:=/home/raj/test.yaml

ros2 topic echo /clicked_point

ros2 run teleop_twist_keyboard teleop_twist_keyboard



