#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:16:37 2021

@author: shubham
"""

import numpy as np

# A function that takes as input a list of numbers and returns
# the list of values given by softmax function

def softmax(L):
    expL = np.exp(L)
    return np.divide (expL, expL.sum())