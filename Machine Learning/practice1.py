import numpy as np
import copy
import matplotlib.pyplot as plt

"""Bài toán: Linear Regression(hồi quy tuyến tính)- ta dự đoán các giá trị y từ các đặc trưng x
   Mục tiêu: tìm w và b sao cho model dự đoán chính xác nhất
   Cần gì: 
   1. Đo lường độ sai lệch(cost function)
   2. Tìm cách cải thiện (gradient - đạo hàm)"""

#Dùng vòng lặp
def compute_cost(X,y,w,b):
    m = X.shape[0]
    cost = 0.0 
    for i in range(m):
        f_wb_i = np.dot(X[i],w) + b
        cost = cost + (f_wb_i - y[i])**2
    cost = cost/(2*m)
    return cost 

#Dùng ma trận
def compute_cost_matrix(X,y,w,b):
    m = X.shape[0]
    f_wb = X @ w + b
    cost = (1/(2*m)) * np.sum((f_wb -y)**2)
    return cost 

X = np.array([[1, 2],    # Mẫu 1: x1=1, x2=2
              [2, 3],    # Mẫu 2: x1=2, x2=3
              [3, 4]])   # Mẫu 3: x1=3, x2=4
y = np.array([5, 8, 11])  # Giá trị thực tế
w = np.array([1, 1])      # Trọng số ban đầu
b = 1

print(f"Cost_function: {compute_cost(X,y,w,b):0.2e}")
print(f"Cost_function_matrix: {compute_cost_matrix(X,y,w,b)}")

#dùng vòng lặp để tính đạo hàm
def compute_gradient(X,y,w,b):
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.0

    for i in range(m):
        err = (np.dot(X[i],w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i,j]
        dj_db = dj_db + err
    
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    return dj_db, dj_dw

#dùng ma trận để tính đạo hàm
def compute_gradient_matrix(X,y,w,b):
    m,n = X.shape
    f_wb = X @ w + b
    err = f_wb - y
    dj_dw = (1/m) * (X.T @ err)
    dj_db = (1/m) * sum(err)
    return dj_db, dj_dw
dj_db1, dj_dw1 = compute_gradient(X,y,w,b)
dj_db2, dj_dw2 = compute_gradient_matrix(X,y,w,b)
print(f"Compute_gradient: {compute_gradient(X,y,w,b)}, dj_db1: {float(dj_db1)}, dj_dw1: {dj_dw1}")
print(f"Compute_gradient_matrix: {compute_gradient_matrix(X,y,w,b)}") 


