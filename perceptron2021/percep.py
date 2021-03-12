# -*- coding: utf-8 -*-
"""
Simple Perceptron Neural Network
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






batch = 8

a0 = x
w =  np.array([0,0,0])



for cnt in range(batch):
    batch_x = x
    batch_y = y
    n = batch_x.shape[0]
    # first layer activation value
    a0 = batch_x
    count=cnt%4

    # feedforward operation for the first layer
    z1 = np.dot(a0, w.T)

    t=np.array([batch_y[count],batch_y[count],batch_y[count]]).T
    net1=np.sum(batch_x[count]*w.T)
    net2=net1
    # when theta=0.2
    if net2>=0.2:
        net2=1
    if ((net2<0.2) and (net2>-0.2)):
        net2=0
    if net2<=-0.2:
        net2=-1
    print(net1)
    print(net2)
    print(batch_y[count])

    if net2==batch_y[count][0]:
        xdelta=[0,0,0]
    else:
        xdelta = t[0]*a0[count]

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
