#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as ny 
import seaborn as sns


# In[4]:


df1 =pd.read_csv(r"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz")


# In[5]:


df2= pd.read_csv(r"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz")


# In[8]:


df1.shape


# In[9]:


df2.shape


# In[10]:


df1


# In[11]:


df2


# In[13]:


df1.lpep_pickup_datetime = pd.to_datetime(df1.lpep_pickup_datetime)
df1.lpep_dropoff_datetime = pd.to_datetime(df1.lpep_dropoff_datetime)


# In[14]:


df2.lpep_pickup_datetime = pd.to_datetime(df2.lpep_pickup_datetime)
df2.lpep_dropoff_datetime = pd.to_datetime(df2.lpep_dropoff_datetime)


# In[15]:


df1


# In[16]:


df2


# In[17]:


from sqlalchemy import create_engine


# In[18]:


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[19]:


engine


# In[21]:


print(pd.io.sql.get_schema(df1, name = 'yellow_taxi_data'))


# In[22]:


print(pd.io.sql.get_schema(df2, name = 'yellow_taxi_data'))


# In[25]:


df1.lpep_pickup_datetime.value_counts(2019-1-15)


# In[27]:


df1.lpep_pickup_datetime.value_counts(2019-1-15).max()


# In[52]:


df1.lpep_pickup_datetime = df1['lpep_pickup_datetime'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
df1.lpep_dropoff_datetime = df1['lpep_dropoff_datetime'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
df1


# In[67]:


df1.lpep_pickup_datetime.value_counts()


# In[66]:


df1.passenger_count.value_counts('df1.lpep_pickup_datetime'== 2019-1-1)


# In[69]:


df1['trip_distance'].value_counts()


# In[ ]:




