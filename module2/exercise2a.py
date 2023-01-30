import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
import pandas as pd
import datetime

# Order: AAPL, BYND, CVX, GME, MRNA
a2D = np.array([[20],[30],[40],[50],[60]])

stocks = ['AAPL', 'BYND', 'CVX', 'GME', 'MRNA']

price_data = yf.download(
    tickers=stocks, 
    start='2020-05-01', end='2020-05-30', 
    interval='1d' )[ 'Close' ] 

for i, row in price_data.iterrows():
    i = datetime.date(i.year, i.month, i.day)
    print(f"Total earnings on %s: USD %s" %
            (i, np.dot(row[stocks].to_numpy(), a2D)[0]))


#1 
for col in stocks:
    for i, row in price_data.iterrows():
        max = np.max(price_data[col])
        min = np.min(price_data[col])
        diff = max - min
        min_date = price_data.index[(price_data[col] == min)]
        min_date = min_date.format(formatter=lambda x: x.strftime('%Y/%m/%d'))[0]
    print(f"Stock: %s, Min: %s, Min Date: %s, Diff: %s" % (col, min, min_date, diff))

price_data_melt = pd.melt(price_data, value_vars=['AAPL','BYND','CVX','GME','MRNA'],ignore_index=False)
price_data_melt.rename(columns={'value':'Price','variable':'Stock'},inplace=True)

fig = plt.figure( figsize=(11,8) )
sns.lineplot(data=price_data_melt, x=price_data_melt.index,y="Price", hue="Stock")
plt.show()


f, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, sharex=True)
sns.lineplot(data=price_data_melt, x=price_data_melt.index,y="Price", hue="Stock", ax=ax1)
sns.lineplot(data=price_data_melt, x=price_data_melt.index,y="Price", hue="Stock", ax=ax2)
ax2.set_ylim(40, 150)
ax1.set_ylim(0.75, 1.6)
plt.show()





