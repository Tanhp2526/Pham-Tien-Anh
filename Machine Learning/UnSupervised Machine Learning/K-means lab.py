import numpy as np
import matplotlib.pyplot as plt
from utils import *
import os 

# tìm tâm cụm gần nhất(finding closest centroids)
"""ý tưởng bài toán: 
   Dữ liệu : X
   Các entroids: u0 đến uk-1 (các cụm tâm)
   
   nhiệm vụ là : ta cần tìm cho mỗi điểm dữ liệu x(i) thì c(i) := j nếu min||x(i)-uj||**2
   
   hiểu đơn giản là khoảng cách từ điểm dữ liệu đến tất cả cá entroids và chọn centroids nhỏ nhất và lưu nó vào idx[i]"""
def find_closest_centroids(X, centroids):
    
    m = X.shape[0]
    K = centroids.shape[0]
    idx = np.zeros(m, dtype=int)

    for i in range(m):
        distance = np.zeros(K)
        for j in range(K):
            distance[j] = np.sum((X[i] - centroids[j])**2)
        
        idx[i] = np.argmin(distance)
    return idx

#Compute centroid means(tính giá trị trung bình của các tâm cụm)
# tức là tính giá trị trinh bình của các điểm dữ liệu đã được gán vào tâm cụm đó.

def compute_centroids(X, idx, K):
    m,n = X.shape
    centroids = np.zeros((K,n))

    for k in range(K):
        points = X[idx == k] # danh sách điểm dữ liệu trong X được gán vào tâm cụm k
        centroids[k] = np.mean(points, axis=0)
    return centroids

def run_kMeans(X, initial_centroids, max_iters = 10, plot_progess = False):
    m,n = X.shape
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    previous_centroids = centroids
    idx = np.zeros(m)
    plt.figure(figsize=(8,6))
    
    #Run
    for i in range(max_iters):

        print(f"K-Mean iteration {(i, max_iters-1)}")

        idx = find_closest_centroids(X, centroids)

        if plot_progess:
            plot_progress_kMeans(X,centroids, previous_centroids,idx,K,i)
            previous_centroids = centroids
        
        centroids = compute_centroids(X,idx,K)
    plt.show()
    return centroids, idx

def kMeans_init_centroids(X,K):
    m = X.shape[0]
    indices = np.random.choice(m, K, replace = False)
    centroids = X[indices]
    return centroids




original_img = plt.imread('File/bird_small.png')
plt.imshow(original_img)
plt.show()
print("Shape of original_img is:", original_img.shape)

"""Vì đầu vào thuật toán K-means là a matrix 2D trong đó mỗi hàng là một mẫu dữ liệu và mỗi cột là một đặc trưng
   nên ta cần chuyển ảnh từ dạng matrix 3D 128x128x3 về dạng mx3 
   trong đó m là tổng số pixel, có 3 đặc trưng là R,G,B"""

X_img = np.reshape(original_img, (original_img.shape[0]*original_img.shape[1],3))

K = 16          
max_iters = 10  

initial_centroids = kMeans_init_centroids(X_img, K)
centroids, idx = run_kMeans(X_img, initial_centroids, max_iters=max_iters)

# Tìm tâm cụm gần nhất cho các điểm dữ liệu(điểm ảnh)
idx = find_closest_centroids(X_img, centroids)

# Thay thế mỗi điểm ảnh bằng giá trị màu của centroid gần nhất tương ứng
X_recovered = centroids[idx, :] 

# Thay đổi kích thước của ảnh về như lúc ban đầu
X_recovered = np.reshape(X_recovered, original_img.shape) 

#  HIỂN THỊ KẾT QUẢ 
# Display original image
fig, ax = plt.subplots(1,2, figsize=(8,4))
plt.axis('off')

ax[0].imshow(original_img)
ax[0].set_title('Original')
ax[0].set_axis_off()


# Display compressed image
ax[1].imshow(X_recovered)
ax[1].set_title('Compressed with %d colours'%K)
ax[1].set_axis_off()
plt.show()