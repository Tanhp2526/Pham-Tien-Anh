import numpy as np
import matplotlib.pyplot as plt
from utils import *

"""Mô tả bài toán:
Giả sử bạn kinh doanh khởi nghiệp nuôi trồng nấm và bán nấm hoang dã
VÌ không biết nấm nào đều ăn được, bạn mong muốn xác định được liệu nấm nào ăn được hoặc có độc dựa trên các thuộc tính vật lý của nó

Ta có sẵn tập dữ liệu: 
10 mẫu nấm, mỗi mẫu có 3 đặc trưng
   Cap Color(Brown or Red)
   Stalk Shape(Tapering (as is \/))of Enlarging(as is /\)
   Solitary(Yes or No)
   
   Nhãn : ăn được(1) or chứa độc(0)
   
Để triển khai cho dễ, chúng ta mã hóa one-hot đặc trưng chuyển tất cả đặc trưng sang giá trị 0 và 1
mầu nâu 1, đỏ:0
thu nhỏ dần:1, mở rộng dần:0
mọc đơn lẻ:1, không đơn lẻ:0"""

X_train = np.array([[1,1,1],
                    [1,0,1],
                    [1,0,0],
                    [1,0,0],
                    [1,1,1],
                    [0,1,1],
                    [0,0,0],
                    [1,0,1],
                    [0,1,0],
                    [1,0,0]])
y_train = np.array([1,1,0,0,1,0,0,1,1,0])

print("First few elements of X_train:\n", X_train[:5])
print("Type of X_train:", type(X_train))

print("First few elements of y_train:", y_train[:5])
print("Type of y_train:", type(y_train))

print ('The shape of X_train is:', X_train.shape)
print ('The shape of y_train is: ', y_train.shape)
print ('Number of training examples (m):', len(X_train))