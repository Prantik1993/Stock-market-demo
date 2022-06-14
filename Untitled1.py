#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


train = pd.read_excel('Downloads\Indian stock market final sheet Part 1.xlsx')


# In[3]:


train.head()


# In[4]:


# check how many missing values
train.isnull().sum()


# # Replace missing categorical values

# In[5]:


def impute_nan_most_frequent_category(DataFrame,ColName):
    # .mode()[0] - gives first category name
     most_frequent_category=DataFrame[ColName].mode()[0]
    
    # replace nan values with most occured category
     DataFrame[ColName + '_new'] = DataFrame[ColName]
     DataFrame[ColName + '_new'].fillna(most_frequent_category,inplace=True)


# In[6]:


for Columns in ['Sub-Sector']:
    impute_nan_most_frequent_category(train,Columns)
    
# Display imputed result
train[['Sub-Sector','Sub-Sector_new']].head(10)


# In[7]:


#3. Drop actual columns
train = train.drop(['Sub-Sector'], axis = 1)


# In[8]:


train.isnull().sum()


# # Replace numerical values with mean

# In[9]:


train['5Y CAGR'].mean()


# In[10]:


train['5Y CAGR'] = train['5Y CAGR'].fillna(train['5Y CAGR'].mean())
train['Earnings Per Share'] = train['Earnings Per Share'].fillna(train['Earnings Per Share'].mean())


# In[11]:


train.isnull().sum()


# In[12]:


train['5Y CAGR'].mean()


# In[13]:


train['Earnings Per Share'].mean()


# In[14]:


import seaborn as sns


# In[ ]:


data.to_excel('Indian stock market final sheet.xlsx', sheet_name='sheet1', index=False)


# In[ ]:




