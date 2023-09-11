#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
li=load_iris()


# In[2]:


df = pd.DataFrame(li.data,columns=li.feature_names)
df = df.drop(['sepal length (cm)','sepal width (cm)'],axis='columns')
df


# In[3]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, li.target, test_size=0.3)


# In[4]:


km=KMeans(n_clusters=9).fit( X_train,y_train)


# In[5]:


km.score(X_test,y_test)


# In[6]:


km.predict([[5.0],[1.2]])


# In[7]:


df1 = pd.read_csv("C:\Artificial Intelligence Course\income.csv")
df1


# In[8]:


df1 = df1.drop(['Name'],axis='columns')
df1


# In[11]:


ss=[]
ran = range(1,10)
for i in ran:
    km = KMeans(n_clusters=i)
    km.fit(df1[['Age','Income($)']])
    ss.append(km.inertia_)
    


# In[12]:


plt.plot(ran,ss)


# In[14]:


km =KMeans(n_clusters=3)
predicted = km.fit_predict(df1[['Age','Income($)']])
predicted


# In[ ]:




