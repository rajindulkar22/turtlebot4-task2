#Step 1: Locate the default Nav2 config files :- 
ros2 pkg prefix turtlebot4_navigation
/opt/ros/humble
#step2:- ls /opt/ros/humble/share/turtlebot4_navigation/config/
localization.yaml   nav2.yaml   slam.yaml


#step3:- Step 2: Copy the Nav2 config into your workspace
mkdir -p ~/ros2_ws/config
cp /opt/ros/humble/share/turtlebot4_navigation/config/nav2.yaml ~/ros2_ws/config/my_nav2.yaml


#step4 : In your nav2.yaml, inside:
#Inside FollowPath

      max_vel_x: 0.15          # max forward speed (was 0.26)
      max_vel_theta: 0.3       # max rotation speed (was 1.0)

      acc_lim_x: 0.1           # linear acceleration limit (was 2.5)
      decel_lim_x: -0.1        # linear deceleration (was -2.5)

      acc_lim_theta: 0.1       # angular acceleration (was 3.2)
      decel_lim_theta: -0.1    # angular deceleration (was -3.2)
      
#Inside velocity_smoother

velocity_smoother:
  ros__parameters:
    use_sim_time: True
    smoothing_frequency: 20.0
    scale_velocities: False
    feedback: "OPEN_LOOP"
    max_velocity: [0.15, 0.0, 0.3]    # linear x, y, angular z
    min_velocity: [-0.15, 0.0, -0.3]
    max_accel: [0.1, 0.0, 0.1]
    max_decel: [-0.1, 0.0, -0.1]
    odom_topic: "odom"
    odom_duration: 0.1
    deadband_velocity: [0.0, 0.0, 0.0]
    velocity_timeout: 1.0

      



