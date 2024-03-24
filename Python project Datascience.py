#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf
import pandas as pd


# In[5]:


apple = yf.Ticker("AAPL")
apple


# In[12]:


import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info


# In[13]:


apple_info['country']


# In[20]:


apple_share_price_data = apple.history(period="max")
apple_share_price_data


# In[21]:


# reset the index in DataFrame
apple_share_price_data.reset_index(inplace=True)


# In[22]:


# plot graph open price and Date
apple_share_price_data.plot(x="Date", y="Open")


# In[23]:


apple.dividends


# In[24]:


apple.dividends.plot()


# In[ ]:




