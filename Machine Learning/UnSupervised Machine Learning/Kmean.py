import numpy as np
import matplotlib.pyplot as plt
from utils import *


"""Thuật toán Kmean
def kMeans_init_centroids(X,K):
    m = X.shape[0]
    indices = np.radom.choices(m, K, replace = False)
    centroids = X[indices]
    return centroids
    
centroids = kMeans_init_centroids(X,K)"""

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

X = load_data()
print("First five elements of X are:\n", X[:5])
print("The shape of X is:", X.shape)

initial_centroids = np.array([[3,3], [6,2], [8 ,5]])
idx = find_closest_centroids(X, initial_centroids)

print(idx[:7])

#Compute centroid means(tính giá trị trung bình của các tâm cụm)
# tức là tính giá trị trunh bình của các điểm dữ liệu đã được gán vào tâm cụm đó.

def compute_centroids(X, idx, K):
    m,n = X.shape
    centroids = np.zeros((K,n))

    for k in range(K):
        points = X[idx == k] # danh sách điểm dữ liệu trong X được gán vào tâm cụm k
        centroids[k] = np.mean(points, axis=0)
    return centroids

K = 3
centroids = compute_centroids(X,idx,K)
print("The centroids are:", centroids)

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

# sinh ngẫu nhiên centroids
def kMeans_init_centroids(X, K):
    """
    This function initializes K centroids that are to be 
    used in K-Means on the dataset X
    
    Args:
        X (ndarray): Data points 
        K (int):     number of centroids/clusters
    
    Returns:
        centroids (ndarray): Initialized centroids
    """
    
    # Randomly reorder the indices of examples
    randidx = np.random.permutation(X.shape[0])
    
    # Take the first K examples as centroids
    centroids = X[randidx[:K]]
    
    return centroids
