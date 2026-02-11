import numpy as np
import copy
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset
from public_tests import *

""" Dataset bao gồm: 
    - Một tập huấn luyện m_train ảnh được gán nhãn là mèo(y = 1) hoặc không phải mèo(y=0)
    - Một tập kiểm tra m_test ảnh được gán nhãn là mèo hoặc không phải mèo
    - Mỗi bức ảnh có kích thước (num_px, num_px, 3)"""

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
#example
index = 27
plt.imshow(train_set_x_orig[index])


m_train = train_set_x_orig.shape[0]#m_train có kích thước(số mẫu, num_px, num_px,3)
m_test = test_set_x_orig.shape[0]
num_px = train_set_x_orig.shape[1]

train_set_x_flatten = train_set_x_orig.reshape(m_train, -1).T
test_set_x_flatten = test_set_x_orig.reshape(m_test, -1).T

# để biểu diễn ảnh màu thì mỗi pixel phải có dạng vector gồm 3 số, mỗi số nằm trong khoảng 0-255
# chuẩn hóa tập dữ liệu 
train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x_flatten / 255

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def initialize_with_zeros(dim):
    w = np.zeros((dim,1))
    b = 0.0
    return w,b

def propagate(w, b, X, Y):
    m = X.shape[1]

    A = sigmoid(np.dot(w.T, X)+b)
    cost = -(1/m)* (np.sum(Y*np.log(A)+(1-Y)*np.log(1-A)))

    dw = (1/m)* np.dot(X,(A-Y).T)
    db = (1/m)* np.sum(A-Y)

    cost = np.squeeze(np.array(cost))

    grads = {"dw": dw, "db": db}

    return grads, cost

def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False):
   
    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    
    costs = []
    
    for i in range(num_iterations):
        
        grads, cost = propagate(w, b, X, Y)
        
        dw = grads["dw"]
        db = grads["db"]
        
    
        w = w - learning_rate*dw
        b = b - learning_rate*db
        
        
        if i % 100 == 0:
            costs.append(cost)
            if print_cost:
                print ("Cost after iteration %i: %f" %(i, cost))
    
    params = {"w": w,
              "b": b}
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    A = sigmoid(np.dot(w.T,X)+b)
    
    for i in range(A.shape[1]):
        if A[0,i] > 0.5:
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0    
    return Y_prediction


def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):

    w, b = initialize_with_zeros(X_train.shape[0])

    params, grads, costs = optimize(
        w, b, X_train, Y_train,
        num_iterations=num_iterations,
        learning_rate=learning_rate,
        print_cost=print_cost
    )

    w = params["w"]
    b = params["b"]

    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    if print_cost:
        print("train accuracy: {} %".format(
            100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
        print("test accuracy: {} %".format(
            100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {
        "costs": costs,
        "Y_prediction_test": Y_prediction_test,
        "Y_prediction_train": Y_prediction_train,
        "w": w,
        "b": b,
        "learning_rate": learning_rate,
        "num_iterations": num_iterations
    }
    return d

logistic_regression_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.005, print_cost=True)

m_test = test_set_x.shape[1]
index_random = np.random.randint(m_test)

plt.imshow(test_set_x_orig[index_random])
plt.axis('off')
plt.title(f"Ảnh test index = {index_random}")
plt.show()

x_rand = test_set_x[:, index_random:index_random+1]
y_true = int(test_set_y[0, index_random])
y_pred = int(predict(logistic_regression_model["w"],
                     logistic_regression_model["b"],
                     x_rand)[0, 0])

# Giải thích nhãn (0 = không mèo, 1 = mèo)
label_meaning = {0: "không phải mèo", 1: "là mèo"}

print("Ảnh test index =", index_random)
print(f"Nhãn thật (y)  = {y_true} -> {label_meaning[y_true]}")
print(f"Dự đoán (ŷ)     = {y_pred} -> {label_meaning[y_pred]}")

