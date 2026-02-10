import copy, math
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2)  # reduced display precision on numpy arrays 

X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
Y_train = np.array([460, 232, 178])

print(f"X Shape: {X_train.shape}, X Type: {type(X_train)}")
print(X_train)
print(f"y Shape: {Y_train.shape}, y Type: {type(Y_train)}")
print(Y_train)

b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
print(f"w_init shape: {w_init.shape}, b_init type: {type(b_init)}")

# Single Prediction element by element
"""𝑓𝐰,𝑏(𝐱)=𝑤0𝑥0+𝑤1𝑥1+...+𝑤𝑛−1𝑥𝑛−1+𝑏"""
def predict_single_loop(x,w,b):
    n = x.shape[0]
    p = 0
    for i in range(n):
        p_i = w[i]*x[i]
        p = p + p_i
    p = p + b
    return p
x_vec = X_train[0,:]
print(x_vec)
f_wb = predict_single_loop(x_vec,w_init, b_init)
print(f_wb)

#Single Prediction, vector
def predict(x, w,b):
    p = np.dot(x,w) + b
    return p
f_wb1 = predict(x_vec,w_init, b_init)
print(f_wb1)

# Compute Cost With Multiple Variables
def compute_cost(X, y,w, b):
    m = X.shape[0]
    cost = 0
    for i in range(m):
        f_wb2 = np.dot(X,w) + b
        cost = cost + (f_wb - y[i]) ** 2
    cost = cost / (2*m)
    return cost
res = compute_cost(X_train, Y_train, w_init, b_init)
print(res)

# Gradient Descent With Multiple Variables
"""Compute Gradient with Multiple Variables(Đạo hàm)"""
def compute_gradient(X,y,w,b):
    """Tính đạo hàm riêng của hồi quy tuyến tính
    Tham số:
      X (ndarry (m,n)): dữ liệu, m ví dụ với n đặc trưng
      y (ndarry (m,)): giá trị mục tiêu
      w (ndarry, (n,)): tham số mô hình
      b (scalar): tham số mô hình 
      
    Trả về: 
      dj_dw (ndarray (n,)): đạo hàm riêng theo tham số w
      dj_db (scalar): đạo hàm riêng theo tham số b"""
    
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    for i in range(m):
        err = (np.dot(X[i],w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i,j]
        dj_db = dj_db + err
    
    dj_dw = dj_dw / m                                
    dj_db = dj_db / m                                
        
    return dj_db, dj_dw

tmp_dj_db, tmp_dj_dw = compute_gradient(X_train, Y_train, w_init, b_init)
print(f'dj_db at initial w,b: {tmp_dj_db}')
print(f'dj_dw at initial w,b: \n {tmp_dj_dw}')

"""Gradient Descent With Multiple Variables"""
def gradient_descent(X,y,w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    J_history = []
    w = copy.deepcopy(w_in) 
    b = b_in
    
    for i in range(num_iters):

        dj_db,dj_dw = gradient_function(X, y, w, b)   

       
        w = w - alpha * dj_dw              
        b = b - alpha * dj_db             
      
       
        if i<100000:      
            J_history.append( cost_function(X, y, w, b))

        #in ra chi phí sau mỗi 10 lần hoặc nếu vòng lặp < 10
        print_every = max(1, num_iters // 10)
        if i % print_every == 0:
            print(f"Iterattion {i:4} Cost {J_history[-1]:0.2e}",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")
        
    return w, b, J_history 

# initialize parameters
initial_w = np.zeros_like(w_init)
initial_b = 0.
# some gradient descent settings
iterations = 1000
alpha = 5.0e-7
# run gradient descent 
w_final, b_final, J_hist = gradient_descent(X_train, Y_train, initial_w, initial_b,
                                                    compute_cost, compute_gradient, 
                                                    alpha, iterations)
print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m,_ = X_train.shape
for i in range(m):
    print(f"prediction: {np.dot(X_train[i], w_final) + b_final:0.2f}, target value: {Y_train[i]}")

# plot cost versus iteration  
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12, 4))
ax1.plot(J_hist)
ax2.plot(100 + np.arange(len(J_hist[100:])), J_hist[100:])
ax1.set_title("Cost vs. iteration");  ax2.set_title("Cost vs. iteration (tail)")
ax1.set_ylabel('Cost')             ;  ax2.set_ylabel('Cost') 
ax1.set_xlabel('iteration step')   ;  ax2.set_xlabel('iteration step') 
plt.show()
