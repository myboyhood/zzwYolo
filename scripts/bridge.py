import rospy
from geometry_msgs.msg import PoseStamped

send_msg = PoseStamped()


def callback2(data2):
    global send_msg
    if(data2.pose.orientation.w == -1000):
        send_msg.pose.position.x = 0;
        send_msg.pose.position.y = 0;
        send_msg.pose.position.z = 0;
        send_msg.pose.orientation.x = 0;
        send_msg.pose.orientation.y = 0;
        send_msg.pose.orientation.z = 0;
        send_msg.pose.orientation.w = -1000;
    else:
        send_msg.pose.position.x = 0;
        send_msg.pose.position.y = 0;
        send_msg.pose.position.z = 0;
        send_msg.pose.orientation.x = 0;
        send_msg.pose.orientation.y = 0;
        send_msg.pose.orientation.z = 0;
        send_msg.pose.orientation.w = -1000;


def callback2():


def do_bridge():
    rospy.init_node('do_bridge', anonymous=True)
    msg_pub = rospy.Publisher('do_bridge', PoseStamped, queue_size=1)
    msg_rev_id = rospy.Subscriber('yolo_target_corner',PoseStamped,callback1)
    msg_rev_pose = rospy.Subscriber('drone_pos_vision',PoseStamped,callback2)
    rospy.spin()


        if msg[0] == '1':
            target_get_flag = True
            #print ("target corner")
            """ QuaternionStamped.x, y, z, w = xmin, ymin, xmax, ymax,   x = time, z= id """
            #target_corner_msg.header.stamp = rospy.get_rostime()
            target_corner_msg.pose.orientation.x = float(msg[1])
            target_corner_msg.pose.orientation.y = float(msg[2])
            target_corner_msg.pose.orientation.z = float(msg[3])
            target_corner_msg.pose.orientation.w = float(msg[4])
            target_corner_msg.pose.position.x = float(msg[5])
            target_corner_msg.pose.position.z = float(msg[6])

        if not target_get_flag:
           # print (" target not found ... ")
            #target_corner_msg.header.stamp = rospy.get_rostime()
            target_corner_msg.pose.orientation.x = -1
            target_corner_msg.pose.orientation.y = 0
            target_corner_msg.pose.orientation.z = 0
            target_corner_msg.pose.orientation.w = 0
            target_corner_msg.pose.position.x = -1
            target_corner_msg.pose.position.z = -1

        yolo_target_pub.publish(target_corner_msg)
        rate.sleep()


if __name__ == "__main__":
    do_bridge()
