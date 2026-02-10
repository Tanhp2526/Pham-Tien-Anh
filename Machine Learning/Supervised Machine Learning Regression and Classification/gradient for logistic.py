import math
import numpy as np
import copy
import matplotlib.pyplot as plt
from lab_utils_common1 import dlc, plt_tumor_data
from plt_quad_logistic import plt_quad_logistic, plt_prob

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def compute_cost_logistic(X,y,w, b):
    m, n = X.shape
    cost = 0.0

    for i in range(m):
        z = np.dot(X[i], w) + b
        f_wb = sigmoid(z)
        cost += -y[i] * np.log(f_wb) - (1 - y[i]) * np.log(1 - f_wb)
    cost = cost / m
    return cost

def plot_data(X,y, ax):
    pos = y == 1
    neg = y == 0
    ax.scatter(X[pos,0], X[pos,1], marker='x', c='b', label='y=1')
    ax.scatter(X[neg,0], X[neg,1], marker='o', c='r', label='y=0')
    ax.legend()

#data set
X_train = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y_train = np.array([0, 0, 0, 1, 1, 1])

fig, ax = plt.subplots(1,1, figsize=(4,4))
plot_data(X_train, y_train, ax)

ax.axis([0,4,0, 3.5])# giới hạn trục 
ax.set_xlabel('$x_0$', fontsize=12)
ax.set_ylabel('$x_1$', fontsize=12)
plt.show()

def compute_gradient_logistic(X, y, w, b):
    m,n = X.shape
    dj_dw = np.zeros((n,))# kích thước (n,) vì w có kích thước (n,)
    dj_db = 0.0

    for i in range(m):
        f_wb_i = sigmoid(np.dot(X[i], w) + b)
        err_i = (f_wb_i - y[i])
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err_i * X[i,j]
        dj_db = dj_db + err_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m   
    return dj_db, dj_dw

X_tmp = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y_tmp = np.array([0, 0, 0, 1, 1, 1])
w_tmp = np.array([2.,3.])
b_tmp = 1.
dj_db_tmp, dj_dw_tmp = compute_gradient_logistic(X_tmp, y_tmp, w_tmp, b_tmp)
print(f"dj_db: {dj_db_tmp}" )
print(f"dj_dw: {dj_dw_tmp.tolist()}")

def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
    J_history = []# lưu cost qua mỗi lần lặp
    w = copy.deepcopy(w_in) # tranh thay đổi w_in ban đầu
    b = b_in

    for i in range(num_iters):
        dj_db, dj_dw = compute_gradient_logistic(X,y,w,b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        if i < 100000:# lưu lại cost trong 100000 lần lặp đầu tiên
            J_history.append(compute_cost_logistic(X,y,w,b))

        if i % math.ceil(num_iters / 10) == 0:# in ra cost mỗi 1/10 số lần lặp
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")    
    return w, b, J_history

w_tmp  = np.zeros_like(X_train[0])# zeros.like tạo mảng zeros có cùng kích thước với X_train[0]
b_tmp  = 0.
alph = 0.1
iters = 10000

w_out, b_out, J_history = gradient_descent(X_train, y_train, w_tmp, b_tmp, alph, iters) 
print(f"\nupdated parameters: w:{w_out}, b:{b_out}")

fig,ax = plt.subplots(1,1,figsize=(5,4))
# plot the probability 
plt_prob(ax, w_out, b_out)

# Plot the original data
ax.set_ylabel(r'$x_1$')
ax.set_xlabel(r'$x_0$')   
ax.axis([0, 4, 0, 3.5])
plot_data(X_train,y_train,ax)

# Plot the decision boundary
x0 = -b_out/w_out[0]
x1 = -b_out/w_out[1]
ax.plot([0,x0],[x1,0], c=dlc["dlblue"], lw=1)
plt.show()
