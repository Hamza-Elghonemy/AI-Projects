#!/usr/bin/env python
# coding: utf-8

# In[114]:


import pandas as pd
import numpy as np
import seaborn as sbs
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
from sklearn import linear_model

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[52]:


df1= pd.read_csv("C:/Artificial Intelligence Course/archive11/Student_Performance.csv")
df1
df=pd.DataFrame(df1)
df


# In[6]:


# Question 1 --> 

df1.describe()


# In[8]:


# Question 2 -->

df1.info()


# In[21]:


# Question 3 -->


df1['Extracurricular Activities'].value_counts().hist()


# In[19]:


# Question 4 -->





df1['Performance Index'].value_counts().hist()


# In[25]:


df1['Hours Studied'].value_counts().plot()


# In[22]:


df1['Previous Scores'].value_counts().hist()


# In[23]:


df1['Sleep Hours'].value_counts().hist()


# In[24]:


df1['Sample Question Papers Practiced'].value_counts().hist()


# In[26]:


# Question 5 -->

plt.scatter(df1['Hours Studied'],df1['Performance Index'])
plt.title('Performance Index Related to Hours Studied ')
plt.xlabel('Hours')
plt.ylabel('Index')


# In[39]:


# Question 6 -->

Extra=df1['Extracurricular Activities']
performance=df1['Performance Index']

plt.bar(Extra,performance)
plt.title('Performance Index Related to Exta Curricular Activities ')
plt.xlabel('Activities')
plt.ylabel('Index')


# In[49]:


# Question 7 -->

performance=df1['Performance Index']
hours=df1['Hours Studied']


plt.bar(df1['Hours Studied'],df1['Performance Index'])


# In[56]:


# Question 8 -->
df2=df.drop(columns='Extracurricular Activities')
sbs.heatmap(df2)


# In[59]:


# Question 9 -->

sbs.violinplot(data=df, x='Sample Question Papers Practiced', y='Performance Index')
plt.show()


# In[60]:


# Question 10 -->

sbs.pairplot(df)


# In[61]:


# Question 11 -->

sbs.pairplot(df, hue="Extracurricular Activities")


# In[65]:


# Question 12 -->

sbs.scatterplot(df,x='Performance Index',y='Previous Scores')


# In[80]:


# Question 13 -->
df3=df.drop(columns='Performance Index')
sbs.catplot(df,x='Hours Studied',y='Performance Index',hue='Extracurricular Activities')
sbs.catplot(df,x='Sleep Hours',y='Performance Index',hue='Extracurricular Activities')
sbs.catplot(df,x='Sample Question Papers Practiced',y='Performance Index',hue='Extracurricular Activities')
sbs.catplot(df,x='Previous Scores',y='Performance Index',hue='Extracurricular Activities')


# In[84]:


# Question 14 -->

sbs.lineplot(df,x='Hours Studied',y='Performance Index',hue='Extracurricular Activities')


# In[89]:


# Question 15 -->

sbs.displot(df,x='Hours Studied',hue='Extracurricular Activities')
sbs.displot(df,x='Performance Index',hue='Extracurricular Activities')
sbs.displot(df,x='Sleep Hours',hue='Extracurricular Activities')
sbs.displot(df,x='Sample Question Papers Practiced',hue='Extracurricular Activities')
sbs.displot(df,x='Previous Scores',hue='Extracurricular Activities')


# In[ ]:


0   Hours Studied                     10000 non-null  int64  
 1   Previous Scores                   10000 non-null  int64  
 2   Extracurricular Activities        10000 non-null  object 
 3   Sleep Hours                       10000 non-null  int64  
 4   Sample Question Papers Practiced  10000 non-null  int64  
 5   Performance Index    


# In[91]:


# Question 16 -->
sbs.heatmap(df.corr(),annot=True)


# In[97]:


# Question 17 -->

corr= df.corr()[['Performance Index']]
sbs.heatmap(corr,annot=True)


# In[105]:


# Question 18 pt1
top=df.sort_values(by='Performance Index',ascending=False)
top
top10=top[0:1000]
top10


# In[109]:


# Question 18 pt2
sbs.catplot(top10,x='Hours Studied',y='Performance Index',hue='Extracurricular Activities',kind='box')
sbs.catplot(top10,x='Sleep Hours',y='Performance Index',hue='Extracurricular Activities',kind='box')
sbs.catplot(top10,x='Previous Scores',y='Performance Index',hue='Extracurricular Activities',kind='box')
sbs.catplot(top10,x='Sample Question Papers Practiced',y='Performance Index',hue='Extracurricular Activities',kind='box')


# In[110]:


# Question 19 -->

sbs.scatterplot(df,x='Previous Scores',y='Performance Index')


# In[120]:


# Question 20 -->
X=df['Performance Index']
y=df['Sleep Hours']
X = X.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.1)


# In[ ]:





# In[121]:


model = LinearRegression()
model.fit(X_train, y_train)

predicted = model.predict(X_test)

score = model.score(X_test, y_test)

print(score)


# In[122]:


plt.plot(X_train, y_train, 'o')
plt.plot(X_test, predicted, color = 'r')
plt.show()


# In[ ]:




