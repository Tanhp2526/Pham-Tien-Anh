import numpy as np
import matplotlib.pyplot as plt
import copy
import math

#hàm load dữ liệu
def load_data():
    data = np.loadtxt("./Machine Learning/Supervised Machine Learning/ex1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X,y

def load_data_multi():
    data = np.loadtxt("./Machine Learning/Supervised Machine Learning/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X,y

#load the dataset
"""x_train: dân số của thành phố
   y_train: lợi nhuận của cửa hàng đó trong thành phố"""
x_train, y_train = load_data()
print("Type of X_train:", type(x_train))
print("First five elements of x_train are:\n", x_train[:5])

print("Type of y_train:", type(y_train))
print("First five elements of y_traing are:\n", y_train[:5])

print ('The shape of x_train is:', x_train.shape)
print ('The shape of y_train is: ', y_train.shape)
print ('Number of training examples (m):', len(x_train))

#Visualize your data
plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Profits vs. Population per city")
plt.ylabel('Profit in $10,000')
plt.xlabel('Population of City in 10,000s')
plt.legend()
plt.show()

#ex1: Compute_cost
def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i])**2
    cost = cost/(2*m)
    return cost

# Compute cost with some initial values for paramaters w, b
initial_w = 2
initial_b = 1

cost = compute_cost(x_train, y_train, initial_w, initial_b)
print(type(cost))
print(f'Cost at initial w: {cost:.3f}') 

#ex2: Compute_gradient
def compute_gradient(x,y,w,b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw = dj_dw + (f_wb - y[i])*x[i]
        dj_db = dj_db + (f_wb - y[i])
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    return dj_dw, dj_db

initial_w = 0
initial_b = 0
tmp_dj_dw, tmp_dj_db = compute_gradient(x_train, y_train, initial_w, initial_b)
print("Gradient at initial w, b (zeros):", tmp_dj_dw, tmp_dj_db)

test_w = 0.2
test_b = 0.2
tmp_dj_dw, tmp_dj_db = compute_gradient(x_train, y_train, test_w, test_b)

print('Gradient at test w, b:', tmp_dj_dw, tmp_dj_db)

#chạy toàn bộ các mẫu huẩn luyện qua mỗi lần lặp(gradient descent)
def gradient_descent(x,y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    m = len(x)
    J_history = []
    w_history = []
    w = copy.deepcopy(w_in)
    b = b_in

    for i in range(num_iters):

        dj_dw1, dj_db1 = compute_gradient(x,y,w,b)

        w = w - alpha * dj_dw1
        b = b - alpha * dj_db1

        if i < 100000: # tránh cạn kiệt tài nguyên
            cost = compute_cost(x,y,w,b)
            J_history.append(cost)

        if i % math.ceil(num_iters / 10) == 0:
            w_history.append(w)
            print(f"Iteration {i:4} Cost {float(J_history[-1]):8.2f}")

    return w, b, J_history, w_history 

initial_w = 0.
initial_b = 0.

# some gradient descent settings
iterations = 1500
alpha = 0.01

w,b,_,_ = gradient_descent(x_train ,y_train, initial_w, initial_b, 
                     compute_cost, compute_gradient, alpha, iterations)
print("w,b found by gradient descent:", w, b)

m = x_train.shape[0]
f_wb = np.zeros(m)

for i in range(m):
    f_wb[i] = w * x_train[i] + b

plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Profits vs. Population per city")
plt.ylabel("Profit in $10,000")
plt.xlabel("Population of City in 10,000s")
plt.plot(x_train, f_wb, c='b')
plt.legend()
plt.show()

predict1 = 3.5 * w + b
print('For population = 35,000, we predict a profit of $%.2f' % (predict1*10000))


