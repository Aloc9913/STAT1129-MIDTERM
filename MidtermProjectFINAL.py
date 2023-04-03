#!/usr/bin/env python
# coding: utf-8

# In[14]:


numbers = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3,6,8,4,5,2,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,2,4,6,8,4,5,2,1,9,0,4,6,7,42,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6]


# In[15]:


numbers.sort()


# In[16]:


print(numbers)


# In[19]:


frequencyDict = dict()
visited = set()
listLength = len(numbers)
for i in range(listLength):
    if numbers[i] in visited:
        continue
    else:
        count = 0 
        element = numbers[i]
        visited.add(numbers[i])
        for j in range(listLength - i):
            if numbers[j+i] == element:
                count += 1
        frequencyDict[element] = count
        
print("Frequency of elements is:")
print(frequencyDict)


# In[21]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42])
y = np.array([9, 14, 18, 20, 21, 10, 26, 17, 13, 24, 14, 1])

plt.bar(x,y)
plt.show()


# In[44]:


import json 
numbers = {0: 9, 1: 14, 2: 18, 3: 20, 4: 21, 5: 10, 6: 26, 7: 17, 8: 13, 9: 24, 10: 14, 42: 1}
with open("midterm_json_file", "w") as fp:
    json.dump(numbers, fp)


# In[27]:


json.load(fp)


# In[ ]:


#beggining of Question 2


# In[55]:


import pandas as pd


# In[57]:


df1 = pd.read_csv('/Users/asherlock/Downloads/midtermproject/USETHIS.csv')


# In[58]:


df1.head()


# In[59]:


df1.mean()


# In[61]:


df1.median()


# In[62]:


df1.mode()


# In[63]:


df1.max()


# In[64]:


df1.min()


# In[65]:


df1.std()


# In[75]:


import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/asherlock/Downloads/midtermproject/USETHIS.csv')

df1.plot(kind = 'bar', x = '04/01/19', y = '35.00')

plt.xlabel("Date")
plt.ylabel("Subtotal Price")
plt.show()

#SHOWS PRICE AND DATE OF PURCHASES 


# In[72]:


df1 = pd.read_csv('/Users/asherlock/Downloads/midtermproject/USETHIS.csv')

y = np.array([17, 30, 10, 43])
mylabels = ["April", "May", "June", "July"]
plt.pie(y, labels = mylabels)
plt.show()

#SHOWS THE PERCENTAGE OF PURCHASES COMPLETED IN EACH MONTH 


# In[84]:


y1 = np.array(["4-1-19", "4-1-19", "4-1-19", "4-4-19" ,"4-5-19", "4-5-19", "4-7-19", "4-8-19", "4-20-19", "4-23-19", "5-5-19", "5-6-19", "5-10-19", "5-14-19", "5-18-19", "5-19-19", "5-21-19", "5/21/19", "5/21/19", "5/22/19", "5/22/19", "5/22/19", "5/24/19", "5/25/19", "5/28/19", "5/29/19", "5/30/19", "5/30/19", "6/3/19", "6/3/19", "6/5/19", "6/18/19", "6/25/19", "6/25/19", "7/3/19", "7/3/19", "7/3/19", "7/3/19", "7/3/19", "7/6/19", "7/6/19", "7/6/19", "7/6/19", "7/6/19", "7/7/19", "7/9/19", "7/17/19", "7/18/19", "7/18/19", "7/18/19", "7/18/19", "7/21/19", "7/21/19", "7/23/19", "7/30/19", "7/30/19", "7/30/19", "7/31/19", "7/31/19"])
y2 = np.array(["4-1-19", "4-1-19", "4-1-19", "4-5-19", "4-7-19", "4-8-19", "4-8-19", "4-8-19", "4-21-19", "4-24-19", "5-7-19", "5-7-19", "5-12-19", "5-15-19", "5-19-19", "5-20-19", "5-22-19", "5/22/19", "5/22/19", "5/22/19", "5/23/19", "5/23/19", "5/25/19", "5/27/19", "5/28/19", "5/30/19", "6/1/19", "5/30/19", "6/5/19", "6/5/19", "6/5/19", "6/19/19", "6/26/19", "6/26/19", "7/4/19", "7/5/19", "7/8/19", "7/5/19", "7/4/19", "7/7/19", "7/8/19", "7/7/19", "7/8/19", "7/7/19", "7/8/19", "7/9/19", "7/18/19", "7/19/19", "7/18/19", "7/18/19", "7/18/19", "7/21/19", "7/22/19", "7/23/19", "7/31/19", "8/1/19", "8/1/19", "7/31/19", "8/1/19"])

plt.plot(y1)
plt.plot(y2)

plt.xlabel("Number of orders")
plt.ylabel("Date")
#Date of order placed 
#Date of order shipped 


# In[ ]:




