import pandas as pd
import datetime
import time
import requests
import io
import yfinance as yf
import numpy as np
import math
import statistics

#define the ticker symbol
sym = input('Enter ticket symbol for stock: ')

tickerSymbol = sym
s_pSymbol = '^GSPC'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
s_p = yf.Ticker(s_pSymbol)

start_date = input('Enter start date(YYYY-MM-DD): ')
end_date = input('Enter end date(YYYY-MM-DD): ')

#get the historical prices for this ticker
tickerDF = pd.DataFrame(tickerData.history(start=start_date, end=end_date, interval='1mo'))
tickerDF = tickerDF.dropna(axis = 0)

s_pDF = pd.DataFrame(s_p.history(start=start_date, end=end_date, interval='1mo'))
s_pDF = s_pDF.dropna(axis = 0)

tickerClose = np.array(tickerDF['Close'])
s_pClose = np.array(s_pDF['Close'])


tickerReturns = []
s_pReturns = []
for i in range(len(tickerClose) - 1, 0, -1):
    tickerReturns.append((tickerClose[i] - tickerClose[i-1])/tickerClose[i-1])
    s_pReturns.append((s_pClose[i] - s_pClose[i-1])/s_pClose[i-1])

# print(tickerReturns)
# print(s_pReturns)

mean_x = sum(tickerReturns) / len(tickerReturns)
mean_y = sum(s_pReturns) / len(s_pReturns)



cov = sum((a - mean_x) * (b - mean_y) for (a,b) in zip(tickerReturns,s_pReturns)) / len(tickerReturns)
var = statistics.variance(s_pReturns)

# print(cov)
# print(var)
print('Calculated Beta is approximately ' + str(cov/var))
