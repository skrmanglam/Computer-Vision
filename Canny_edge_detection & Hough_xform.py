#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:42:19 2021

@author: shubham
"""
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
image= mpimg.imread('exit_ramp.jpg')
plt.imshow(image)


#greyscale conversion
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) 
#plt.imshow(gray, cmap='gray')

#Define a kernel size for Gaussian smoothing/blurring
#Note: this step is optional as cv2.Canny() applies a 5*5 gaussian(blur) internally
#Note: A larger kernel_size implies averaging, or smoothing, over a larger area.

kernel_size=5
blur_gray=cv2.GaussianBlur(gray,( kernel_size, kernel_size),0)

#Define parameters for Canny and runit
low_threshold=50
high_threshold=150
edges= cv2.Canny(blur_gray,low_threshold,high_threshold)

#display the image
plt.imshow(edges, cmap='Greys_r')

#code to create maskedd egges image using cv2.fillPly()
mask=np.zeros_like(edges)
ignore_mask_color=255 

#defining a 4 sided polygon to mask
imshape=image.shape
vertices=np.array([[(0, imshape[0]),(450,290),(490,290),(imshape[1],imshape[0])]],dtype=np.int32)
cv2.fillPoly(mask,vertices,ignore_mask_color)
masked_edges=cv2.bitwise_and(edges,mask)



##############Hough Xform code#######################################

#Define Hough transform Parameters
#Make a blanj the same size as our image to draw om
rho=2               #distance resolution in pixels of the Hough grid
theta=np.pi/180     #angular resolution in radians of the hough grid
threshold =15        #minimum no of votes(intersections in Hough grid cell)
min_line_length=40  #minimum number of pixel making a line
max_line_gap=20      #maximum gap in pixels making up a line

#creating a blank to draw lines on
line_image=np.copy(image)*0 

#Run hpugh on edge detected image
#Output"lines" is an array containing endpoints of the detected line segments
lines = cv2.HoughLinesP(masked_edges,rho, theta, threshold, np.array([]),min_line_length, max_line_gap)

#Iterate over the ouput "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
        
#create a "color" binary image to combine with line image
color_edges=np.dstack((edges, edges, edges))

#Draw lines on the edge image
line_edges=cv2.addWeighted(color_edges, 0.8, line_image, 1,0)
plt.imshow(line_edges)        
        