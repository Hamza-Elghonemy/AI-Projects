#!/usr/bin/env python
# coding: utf-8

# In[24]:


import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv("C:\Artificial Intelligence Course\canada_per_capita_income.csv")
X=df.year.to_numpy()
Y=df['per capita income (US$)']


# In[20]:


print(X)


# In[8]:


print(Y)


# In[25]:


#Y=Y.reshape(-1,1)
X = X.reshape(-1,1)
X_train, X_test, y_train, y_test= train_test_split(X, Y, test_size=0.1)
model = LinearRegression()
model.fit(X_train, y_train)
#################################
predicted = model.predict(X_test)
print(model.coef_)
print(model.intercept_)
print(model.coef_*202+model.intercept_)


# In[26]:


df1= pd.read_csv("C:\Artificial Intelligence Course\hiring.csv")
df1


# In[27]:


df1.experience = df1.experience.fillna('zero')
df1['test_score(out of 10)'] = df1['test_score(out of 10)'].fillna(0)
df1


# In[45]:


get_ipython().system('pip install word2number')



# In[46]:


from word2number import w2n
df1.experience = df1.experience.apply(w2n.word_to_num)
df1


# In[ ]:




