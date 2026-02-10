import numpy as np
import matplotlib.pyplot as plt
from lab_utils_common1 import plot_data, sigmoid, draw_vthresh

#data set
X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y = np.array([0, 0, 0, 1, 1, 1]).reshape(-1,1) 
#plot data
fig, ax = plt.subplots(1,1, figsize=(4,4))
pos = y == 1
neg = y == 0
ax.scatter(X[pos[:,0],0], X[pos[:,0],1], c='r', marker='x', label='y = 1') 
ax.scatter(X[neg[:,0],0], X[neg[:,0],1], c='b', marker='o', label='y = 0')
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.set_title('Data Points')
ax.axis([0, 4, 0, 3.5])
ax.legend()

# Plot sigmoid(z) over a range of values from -10 to 10
z = np.arange(-10,11)

fig,ax = plt.subplots(1,1,figsize=(5,3))
# Plot z vs sigmoid(z)
ax.plot(z, sigmoid(z), c="b")

ax.set_title("Sigmoid function")
ax.set_ylabel('sigmoid(z)')
ax.set_xlabel('z')
draw_vthresh(ax,0)
plt.show()

# Plot decision boundary
x0 = np.arange(0,6)
x1 = 3 - x0
fig, ax = plt.subplots(1,1, figsize=(5,4))

ax.plot(x0,x1, c = "b")
ax.axis([0, 4, 0, 3.5])

ax.fill_between(x0, x1,alpha=0.2) # hàm này để tô màu vùng dưới đường thẳng

plot_data(X,y,ax)#vẽ dữ liệu lên cùng đồ thị
ax.set_ylabel(r'$x_1$')
ax.set_xlabel(r'$x_0$')
plt.show()