#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:20:59 2019

@author: tiago
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
from  time import time

#%% For plotting 3D
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#%%
def createWhiteDisk(height = 100, width = 100, xc = 50, yc = 50, rc = 20):
    disk = np.zeros((height, width), np.float64)
    for x in range(disk.shape[0]):
        for y in range(disk.shape[1]):
            if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= rc * rc:
                disk[x][y] = 1.0
    return disk

def createWhiteDisk2(height = 100, width = 100, xc = 50, yc = 50, rc = 20):
    xx, yy = np.meshgrid(range(height), range(width))
    img = np.array(
            ( (xx - xc)**2 + (yy - yc)**2 - rc**2  ) < 0).astype('float64')
    return img

def createSineImage2(height = 100, width = 100, freq = 0.5, theta = 0):
    img = np.zeros((height, width), dtype=np.float64)
    xx, yy = np.meshgrid(range(height), range(width))
    theta = np.deg2rad(theta)
    rho = (xx * np.cos(theta) - yy * np.sin(theta))
    img[:] = np.sin(2 * np.pi * freq * rho)
    return img

#%% Define image's parameters.
height = 100
width= 100
xc = height/2
yc = width/2
rc = 20

#%% Illustrate the use  of meshgrid.
xx, yy = np.meshgrid(range(height), range(width))
plt.subplot(121), plt.imshow(xx, cmap='gray')
plt.subplot(122), plt.imshow(yy, cmap='gray')
plt.show()

#%% Create a praboloid
zz = (xx - width//2)**2 + (yy - height//2)**2
plt.imshow(zz)
plt.show()

#%% This import registers the 3D projection, but is otherwise unused.
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#plt.savefig('paraboloid')


#%%
tic = time()
img = createWhiteDisk()
toc = time()
print(1000 * (toc - tic))
plt.imshow(disk, cmap="gray")
plt.show()

#%%
tic = time()
img = createWhiteDisk2()
toc = time()
print(1000 * (toc - tic))
plt.imshow(disk, cmap="gray")
plt.show()


#%%
img3 = createSineImage2()
plt.imshow(img3, cmap='gray')
plt.show()

#%%
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, img3, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()



