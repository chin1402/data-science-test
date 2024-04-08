# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:09:46 2024

@author: INSHA7
"""

import os
os.chdir(r"C:\Users\INSHA7\Downloads\Check")

import rpy2.robjects as robjects
robjects.r['source']('Sen_word.R')

return_str = robjects.r['main']()

print(return_str)
print("hi")