import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import linear, relu, sigmoid
import matplotlib.pyplot as plt


import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

from public_tests import * 
from lab_utils_softmax import plt_softmax
np.set_printoptions(precision=2)

import numpy as np

def load_data():
    X = np.load("./Machine Learning/Advanced Learning Algorithms/X1.npy")
    y = np.load("./Machine Learning/Advanced Learning Algorithms/y1.npy")
    return X, y

def load_weights():
    w1 = np.load("./Machine Learning/Advanced Learning Algorithms/w1.npy")
    b1 = np.load("./Machine Learning/Advanced Learning Algorithms/b1.npy")
    w2 = np.load("./Machine Learning/Advanced Learning Algorithms/w2.npy")
    b2 = np.load("./Machine Learning/Advanced Learning Algorithms/b2.npy")
    return w1, b1, w2, b2

def sigmoid(x):
    return 1. / (1. + np.exp(-x))

#Dataset
X, y = load_data()
#print("The first element of X is: ", X[0])
print("The first element of y is: ", y[0,0])
print("The last element of y is: ", y[-1,0])
print(X.shape)
print(y.shape)

#trực quan hóa dữ liệu
"""Lấy ngẫu nhiên 64 bức ảnh từ X và ánh xạ về dạng (20,20) và hiển thị bức ảnh đó, nhã bức ảnh hiển thị phía trên"""

m,n = X.shape

fig, axes = plt.subplots(8,8, figsize=(8,8))
fig.tight_layout(pad = 0.13, rect=[0, 0.03, 1, 0.91]) #[left, bottom, right, top]

for i , ax in enumerate(axes.flat):
    random_index = np.random.randint(m)

    X_random_reshaped = X[random_index].reshape((20,20)).T

    ax.imshow(X_random_reshaped, cmap="gray")

    ax.set_title(y[random_index,0])
    ax.set_axis_off()
    fig.suptitle("Label, image", fontsize=14)

plt.show()

# Triển khai mô hình bằng TensoFlow
tf.random.set_seed(1234)
model = Sequential(
    [
        Dense(units = 25, activation='relu', name="L1"),
        Dense(units = 15, activation='relu', name="L2"),
        Dense(units = 10, activation='linear', name="L3"),
    ], name = "my_model"
)

model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate = 1e-3),
)

history = model.fit(X,y, epochs= 40)


#predict
image_of_two = X[1015]

prediction = model.predict(image_of_two.reshape(1,400))
print(f" predicting a Two: \n{prediction}")
print(f" Largest Prediction index: {np.argmax(prediction)}")
