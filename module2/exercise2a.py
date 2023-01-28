# You will do the following
# 1. The starter code has been created for you. Specifically, there is an example of how you will access historical 
    #  stock data from Yahoo Finance module. Adapt and use this sample code to get the required data for the stocks above.
    #  The stock symbols are provided above, which is needed for the TICKERS parameter.
# 2. Create a 2D NumPy array which represent the number of shares per stock.
    # Then use the dot product, to find the value of the entire portfolio for each day in May.
    # Create a data frame with the dates and the portfolio values.
# 3. Create a lineplot using seaborn that plots the prices for each stock. 
    # The x axis are the days (they can just be days numbered 0 through 20). 
    # The y axis is the price of the stocks. 
    # HINT: use the pd.melt() function to reconfigure the DF so you can plot 
    # multiple lines using the HUE parameter in the lineplot() function. 
    # After calling pd.melt(), name the value column 'Price' and the variable (column) name 'Stock'.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
import pandas as pd

# This is an example code to download the historic stock price data during March 2020 for AMC and TSLA (Tesla)
# stock. It will collect the data in intervals of one day. You will get a DataFrame of closing 
# prices for each day. The index of row is the TimeStamp for each day. This line also extracts the 
# 'Close' column as we are using that to determine # the price of each stock. 
price_data = yf.download( tickers=['AMC','TSLA'], start='2020-03-01', end='2020-03-30', interval='1d' )[ 'Close' ] 
print( price_data )

# type: ignore
a2D = np.array([['AAPL',20],['BYND',30],['CVX',40],['GME',50],['MRNA',60]])

price_data = yf.download(
    tickers=list(a2D[:,0]), 
    start='2020-05-01', end='2020-05-30', 
    interval='1d' )[ 'Close' ] 

price_data['AAPL'] = price_data['AAPL'] * int(a2D[0,1])
price_data['BYND'] = price_data['BYND'] * int(a2D[1,1])
price_data['CVX'] = price_data['CVX'] * int(a2D[2,1])
price_data['GME'] = price_data['GME'] * int(a2D[3,1])
price_data['MRNA'] = price_data['MRNA'] * int(a2D[4,1])

price_data = pd.melt(price_data, value_vars=['AAPL','BYND','CVX','GME','MRNA'],ignore_index=False)
price_data.rename(columns={'value':'Price','variable':'Stock'},inplace=True)

fig = plt.figure( figsize=(11,8) )
sns.lineplot(data=price_data, x=price_data.index,y="Price", hue="Stock")
plt.show()