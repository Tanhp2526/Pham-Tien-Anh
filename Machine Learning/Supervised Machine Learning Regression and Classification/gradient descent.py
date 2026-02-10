import numpy as np
import matplotlib.pyplot as plt

#Data set
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

#Model function
def compute_model_outpuw(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb

#cost function
def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i]) ** 2
    total_cost = (cost) / (2*m)
    return total_cost

#compute_gradient(tính đạo hàm)
def compute_gradient(x,y,w,b):
    """
    Computes the gradient for linear regression
    Tham số:
    x (ndarray (m,)): dữ liệu , m là số ví dụ
    y (ndarry (m,)): giá trị mục tiêu
    w,b(scalar) : tham số mô hình

    Return
    dj_dw (scalar): the gradient of the cost w.r.t the parameters w
    dj_db (scalar): the gradient of the cost w.r.t the parameter b 
    """
    m = x.shape[0]
    dj_dw = 0.0
    dj_db = 0.0

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw_i = (f_wb - y[i]) * x[i]
        dj_db_i = f_wb - y[i]
        dj_dw = dj_dw + dj_dw_i
        dj_db = dj_db + dj_db_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db

#gradient descent
"""Thực hiện giảm độ dốc để phù hợp w,b.
Cập nhật w,b bằng cách thực hiện từng bước giảm độ dốc với tốc độ học alpha.

Tham số: 
x : (mảng) dữ liệu, m ví dụ
y: (mảng) giá trị mục tiêu
w_in,b_in(scalar): giá trị khởi tạo
alpha: tốc độ học tập
number_iters (int): số vòng lặp để chạy giảm độ dốc
cost_function: hàm để gọi tới chi phí 
gradient_function: hàm gọi tới độ dốc

Trả về:
w,b(scalar): cập nhật giá trị tham số sau lần chạy giảm độ dốc
J_history(list): lưu trữ giá trị chi phí sau mỗi lần chạy
p_history(list): lưu trữ giá trị của cặp [w,b]"""

def gradient_descent(x,y, w_in, b_in, alpha, number_iters, cost_function, gradient_function):
    #Khởi tạo mảng lưu trữ
    J_history = []
    p_history = []
    b = b_in
    w = w_in

    for i in range(number_iters):
        #tính đạo hàm
        dj_dw, dj_db= compute_gradient(x,y,w,b)
        
        #update
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        #save
        if i < 100000: #ngăn chặn cạn kiệt tài nguyên
            J_history.append(compute_cost(x,y,w,b))
            p_history.append([w,b])

        #in ra chi phí sau mỗi 10 lần hoặc nếu vòng lặp < 10
        print_every = max(1, number_iters // 10)
        if i % print_every == 0:
            print(f"Iterattion {i:4} Cost {J_history[-1]:0.2e}",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")
            
    return w,b,J_history,p_history

# initialize parameters
w_init = 0
b_init = 0
# some gradient descent settings
iterations = 10000
tmp_alpha = 1.0e-2
# run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha, 
                                                    iterations, compute_cost, compute_gradient)
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")

# plot cost versus iteration  
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout= True, figsize=(12,4))
ax1.plot(np.arange(100),J_hist[:100])
ax2.plot(1000 + np.arange(len(J_hist[1000:])), J_hist[1000:])
ax1.set_title("Cost vs. iteration(start)")
ax2.set_title("Cost vs. iteration(end)")
ax1.set_xlabel('iteration step')
ax2.set_xlabel('iteration step')
ax1.set_ylabel('Cost')
ax2.set_ylabel('Cost')
plt.show()

#dự đoán giá nhà
print(f"1000 sqft house prediction {w_final*1.0 + b_final:0.1f} Thousand dollars")
print(f"1200 sqft house prediction {w_final*1.2 + b_final:0.1f} Thousand dollars")
print(f"2000 sqft house prediction {w_final*2.0 + b_final:0.1f} Thousand dollars")