#!/usr/bin/env python

import cv2
import urllib 
import numpy as np
from sensor_msgs.msg import Image 
import roslib
import sys
import rospy
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError 


########################################################################################################
#################################### IPCamera classs ###################################################
########################################################################################################

class IPCamera(object):
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("camera_image",Image,self.callback)


    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e:
            print e

	(cols,rows) = cv_image.shape[:2]
        if cols > 60 and rows > 60 :
            cv2.circle(cv_image, (50,50), 10, 255)

        cv2.imshow("ip_camera Listener Image", cv_image)
        cv2.waitKey(3)


########################################################################################################
######################################### Main #########################################################
########################################################################################################
        
if __name__ == '__main__':
  ip_camera_listener = IPCamera()
  rospy.init_node('IPCAM', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv2.DestroyAllWindows()
