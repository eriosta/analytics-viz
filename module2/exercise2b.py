import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

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


df2_melt = df2.melt(
    id_vars='Day',
    value_vars=['AMC Close','GME Close','AMC Volume','GME Volume'],
    ignore_index=False)

df2_melt.rename(columns={'value':'Value','variable':'Type'},inplace=True)

df2_melt['Day'] = df2['Day'].dt.strftime("%d/%m/%Y")
df2_melt['Day'] = pd.to_datetime(df2['Day'], format="%d/%m/%Y")

grid = sns.FacetGrid(df2_melt, row="Type",hue="Type")
grid.map(sns.lineplot, "Day","Value")
plt.show()


