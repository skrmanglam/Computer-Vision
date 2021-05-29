# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# read image and print stats
image=mpimg.imread('test.jpg')
print('This image is:', type(image),'with dimensions:', image.shape)
#plt.imshow(image)

#grab the x and y size and make a copy of the image
ysize=image.shape[0]
xsize=image.shape[1]

color_select=np.copy(image)

#Define our color slection criteria
red_threshold=200
green_threshold=200
blue_threshold=200
rgb_threshold=[red_threshold,green_threshold,blue_threshold]

# Identify pixels below the threshold
color_thresholds=(image[:,:,0]<rgb_threshold[0])\
            |(image[:,:,1]<rgb_threshold[1])\
            |(image[:,:,2]<rgb_threshold[2]) 

#color_select[thresholds]=[0,0,0]

#Display the image
#plt.imshow(color_select)
#plt.show()

# Appending ROI concept
#define a traingular ROI
#x=0 and y=0 upper left
left_bottom=[0,539]
right_bottom=[900,539]
apex=[475,320]


##Using points to draw lines
#Fit lines (y=mx+b) to identify the 3 sided roi
#np.ployfit() returns m and b co-efficient of the fit
fit_left=np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right=np.polyfit((right_bottom[0],apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom=np.polyfit((left_bottom[0],right_bottom[0]),(left_bottom[1],right_bottom[1]),1)

# find the region inside ROI
XX, YY= np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))
region_thresholds=(YY>(XX*fit_left[0]+fit_left[1]))&\
                (YY>(XX*fit_right[0]+fit_right[1]))&\
                (YY<(XX*fit_bottom[0]+fit_bottom[1]))
                
#color pixel red which are inside the ROI
region_select=np.copy(image)
region_select[region_thresholds]=[255,0,0]

#Display the image
plt.imshow(region_select)

#appending line logic
line_image=np.copy(image)

# mask color selection
color_select[color_thresholds]=[0,0,0] 

# find where image is both colored right and in the region
line_image[~color_thresholds & region_thresholds]=[255,0,0]

# Display 2 op images
plt.imshow(color_select)
plt.imshow(line_image)
