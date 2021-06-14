#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:16:20 2021

@author: shubham
"""

import numpy as np


#Defining the sigmoid function for activation
def sigmoid(x):
    return 1/(1+np.exp(-x))

#derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

#Input data
x=np.array([1,2])
#Target
y=np.array(0.5)
#Initial weights
weights=np.array([0.5,-0.5])

#The learning rate, eta in the weight step equation
learnrate=0.5

#The neural network output(y-hat)
nn_output=sigmoid(x[0]*weights[0]+x[1]*weights[1])
# or nn_output=sigmoid(np.dot(x,weights))

#output error(y-y-hat)
error=y-nn_output

#error term(lowercase delta)
error_term=error*sigmoid_prime(np.dot(x,weights))

#Gradient descent step
del_ws=[learnrate*error_term*x[0],learnrate*error_term*x[1]]
#or del_w=learnrate*error_term*x

#calculate the change in weights
del_w=learnrate*error*nn_output*(1-nn_output)*x

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(del_w)