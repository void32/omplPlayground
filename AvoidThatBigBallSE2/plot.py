from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
data = numpy.loadtxt('/tmp/path.txt')
fig = plt.figure()
ax = fig.gca() #projection='2d'
ax.plot(data[:,0],data[:,1],'.-')
plt.show()

