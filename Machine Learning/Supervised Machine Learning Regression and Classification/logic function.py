import numpy as np
import matplotlib.pyplot as plt
from plt_one_addpt_onclick import plt_one_addpt_onclick
from lab_utils_common1 import draw_vthresh

#Input is an array
input_array = np.array([1,2,3])
exp_array = np.exp(input_array)

print("Input to exp:", input_array)
print("Output of exp:", exp_array)

#Input is single number
input_val = 1
exp_val = np.exp(input_val)

print("Input of exp:", input_val)
print("Output of exp:", exp_val)

# Sigmoid function
def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g

# Generate an array of evenly spaced values between -10 and 10
z_tmp = np.arange(-10 , 11)
y = sigmoid(z_tmp)

np.set_printoptions(precision = 3)# bảo đảm in ra 3 chữ số thập phân
print("Input (z), Output (sigmoid(z)")
print(np.c_[z_tmp, y]) #np.c_ để ghép mảng theo cột

# plot z vs sigmoid(z)
fig, ax = plt.subplots(1,1, figsize=(5,3))
ax.plot(z_tmp, y, c="b")

ax.set_title('Sigmoid Function')
ax.set_xlabel('z')
ax.set_ylabel('sigmoid(z)')
draw_vthresh(ax,0)

#logistic function 
x_train = np.array([0. , 1, 2, 3, 4, 5])
y_train = np.array([0, 0, 0, 1, 1, 1])

w_in = np.zeros((1))
b_in = 0

plt.close('all') 
addpt = plt_one_addpt_onclick( x_train,y_train, w_in, b_in, logistic=True)
plt.show()


