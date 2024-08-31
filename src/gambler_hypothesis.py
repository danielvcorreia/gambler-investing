#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame


# In[2]:


# Choose minimum ammount to reinforce every day in $dollars
reinforce=10


# In[3]:


# Load data into memory
sp500_index = pd.read_csv('../data/sp500_index.csv', delimiter=',')


# In[4]:


# Print a sample
sp500_index.head()


# In[5]:


last_day_price=sp500_index['S&P500'][0]
year_days=365
month_days=30
total_days_counter=0

counter_for_year=1
counter_for_month=1

reinforce_strat_2=0
reinforce_strat_3=0

wallet_strat_1=0
wallet_strat_2=1.5*reinforce*year_days
wallet_strat_3=1.5*reinforce*month_days

total_invested_strat_1=wallet_strat_1
total_invested_strat_2=wallet_strat_2
total_invested_strat_3=wallet_strat_3


# In[6]:


# For each day from 2014-2024
for index, row in sp500_index.iterrows():
    # Daily close price of s&p500 index
    daily_close_price = row['S&P500']
    
    # Check if amount to reinforce the wallet first strategy
    day_reinforce = reinforce if last_day_price < daily_close_price else 2*reinforce
    
    
    
    # Update wallet with gains
    wallet_strat_1 = wallet_strat_1 * daily_close_price / last_day_price
    # Update wallet of first strategy
    wallet_strat_1 += day_reinforce
    # Update total invested for first strategy
    total_invested_strat_1 += day_reinforce
    
    # Update the ammount to invest in strategy 2
    reinforce_strat_2 += day_reinforce
    # Update the ammount to invest in strategy 3
    reinforce_strat_3 += day_reinforce

    
    # Update wallet with gains
    wallet_strat_2 = wallet_strat_2 * daily_close_price / last_day_price
    # Update wallet of second strategy
    if counter_for_year >= year_days:
        wallet_strat_2 += reinforce_strat_2
        # Update total invested for second strategy
        total_invested_strat_2 += reinforce_strat_2
        # Reset day counter
        counter_for_year = 1
        # Reset ammount to invest in strategy 2
        reinforce_strat_2 = 0
    else:
        # Update day counter
        counter_for_year += 1

        
    # Update wallet with gains
    wallet_strat_3 = wallet_strat_3 * daily_close_price / last_day_price
    # Update wallet of third strategy
    if counter_for_month >= month_days:
        wallet_strat_3 += reinforce_strat_3
        # Update total invested for third strategy
        total_invested_strat_3 += reinforce_strat_3
        # Reset day counter
        counter_for_month = 1
        # Reset ammount to invest in strategy 3
        reinforce_strat_3 = 0
    else:
        # Update day counter
        counter_for_month += 1
        
        
    
    # Update last day price to current day
    last_day_price = daily_close_price
    
    # Update total days passed
    total_days_counter += 1

print('Strategy 1: invest the ammount defined in "reinforce" variable if the stock goes up and double if it goes down\n')
print(f'For {total_days_counter/year_days} years you invested a total of {total_invested_strat_1}$')
print(f'And you ended up with a total of {wallet_strat_1}$')

print('\n\n\n')

print('Strategy 2: invest the same total ammount of strategy 1 but all-in in the begining of the year\n')
print(f'For {total_days_counter/year_days} years you invested a total of {total_invested_strat_2}$')
print(f'And you ended up with a total of {wallet_strat_2}$')

print('\n\n\n')

print('Strategy 3: invest the same total ammount of strategy 1 and 2 but in the begining of the month\n')
print(f'For {total_days_counter/year_days} years you invested a total of {total_invested_strat_3}$')
print(f'And you ended up with a total of {wallet_strat_3}$')

