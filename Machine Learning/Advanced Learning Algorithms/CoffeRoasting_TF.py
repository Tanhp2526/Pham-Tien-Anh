import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from lab_utils_common import dlc
from lab_coffee_utils import * 
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

#data set 
X,Y = load_coffee_data();
print(X.shape, Y.shape)
#plt_roast(X,Y)
#print(np.max(X[:,0]), np.min(X[:,0])) trả về max min của cột 0
#normalize Data
print(f"Temperature Max, Min pre normalization: {np.max(X[:,0]):0.2f}, {np.min(X[:,0]):0.2f}")
print(f"Duration Max, Min pre normalization: {np.max(X[:,1]):0.2f}, {np.min(X[:,1]):0.2f}")
norm_l = tf.keras.layers.Normalization(axis=-1) # tạo lớp chuẩn hóa  
norm_l.adapt(X) # học trung bình và độ lệch chuẩn từ dữ liệu X
Xn = norm_l(X) # chuẩn hóa dữ liêu X
print(f"Temperature Max, Min post normalization: {np.max(Xn[:,0]):0.2f}, {np.min(Xn[:,0]):0.2f}")
print(f"Duration Max, Min post normalization: {np.max(Xn[:,1]):0.2f}, {np.min(Xn[:,1]):0.2f}")

#Tile/copy
Xt = np.tile(Xn , (1000,1))# tạo 1000 bản sao của Xn
Yt = np.tile(Y , (1000,1))# tạo 1000 bản sao của Y
print(Xt.shape, Yt.shape)

tf.random.set_seed(1234) # sau mỗi lần chạy sẽ cho kết quả giống nhau
model = Sequential(
    [
        tf.keras.Input(shape=(2,)), #mỗi mẫu dữ liệu đầu vào có 2 features
        Dense(3, activation='sigmoid', name='layer1'),
        Dense(1, activation='sigmoid', name='layer2')
    ]
)

#model.fit : huấn luyện mô hình
model.summary()#mô tả về mạng đó

W1, b1 = model.get_layer("layer1").get_weights()
W2, b2 = model.get_layer("layer2").get_weights()
print(f"W1{W1.shape}:\n", W1, f"\nb1{b1.shape}:", b1)
print(f"W2{W2.shape}:\n", W2, f"\nb2{b2.shape}:", b2)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01),
)

model.fit(
    Xt,Yt,            
    epochs=10,
)

#after fitting
W1, b1 = model.get_layer("layer1").get_weights()
W2, b2 = model.get_layer("layer2").get_weights()
print("W1:\n", W1, "\nb1:", b1)
print("W2:\n", W2, "\nb2:", b2)

# Set weights from a previous run. 
W1 = np.array([
    [-8.94,  0.29, 12.89],
    [-0.17, -7.34, 10.79]] )
b1 = np.array([-9.87, -9.28,  1.01])
W2 = np.array([
    [-31.38],
    [-27.86],
    [-32.79]])
b2 = np.array([15.54])

# Replace the weights from your trained model with
# the values above.
model.get_layer("layer1").set_weights([W1,b1])
model.get_layer("layer2").set_weights([W2,b2])

# Check if the weights are successfully replaced
W1, b1 = model.get_layer("layer1").get_weights()
W2, b2 = model.get_layer("layer2").get_weights()
print("W1:\n", W1, "\nb1:", b1)
print("W2:\n", W2, "\nb2:", b2)

X_test = np.array([[200, 13.9],[200,17]])
X_testn = norm_l(X_test)
predictions = model.predict(X_testn)
print("predictions = \n", predictions)

y_hat = np.zeros_like(predictions)
for i in range(len(predictions)):
    if predictions[i] >= 0.5:
        y_hat[i] = 1
    else:
        y_hat[i] = 0
print(f"decisions = \n{y_hat}")

plt_layer(X,Y.reshape(-1,),W1,b1,norm_l)