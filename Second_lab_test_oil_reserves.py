#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


data=pd.read_csv('oil_reserves.csv')


# In[6]:


data1=data.applymap(lambda x:x.strip() if isinstance(x,str) else x)


# In[7]:


data1.head(5)


# In[8]:


data1.isnull().sum()


# In[9]:


data1.shape


# In[ ]:





# In[31]:


#1.	Which region has max oil reserves from 2014 to 2016?
d1=data1.groupby('Region')['2014','2015','2016'].sum(axis=1)
print(d1.columns)
d1


# In[38]:


d1.sum(axis=1).idxmax(axis=1)


# In[48]:


#2.	With suitable visualization show the oil reserves of India from 2010 to 2016.
d2=data1[data1['Country/ Region']=='India']
d2


# In[76]:


d3=d2.drop('Region',axis=1)
d4=d3.set_index('Country/ Region')
x=d4.columns
y=d4.iloc[0,:].values
print(x)
print(y)
print(type(y))
print(type(y))
d4


# data1.head()

# In[80]:


plt.plot(x,y,linestyle="dotted", marker='o')
#labels
plt.xlabel("Year")
plt.ylabel("Oil Reserves")
plt.title("Oil Reserves in India")

plt.show()


# In[106]:


#3.	List the countries having maximum oil reserves in each region.
data1['total_oil_reserve']=data1.iloc[:,2:9].sum(axis=1)
data1


# In[150]:


new1=data1.groupby(['Region'])['total_oil_reserve'].max()
new1.values
new1.index


# In[154]:


#4 Draw suitable visualization which shows the share of oil reserves by each region
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = new1.index
sizes = new1.values
#explode = (0, 0, 0, 0)
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=135)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[175]:


#5.	Find the world’s top 5 countries having maximum oil reserves in the 2015. 
#Show their % of share in total oil reserve for the same year.
new2=data1.sort_values('2015')[['Country/ Region','2015']].tail(5)
new2


# In[176]:


import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = new2['Country/ Region']
sizes = new2['2015']
#explode = (0, 0, 0, 0)
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=135)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[ ]:




