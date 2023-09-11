#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import csv
import seaborn as sb
Aincome=pd.read_csv("C:/Artificial Intelligence Course/Adultincome/adult.csv")
Adulti=pd.DataFrame(Aincome)
Adulti


# In[4]:


# Question 1--> Show first 10 rows

Aincome.head(10)


# In[9]:


# Question 2--> Check last 10 rows

Aincome.tail(10)


# In[7]:


# Question 3 --> Show no. of rows and coloumns

print ('Number of rows:',Aincome.shape[0])

print ('Number of columns:',Aincome.shape[1])


# In[13]:


# Question 4 --> Getting information about our dataset

Aincome.info()


# In[8]:


# Question 5 --> Fetching random samples from data set [50%]
df1=Aincome.sample(frac=0.5)
df1


# In[13]:


# Question 6 --> Find null values

Aincome.isnull().sum()
#sb.heatmap(Aincome.isnull())


# In[25]:


# Question 7 --> replace(?) with (NaN)..

Aincome['workclass']=Aincome['workclass'].replace("?",np.nan)
Aincome['native-country']=Aincome['native-country'].replace("?",np.nan)
Aincome['occupation']=Aincome['occupation'].replace("?",np.nan)
Aincome.isin(['?']).sum()
Aincome.isnull().sum()


# In[31]:


# Question 8 --> Drop missing values

df2=Aincome.dropna()
df2


# In[33]:


# Question 9 --> Check for duplicates and drop them

df3=Aincome.drop_duplicates()
df3.shape


# In[37]:


# Question 10 --> Show statistics of the dataframe

Aincome.describe()


# In[34]:


# Question 11 -->  Drop The Columns education-num, capital-gain, and capital-loss
Aincome
new_df=Aincome.drop(columns=['educational-num','capital-gain','capital-loss'])
new_df.columns


# In[35]:


#Question 12 --> Distribution of Age 

Aincome['age'].hist()


# In[69]:


# Question 13 -->  Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method


series=pd.Series(Aincome['age'])
series.between(17,48).sum()


# In[36]:


# Question 14 --> Find distribution of workclass

Aincome['workclass'].hist()


# In[41]:


# Question 15 --> How Many Persons Having Bachelors and Masters Degree?

Bachelors=Aincome['education']=='Bachelors'

Masters=Aincome['education']=='Masters'
len(Aincome[Masters | Bachelors ])


# In[22]:


# Question 16 -->Biavariate Analysis

plt.scatter(Aincome['race'],Aincome['hours-per-week'])
plt.title('Race vs Hours of work/week')
plt.xlabel('Race')
plt.ylabel('hours of work/week')


# In[33]:


# Question 17 --> Replace Salary Values With 0 and 1?

vals_to_replace={'>50K':'1','<=50K':'0'}
Adulti['income']=Adulti['income'].map(vals_to_replace)
Adulti


# In[59]:


# Question 18 --> Which Workclass Getting The Highest Salary?

Adulti['workclass'][Adulti['income']==Adulti['income'].max()].value_counts()


# In[60]:


# Question 19 Who Has Better Chance To Get Salary greater than 50K Male or Female?

Adulti['gender'][Adulti['income']==Adulti['income'].max()].value_counts()


# In[62]:


# Question 20 --> Covert workclass Columns Datatype To Category Datatype?

Adulti['workclass']=Adulti['workclass'].astype('category')
Adulti['workclass'].dtype


# In[ ]:




