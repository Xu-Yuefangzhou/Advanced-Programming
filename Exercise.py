
# coding: utf-8

# In[1]:

2 + 2


# In[2]:

2.0 + 2.5


# In[3]:

2 + 2.5


# In[4]:

a = 0.2


# In[5]:

s = "Hello!" 
s


# In[6]:

s = '''Hello! '''
s


# In[9]:

s = '''hello
world'''
print (s)


# In[10]:

s = "hello" + "world"
s


# In[11]:

s[0]


# In[12]:

s[-1]


# In[13]:

s[0:5]


# In[14]:

s.split()


# In[15]:

s='hello world'
s.split()


# 也可以用符号来分割

# In[19]:

s='hello / world'
s.split('/')


# In[20]:

s='hello / world'
s.split(' / ')


# 列表List

# In[21]:

a = [1,2.0,'hello',5+10]
a


# In[22]:

a+a


# In[23]:

s={2,3,4,2}
s


# In[24]:

len(s)


# In[26]:

s.add(1)
s


# In[27]:

a = {1,2,3,4}
b = {2,3,4,5}
a & b


# In[28]:

a ^ b


# In[29]:

d = {'dogs':5, 'cats':4}
d


# In[30]:

len(d)


# In[32]:

d["dogs"]=2
d


# In[34]:

d.keys()


# In[35]:

d.items()


# In[36]:

d.values()


# In[37]:

from numpy import array
a=array([1,2,3,4])
a


# In[38]:

a+2


# In[39]:

get_ipython().magic('matplotlib inline')
from matplotlib.pyplot import plot
plot(a,a**2)


# In[40]:

line = '1 2 3 4 5'
fields = line.split()
fields


# In[41]:

total = 0
for field in fields:
    total += int(field)
total


# In[42]:

cd ~


# In[43]:

def poly(x, a, b, c):
    y = a * x ** 2 + b * x + c
    return y

x = 1
poly(x, 1, 2, 3)


# In[44]:

x = array([1, 2, 3])
poly(x, 1, 2, 3)


# In[45]:

from numpy import arange

def poly(x, a = 1, b = 2, c = 3):
    y = a*x**2 + b*x + c
    return y

x = arange(10)
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[46]:

poly(x)

