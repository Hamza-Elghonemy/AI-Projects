#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as 


# In[ ]:


import statsmodels.api as sm
df = sm.datasets.get_rdataset('GaltonFamilies',package="Misdata").data
df


# In[35]:


#mean
def mean(x):
    summation=0
    for num in data:
        summation+=num
    mean=summation/len(data)
    print(mean)

data=[12,22,344,5,3,66,7,10]
mean(data)


# In[36]:


#median
def median(x):
    
    data2.sort()
    print(data2)
    print(len(data2))
    index=int((len(data2)+1)/2)
    if len(data2)%2==1:
        print(data2[index])
    else:
        print((data2[index-1]+data2[index])/2)
data2=[12,22,344,5,3,66,7,10]        
median(data)


# In[37]:




