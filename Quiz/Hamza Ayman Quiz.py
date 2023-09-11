#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


#  1-Create an array of 10 fives

# In[1]:


arr=[]
for i in range(10):
    arr.append(5)
print (arr)


# 2-Create an array of all the even integers from 10 to 50

# In[5]:


arr=[]

for i in range(10,51,1):
    if i%2==0:
        arr.append(i)
print(arr)


# In[6]:


#help(range)


# 3-Create a 3x3 matrix with values ranging from 0 to 8

# In[37]:


matrix=np.random.randint(8,size=(3,3))
matrix


# In[22]:


#help(np.array)


# 4-Create the following matrix:
# 
# array([[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ],
#        [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 ],
#        [0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 ],
#        [0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 ],
#        [0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 ],
#        [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6 ],
#        [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7 ],
#        [0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8 ],
#        [0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9 ],
#        [0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.  ]])

# In[46]:


matrix=np.arange(0.01,1.01,0.01).reshape(10,10)
matrix


# In[1]:


#help(np)


# 5-So Provided that we have a set of data. How can we find the median? (implement median function)
# x = [6, 3, 8, 1, 7, 9, 3] , x = [6, 3, 2, 8, 9, 1, 5, 4]

# In[182]:


x = [6, 3, 8, 1, 7, 9, 3] 
sum=0
for i in x:
    sum+=i
sum

median=(sum/len(x))
print('The median is: ',median)


# 6-What is AI?

# In[ ]:


### Artificial Intelligence, is a huge art of upcoming technology. It is based on machine learning, data science and data analysis. ALl these features help in making computers make better decesions than human beings in things that require no emotions. 


# 7-Why AI is used ?

# In[ ]:


#To help humans make better rational descisions in important situations and to make monotonous day to day work easier for humans


# 8-When to use AI ?

# In[ ]:


#To predict a certain outcome or to identify certain diseases or to make crucial descisions 


# 9-What is  AI pipeline?

# In[ ]:


# AI pipeline is the sequence of steps the AI uses to do certain jobs


# 10-AI is ....% Data Operations , and ..... Model Creation 

# In[ ]:


#80 20


# 11-how to convert data that not normal distribution to normal distribution?

# In[ ]:


#we can take the mean of the values and analyze data according to it or by taking the log to the values and analyzing based on it


# 11-What is Feature Engineering? 

# In[ ]:


#feature engineering is when engineers maange the usage of data correctly in order for the machine to have better accuracy


# 12-How to avoid bad Sampling

# In[ ]:


# By taking the random samples depending on standard deviation and removing outliers


# 13-Why do we do Sampling?

# In[ ]:


# In order to have better understanding of the data in our hands as it is too bigand try and discover trends and relations between the data


# 14-What is a programming language?

# In[ ]:


# A programming language is a way for us to make computers understand our english and preform according to the instructions we give it
# There are two types of programming languages high level and low level
#highlevel--> C++ and python
#low level--> assembly


# 15-Create a random vector of size 30 and find the mean value

# In[52]:


vector=np.random.randint(30,size=(1,30))
print(vector)
m=vector.mean()
print('The mean of the vector is: ' ,m)


# 16-Create a 10x10 array with random values and find the minimum and maximum values

# In[54]:


matrix=np.random.randint(100,size=(10,10))
print(matrix)
mx=matrix.max()
mn=matrix.min()
print("The maximum value is: ",mx)
print("The minimum value is: ",mn)


# 17- Write a NumPy program to create a 2D array with 1 on the border and 0 inside

# In[62]:


matrix=np.ones([4,4],dtype='int16')
matrix[1][1:3]=0
matrix[2][1:3]=0
matrix


# 18-Create a 8x8 matrix and fill it with a checkerboard pattern

# In[7]:


matrix=np.tile(([1,0],[0,1]),(4,4))
matrix


# In[8]:


#help(matrix)


# 19-generates a 5x5 NumPy array filled with random integers from 1 to 99.

# In[11]:


matrix=np.random.randint(100,size=(5,5))
matrix


# 20-mean,std,mim and max

# In[12]:


s=matrix.std()
me=matrix.mean()
mi=matrix.min()
mx=matrix.max()
print('The mean is: ',me)
print('The standard deviation is: ',s)
print('The minimum is: ',mi)
print('The maximum is: ',mx)


# 21-what is Types of Data

# In[ ]:


# Nominal or discrete data


# 22-calc the Z score x=25 ,std=5 ,mean= 20

# In[13]:


# Zsscore= x-mean/std
x=int(input('Enter a number: '))
std=int(input('Enter the standard deviation: '))
mean=int(input('Enter the mean: '))
Zscore=(x-mean)/std
print('The Z score of your data is: ',Zscore)


# 23-Create a list of theses elements : 1,3,4,16,17,20, "Ahmed", "Mazen", True

# In[133]:


l2=[1,3,4,16,17,20,'Ahmed','Mazen','True']
type(l2)


# 24-add 7 to the list 

# In[134]:


l2.insert(3,7)
l2


# 25-remove 3 from the list 

# In[135]:


l2.remove(3)
l2


# 26-Count how many numbers 4 has occured

# In[138]:


count=0
for i in l2:
    if i==4:
        count+=1
count


# 27-print only the even numbers in the list

# In[141]:


for i in l2:
    if  str(i).isdigit():
        if i%2==0:
            print(i)


# 28-Sum only the numeric elements in the list

# In[143]:


sum=0
for i in l2:
    if  str(i).isdigit():
        sum+=int(i)
print(sum)


# 29-When must we use Assembly?

# In[ ]:


# When we are talking to the operating system of the computer


# 30-Why Companies can't move from OOP to Functional programming?

# In[ ]:


#Because OOP is much easier to work with and easier to understand than functional 
# In addition it simplifies the code and allows for easier function calls


# 31- Agile and waterfall
# 

# In[ ]:


#


# 32-What is Sample Size ?

# In[ ]:


#It is a a group of data used to represent a greater set of data top find relations


# 33-Why do we do Sampling?

# In[ ]:


# same as before


# 34-What are the types of medical image files?

# In[ ]:


#png and jpg


# 35-what is series?

# In[ ]:


#Series is form of data similar to a dataframe that can be used to preform data analysis 


# 36-Create pandas dataframe as input from users
# 
# name, age, id, gender, email, phone number, city,
# 
# then
# 
# a. group by city
# b. which city has the most students
# c. get the average of ages for each gender
# d. plot the relation between number of males to females
# e. plot the relation between age and gender

# In[116]:


import pandas as pd
l=[]
name=['Hamza','Jihan','Mohammed','Noureen']
age=['19','22','12','30']
Id=['1','2','3','4']
gender=['Male','Female','Male','Female']
email=['hamza@gmail.com','jihan@gmail.com','mo@gmail.com','nour@gmail.com']
phone_number=['0111022112','01100221121','01001221231','01222311331']
city=['Cairo','Giza','Cairo','Cairo']

#for i in range(3):
    #name=input('Enter a name:')
    #age=input('Enter age:')
    #Id=input('Enter ID:')
    #gender=input('Enter gender:')
    #email=input('Enter email:')
    #phone_number=input('Enter phone number:')
    #city=input('Enter city: ')
for i in range(4):    
    l.append([name[i],age[i],Id[i],gender[i],email[i],phone_number[i],city[i]])
df=pd.DataFrame(l,columns=['name','age','Id','gender','email','phone_number','city'])
#df
sumf=0
summ=0
gc=df.groupby('city')
gc.head()
df['city'].value_counts()
j=0
malec=0
femalec=0
for i in df['gender']:

    if i == 'Male':
        strage=df._get_value(j,'age')
        summ+=int(strage)
        malec+=1
    else :
        strage=df._get_value(j,'age')
        sumf+=int(strage)
        femalec+=1
    j+=1

plt.scatter(df['gender'],df['age'])
plt.title('Age to Gender')
plt.xlabel('Gender')
plt.ylabel('age')
plt.show()
avgmales=(summ/malec)
avgfemales=(sumf/femalec)
print('The average female ages is:',avgfemales)
print('The average male ages is: ',avgmales)
#df['city'].sum().max()
#df['gender']=='male'


# In[114]:


df['gender'].hist()


# In[ ]:





# In[105]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Exercises

#Follow the instructions to recreate the plots using this data:

## Data

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

import matplotlib.pyplot as plt


# ## Exercise 1
# 
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
# 

# In[175]:


fig=plt.figure()
ax=fig.add_axes( [0,0,1,1])
plt.plot(x,y)


# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**
# 

# In[176]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.2,.2])
plt.plot(x,y)


# In[19]:


#help(plt)


# In[ ]:




