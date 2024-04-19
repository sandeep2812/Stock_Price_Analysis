#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import glob


# In[3]:


glob.glob(r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/*csv')


# In[4]:


len(glob.glob(r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/*csv'))


# In[5]:


company_list = [
    r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/AAPL_data.csv',
    r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/AMZN_data.csv',
    r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/GOOG_data.csv',
    r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/MSFT_data.csv'
]


# In[6]:


import warnings
from warnings import filterwarnings
filterwarnings('ignore')


# In[7]:


all_data = pd.DataFrame()
for file in company_list:
    current_df=pd.read_csv(file)
    all_data=current_df.append(all_data, ignore_index=True)


# In[8]:


all_data.head(10)


# In[9]:


all_data.shape


# In[10]:


all_data.size


# In[11]:


all_data.ndim


# In[12]:


all_data.dtypes     


# In[13]:


# date - object : this has to be fixed, it cant be string, it should be DataTime.


# In[14]:


all_data['date']=pd.to_datetime(all_data['date'])


# In[15]:


all_data['date']


# In[16]:


tech_list=all_data['Name'].unique()


# In[17]:


tech_list


# In[ ]:





# In[18]:


plt.figure(figsize = (20,12))
for index, company in enumerate(tech_list,1):
    plt.subplot(2, 2, index)         #creating subplot for each stock
    filter1=all_data['Name']==company
    df=all_data[filter1]
    plt.plot(df['date'],df['close'])
    plt.title(company)


# In[ ]:





# # Moving average of the various stocks

# In[19]:


all_data.head(15)


# In[20]:


all_data['close'].rolling(window=10).mean().head(14)


# In[21]:


new_data = all_data.copy()


# In[22]:


new_data


# In[23]:


new_data.head()


# In[24]:


new_data.tail(7)


# In[25]:


ma_day=[10,20,50]
for ma in ma_day:
    new_data['close_'+str(ma)]=new_data['close'].rolling(ma).mean()


# In[26]:


new_data


# In[27]:


new_data.tail(7)


# In[28]:


new_data.set_index('date', inplace=True)


# In[29]:


new_data


# In[30]:


new_data.columns


# In[31]:


plt.figure(figsize=(20,15))
for index, company in enumerate(tech_list,1):
    plt.subplot(2, 2, index)
    filter1 = new_data['Name']==company
    df = new_data[filter1]
    df[['close_10', 'close_20', 'close_50']].plot(ax=plt.gca())
    plt.title(company)


# In[ ]:





# # analyse Closing price change in apple stock !
# Daily Stock Return Formula
# To calculate how much you gained or lost per day for a stock, subtract the opening price from the closing price. Then, multiply the result by the number of shares you own in the company. 

# In[32]:


company_list


# In[33]:


apple = pd.read_csv(r'/Users/sandeepkumar/Downloads/S&P_resources/individual_stocks_5yr/AAPL_data.csv')


# In[34]:


apple


# In[35]:


apple.head()


# In[36]:


apple.tail()


# In[37]:


apple.size


# In[38]:


apple.ndim


# In[39]:


apple.dtypes


# In[40]:


apple['close']


# In[41]:


apple['daily return (in %)']=apple['close'].pct_change()*100


# In[42]:


apple.head(4)


# In[43]:


import plotly.express as px


# In[44]:


px.scatter(apple, x='date' , y='daily return (in %)')


# In[45]:


px.line(apple, x='date' , y='daily return (in %)')


# In[ ]:





# Performing resampling analysis of closing price ..
# Before doing resampling,first u have to make your date feature 'row-index' so that u can resample data on various basis :
# 
# a..yearly('Y')  , 
# b..quarterly('Q')   ,
# c..monthly('M') ,
# d..weekly basis ('W'), 
# e..Daily_basis('D')  
# f..minutes ('3T') , 
# g..30 second bins('30S')   ,
# h..resample('17min')

# In[46]:


apple.head()


# In[47]:


apple.dtypes


# In[48]:


apple['date']=pd.to_datetime(apple['date'])


# In[49]:


apple.dtypes


# In[50]:


apple.head(4)


# In[51]:


apple.set_index('date', inplace=True)


# In[52]:


apple.head(4)


# In[53]:


# resampling the data


# In[54]:


# on monthly basis


# In[55]:


apple['close'].resample('M').mean()


# In[58]:


apple['close'].resample('M').mean().plot()


# In[59]:


# on yearly basis


# In[60]:


apple['close'].resample('Y').mean()


# In[61]:


apple.head(4)


# In[63]:


apple['close'].resample('Y').mean().plot()


# In[64]:


# on quarterly basis


# In[65]:


apple['close'].resample('Q').mean()


# In[67]:


apple['close'].resample('Q').mean().plot()


# In[68]:


#on weekely basis


# In[69]:


apple['close'].resample('W').mean()


# In[70]:


apple['close'].resample('W').mean().plot()


# In[71]:


apple['close'].resample('D').mean()


# In[72]:


apple['close'].resample('D').mean().plot()


# In[73]:


#minutes


# In[74]:


apple['close'].resample('3T').mean()


# In[75]:


apple['close'].resample('3T').mean().plot()


# In[76]:


apple['close'].resample('17MIN').mean()


# In[77]:


apple['close'].resample('17MIN').mean().plot()


# In[ ]:





# # Whether closing prices of these tech companies (Amazon,Apple,Google,Microsoft) are correlated or not !¶

# In[78]:


company_list


# In[79]:


company_list[0]


# In[80]:


app = pd.read_csv(company_list[0])
amzn = pd.read_csv(company_list[1])
google = pd.read_csv(company_list[2])
msft = pd.read_csv(company_list[3])


# In[81]:


closing_price = pd.DataFrame()


# In[82]:


closing_price['apple_close'] = app['close']
closing_price['amazon_close'] = amzn['close']
closing_price['google_close'] = google['close']
closing_price['msft_close'] = msft['close']


# In[83]:


closing_price


# In[84]:


sns.pairplot(closing_price)


# In[ ]:





# In[85]:


closing_price.corr()


# In[88]:


sns.heatmap(closing_price.corr(), annot = True)       

Conclusions : 
Closing price of Google and Microsoft are well correlated
& Closing price of Amazon and Microsoft have a co-relation of 0.96
# In[ ]:





# 
# # analyse Whether Daily change in Closing price of stocks or Daily Returns in Stock are co-related or not !

# In[90]:


closing_price


# In[91]:


closing_price['apple_close']


# In[92]:


closing_price['apple_close'].shift(1)


# In[93]:


#This shifts the values of the selected column by one position. As a result, each value in the new column will be the 
#previous day's closing price of Apple stock.


# In[ ]:





# In[94]:


(closing_price['apple_close']-closing_price['apple_close'].shift(1))/closing_price['apple_close'].shift(1)*100


# In[97]:


for col in closing_price.columns:
    closing_price[col + '_pct_change'] = (closing_price[col]-closing_price[col].shift(1))/closing_price[col].shift(1)*100


# In[98]:


closing_price


# In[99]:


closing_price.columns


# In[100]:


clg_price=closing_price[['apple_close_pct_change','amazon_close_pct_change','google_close_pct_change','msft_close_pct_change']]


# In[101]:


clg_price


# In[103]:


g = sns.PairGrid(data= clg_price)
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot)
g.map_upper(sns.kdeplot)


# In[105]:


clg_price.corr()


# In[ ]:




