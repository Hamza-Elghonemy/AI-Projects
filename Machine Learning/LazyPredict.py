#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install lazypredict')
from sklearn.datasets import load_iris


# In[2]:


import pandas as pd
li = load_iris()
df=pd.DataFrame(li.data,columns=li.feature_names)
df['target']=li.target
df


# In[3]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3)


# In[4]:


from lazypredict.Supervised import LazyClassifier
clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)


# In[5]:


models


# In[ ]:




