#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
li=load_iris()
print(li)
dir(li)


# In[3]:


df= pd.DataFrame(li.data,columns=li.feature_names)
df['target']=li.target
df


# In[4]:


df.dropna


# In[5]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3)


# In[6]:


from sklearn.svm import SVC
rbf_model = SVC(kernel='rbf')


# In[7]:


rbf_model.fit(X_train,y_train)


# In[8]:


rbf_model.score(X_test,y_test)


# In[9]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)


# In[10]:


score = model.score(X_test,y_test)
print(score)


# In[11]:


from sklearn.neighbors import KNeighborsClassifier


# In[13]:


knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)


# In[14]:


knn.score(X_test,y_test)


# In[ ]:




