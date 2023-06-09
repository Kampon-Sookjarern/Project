#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def go_home(req):
    rospy.loginfo("Going to home")
    time.sleep(2)
    rospy.loginfo("Arrived")
    return EmptyResponse()
def go_to_kitchen(req):
    rospy.loginfo("Going to kitchen")
    time.sleep(2)
    rospy.loginfo("“Arrived.”")
    return EmptyResponse()
def stop (req):
    rospy.loginfo("stop")
    return EmptyResponse()



rospy.init_node('nodeservice')
rospy.loginfo("start")
rospy.Service('go_home',Empty,go_home)
rospy.Service('go_to_kitchen',Empty,go_to_kitchen)
rospy.Service('stop',Empty,stop)

rospy.spin()


    
    
                  