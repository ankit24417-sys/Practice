import numpy as np

#this  is for np.array() function.

a=np.array([[1,2,3],[4,5,6],[7,8,9]]) # this will create a 2D array with 3 rows and 3 columns
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)


#this is for np.arange() function.

b=np.arange(1,10) # this will create an array of numbers from 1 to 9 (10 is not included)
print(b)
b=np.arange(1,10,2) # this will create an array of numbers from 1 to 9 with a step of 2 (10 is not included)
print(b)


# this is for np.reshape() function.

c=np.arange(1,10).reshape(3,3) # this will create a 2D array with 4 rows and 3 columns from the array of numbers from 1 to 9
print(c)


# this is for np.ones() function.
 
d=np.ones((3,4)) # this will create a 2D array of shape (3,4) filled with ones
e=np.ones((2,3,4)) # this will create a 3D array of shape (2,3,4) filled with ones
print(d)
print(e)


# this is for np.zeros() function.

f=np.zeros((3,4)) # this will create a 2D array of shape (3,4) filled with zeros
print(f)


 # this is for np.random

g=np.random.rand(3,4) # this will create a 2D array of shape (3,4) filled with random numbers between 0 and 1
print(g)



# this is for np.linspace() function.
 
h=np.linspace(1,10,5,dtype=int) # this will create an array of 5 evenly spaced numbers between 1 and 10 (inclusive)
print(h)



# this is for np.identity() function.

i=np.identity(4) # this will create a 4x4 identity matrix
print(i)



# this is for array attributes.

# ndim: number of dimensions
# shape: dimensions of the array
# size: total number of elements in the array
# dtype: data type of the elements in the array
#itemsize: size of each element in bytes

#this is for ndim attribute.

print(a.ndim) # this will print the number of dimensions of the array a

# this is for shape attribute.
print(a.shape) # this will print the dimensions of the array a


# this is for size attribute.
print(a.size) # this will print the total number of elements in the array a


# this is for dtype attribute.
print(a.dtype) # this will print the data type of the elements in the array a

# this is for itemsize attribute.
print(a.itemsize) # this will print the size of each element in the array a in bytes




# this is for changing the data type of an array.
# astype() function is used to change the data type of an array
j=a.arange(1,10).reshape(3,3).astype(float) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9 and change the data type to float
j.astype(np.int32) # this will change the data type of the array j to int32





# this is for mathematical operations on arrays.
# scaler multiplicaton
k=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(k*2) # this will multiply each element of the array k by 2

# element-wise addition
l=np.arange(1,10).reshape(3,3) # this will create a
m=np.arange(10,19).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 10 to 18
print(l+m) # this will add the corresponding elements of the arrays l and m


# relational operators
n=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(n>5) # this will return a boolean array where each element is True if the 



# max/min/sum/prod functions

o=np.arange(1,10).reshape(3,3) # this will create a
print(np.max(o)) # this will return the maximum element in the array o
print(np.max(0),axis=0) # this will return the maximum element in each column of the array o


print(np.min(o)) # this will return the minimum element in the array o
print(np.min(o,axis=1)) # this will return the minimum element in each row of the array o
print(np.min(o,axis=0)) # this will return the minimum element in each column of the array o
 

print(np.sum(o)) # this will return the sum of all the elements in the array o
print(np.sum(o,axis=0)) # this will return the sum of each column of the array o
print(np.sum(o,axis=1)) # this will return the sum of each row of   


print(np.prod(o)) # this will return the product of all the elements in the array o
print(np.prod(o,axis=0)) # this will return the product of each column of the array o
print(np.prod(o,axis=1)) # this will return the product of each row of the array o




# mean/median/std/vars functions
print(np.mean(o)) # this will return the mean of all the elements in the array o
print(np.mean(o,axis=0)) # this will return the mean of each column of the array o
print(np.mean(o,axis=1)) # this will return the mean of each row of the array o

print(np.median(o)) # this will return the median of all the elements in the array o
print(np.median(o,axis=0)) # this will return the median of each column of the array o
print(np.median(o,axis=1)) # this will return the median of each row of the array o

print(np.std(o)) # this will return the standard deviation of all the elements in the array o
print(np.std(o,axis=0)) # this will return the standard deviation of each column of the array o
print(np.std(o,axis=1)) # this will return the standard deviation of each row of the array o

print(np.var(o)) # this will return the variance of all the elements in the array o
print(np.var(o,axis=0)) # this will return the variance of each column of the array o
print(np.var(o,axis=1)) # this will return the variance of each row of the array 



# dot product of two arrays
p=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
q=np.arange(10,19).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 10 to 18
print(np.dot(p,q)) # this will return the dot product of the arrays p and q 


# transpose of an array
r=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(r.T) # this will return the transpose of the array r


# inverse of an array
s=np.array([[1,2],[3,4]]) # this will create a 2D array with 2 rows and 2 columns
print(np.linalg.inv(s)) # this will return the inverse of the array s   


# log and exp functions
t=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(np.log(t)) # this will return the natural logarithm of each element in the array t
print(np.exp(t)) # this will return the exponential of each element in the array t      

 
# random/floor/ceil functions
u=np.random.rand(3,3) # this will create a 2D array with 3 rows and 3 columns filled with random numbers between 0 and 1
print(np.floor(u)) # this will return the floor of each element in the array u          
print(np.ceil(u)) # this will return the ceiling of each element in the array u






# indexing and slicing of arrays

v=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(v[0,0]) # this will return the element at the first row and first column of the array v
print(v[1,2]) # this will return the element at the second row and third

#column of the array v
print(v[0,:]) # this will return the first row of the array v       
print(v[:,0]) # this will return the first column of the array v
print(v[1:3,1:3]) # this will return the subarray of the array v from the second row to the third row and from the second column to the third column



# iterating over an array

w=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
for i in w:
    for j in i:
        print(j) # this will print each element of the array w


 # horizontal and vertical stacking of arrays
x=np.arange(1,5).reshape(2,2) # this will create a 2D array with 2 rows and 2 columns from the array of numbers from 1 to 4
y=np.arange(5,9).reshape(2,2) # this will create a 2D array with 2 rows and 2 columns from the array of numbers from 5 to 8
print(np.hstack((x,y))) # this will return the horizontal stacking of the arrays x and y
print(np.vstack((x,y))) # this will return the vertical stacking of the arrays x and y  


# horizontal and vertical splitting of arrays
z=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(np.hsplit(z,3)) # this will return the horizontal splitting of the array z        
print(np.vsplit(z,3)) # this will return the vertical splitting of the array z






# python list vs numpy array  in time


# python list 

import time
start=time.time()
a=[i for i in range(1000000)] # this will create a list of numbers from 0 to 999999
b=[i for i in range(1000000)] # this will create a list of numbers from 0 to 999999
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i]) # this will add the corresponding elements of the lists a and b and append the result to the list c
    print(time.time()-start) # this will print the time taken to add the corresponding elements of the lists a and b and append the result to the list c
  

# numpy array
start=time.time()
a=np.arange(1000000) # this will create a numpy array of numbers from 0 to 999999
b=np.arange(1000000) # this will create a numpy array of numbers from   
c=a+b # this will add the corresponding elements of the arrays a and b and store the result in the array c
print(time.time()-start) # this will print the time taken to add the corresponding elements of the arrays a and b and store the result in the array c   
 

#python list vs numpy array in memory

# python list

import sys
a=[i for i in range(1000000)] # this will create a list of numbers from 0 to 999999
print(sys.getsizeof(a)) # this will print the memory size of the list a in bytes

# numpy array

a=np.arange(1000000) # this will create a numpy array of numbers from 0 to 999999
print(sys.getsizeof(a)) # this will print the memory size of the numpy array a in bytes





# fancy indexing of arrays
a=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(a[[0,1],[0,1]]) # this will return the elements at the first row and first column, and the second row and second column of the array a    



# broadcasting of arrays
a=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
b=np.array([1,2,3]) # this will create a 1D array with 3 elements
print(a+b) # this will add the array b to each row of the array a using

x=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
y=np.arange(3)
print(x+y) # this will add the array y to each column of the array x using broadcasting
 
 # below code  generates an error because the shapes of the arrays are not compatible for broadcasting
z=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
w=np.arange(4) # this will create a 1D array with 4 elements                
print(z+w) # this will generate an error because the shapes of the arrays z and w are not compatible for broadcasting




# sigmoid function
# s(x)= 1/(1+exp(-x))
def sigmoid(x):
    return 1/(1+np.exp(-x)) # this will return the sigmoid of each element in the array x
a=np.arange(-10,11) # this will create a 1D array of numbers from -10 to 10
print(sigmoid(a)) # this will return the sigmoid of each element in the array a 



#mean squared error function
# MSE= (1/n)*sum((y_prediction-y_true)^2)
def mse(y_prediction,y_true):
    return np.mean((y_prediction-y_true)**2) # this will return the mean squared error between the arrays y_prediction and y_true   
y_true=np.array([1,2,3]) # this will create a 1D array with 3 elements
y_prediction=np.array([1.5,2.5,3.5]) # this will create a 1D array with 3 elements
print(mse(y_prediction,y_true)) # this will return the mean squared error between the arrays y_prediction and y_true



# binary cross entropy function
# BCE= -(1/n)*sum(y_true*log(y_prediction)+(1-y_true)*log(1-y_prediction))
def bce(y_prediction,y_true):       
    return -np.mean(y_true*np.log(y_prediction)+(1-y_true)*np.log(1-y_prediction)) # this will return the binary cross entropy between the arrays y_prediction and y_true
y_true=np.array([1,0,1]) # this will create a 1D array with 3 elements
y_prediction=np.array([0.9,0.1,0.8]) # this will create a 1D array with 3 elements  
print(bce(y_prediction,y_true)) # this will return the binary cross entropy between the arrays y_prediction and y_true
     