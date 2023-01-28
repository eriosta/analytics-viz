import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# 1. The starter code has been created for you. 
# 2. Using the Yahoo Finance module, download the stock data for the stocks AMC and GME between December 1, 2021 and around the day you started this exercise (June or July 2021) in intervals of one day. You will focus only on the ```Close``` price and ```Volume``` traded. 
# 3. Using the data downloaded from ```yfinance```, create a new ```DataFrame``` that contains these five columns: ```Day```, ```AMC Close```, ```AMC Volume```, ```GME Close```, and```GME Volume```. Note the index for the ```DataFrame``` is the YYYY-MM-DD date, but you will need to make it a column. 
# 4. Apply ```pd.melt()``` to this new ```DataFrame``` created in Step 3, such that the ```Day``` column is kept. The variable column will contain either ```AMC Close```, ```AMC Volume```, ```GME Close```, and```GME Volume```. Rename this column to ```'Type'```. The values column will contain either the closing price or the volume traded for the respective stock on that day. 
# 5. Create a FacetGrid of four lineplots on the stock data using the ```DataFrame``` generated in Step 4. Each lineplot will show either the closing prices or volume traded over the days within the time frame. The FacetGrid will separate the lineplots on the four different types of information: ```AMC Close```, ```AMC Volume```, ```GME Close```, and```GME Volume``` Set the ```suptitle``` to 'AMC and GME between Dec 2020 and Jun 2021'. The dates will be plotted on the x axis. The y axis will be ```Close``` price or ```Volume``` traded. 
# 6. Create two Seaborn scatterplots to explore the relationships between AMC and GME stocks. The first scatterplot will show the relationship between the ```AMC Close``` prices versus the ```GME Close``` prices. Set the title of this scatterplot to 'AMC versus GME Closing Prices'. The second scatterplot will show the relationship between the ```AMC Volume``` versus the ```GME Volume```. Set the ```suptitle``` to 'AMC and GME between Dec 2020 and Jun 2021'. Set the title of this scatterplot to 'AMC versus GME Volumes'.
# 7. Answer the questions below.

df = yf.download( tickers=['AMC','GME'], start='2022-12-01', \
                         end='2023-01-27', interval='1d' )

df = df.loc[:,df.columns.get_level_values(0).isin({"Volume", "Close"})]

df.reset_index(inplace=True)

df2 = pd.DataFrame()
df2['AMC Close'] = df[('Close','AMC')].copy()
df2['GME Close'] = df[('Close','GME')].copy()
df2['AMC Volume'] = df[('Volume','AMC')].copy()
df2['GME Volume'] = df[('Volume','GME')].copy()
df2['Day'] = df[('Date',)].copy()

sns.scatterplot(data=df2, x="GME Volume", y="AMC Volume").set(title='GME Volume prices versus the AMC Volume')
plt.show()
sns.scatterplot(data=df2, x="GME Close", y="AMC Close").set(title='GME Close prices versus the AMC Close')
plt.show()


df2 = df2.melt(
    id_vars='Day',
    value_vars=['AMC Close','GME Close','AMC Volume','GME Volume'],
    ignore_index=False)

df2.rename(columns={'value':'Value','variable':'Type'},inplace=True)

df2['Day'] = df2['Day'].dt.strftime("%d/%m/%Y")
df2['Day'] = pd.to_datetime(df2['Day'], format="%d/%m/%Y")

grid = sns.FacetGrid(df2, row="Type",hue="Type")
grid.map(sns.lineplot, "Day","Value")
plt.show()


