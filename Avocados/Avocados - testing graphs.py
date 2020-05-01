'''
EDA of Avocado dataset 
'''

# Import the necessary packages - basic EDA so no need for too many 
import numpy as np 
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt


# Import the file as csv 
df = pd.read_csv('avocado.csv')

# Initial analysis - checking what the data is
df.head(10)                                     # take a note of all the headers on a paper to have them handy


# Check the date range that we have 
df['Date'].max()
df['Date'].min()

#Check the datatypes for optimisation 
df.info()                                       # date is stored as object 
df['Date'] =  pd.to_datetime(df['Date'])

# Null values 
df.isnull().sum()                               # swell nothing is null

# There are regions listed - how many unique 
df['region'].nunique()

# Average price of avocados per year 
average_year_price = df.groupby('year')['AveragePrice'].mean()
type(average_year_price)
average_year_price.plot(figsize=(15,11))


# Comparison between conventional and organic 
# For simplicity, let us look at one year, and two region. 

con_conventional = df['type'] == 'conventional'
con_organic = df['type']=='organic'
con_2015 = df['year'] == 2015
con_2016 = df['year'] == 2016
con_region_calif = df['region']== 'California'
con_region_la = df['region'] == 'LosAngeles'

average_15_conv_calif = df[con_conventional & con_2015 & con_region_calif]
average_15_conv_calif.sort_values('Date')
average_15_conv_calif.plot(y='AveragePrice',x='Date', title='Conventional')

average_15_orga_calif = df[con_organic & con_2015 & con_region_calif]
average_15_orga_calif.sort_values('Date')
average_15_orga_calif.plot(y='AveragePrice',x='Date',title='Organic')

# Plotting both graphs together 
graph_15_conv_calif=average_15_conv_calif.plot(y='AveragePrice',x='Date',label='Conventional')
average_15_orga_calif.plot(ax=graph_15_conv_calif,y='AveragePrice',x='Date',label='Organic')

#Looking at 2016 as a comparative 
average_16_conv_calif= df[con_conventional & con_2016 & con_region_calif]
average_16_orga_calif = df[con_organic & con_2016 & con_region_calif]
average_16_conv_calif.sort_values('Date')
average_16_orga_calif.sort_values('Date')

average_16_conv_calif.plot(y='AveragePrice',x='Date', title='Conventional')
average_16_orga_calif.plot(y='AveragePrice',x='Date',title='Organic')

graph_16_conv_calif=average_16_conv_calif.plot(y='AveragePrice',x='Date',label='Conventional')
average_16_orga_calif.plot(ax=(graph_16_conv_calif),y='AveragePrice',x='Date',label='Organic')


# All the above - for Los Angelis 


average_15_conv_la = df[con_conventional & con_2015 & con_region_la]
average_15_conv_la.sort_values('Date')
average_15_conv_la.plot(y='AveragePrice',x='Date', title='Conventional')

average_15_orga_la = df[con_organic & con_2015 & con_region_la]
average_15_orga_la.sort_values('Date')
average_15_orga_la.plot(y='AveragePrice',x='Date',title='Organic')


graph_15_orga_la=average_15_conv_la.plot(y='AveragePrice',x='Date',label='Conventional')
average_15_orga_la.plot(ax=graph_15_orga_la,y='AveragePrice',x='Date',label='Organic')

# Los Angelis for 2016

average_16_conv_la= df[con_conventional & con_2016 & con_region_la]
average_16_orga_la = df[con_organic & con_2016 & con_region_calif]
average_16_conv_la.sort_values('Date')
average_16_orga_la.sort_values('Date')

average_16_conv_la.plot(y='AveragePrice',x='Date', title='Conventional')
average_16_orga_la.plot(y='AveragePrice',x='Date',title='Organic')

ax=average_16_conv_la.plot(y='AveragePrice',x='Date',label='Conventional')
graph_15_orga_la=average_15_conv_la.plot(y='AveragePrice',x='Date',label='Conventional')
average_16_orga_la.plot(ax=ax,y='AveragePrice',x='Date',label='Organic')

# All 2015 

# 2015 LA, Calif, Organic, Conventional 

df_15_LA_calif = df[con_region_la | con_region_calif]
df_15_LA_calif = df_15_LA_calif[con_2015]
df_15_LA_calif_org = df_15_LA_calif[con_organic]

df_15_LA_calif_org.plot(y='AveragePrice',x='Date',title= '2015 - LA & Calif')

