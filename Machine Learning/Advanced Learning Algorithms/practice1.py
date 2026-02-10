import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from autils import *

import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

#load data set
X,y = load_data()
#print("The first element of X is: ", X[0])
#print("The first element of y is: ", y[0,0])
#print("The last element of y is: ", y[-1,0])

#check dimensions
print("The shape of X is: "+ str(X.shape))
print("The shape of y is: " + str(y.shape))

#visualizing the data
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#m, n = X.shape # m là số mẫu huấn luyện, n là số đặc trưng

#fig, axes = plt.subplots(8,8, figsize=(8,8)) # tạo lưới 8x8 để hiển thị 64 hình ảnh 
#fig.tight_layout(pad=0.5) # giữ khoảng cách giữa các hình con trong lưới


#for i, ax in enumerate(axes.flat): # axes.flat trải phẳng mảng 2D thành 1D để dễ dàng lặp
    # chọn ngẫu nhiên chỉ số 
    #ax.imshow(X_random_reshaper, cmap="gray")

    # hiển thị label tương ứng dưới ảnh
    #ax.set_axis_off() # tắt trục để chỉ hiển thị ảnh
#plt.show()

model = Sequential(
    [
        tf.keras.Input(shape=(400,)), # chỉ định đầu vào
        Dense(units=25, activation='sigmoid', name="dense"),
        Dense(units = 15, activation = 'sigmoid', name="dense_1"),
        Dense(units = 1, activation ='sigmoid', name="dense_2")
    ], name="my_model"
)

model.summary()

L1_num_params = 400 * 25 + 25  # W1 parameters  + b1 parameters
L2_num_params = 25 * 15 + 15   # W2 parameters  + b2 parameters
L3_num_params = 15 * 1 + 1     # W3 parameters  + b3 parameters
print("L1 params = ", L1_num_params, ", L2 params = ", L2_num_params, ",  L3 params = ", L3_num_params )

[layer1, layer2, layer3] = model.layers
W1, b1 = layer1.get_weights()
print(W1.shape)
print(b1.shape)

#model.compile(tính hàm loss)
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
)

#model.fit(chạy gradient descent và huấn luyện trọng sôs)
#model.fit(
    #X,y,
    #epochs=20
#)

prediction = model.predict(X[0].reshape(1,400))
print(f"predicting a zero: {prediction}")


#dự đoán của các mô hình với nhãn thực từ 64 số ngẫu nhiên
m,n = X.shape

fig, axes = plt.subplots(8,8, figsize=(8,8))
fig.tight_layout(pad=0.1,rect=[0, 0.03, 1, 0.92]) #[left, bottom, right, top]

for i, ax in enumerate(axes.flat):
    random_index = np.random.randint(m)

    X_random_reshaped = X[random_index].reshape((20,20)).T

    ax.imshow(X_random_reshaped, cmap="gray")

    prediction = model.predict(X[random_index].reshape(1,400))
    if prediction >= 0.5:
        yhat = 1
    else:
        yhat = 0
    
    ax.set_title(f"{y[random_index,0]}, {yhat}")
    ax.set_axis_off()

fig.suptitle("Label, yhat", fontsize = 16)
plt.show()

#numpy model implement
def my_dense(a_in, W,b, g):
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:,j]
        z = np.dot(w,a_in) + b[j]
        a_out[j] = g
        return a_out
    
def my_sequential(x, W1, b1, W2, b2, W3, b3):
    a1 = my_dense(x,  W1, b1, sigmoid)
    a2 = my_dense(a1, W2, b2, sigmoid)
    a3 = my_dense(a2, W3, b3, sigmoid)
    return(a3)

W1_tmp,b1_tmp = layer1.get_weights()
W2_tmp,b2_tmp = layer2.get_weights()
W3_tmp,b3_tmp = layer3.get_weights()
  
prediction = my_sequential(X[0], W1_tmp, b1_tmp, W2_tmp, b2_tmp, W3_tmp, b3_tmp )
if prediction >= 0.5:
    yhat = 1
else:
    yhat = 0
print( "yhat = ", yhat, " label= ", y[0,0])
prediction = my_sequential(X[500], W1_tmp, b1_tmp, W2_tmp, b2_tmp, W3_tmp, b3_tmp )
if prediction >= 0.5:
    yhat = 1
else:
    yhat = 0
print( "yhat = ", yhat, " label= ", y[500,0])


