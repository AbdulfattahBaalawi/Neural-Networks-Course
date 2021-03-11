# -*- coding: utf-8 -*-
"""
Simple Hebb Neural Network
"""

import numpy as np

# training inputs

x = np.array([[1, 1, 1],
              [1, -1, 1],
              [-1, 1, 1],
              [-1, -1, 1]])

y = np.array([[1],
              [-1],
              [-1],
              [-1]])


# sigmoid

def sigmoid(z):
    return (1 / (1 + np.exp(-z)))

batch = 4

a0 = x
w =  np.array([0,0,0])



for cnt in range(batch):
    batch_x = x
    batch_y = y
    n = batch_x.shape[0]
    # first layer activation value
    a0 = batch_x

    # feedforward operation for the first layer
    z1 = np.dot(a0, w.T)
    #print(batch_y[cnt])
    #print (a0[cnt])
    t=np.array([batch_y[cnt],batch_y[cnt],batch_y[cnt]]).T
    #print(t[0])
    xdelta = t[0]*a0[cnt]


    print("Delta=  {}".format(xdelta))
    w=np.add(w,xdelta)
    print ("weights=  {}".format(w))
    print()



# test function
def test_NN(z):
    k1 = np.dot(z, w)

    return k1


# given datas
x1 = np.array([1, -1, 1])
x2 = np.array([1, 1, 1])
print(w)

# output y1 for x1 data
test_NN(x1)
print(2*int(round(sigmoid(test_NN(x1))))-1)
# output y2 for x2 data
test_NN(x2)
print(2*(int(round(sigmoid(test_NN(x2)))))-1)
