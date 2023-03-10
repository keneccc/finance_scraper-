import yfinance as yf 
import pandas as pd 
from pandas_datareader import data as pdr
from yahoo_fin import stock_info
import time 
import datetime
import glob
import csv

def get_ticker_data(ticker,i):
    data = []
    
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
    while datetime.datetime.now() <= end_time:
        try:
            tsla_price = stock_info.get_live_price(ticker)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.datetime.now().strftime("%m/%d/%Y")

            # print("The current live price of TSLA (Tesla Inc) at " + timestamp + " is $" + str(tsla_price) + ".")
            
            data.append({'timestamp': timestamp, 'date':date,  'price': tsla_price})

            #time.sleep(60) # waits for 1 minute
        except: 
            pass 

    print(data)

    with open(f'{ticker}_data_{i}.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['timestamp','date', 'price'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # save csv file
    csvfile.close()


