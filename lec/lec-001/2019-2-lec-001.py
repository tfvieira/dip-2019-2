#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:10:53 2019

@author: tiago
"""

#%% Import modules
import os
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

print("NumPy version: ", np.__version__)
print("OpenCV version: ", cv2.__version__)
print("Current working directory: ", os.getcwd())
print("Python interpreter path: ", sys.executable)

folder = "/Users/tiago/Dropbox/pro/src/cvi/dip/db"

#%% Read a grayscale image
img = cv2.imread(os.path.join(folder, "baboon.png"), cv2.IMREAD_GRAYSCALE)
if img.all() == None:
    print("Image not found")

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.imshow("img", img)
#cv2.waitKey(0)
while True:
    if 0xFF & cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

#%% Read a color image
img = cv2.imread(os.path.join(folder, "baboon.png"), cv2.IMREAD_COLOR)
if img.all() == None:
    print("Image not found")

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.imshow("img", img)
while True:
    if 0xFF & cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

#%%
bgr = cv2.imread(os.path.join(folder, "baboon.png"), 
                 cv2.IMREAD_COLOR)
if bgr.all() == None:
    print("Image not found")

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

#%% Splitting RGB channels
bgr = cv2.imread(os.path.join(folder, "baboon.png"), 
                 cv2.IMREAD_COLOR)

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
rgb_lst = cv2.split(rgb)

plt.figure(1), plt.clf
plt.subplot(232), plt.imshow(rgb), plt.title('RGB')
plt.subplot(234), plt.imshow(rgb_lst[0], cmap='gray'), plt.title('R')
plt.subplot(235), plt.imshow(rgb_lst[1], cmap='gray'), plt.title('G')
plt.subplot(236), plt.imshow(rgb_lst[2], cmap='gray'), plt.title('B')
plt.show()

#%% Using function handle
bgr2rgb = lambda x : cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
bgr = cv2.imread(os.path.join(folder, "baboon.png"), 
                 cv2.IMREAD_COLOR)
plt.figure(2)
plt.imshow(bgr2rgb(bgr))
plt.show()

#%% Splitting RGB channels
bgr = cv2.imread(os.path.join(folder, "baboon.png"), 
                 cv2.IMREAD_COLOR)
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(rgb)

plt.figure(1), plt.clf
plt.subplot(232), plt.imshow(rgb), plt.title('RGB')
plt.subplot(234), plt.imshow(r, cmap='gray'), plt.title('R')
plt.subplot(235), plt.imshow(g, cmap='gray'), plt.title('G')
plt.subplot(236), plt.imshow(b, cmap='gray'), plt.title('B')
plt.show()























