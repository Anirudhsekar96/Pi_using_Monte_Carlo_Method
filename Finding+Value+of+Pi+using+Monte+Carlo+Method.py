
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[2]:

get_ipython().magic(u'matplotlib inline')


# In[3]:

import numpy as np


# In[4]:

inCircle = 0
inSquare = 0
graph = []
for i in range(1,10000000):
    x = np.random.rand()
    y = np.random.rand()
    inSquare = inSquare + 1
    if((x**2 + y**2)<=1):
        inCircle = inCircle + 1
    pi = 4 * inCircle/(inSquare*1.0)
    graph.append(pi)
    
pi = 4 * inCircle/(inSquare*1.0)


# In[5]:

print(pi)


# In[6]:

plt.plot(graph)
plt.show()


# In[7]:

plt.plot(graph)
plt.savefig("pi_converence.png")


# In[8]:

plt.plot(graph[100000:])
plt.savefig("pi_converence_smaller.png")


# In[ ]:




# In[ ]:



