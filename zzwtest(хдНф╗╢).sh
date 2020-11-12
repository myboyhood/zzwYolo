#!/bin/bash
### BEGIN INIT INFO
# Provides: test
# Short-Description: mlkk test
# Description:  
# Required-Start: $remote_fs $local_fs
# Required-Stop: $remote_fs $local_fs
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
### END INIT INFO
source ~/.bashrc   ### zzw_source
source /home/gf/zzw/test_ws/devel/setup.bash
roslaunch gaofen2020 gaofen2020.launch
roslaunch px4_realsense_bridge bridge_mavros.launch & sleep 15
roslaunch vision_to_mavros t265_all_nodes.launch & sleep 5	
### zzw_nodes_run
cd /home/gf/zzw/test_ws/src/test_projects/scripts
python3 /home/gf/zzw/test_ws/src/test_projects/scripts/yolo_realsense_tcp.py & sleep 5
python3 /home/gf/zzw/test_ws/src/test_projects/scripts/yolo_client.py & sleep 15

rosrun rosrun test_node test_node_time 
exit 0
