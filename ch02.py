
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[4]:


get_ipython().run_line_magic('ls', '')


# In[5]:


get_ipython().run_line_magic('pwd', '')


# In[6]:


ls


# In[7]:


def func_with_keywords(abra=1, abbra=2, abbbra=3):
    return abra, abbra, abbbra


# In[9]:


func_with_keywords(abbbra)


# In[10]:


def add_numbers(a, b):
    return a + b


# In[11]:


get_ipython().run_line_magic('pinfo', 'add_numbers')


# In[12]:


get_ipython().run_line_magic('pinfo2', 'add_numbers')


# In[13]:


get_ipython().run_line_magic('psearch', 'np.*load*')


# In[14]:


ls


# In[15]:


cd ./Desktop/


# In[16]:


ls


# In[17]:


cd ./DataAnalysis_Mac


# In[18]:


ls


# In[19]:


pwd


# In[21]:


run ipython_script_test.py


# In[22]:


get_ipython().run_line_magic('run', 'ipython_script_test.py')


# In[23]:


get_ipython().run_line_magic('run', 'ipython_script_test.py')


# In[27]:


get_ipython().run_line_magic('run', 'ipython_script_test.py')


# In[28]:


result


# In[29]:


run ipython_script_test.py


# In[30]:


result


# In[ ]:


# %load ipython_script_test.py
def f(x, y, z) :
	return (x + y) / z
a = 5
b = 6
c = 7.5

result = f(a, b, c)


# In[32]:


paste


# In[33]:


get_ipython().run_line_magic('paste', '')


# In[34]:


get_ipython().run_line_magic('cpaste', '')


# In[35]:


x = 5 y = 7 if x > 5:

x += 1

y = 8


# In[36]:


x = 5 
y = 7 
if x > 5:

    x += 1

    y = 8


# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


import matplotlib as plt
plt.plot(np.random.randn(50).cumsum())


# In[39]:


import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())


# In[40]:


import numpy as np


# In[41]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[42]:


import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())


# In[43]:


type(None)


# In[44]:


from datetime import datetime, date, time


# In[45]:


dt = datetime(2011, 10, 29, 20, 30, 21)


# In[46]:


dt.day


# In[47]:


dt.minute


# In[48]:


dt.date()


# In[50]:


dt.time()


# In[51]:


dt.strftime('%m/%d/%Y/ %H:%M')


# In[52]:


datetime.strptime('20091031', '%Y%m%d')


# In[53]:


dt.replace(minute=0, second=0)


# In[54]:


dt2 = datetime(2011, 11, 15, 22, 30)


# In[55]:


delta = dt2 - dt


# In[56]:


delta


# In[57]:


type(delta)


# In[58]:


dt


# In[59]:


dt + delta


# In[60]:


sequence = [1, 2, 0, 4, 6, 5, 2, 1]


# In[61]:


total_until_5 = 0


# In[63]:


for value in sequence:
    if value == 5:
        break
    total_until_5 += value


# In[64]:


for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))


# In[65]:


x = 265
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2


# In[66]:


x


# In[67]:


range(10)


# In[68]:


list(range(10))


# In[69]:


list(range(0, 20, 2))


# In[70]:


list(range(5, 0, -1))


# In[71]:


sum = 0
for i in range(10000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i


# In[72]:


sum

