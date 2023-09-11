#!/usr/bin/env python
# coding: utf-8

# In[5]:


i=1
while i<11:
    if i<10:
        print(i,end='+')
    else:
        print(i)
    i+=1

    
    


# In[7]:


i=0
while i<=10:
    i+=1
    if i%2==0:
        continue
    print(i)
    print("ODD")


# In[29]:





# In[30]:


x=int(input('Enter number:'))
while x>0:
    rem=x%10              #x=153,15,1
    print(rem,end='')     #rem=3,5,1
    x=x//10
    


# In[36]:


x=int(input('Enter number:'))
sum=0
while x>0:
    rem=x%10 
    sum+=rem    
    x=x//10
print(sum)


# In[58]:


x=int(input('Enter number:'))
check=x
power=len(str(x))
num=0
while x>0:
    rem=x%10
    num+=rem**power
    x=x//10

if num==check:
    print('yes')
else:
    print('no')
    


# In[ ]:





# In[ ]:




