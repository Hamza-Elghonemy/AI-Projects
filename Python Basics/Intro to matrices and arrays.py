#!/usr/bin/env python
# coding: utf-8

# In[3]:


S={4,3,-6}
print(S)
S.add(-10)
print(S)
S.pop()
print(S)


# In[23]:


x=int(input('Enter a number: '))
year=(x//365)
print(year)
month=(x%365)//30
print(month)
days=(x%365)%30
print(days)
print('year:',year,'month(s):',month,'day(s):',days)


# In[66]:


rows,colmns=(4,4)
matrix=[[0]*colmns]*rows

last=3
print(matrix)
for i in range(4):  
    matrix[i][0]=1
    matrix[i][last]=1
    for j in range(4):
        matrix[0][j]=1
        matrix[last][j]=1
    
print(matrix)


# In[86]:


import numpy as np
rows=int(input('Enter rows:'))
coloumns=int(input('Enter coloumns:'))
matrix=np.ones((rows,coloumns))
#matrix=np.zeros((rows,coloumns))
#for i in range(rows):  
    #matrix[i][0]=1
    #matrix[i][coloumns-1]=1
    #for j in range(coloumns):
        #matrix[0][j]=1
       #matrix[rows-1][j]=1
matrix[1:rows-1,1:coloumns-1]=0
print(matrix)


# In[ ]:





# In[ ]:





# In[ ]:




