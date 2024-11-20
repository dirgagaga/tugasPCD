__author__ = 'Charlie'
import os, inspect, sys
import cv2
import numpy as np
import argparse

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0],"..","..","Image_Lib")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import image_utils as utils
"""
ap = argparse.ArgumentParser("Find clusters in images and colors the image accordingly")
ap.add_argument("-i", "--image", required = True, help ="Path to image")
ap.add_argument("-k", "--clusters", required = False, type = int, help = "No of clusters to form in image (default = 10)")
args = vars(ap.parse_args())
  """  
def image_resize(image, width=-1, height=-1):
    shape = image.shape
    if width == -1:
        if height == -1:
            return image
        else:
            return cv2.resize(image, (int(height * shape[1] / shape[0]), height))
    elif height == -1:
        return cv2.resize(image, (width, int(width * shape[0] / shape[1])))
    else:
        cv2.resize(image, (width, height))
        
image = cv2.imread('C:/pcd/charlie.jpeg').astype("float32")
data = image.reshape((-1,3))
K = 10
"""
if(args["clusters"] != None):
    K = args["clusters"]
"""
termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
ret, lbl, centers = cv2.kmeans(data, K, None, termination, 3, cv2.KMEANS_PP_CENTERS)

centers = centers.astype("uint8")
result = centers[lbl.flatten()]
output = result.reshape(image.shape)
cv2.imshow("Result", image_resize(output, height = 500))
cv2.imwrite("result.jpg", output)
cv2.waitKey()
cv2.destroyAllWindows()