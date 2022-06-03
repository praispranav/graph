#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib as mat


# In[3]:


GooglePlayStoreDataFrame = pd.read_csv('googleplaystore.csv')


# In[4]:


GoogleUserReviewDataFrame = pd.read_csv('googleplaystore_user_reviews.csv')


# In[5]:


GoogleUserReviewDataFrame = GoogleUserReviewDataFrame.dropna(axis=0)


# In[6]:


GoogleUserReviewDataFrame.dropna(axis=0)


# In[7]:


GooglePlayStoreDataFrame


# In[8]:


GooglePlayStoreDataFrame = GooglePlayStoreDataFrame.dropna(axis=0)


# In[9]:


GooglePlayStoreDataFrame


# In[10]:


GooglePlayStoreDataFrame[GooglePlayStoreDataFrame.Rating > 5]


# In[11]:


pie_android_version_play_store_data_frame = GooglePlayStoreDataFrame.value_counts(subset="Android Ver")


# In[12]:


pie_android_version_play_store_data_frame.plot.pie(subplots=True, figsize=(11, 6))


# In[13]:


pie_category_play_store_data_frame = GooglePlayStoreDataFrame.value_counts(subset="Category")
pie_category_play_store_data_frame


# In[14]:


pie_category_play_store_data_frame.plot.pie(subplots=True, figsize=(11, 6))


# In[15]:


GooglePlayStoreDataFrame["Rating"]


# In[16]:


hist_rating=GooglePlayStoreDataFrame['Rating'].astype(float)
hist_rating.plot.hist(bins=20)


# In[17]:


hist_review=GooglePlayStoreDataFrame['Reviews'].astype(float)
hist_review.plot.hist(bins=20)


# In[18]:


bar_sentiments  = GoogleUserReviewDataFrame.value_counts(subset="Sentiment")
bar_sentiments.plot.bar(subplots=True)


# In[19]:


merged_data_frame = GoogleUserReviewDataFrame.merge(GooglePlayStoreDataFrame, left_on='App', right_on='App')
merged_data_frame = merged_data_frame.dropna(axis=0)
merged_data_frame


# In[ ]:




