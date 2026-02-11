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
     




# important numpy functions
 

 # this is for np.sort() function.
a=np.arange(1000).reshape(10,100) # this will create a 2D array with 10 rows and 100 columns from the array of numbers from 0 to 999
print(np.sort(a,axis=0)) # this will return the sorted array a along the columns
print(np.sort(a,axis=1)) # this will return the sorted array a along the rows   

# for reverse sorting
print(np.sort(a,axis=0)[::-1]) # this will return the sorted array


# this is for np.append() function.
a=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
b=np.array([[10,11,12]]) # this will create a 2D array  with 1 row and 3 columns
print(np.append(a,b,axis=0)) # this will append the array b to the array a along the rows
print(np.append(a,b,axis=1)) # this will append the array b to the array a along the columns    


# this is for np.concatenate() function.
a=np.arange(1,10).reshape(3,3) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9                                
b=np.array([[10,11,12]]) # this will create a 2D array  with 1 row and 3 columns
print(np.concatenate((a,b),axis=0)) # this will concatenate the arrays a and b along the rows
print(np.concatenate((a,b.T),axis=1)) # this will concatenate the arrays a  and b along the columns     



 # this is for np.unique() function.
a=np.array([1,2,3,4,5,5,6,7,8,9]) # this will create a 1D array with 10 elements    
b=np.unique(a) # this will return the unique elements of the array a and store it in the array b    
print(b) # this will print the unique elements of the array a stored in the array b 



# this is for expand_dims() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements       
print(np.expand_dims(a,axis=0)) # this will return the array a with an added dimension at the first axis
print(np.expand_dims(a,axis=1)) # this will return the array a with an  added dimension at the second axis
        

# this is for np.where() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.where(a>3)) # this will return the indices of the elements in the array a that are greater than 3
print(np.where(a>3,1,0)) # this will return an array where the  elements in the array a that are greater than 3 are replaced with 1 and the elements that are less than or equal to 3 are replaced with 0   


# this is for np.argmax() function. 
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.argmax(a)) # this will return the index of the maximum element in the array a  


# this is for np.argmin() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.argmin(a)) # this will return the index of the minimum element in the array a  


# this is for np.cumsum() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.cumsum(a)) # this will return the cumulative sum of the elements in the array a
# output will be [1,3,6,10,15] because 1 is the first element, 1+2=3 is the second element, 1+2+3=6 is the third element, 1+2+3+4=10 is the fourth element and 1+2+3+4+5=15 is the fifth element of the output array.       


# this is for cumprod() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.cumprod(a)) # this will return the cumulative product of the elements in the array a
# output will be [1,2,6,24,120] because 1 is    the first element, 1*2=2 is the second element, 1*2*3=6 is the third element, 1*2*3*4=24 is the fourth element and 1*2*3*4*5=120 is the fifth element of the output array.  


# this is for np.percentile() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.percentile(a,50)) # this will return the 50th percentile (median) of the elements in the array a
print(np.percentile(a,25)) # this will return the 25th percentile of the elements in the array a
print(np.percentile(a,75)) # this will return the 75th percentile of the    elements in the array a     
# output will be 3.0 for the 50th percentile, 2.0 for the 25th percentile and 4.0 for the 75th percentile because 3 is the middle element of the sorted array [1,2,3,4,5], 2 is the middle element of the lower half of the sorted array [1,2] and 4 is the middle element of the upper half of the sorted array [4,5].         


# this is for np.histogram() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.histogram(a,bins=5)) # this will return the histogram of the elements in the array a with 5 bins
# output will be (array([1,1,1,1,1]), array([   1., 2., 3., 4., 5., 6.])) because there is one element in the array a that falls into each of the 5 bins defined by the edges [1., 2., 3., 4., 5., 6.]. The first bin includes the elements that are greater than or equal to 1 and less than 2, the second bin includes the elements that are greater than or equal to 2 and less than 3, the third bin includes the elements that are greater than or equal to 3 and less than 4, the fourth bin includes the elements that are greater than or equal to 4 and less than 5, and the fifth bin includes the elements that are greater than or equal to 5 and less than 6.      


# this is for np.corrcoef() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([2,3,4,5,6]) # this will create a 1D array with 5 elements
print(np.corrcoef(a,b)) # this will return the correlation coefficient matrix of the arrays a and b
# output will be [[1. 1.] [1. 1.]] because the correlation coefficient between the arrays a and b is 1, which indicates a perfect positive linear relationship between the two arrays. The diagonal elements of the matrix are 1 because they represent the correlation of each array with itself, which is always 1. The off-diagonal elements are also 1 because they represent the correlation between the two different arrays, which is also 1 in this case.       


# this is for np.isin() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([3,4,5,6,7]) # this will create a 1D array with 5 elements
print(np.isin(a,b)) # this will return a boolean array where each element is True if the corresponding element in the array a is present in the array b and False otherwise
# output will be [False False  True  True  True] because the elements 3, 4, and 5 in the array a are present in the array b, while the elements 1 and 2 in the array a are not present in the array b.          


# this is for np.flip() function.
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) # this will create a 2D array with 3 rows and 3 columns from the array of numbers from 1 to 9
print(np.flip(a,axis=0)) # this will return the array a flipped along the first axis (rows)         
print(np.flip(a,axis=1)) # this will return the array a flipped along the second axis (columns)
# output will be [[7 8 9] [4 5 6] [1 2 3]] for the first print statement because the rows of the array a are reversed, and [[3 2 1] [6 5 4] [9 8 7]] for the second print statement because the columns of the array a are reversed.        


# this is for np.put() function.
a=np.array([1,2,3,4,5]) # this will create a    1D array with 5 elements
np.put(a,[0,2],[10,30]) # this will replace the elements at the indices 0 and 2 of the array a with the values 10 and 30 respectively
print(a) # this will print the modified array a, which will be [10, 2, 30, 4, 5] because the element at index 0 has been replaced with 10 and the element at index 2 has been replaced with 30. 


# this is for np.delete() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.delete(a,0)) # this will return a new array with the element at index 0 of the array a deleted
print(np.delete(a,2)) # this will return a new array with the element at index 2 of the array a deleted
# output will be [2 3 4 5] for the first print statement because the element at index 0 (which is 1) has been deleted, and [1 2 4 5] for the second print statement because the element at index 2 (which is 3) has been deleted.   







# set functions for arrays

# this is for np.union1d() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([4,5,6,7,8]) # this will create a 1D array with 5 elements
print(np.union1d(a,b)) # this will return the sorted unique elements that are in either of the arrays a or b
# output will be [1 2 3 4 5 6 7 8] because the unique elements that are in either of the arrays a or b are 1, 2, 3, 4, 5, 6, 7, and 8.  

# this is for np.intersect1d() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([4,5,6,7,8]) # this will create a 1D array with 5 elements
print(np.intersect1d(a,b)) # this will return the sorted unique elements that are in both of the arrays a and b
# output will be [4 5] because the unique elements that are in both of the arrays a and b are 4 and 5.  
 
 # this is for np.setdiff1d() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([4,5,6,7,8]) # this will create a 1D array with 5 elements
print(np.setdiff1d(a,b)) # this will return the sorted unique elements that are in the array a but not in the array b
# output will be [1 2 3] because the unique elements that are in the array a but not in the array b are 1, 2, and 3.    
 
 # this is for np.setxor1d() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([4,5,6,7,8]) # this will create a    1D array with 5 elements
print(np.setxor1d(a,b)) # this will return the sorted unique elements that are in either of the arrays a or b but not in both
# output will be [1 2 3 6 7 8] because the unique elements that are in either of the arrays a or b but not in both are 1, 2, 3, 6, 7, and 8.    

# this is for np.in1d() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
b=np.array([4,5,6,7,8]) # this will create a 1D array with 5 elements
print(np.in1d(a,b)) # this will return a boolean array where each element is True if the corresponding element in the array a is present in the array b and False otherwise
# output will be [False False False  True  True] because the elements 4 and 5 in the array a are present in the array b, while the elements 1, 2, and 3 in the array a are not present in the array b.





# this is for np.clip() function.
a=np.array([1,2,3,4,5]) # this will create a 1D array with 5 elements
print(np.clip(a,2,4)) # this will return an array where the elements in the array a that are less than 2 are replaced with 2, the elements that are greater than 4 are replaced with 4, and the elements that are between 2 and 4 (inclusive) are unchanged
# output will be [2 2 3 4 4] because the elements 1 and 2 in the array a are less than 2, so they are replaced with 2, the element 3 is between 2 and 4, so it is unchanged, and the elements 4 and 5 in the array a are greater than 4, so they are replaced with 4.   
