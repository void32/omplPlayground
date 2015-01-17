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
ax = figure.gca() #projection='2d'
ax.plot(data[:,0],data[:,1],'.-')

#plot ball
circle=plt.Circle((0.0,0.0),0.7,fc=np.random.random(3),picker=True, alpha=0.5)
figure.gca().add_patch(circle)

#Display the plot
plt.show(block=True) #keep the window open
