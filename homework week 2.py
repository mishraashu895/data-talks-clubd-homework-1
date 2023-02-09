#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.cloud import bigquery


# In[5]:


bigquery


# In[6]:


import pandas as pd


# In[7]:


df1 =pd.read_csv(r"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz")
df2= pd.read_csv(r"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz")


# In[15]:


df = pd.concat([df1,df2], axis=1)


# In[16]:


df.head()


# In[17]:


df.columns


# In[19]:


df.shape


# In[20]:


df.nunique()


# In[21]:


df.drop(["congestion_surcharge","ehail_fee"],axis =1)


# In[25]:


query = """
SELECT * FROM (
    SELECT
        fare_amount,
        extract(DAYOFWEEK from pickup_datetime) as day_of_week,
        ABS(dropoff_longitude - pickup_longitude) as londiff,
        ABS(dropoff_latitude - pickup_latitude) as latdiff,
        passenger_count
    FROM
      `df`
) 
WHERE 
  -- do some quality control
  londiff < 5.0 AND latdiff < 5.0 
  AND fare_amount > 1 AND fare_amount < 200
  -- sample the dataset for now. can remove the sampling later
  AND RAND() < 0.001
        """


# In[32]:


query


# In[37]:





# In[ ]:




