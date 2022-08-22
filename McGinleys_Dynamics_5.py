#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from datetime import timedelta

def MD(data, k, N, stock_name):
    close  = f'{stock_name} close'
    columns = [close, "md"]
    new_data = pd.DataFrame(columns = columns) 
    new_data[close] = (data)
    arr = np.array(new_data[close])
    newline = []
    for i in range(len(arr)):
        if i == 0:
            close = md = arr[i]
            ratio = 1
        else:
            close = arr[i]
            ratio = (close/md)**4
        md1 = md + ((close-md)/(k*N*ratio))
        md = xx = md1
        newline.append(xx)

    new_data["md"] = (newline)
    new = f'{stock_name}_close'

    print(new_data.head())
    new_data.to_csv('file2.csv', mode = 'a', index = True, header = True, sep = "\t")
    return
    
def main():
    N = 7
    k = 0.6
    today= date.today()
    yesterday = today - timedelta(days=1)
    COLUMNS = ["AAPL", "GOOGL", "TSLA", "NVDA", "FB", "MSFT", "AMZN", "EBAY", "TCS", "HDFC", "SBI"]
    #print(COLUMNS)
    today= date.today()
    data = pd.DataFrame( columns = COLUMNS)
    for i in COLUMNS:
        stock_name = i 
        yesterday = today - timedelta(days=2)
        data1 = yf.download(tickers=stock_name, start=yesterday, interval='5m')
        if len(data1) > 3:
            data[stock_name]= data1["Close"]
            MD(data[stock_name], k, N, stock_name)
        else:
            print(f"The filed to download the data of {stock_name}")
            continue

        
    
if __name__ == "__main__":
    main()


# In[ ]:




