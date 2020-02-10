#!/usr/bin/env python
import urllib
import roslib
import rospy
import sys
from std_msgs.msg import String

ip = "http://192.168.1.100:8080/photoaf.jpg"

def callback(data):
    global ip
    urllib.urlretrive(ip,  "photo.jpg")
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Photo", String, callback)
    rospy.spin()

if __name__ == '__main__':
    global ip
    if len(sys.argv) == 2:
        ip = sys.argv[1]
    listener()
