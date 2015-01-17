#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#setup figure
figure = plt.figure('Plot of path')
figure.gca().set_aspect('equal')
figure.gca().set_xlim(-1, 1)
figure.gca().set_ylim(-1, 1)

#plot data
data = np.loadtxt('/tmp/path.txt')
print data
ax = figure.gca() #projection='2d'
ax.plot(data[:,0],data[:,1],'.-')

#plot ball
ball = np.loadtxt('/tmp/ball.txt')
xBall, yBall, radiusBall = ball[0], ball[1], ball[2]
circle=plt.Circle((xBall,yBall),radiusBall,fc=np.random.random(3),picker=True, alpha=0.5)
figure.gca().add_patch(circle)

#Display the plot
plt.show(block=True) #keep the window open
