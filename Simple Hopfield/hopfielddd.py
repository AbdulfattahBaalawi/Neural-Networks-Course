# Import Python Libraries
import numpy as np

# Take two sets of patterns:
# Set A: Input Pattern
x1 = np.array([1, 1, 1, -1]).reshape(4, 1)
x2 = np.array([-1, 1, 1, 1]).reshape(4, 1)

# Set B: Target Pattern
y1 = np.array(x1).reshape(1, 4)
y2 = np.array(x2).reshape(1, 4)

''' 
print("Set A: Input Pattern, Set B: Target Pattern") 
print("\nThe input for pattern 1 is") 
print(x1) 
print("\nThe target for pattern 1 is") 
print(y1) 
print("\nThe input for pattern 2 is") 
print(x2) 
print("\nThe target for pattern 2 is") 
print(y2) 
print("\nThe input for pattern 3 is") 
print(x3) 
print("\nThe target for pattern 3 is") 
print(y3) 
print("\nThe input for pattern 4 is") 
print(x4) 
print("\nThe target for pattern 4 is") 
print(y4) 

print("\n------------------------------") 
'''
# Calculate weight Matrix: W


inputSet = np.concatenate((x1, x2), axis = 1)
w1=np.dot(x1, y1)
w2=np.dot(x2, y2)


weight=w1+w2
print("\nWeight matrix:")
print(weight)

print("\n------------------------------")

# Testing Phase
# Test for Input Patterns: Set A
print("\nTesting for input patterns: Set A")
def testInputs(x, weight):
    wi=weight
    """
    
    for i in range (0,len(x)):
        for j in range(0,len(x)):
            if i==j:
                wi[i,j]=0
    print(wi)
    """
    step=0
    y = x
    for ii in range(0,len(x)) :
        yi = np.sum(wi[ii]*y)+x[ii]
        print(yi)
        if yi<0:
            yi=0
        if yi > 0:
            yi=1
        y[ii]=yi
    return np.array(y)
x3 = np.array([ 0, 0, 1, -1]).reshape(4, 1)
x3 = np.array([ 0, 0, 0, -1]).reshape(4, 1)
print("\nOutput of input pattern 1")
print(testInputs(x1, weight))
print("\nOutput of input pattern 2")
print(testInputs(x2, weight))


