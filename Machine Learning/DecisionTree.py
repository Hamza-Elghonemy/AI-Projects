#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("C:\Artificial Intelligence Course\music.csv")
df


# In[3]:


from sklearn import tree
from sklearn.model_selection import train_test_split
clf = tree.DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(df.drop('genre',axis='columns'), df.genre, test_size=0.3)
clf = clf.fit(X_train, y_train)
clf.score(X_test,y_test)


# In[ ]:




