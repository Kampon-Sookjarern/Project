#!/usr/bin/env python3
import rospy

from std_srvs.srv import Empty
import time
def main():
    rospy.wait_for_service('go_to_kitchen')
    data2=rospy.ServiceProxy('go_to_kitchen',Empty)

    rospy.wait_for_service('stop')
    data3=rospy.ServiceProxy('stop',Empty)

    rospy.wait_for_service('go_home')
    data1=rospy.ServiceProxy('go_home',Empty)
    
    data1()
    data2()
    data3()
    data1()
    data3()
   
if __name__ == '__main__':
    try:
        main()
        
    except rospy.ROSInterruptException:
        pass
