import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,100,5)
z = np.linspace(0,10000, 5)
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5, .4, .4])
ax1.plot(x, z, 'b')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
x = np.linspace(20,22,5)
y = np.linspace(30,50,5)
ax2.plot(x, y, 'b')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom');
plt.show()