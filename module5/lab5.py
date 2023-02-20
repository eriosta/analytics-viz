import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

class MetropolitanArea:
    def __init__(self, region_name):
        self.region_name = region_name
        self.df = pd.read_csv('module5/Metro_zhvi_uc_sfrcondo_tier_0.67_1.0_sm_sa_mon.csv')
        self.df = self.df.melt(id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], 
                               var_name='Date', value_name='ZHVI')
        self.df = self.df[self.df['RegionName'] == self.region_name]
        self.df['Date'] = self.df['Date'].str.extract(r'(\d{4})').astype(int)
        self.slope, self.intercept, self.r_value, self.p_value, self.std_err = linregress(self.df['Date'], self.df['ZHVI'])
    
    def predict_home_value(self, year):
        return self.slope * year + self.intercept

    def plot_data(self, ax):
        sns.regplot(x='Date', y='ZHVI', data=self.df, ax=ax, label='data')
        x_values = np.arange(1996, 2031)
        y_values = self.predict_home_value(x_values)
        ax.plot(x_values, y_values, color='red', label='regression line')
        r_squared = round(self.r_value ** 2, 2)
        line_formula = f'y = {round(self.slope, 2)}x + {round(self.intercept, 2)}'
        ax.text(0.20, 0.15, f'R-squared = {r_squared}\n{line_formula}', transform=ax.transAxes, va='top')
        ax.set_title(self.region_name)
        ax.set_xlabel('Year')
        ax.set_ylabel('ZHVI')
        ax.set_xlim(1996, 2030)
        ax.set_ylim(0, 1000000)
        ax.legend()

# Create the metropolitan areas
sa = MetropolitanArea('San Antonio, TX')
nyc = MetropolitanArea('New York, NY')
third_area = MetropolitanArea('Austin, TX')

# Create the subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Plot the data for each metropolitan area
sa.plot_data(ax=axes[0])
nyc.plot_data(ax=axes[1])
third_area.plot_data(ax=axes[2])

plt.show()