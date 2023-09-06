#!/usr/bin/env python
# coding: utf-8

# In[6]:


#TASK 2
import re
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
hamzaelghonemy77_0@email.ca
'''

pattern= re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.\w+')
matches=pattern.finditer(emails)

for match in matches:
  print(match)


# In[ ]:





# In[ ]:




