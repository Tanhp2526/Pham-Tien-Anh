import numpy as np

def load_data():
    X = np.load("./Machine Learning/Advanced Learning Algorithms/X.npy")
    y = np.load("./Machine Learning/Advanced Learning Algorithms/y.npy")
    X = X[0:1000]
    y = y[0:1000]
    return X, y

def load_weights():
    w1 = np.load("./Machine Learning/Advanced Learning Algorithms/w1.npy")
    b1 = np.load("./Machine Learning/Advanced Learning Algorithms/b1.npy")
    w2 = np.load("./Machine Learning/Advanced Learning Algorithms/w2.npy")
    b2 = np.load("./Machine Learning/Advanced Learning Algorithms/b2.npy")
    return w1, b1, w2, b2

def sigmoid(x):
    return 1. / (1. + np.exp(-x))
