import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wl/Documents/ros2_ws/install/turtlebot3_teleop'
