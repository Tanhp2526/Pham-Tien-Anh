import numpy as np
import time

#Vector
"""Vector Vector dot product"""
def my_dot(a,b):
    x = 0
    n = a.shape[0]
    for i in range(n):
        x = x + a[i]*b[i]
    return x
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
c =np.dot(a,b)
d = my_dot(a,b)

"""The Need for Speed: vector vs for loop"""
np.random.seed(1)
a = np.random.rand(10000000)
b = np.random.rand(10000000)
tic = time.time()# chụp thơi gian bắt đầu
c = np.dot(a,b)
toc = time.time()
print(f"np.dot(a,b) : {c:.4f}")
print(f"Vectorized version duration: {1000*(toc-tic):.4f} ms")

tic = time.time()  # capture start time
c = my_dot(a,b)
toc = time.time()  # capture end time

print(f"my_dot(a, b) =  {c:.4f}")
print(f"loop version duration: {1000*(toc-tic):.4f} ms ")

del(a)
del(b)

# show common Course 1 example
X = np.array([[1],[2],[3],[4]])
w = np.array([2])
c = np.dot(X[1], w)
print(X)
print(f"X[1] has shape {X[1].shape}")
print(f"w has shape {w.shape}")
print(f"c has shape {c.shape}")

# Matrix
a = np.arange(6).reshape(-1, 2)
print(a)