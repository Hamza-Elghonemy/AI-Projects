#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

array=np.zeros(10)
array[3]=1
print (array)


# In[11]:


#start,stop,step
matrix=np.arange(0.01,1.01,0.01).reshape(10,10) #reshape used in making into a matrix
print(matrix)


# In[19]:


matrix=np.ones((8,8))
matrix[::2, 1::2] = 0
matrix[1::2, ::2] = 0
print (matrix)
#x[::2, 1::2] = 1: This line uses array slicing to select every other row (starting from the first row) and every other column (starting from the second column) in the array 'x' and sets their elements to ones. The slice ::2 means "every second element" in both the rows and columns, while the slice 1::2 means "every second element, starting from the second element".

#x[1::2, ::2] = 1: This line uses array slicing to select every other row (starting from the second row) and every other column (starting from the first column) in the array 'x' and sets their elements to ones. The slice 1::2 means "every second element, starting from the second element" in both the rows and columns.

#or we can use

np.tile(np.array([[1,0],[0,1]]),(4,4)) #first row,second row repeated 4 times 


# In[22]:


get_ipython().system(' pip install requests')


# In[23]:


get_ipython().system(' pip install beautifulsoup4')


# In[10]:


import requests
from bs4 import BeautifulSoup
import csv
get_ipython().system(' pip install lxml')


# In[4]:


with open ("C:\\Artificial Intelligence Course/test.txt") as file: 
    y = file.readlines()
print(y)
print(len(y))

# y = [i.strip() for i in y ]   #is a list comprehension
# y
for i in y:
    print(i.strip())


# In[11]:


with open ('C:\\Artificial Intelligence Course/simple.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml') # parser, #parsing  --> to convert byte code into simple code


# In[12]:


soup


# In[14]:


website = requests.get("https://9animetv.to/home").text # website link ( URL ) 
print(type(website)) # returns string ( website code) 
website
# retirieve website html code ( i.e. syntax)


# In[15]:


soup = BeautifulSoup(website , 'lxml') # parsing ( understand txt string as html tags, id, class)


# In[16]:


print(soup.prettify())


# In[18]:


title=soup.title.text
print(title)


# In[30]:


import pandas as pd
df=pd.read_csv("C://Artificial Intelligence Course/archive/tested.csv")
print(df)


# In[36]:


print(type(df['Age']))
df['Age']=df['Age'].mean
print(df['Age'])


# In[35]:


#%matplotlib inline
#from matplotlib import pyplot as plt

#df['Age'].plot.hist(title='Ages', bins=19)
#plt.xlabel('')
#plt.ylabel('')
#plt.show()


# In[40]:


df.Embarked


# In[42]:


df['Fare'].max()


# In[65]:


df['Age']=df['Age'].astype('str')
print(df['Age'])


# In[46]:


df.index


# In[48]:


df.columns


# In[49]:


x=df.columns.to_list()
print(x)
print(type(x))


# In[50]:


for i in df.Fare:
    if(i>246):
        print(i)
        


# In[52]:


df[df.Survived==1]


# In[53]:


df['Embarked'][df.Survived==1]


# In[54]:


print(df.Age.dtype)


# In[59]:


print(f"you have: {len(df.columns)} columns")


# In[60]:


df.describe


# In[62]:


df.info()


# In[63]:


df.fillna('?')


# In[ ]:




