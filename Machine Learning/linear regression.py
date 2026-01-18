"""Use the motivating example of housing price prediction.
This lab will use a simple data set with only two data points:
* a house with 1000 square feet(sqrt) sold for $300000
* a house with 2000 square feet sold for $500000

Two points will constitute của traing set(bộ đào tạo)"""

import numpy as np
import matplotlib.pyplot as plt


# x_train là biến đầu vào(size của ngôi nhà được tính theo đơn vị 1000 feet)
x_train = np.array([1.0, 2.0])
#y_train là mục tiêu(giá được tính theo 1000 đô)
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
print("===================")
#m là số lượng ví dụ đào tạo
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]#trả về số hàng và số cột của mảng
print(f"Số lượng ví dụ đào tạo: {m}")
print("===================")
#lấy mẫu huấn luyện
i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i}) = ({x_i}, {y_i}))")
print("===================")

#model function
w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")

def compute_model_output(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()


#dự đoán giá nhà với 1200 feet^2 
x_i = 1.2
cost_1200sqft = w * x_i + b

print(f"${cost_1200sqft:.0f} thousand dollars")