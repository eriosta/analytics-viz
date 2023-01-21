import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data is from https://en.wikipedia.org/wiki/List_of_largest_cities

# Manually create the DataFrame
data = [ { 'City': 'Tokyo', 'Population' : 37400088 }, \
        { 'City': 'Delhi', 'Population' : 28514000 }, \
        { 'City': 'Shanghai', 'Population' : 25582000 }, \
        { 'City': 'Sao Paulo', 'Population' : 21650000 },\
        { 'City': 'Mexico City', 'Population' : 21581000 }, \
        { 'City': 'Cairo', 'Population' : 20076000 }, \
        { 'City': 'Mumbai', 'Population' : 19980000 }, \
        { 'City': 'Beijing', 'Population' : 19618000 }, \
        { 'City': 'Dhaka', 'Population' : 19578000 }, \
        { 'City': 'Osaka', 'Population' : 19281000 } ]
df = pd.DataFrame( data, columns=[ 'City', 'Population'] )

# Create the Seaborn barplot
# The barplot is too small. Change the dimensions in the figsize tuple so that 
# you can easily read the labels on the X axis.
plt.figure( figsize=(12,5) )
axes = sns.barplot( x='City', y='Population', data=df, palette='bright' )
axes.set_title( 'Top Ten Most Populous Cities in the World' )
plt.show()