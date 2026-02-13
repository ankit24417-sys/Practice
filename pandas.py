import numpy as np
import pandas as pd



   # series in padas
    

    # series for list
    
    # a) string list
country=['India','USA','UK','Germany','France']
s1=pd.Series(country)
print(s1)   
# output:
# 0     India       
# 1     USA
# 2     UK
# 3     Germany 
# 4     France
# dtype: object 

# b) numeric list
marks=[90,80,70,60,50]          
s2=pd.Series(marks)
print(s2)
# output:
# 0    90
# 1    80
# 2    70
# 3    60
# 4    50
# dtype: int64      
 
 # c) custom index list
name=['Ravi','Rahul','Ramesh','Suresh','Mahesh']
marks=[90,80,70,60,50]
s3=pd.Series(marks,index=name)  
print(s3)
# output:   
# Ravi      90
# Rahul     80
# Ramesh    70  
# Suresh    60
# Mahesh    50
# dtype: int64


# settting a name to series
cricketers=['Sachin','Dravid','Laxman','Ganguly','Kohli']
runs=[10000,13000,8000,12000,9000]
s4=pd.Series(runs,index=cricketers,name='Runs')     
print(s4)
# output:
# Sachin     10000
# Dravid     13000
# Laxman      8000
# Ganguly     12000
# Kohli       9000
# Name: Runs, dtype: int64



          # series for dictionary
marks={'Ravi':90,'Rahul':80,'Ramesh':70,'Suresh':60,'Mahesh':50}
s5=pd.Series(marks)     
print(s5)
# output:
# Ravi      90
# Rahul     80
# Ramesh    70
# Suresh    60
# Mahesh    50
# dtype: int64




  # atttribute of a series

  # a) size of a series
print(s3.size)   # output: 5    
 
 # b) dtype of a series
print(s3.dtype)  # output: int64    
 
 # c) name of a series
print(s4.name)   # output: Runs 
 
 # d) is_unique of a series
print(s3.is_unique)  # output: True

# e) index of a series
print(s3.index)  # output: Index(['Ravi', 'Rahul', 'Ramesh', 'Suresh', 'Mahesh'], dtype='object')   

# f) values of a series
print(s3.values)  # output: [90 80 70 60 50]





# series using read_csv() function

# a) data having one column
s6=pd.read_csv('country.csv',squeeze=True)
print(s6)       
# output:
#   country
# 0   India
# 1   USA

# b) data having two columns
s7=pd.read_csv('country_population.csv',index_col='country',squeeze=True)
print(s7)
# output:   
# country
# India     1300000000
# USA        330000000
# UK          67000000


# series methods

# a) head() method and tail() method

print(s7.head(2))  # output:
# country
# India    1300000000
# USA       330000000

print(s7.tail(2))  # output:
# country
# USA       330000000
# UK          67000000

# b) sample() method    
print(s7.sample(2))  # output:
# give a random output each time we run the code

# c) value_counts() method
s8=pd.Series(['India','USA','UK','India','USA'])    
print(s8.value_counts())  # output:
# India    2
# USA      2
# UK       1

# d) sort_values() method
print(s7.sort_values())  # output:
# country
# UK          67000000
# USA       330000000
# India     1300000000





# series math fuctions()

 # a) count() method
print(s7.count())  # output: 3

# b) sum() method
print(s7.sum())  # output: 1667000000

# c) mean() method
print(s7.mean())  # output: 555666666.6666666

# d) median() method
print(s7.median())  # output: 330000000.0

# e) min() method
print(s7.min())  # output: 67000000

# f) max() method
print(s7.max())  # output: 1300000000



  # series indexing #

  # interger indexing
print(s3[0])  # output: 90
print(s3[1])  # output: 80


