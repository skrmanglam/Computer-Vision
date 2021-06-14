#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:23:55 2021

@author: shubham
"""

import numpy as np

def cross_entropy(Y, P):
    Y= np.float_(Y)
    P=np.float_(P)
    return -np.sum(Y*np.log(P)+(1-Y)*np.log(1-P))