import numpy as np
import matplotlib.pyplot as plt


x_train = np.array([1.0, 2.0]) # diện tích nhà(đơn vị: 1000 sqft)
y_train = np.array([300.0, 500.0])# giá nhà(đơn vị: 1000 đô la)

#model function(hàm dự đoán)
def compute_model_output(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb
plt.scatter(x_train,y_train, marker='x', c='r', label = "Actual Values")
plt.xlabel("Size (1000 sqft)")
plt.ylabel("Price (1000 USD)")
plt.title("Housing Price")
plt.legend()
plt.show()

#compute_cost function
def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost_sum = 0
    
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum = cost_sum + cost
    total_cost = (1/(2*m)) * cost_sum

    return total_cost

# vẽ nhiều đường dự đoán
w_list = [0, 100, 200, 300]
b = 100
plt.scatter(x_train, y_train, c = 'r', marker='x', label = "Actual Values")

for w in w_list:
    y_hat = compute_model_output(x_train,w,b)
    plt.plot(x_train, y_hat, c = 'blue', label = f"w = {w}, b = {b}")
plt.xlabel("Size (1000 sqft)")
plt.ylabel("Price (1000 đô la)")
plt.title("Model Prediction with Different w")
plt.legend()
plt.show()

# vẽ cost theo w
w_range = np.linspace(0,300,100)
b = 100
cost_values = []
for w in w_range:
    res = compute_cost(x_train,y_train, w, b)
    cost_values.append(res)

plt.plot(w_range, cost_values)
plt.xlabel("w")
plt.show()
