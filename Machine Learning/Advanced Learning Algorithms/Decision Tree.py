import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import * 

#Data set
"""Ta sẽ sử dụng one hot để mã hóa phân loại đặc trưng
Ear Shape: Pointy = 1, Floppy = 0
Face Shape: Round = 1, Not Round = 0
Whiskers: Present = 1, Absent = 0

Ta có 2 tập dữ liệu:
X_train: mẫu ví dụ, chứa 3 đặc trưng:
      - Ear Shape (1 if pointy, 0 otherwise)
      - Face Shape (1 if round, 0 otherwise)
      - Whiskers (1 if present, 0 otherwise)
      
y_train: cho biết con vật là mèo hay không
    - 1 if the animal is a cat
      - 0 otherwise"""

X_train = np.array([[1, 1, 1],
[0, 0, 1],
 [0, 1, 0],
 [1, 0, 1],
 [1, 1, 1],
 [1, 1, 0],
 [0, 0, 0],
 [1, 1, 0],
 [0, 1, 0],
 [0, 1, 0]])

y_train = np.array([1, 1, 0, 0, 1, 1, 0, 1, 0, 0])

def entropy(p):
    if p == 0 or p == 1:
        return 0
    else:
        return -p*np.log2(p) - (1-p)*np.log2(1-p)

print(entropy(0.5))


# để minh họa độ lợi thông tin, ta chia nút theo từng đặc trưng theo hàm sau
def split_indices(X, index_feature):
    """Cho một tập dữ liệu và chỉ số đặc trưng, trả về 2 danh sách tương ứng với 2 nút sau khi chia, 
       nút bên trái là động vật có feature = 1 và nút bên phải có feature = 0
       index feature = 0 => ear shape
       index feature = 1 => face shape
       index feature = 2 => whiskers"""
    
    left_indices = []
    right_indices =  []

    for i,x in enumerate(X):
        if x[index_feature] == 1:
            left_indices.append(i)
        else:
            right_indices.append(i)
    return left_indices, right_indices

print(split_indices(X_train, 0))

#sau khi được tách ta sẽ tính entropy trọng số của các nút
"""w_left và w_right: tỷ lệ số lượng mẫu động vật trong mỗi node
   p_left và p_right: tỷ lệ thuộc lớp mèo trong mỗi lần chia tách"""

def weighted_entropy(X,y,left_indices,right_indices):
    """Hàm này nhận vào tập dữ liệu đã được tách (splitted dataset) cùng với các chỉ số (indices) được chọn để thực hiện việc tách, và trả về giá trị entropy có trọng số (weighted entropy)."""
     
    w_left = len(left_indices)/len(X)
    w_right = len(right_indices)/len(X)
    p_left = sum(y[left_indices])/len(left_indices)
    p_right = sum(y[right_indices])/len(right_indices)

    weighted_entropyy = w_left*entropy(p_left) + w_right*entropy(p_right)
    return weighted_entropyy

left_indices, right_indices = split_indices(X_train, 0)
print(weighted_entropy(X_train, y_train, left_indices, right_indices))

def information_gain(X, y, left_indices, right_indices):
    """
    Here, X has the elements in the node and y is theirs respectives classes
    """
    p_node = sum(y)/len(y)
    h_node = entropy(p_node)
    w_entropy = weighted_entropy(X,y,left_indices,right_indices)
    return h_node - w_entropy

print(information_gain(X_train, y_train, left_indices, right_indices))

# tính độ lợi thông tin khi ta chia từ node gốc với từng đặc trưng

for i, feature_name in enumerate(['Ear Shape', 'Face Shape', 'Whiskers']):
    left_indices, right_indices = split_indices(X_train, i)
    i_gain = information_gain(X_train, y_train, left_indices, right_indices)
    print(f"Features: {feature_name}, information gain if we split the root node using this feature: {i_gain:.2f} ")

