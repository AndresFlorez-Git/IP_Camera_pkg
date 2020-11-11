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
import argparse

########################################################################################################
####################################### IP Address #####################################################
########################################################################################################

IP_address = '192.168.20.23'


########################################################################################################
#################################### IPCamera classs ###################################################
########################################################################################################

class IPCamera(object):
    def __init__(self, url):
        try:
            self.stream=urllib.urlopen(url)
        except:
            rospy.logerr('Unable to open camera stream: ' + str(url))
            sys.exit() #'Unable to open camera stream')
        self.bytes=''
        self.image_pub = rospy.Publisher("camera_image", Image, queue_size=10)
        self.bridge = CvBridge()

########################################################################################################
######################################### Main #########################################################
########################################################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ip_camera.py', description='reads a given url string and dumps it to a ros_image topic')

    # Para visualizar la imagen capturada del LAN ip cam: $ rosrun camera_pkg publisher.py --gui
    parser.add_argument('-g', '--gui', action='store_true', help='show a GUI of the camera stream')
    # Definir la direccion ip agragando la url del stream en default o ejecutar en ventana de comandos : $rosrun camera_pkg publisher.py -u YOUR_CAMERA_URL --gui
    parser.add_argument('-u', '--url', default='http://'+ IP_address +':8080/video', help='camera stream url to parse')
    args = parser.parse_args()
    
    rospy.init_node('IPCamera', anonymous=True)
    ip_camera = IPCamera(args.url)

    while not rospy.is_shutdown():
        ip_camera.bytes += ip_camera.stream.read(1024)
        a = ip_camera.bytes.find('\xff\xd8')
        b = ip_camera.bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = ip_camera.bytes[a:b+2]
            ip_camera.bytes= ip_camera.bytes[b+2:]
            if len(jpg) >0:
            	i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
	    image_message = i	
            ip_camera.image_pub.publish(ip_camera.bridge.cv2_to_imgmsg(image_message, "bgr8"))

	    if args.gui:
               cv2.imshow('IP Camera Publisher Cam',i)
	    if cv2.waitKey(1) ==27: # wait until ESC key is pressed in the GUI window to stop it
	       exit(0) 
