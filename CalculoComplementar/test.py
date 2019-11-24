import matplotlib.pyplot as plt 
#%matplotlib inline 
#plt.show()
import numpy as np 
from random import sample 

data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show(data)

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)

x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)

# plt.plot(x, y, 'r')
# plt.xlabel('X Axis Title Here')
# plt.ylabel('Y Axis Title Here')
# plt.title('X Axis Title Here')
# plt.show()

# plt.subplot(1,2,1)
# plt.plot(x, y, 'r--')
# plt.subplot(1,2,2)
# plt.plot(y, x, 'g*-')
# plt.show()

# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# axes.plot(x,y, 'b')
# axes.set_xlabel('Set X Label')
# axes.set_ylabel('Set Y Label')
# axes.set_title('Set Title')
# plt.show()


# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# axes1.plot(x, y, 'b')
# axes1.set_xlabel('X_Label_axes1')
# axes1.set_ylabel('Y_Label_axes1')
# axes1.set_title('Axes 1 Title')
# axes2.plot(x, y, 'r')
# axes2.set_xlabel('Set X_Label_axes2')
# axes2.set_ylabel('Set Y_Label_axes2')
# axes2.set_title('Axes 2 Title')

# plt.show()

# fig, axes = plt.subplots()
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# plt.show()

# fig, axes = plt.subplots(nrows=1, ncols=2)
# for ax in axes: 
# 	ax.plot(x, y, 'b')
# 	ax.set_xlabel('x')
# 	ax.set_ylabel('y')
# 	ax.set_title('title')

# plt.show(fig)

# fit = plt.figure(figsize=(8,4), dpi=100)
# print(fit)

# fig, axes = plt.subplots(figsize=(12, 3))

# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# plt.show()
# #PNG, JPG, EPS, SVG, PGF e PDF
# fig.savefig("graph.png", dpi=200)

#legend
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x, x**2, label='x**2')
# ax.plot(x, x**3, label='x**3')
# ax.legend()
# #ax.legend(loc=1) loc == position 
# # ax.legend(loc=2)
# #ax.legend(loc=3)
# #ax.legend(loc=4)
# #ax.legend(loc=0)
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(x, x**2, 'b.-') blue with a pont
# ax.plot(x, x**3, 'g--') green with traceroute
# plt.show()
# fig, ax = plt.subplots()
# ax.plot(x, x+1, color='blue', alpha=0.5) #transparent
# ax.plot(x, x+2, color='#8B008B') #rgb hex code
# ax.plot(x, x+2, color='#FF8C00') #hex code
# plt.show()

#rainbow options

# fig, ax = plt.subplots()
# ax.plot(x, x+1, color='red', linewidth=0.25)
# ax.plot(x, x+2, color='red', linewidth=0.50)
# ax.plot(x, x+3, color='red', linewidth=1.00)
# ax.plot(x, x+4, color='red', linewidth=2.00)

# #type line
# ax.plot(x, x+5, color='green', lw=3, linestyle='-')
# ax.plot(x, x+6, color='green', lw=3, ls='-')
# ax.plot(x, x+7, color='green', lw=3, ls=':')

# #trace
# line, = ax.plot(x, x+8, color='black', lw=1.50)
# line.set_dashes([5,10,15,10]) #format size row, large space

# #add simbols
# ax.plot(x,x+9, color='blue', lw=3, ls='-', marker='+')
# ax.plot(x,x+10, color='blue', lw=3, ls='--', marker='o')
# ax.plot(x,x+11, color='blue', lw=3, ls='-', marker='s')
# ax.plot(x,x+12, color='blue', lw=3, ls='--', marker='1')

# #size and color mark
# ax.plot(x,x+13, color='purple', lw=1, ls='-', marker='o', markersize=2)
# ax.plot(x,x+14, color='purple', lw=1, ls='-', marker='o', markersize=4)
# ax.plot(x,x+15, color='purple', lw=1, ls='-', marker='o', markersize=8, markerfacecolor='red')
# ax.plot(x,x+16, color='purple', lw=1, ls='-', marker='s', markersize=8, markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')

# fig, axes = plt.subplots(1,3, figsize=(12,4))
# axes[0].plot(x, x**2, x, x**3)
# axes[0].set_title("default axes ranges")

# axes[1].plot(x, x**2, x, x**3)
# axes[1].axis('tight')
# axes[1].set_title('tight axes')

# axes[2].plot(x, x**2, x, x**3)
# axes[2].set_ylim([0, 60])
# axes[2].set_ylim([2, 5])
# axes[2].set_title("custom axes range")
# plt.show()

# plt.scatter(x,y)
# plt.show()

