#!/usr/bin/env python
# coding: utf-8

# # STOCK MARKET VISUALISATION

# In[48]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import plotly.express as px


# In[49]:


#Installing yfinance library

## pip install yfinance


# In[50]:


# load Yahoo Finance Live Data 
import yfinance as yf


# In[51]:


## pip install yahoofinancials


# In[52]:


## from yahoofinancials import YahooFinancials


# In[53]:


print('Enter first stock name:')
x = input()
print('Enter period:')
y = input()
print('Enter interval:')
z = input()


# In[54]:


print('Enter second stock name:')
x1 = input()
print('Enter period:')
y1 = input()
print('Enter interval:')
z1 = input()


# In[55]:


# Downloading the stock
df = yf.download(x, period = y, interval = z)


# In[56]:


# Downloading the stock
df1 = yf.download(x1, period = y1, interval = z1)


# In[57]:


df.head(5)


# In[58]:


df1.head(5)


# ### VISUALISATION OF STOCK-1

# In[59]:


print('Closing Price of',x)


price_chart = px.line(df['Close'], 
                           title='Closing Price', 
                           color_discrete_map={'Close':'red'}
                        )

price_chart.show()


# In[60]:


print('Daily Volume',x)
volume_chart = px.area(df['Volume'], 
                            title='Daily Volume', 
                            color_discrete_map={'Volume':'blue'} )
volume_chart.show()


# In[61]:


print('Opening Price of',x)
open_chart = px.line(df['Open'], 
                           title='Opening Price', 
                           color_discrete_map={'Open':'red'}, 
                           width=800, height=800)
open_chart.show()


# In[62]:


print('Day High of',x)
high_chart = px.area(df['High'], 
                           title='Day High', 
                           color_discrete_map={'High':'red'}, 
                           width=800, height=800)
high_chart.show()


# In[63]:


print('Day Low of',x)
low_chart = px.area(df['Low'], 
                           title='Day Low', 
                           color_discrete_map={'Low':'green'}, 
                           width=800, height=800)
low_chart.show()


# In[ ]:





# ### VISUALISATION FOR STOCK-2

# In[64]:


#DO SIMILARLY FOR STOCK 2


# In[65]:


print('Closing Price of',x1)


price_chart1 = px.line(df1['Close'], 
                           title='Closing Price', 
                           color_discrete_map={'Close':'red'}
                        )

price_chart1.show()


# In[66]:


print('Daily Volume',x1)
volume1_chart = px.area(df1['Volume'], 
                            title='Daily Volume', 
                            color_discrete_map={'Volume':'blue'} )
volume1_chart.show()


# In[67]:


print('Opening Price of',x1)
open1_chart = px.line(df1['Open'], 
                           title='Opening Price', 
                           color_discrete_map={'Open':'red'}, 
                           width=800, height=800)
open1_chart.show()


# In[68]:


print('Day High of',x1)
high1_chart = px.area(df1['High'], 
                           title='Day High', 
                           color_discrete_map={'High':'red'}, 
                           width=800, height=800)
high1_chart.show()


# In[69]:


print('Day Low of',x1)
low1_chart = px.area(df1['Low'], 
                           title='Day Low', 
                           color_discrete_map={'Low':'green'}, 
                           width=800, height=800)
low1_chart.show()


# ### COMPARING THE STOCKS

# In[70]:


import matplotlib.pyplot as plt


# In[71]:


plt.plot(df['Open'])
plt.plot(df1['Open'])

plt.suptitle("Comparing the opening price of both stocks")
plt.show()


# In[72]:


plt.plot(df['Volume'])
plt.plot(df1['Volume'])

plt.suptitle("Comparing Volume of both stocks")
plt.show()


# In[73]:


plt.plot(df['High'])
plt.plot(df1['High'])

plt.suptitle("Comparing High of both stocks")
plt.show()


# In[74]:


plt.plot(df['Low'])
plt.plot(df1['Low'])

plt.suptitle("Comparing Low of both stocks")
plt.show()


# In[75]:


plt.plot(df['Close'])
plt.plot(df1['Close'])

plt.suptitle("Comparing closing price of both stocks")
plt.show()


# In[ ]:





# ### STOCK - 1 DAY GRAPH

# In[77]:


df = yf.download(x, period = '1d', interval = '1h')


# In[78]:


df.head(5)


# In[80]:


plt.plot(df['Open'])
plt.plot(df['Close'])

print(x)
plt.suptitle("Comparing the opening and closing price")
plt.show()


# In[81]:


plt.plot(df['High'])
plt.plot(df['Low'])

print(x)
plt.suptitle("Comparing the High and Low price")
plt.show()


# In[82]:


plt.plot(df['Volume'])

print(x)
plt.suptitle("Volume")
plt.show()


# In[ ]:





# ### STOCK - 2 DAY GRAPH

# In[83]:


df = yf.download(x1, period = '1d', interval = '1h')


# In[84]:


df.head(5)


# In[85]:


plt.plot(df['Open'])
plt.plot(df['Close'])

print(x1)
plt.suptitle("Comparing the opening and closing price")
plt.show()


# In[86]:


plt.plot(df['High'])
plt.plot(df['Low'])

print(x1)
plt.suptitle("Comparing the High and Low price")
plt.show()


# In[87]:


plt.plot(df['Volume'])

print(x1)
plt.suptitle("Volume")
plt.show()


# In[ ]:




