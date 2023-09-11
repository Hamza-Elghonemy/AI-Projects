#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas import DataFrame
import csv


# In[4]:


url_data='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo=pd.read_table(url_data)
chipo


# In[5]:


chipo['item_name']


# In[8]:


chipo.head()


# In[14]:


chipo[0:10]


# In[21]:


chipo.info()


# In[23]:


chipo.index


# In[25]:


chipo['item_name'][chipo['quantity']==chipo['quantity'].max()]


# In[26]:


chipo['quantity'].max()


# In[6]:


#chipo['choice_description'][chipo['quantity']==chipo['quantity'].max()]
#if (chipo['choice_description'][chipo['quantity']==chipo['quantity'].max()] != 'NaN' ):
#print(chipo['choice_description'][chipo['quantity']==chipo['quantity'].max()])


# In[32]:


chipo['quantity'].sum()


# In[38]:


chipo['item_price'].dtype


# In[35]:


type(chipo['item_price'])


# In[1]:


#chipo['item_price'].sum()


# In[7]:


len(chipo['item_name'].value_counts())


# In[43]:


chipo['order_id'].max()


# In[ ]:




