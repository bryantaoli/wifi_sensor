#!/usr/bin/env python

import rospy
import time
import pywifi
import numpy as np
# from msg import *
from std_msgs.msg import String



def pub_wifi():
  rospy.init_node('wifisensor',anonymous = True)
  pub = rospy.Publisher('wifi',String,queue_size=10)
  rate = rospy.Rate(10)

#from comtypes import GUID
  wifi = pywifi.PyWiFi()
  iface = wifi.interfaces()[0]
  iface.scan()
  time.sleep(2)
  while not rospy.is_shutdown():
    t = time.time()
    result=iface.scan_results()
    for i in range(len(result)):
        #print(result[i])
        # print(t, result[i].ssid, result[i].bssid, result[i].signal)
        a=[t, result[i].ssid, result[i].bssid, result[i].signal]
        b = ","  . join(str(v) for v in a)
        #c = b%rospy.get_time()
	rospy.loginfo(b)
        pub.publish(b)
    rate.sleep()
    

if __name__ == '__main__':
    try:
        pub_wifi()
    except rospy.ROSInterruptException:
        pass


