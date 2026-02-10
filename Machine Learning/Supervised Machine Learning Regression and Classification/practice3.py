import numpy as np
import matplotlib.pyplot as plt
from utils import *
import copy
import math

def load_data(file_name):
    data = np.loadtxt(file_name, delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X,y

def sigmoid(z):
    return 1/(1+ np.exp(-z))

def plot_data(X,y,ax):
    pos = y == 1
    neg = y == 0

    ax.scatter(X[pos,0], X[pos,1], marker = '+', c ='r', label = "Admitted")
    ax.scatter(X[neg,0], X[neg,1], marker = 'o', c = 'b', label = "Not admitted")
    ax.legend()

X_train, y_train = load_data()

print("First five elements in X_train are:\n", X_train[:5])
print("Type of X_train:",type(X_train))

print("First five elements in y_train are:\n", y_train[:5])
print("Type of y_train:",type(y_train))

print ('The shape of X_train is: ' + str(X_train.shape))
print ('The shape of y_train is: ' + str(y_train.shape))
print (f"We have m {len(y_train)} training examples")

# Plot examples
fig, ax= plt.subplots(1,1, figsize=(5,4))
plot_data(X_train,y_train,ax)

# Set the y-axis label
plt.ylabel('Exam 2 score') 
# Set the x-axis label
plt.xlabel('Exam 1 score') 
plt.legend(loc="upper right")
plt.show()

def compute_cost(X,y,w,b, *argv):
    m,n = X.shape
    cost = 0.0

    for i in range(m):
        z = np.dot(X[i],w) + b
        f_wb = sigmoid(z)
        cost += -y[i]*np.log(f_wb) - (1-y[i])*np.log(1-f_wb)
    cost = cost/m
    return cost 

def compute_gradient(X,y,w,b, *argv):
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.0

    for i in range(m):
        z = np.dot(X[i],w) + b
        f_wb = sigmoid(z)
        err = f_wb - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i,j]
        dj_db = dj_db + err
    dj_dw = dj_dw/m
    dj_db = dj_db / m
    return dj_db, dj_dw

def gradient_descent(X,y,w_in, b_in, cost_function, gradient_function, alpha, num_iters, lambda_):
    m = len(X)

    J_history = []
    w_history = []

    for i in range(num_iters):
        dj_db, dj_dw = compute_gradient(X,y,w_in, b_in, lambda_)

        w = w - alpha*dj_dw
        b = b - alpha*dj_db

        if i < 10000:
            J_history.append(compute_cost(X,y, w_in, b_in, lambda_))

        if i% math.ceil(num_iters/10) == 0 or i == (num_iters-1):
            w_history.append(w_in)
            print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.2f}   ")
        
    return w_in, b_in, J_history, w_history

def predict(X,w,b):
    m = X.shape[0]
    y_pred = np.zeros(m)
    z = np.dot(X,w) + b
    f_wb = sigmoid(z)

    for i in range(m):
        if f_wb[i] >= 0.5:
            y_pred[i] = 1
        else:
            y_pred[i] = 0
    return y_pred



    