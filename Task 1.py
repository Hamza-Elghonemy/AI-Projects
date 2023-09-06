#!/usr/bin/env python
# coding: utf-8

# In[6]:


string_number='10'
convert=int(x)
print(y)


# In[5]:


string_word='TEN'
convert=int(string_word)
print(convert)


# In[8]:


integer=10
convert=str(integer)
print(convert)


# In[16]:


boolean=True
convert=str(boolean)
print(convert)


# In[18]:


string='true'
convert=bool(string)
print(convert)


# In[20]:


string=''
convert=bool(string)
print(convert)


# In[21]:


string='Hamza'
convert=bool(string)
print(convert)


# In[22]:


string='Hamza'
convert=float(string)
print(convert)


# In[23]:


number=70/13
convert=float(number)
print(convert)


# In[24]:


integer=70/13
convert=float(integer)
convert_to_int=int(convert)
print(convert_to_int)


# In[25]:


integer=20
convert=float(integer)
print(convert)


# In[27]:


list1=[1,2,3,'Hamza']
convert=tuple(list1)
print(convert)


# In[29]:


tuple1=(1,2,3,'Hamza')
convert=list(tuple1)
print(convert)


# In[31]:


dict1={'one':1,'two':2,'three':3}
convert=list(dict1)
print(convert)


# In[32]:


dict1={'one':1,'two':2,'three':3}
convert=tuple(dict1)
print(convert)


# In[33]:


list1=[1,2,3,'Hamza']
convert=dict(list1)
print(convert)


# In[34]:


tuple1=(1,2,3,'Hamza')
convert=dict(tuple1)
print(convert)


# In[35]:


arr=[1,2,3,4]
convert=list(arr)
print(convert)


# In[36]:


arr=[1,2,3,4]
convert=tuple(arr)
print(convert)


# In[37]:


arr=[1,2,3,4]
convert=dict(arr)
print(convert)


# In[38]:


print(8<<1)


# In[41]:


print(8>>2)
#8->1000
#shiftright(2)-->0010=2


# In[40]:


print(10<<2)
#10->00001010
#shiftleft(2)-->00101000=40


# In[42]:


print(10>>2)
#10->00001010
#shiftleft(2)-->00000010=2


# In[54]:


list=[1,2,3,4,5,6]
print('The odd numbers are:',list[0:6:2]) #list[start:stop:step]


# In[55]:


list=[1,2,3,4,5,6]
print('The even numbers are:',list[1:6:2])


# In[60]:


x=int(input('Enter a year:'))
if x%4==0:
    print('Youve entered a leap year!')
else: 
    print('The year you entered is not a leap year')


# In[61]:


x=int(input('Enter a year:'))
if x%4==0:
    print('Youve entered a leap year!')
else: 
    print('The year you entered is not a leap year')


# In[63]:


x=int(input('Enter age of first person:'))
y=int(input('Enter age of second person:'))
z=int(input('Enter age of third person:'))
if x>z and x>y:
    max=x
elif z>y and z>x:
    max=z
else: 
    max=y

if x<z and x<y:
    min=x
elif z<y and z<x:
    min=z
else: 
    min=y
    
print('The maximum age is: ',max)
print('The minimum age is: ',min)


# In[ ]:




