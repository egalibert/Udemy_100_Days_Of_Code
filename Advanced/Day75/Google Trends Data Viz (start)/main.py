import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

# Challenge:

# 1.What are the shapes of the dataframes?
# 2. How many rows and columns?
# 3. What are the column names?
# 4. Complete the f-string to show the largest/smallest number in the search data column
# 5. Try the .describe() function to see some useful descriptive statistics
# 6. What is the periodicity of the time series data (daily, weekly, monthly)?
# 7. What does a value of 100 in the Google Trend search popularity actually mean?

# Tesla
# 1, 2, 3
print(df_tesla.shape)
df_tesla.head()

# 4
print(f'Largest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].min()}')

# 5
df_tesla.describe()

# Unemployment

df_unemployment.shape
df_unemployment.head()

print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()}')

#Bitcoin

df_btc_price.shape
df_btc_price.head()

df_btc_search.shape
df_btc_search.head()

print(f'largest BTC News Search: {df_btc_search["BTC_NEWS_SEARCH"].max()}')

# Challenge: Are there any missing values in any of the dataframes? If so, 
# which row/rows have missing values? How many missing values are there?

print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')

# This one has some
print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')
# Two to be exact
print(f'Number of missing values: {df_btc_price.isna().values.sum()}')

# Challenge: Remove any missing values that you found.
df_btc_price = df_btc_price.dropna()

# Challenge
# Our DataFrames contain time-series data. 
# Do you remember how to check the data type of the entries in the DataFrame?
# Have a look at the data types of the MONTH or DATE columns.
# Convert any strings you find into Datetime objects.
# Do this for all 4 DataFrames. Double-check if your type conversion was successful.

df_tesla.dtypes

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)


# Challenge
# Plot the Tesla stock price against the Tesla search volume using a line chart and
# two different axes.

ax1 = plt.gca() 
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price')
ax2.set_ylabel('Search Trend')
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)

# Challenge
# Try using one of the blue colour names for the search volume and
#  a HEX code for a red colour for the stock price. 

ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E') # can use a HEX code
ax2.set_ylabel('Search Trend', color='skyblue') # or a named colour
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

# Challenge
# There are still some ways to improve the look of this chart. First off, let's make it larger. Can you make the following changes:

# Increase the figure size (e.g., to 14 by 8).

# Increase the font sizes for the labels and the ticks on the x-axis to 14.

# Rotate the text on the x-axis by 45 degrees.

# Add a title that reads 'Tesla Web Search vs Price'

# Make the lines on the chart thicker.

# Keep the chart looking sharp by changing the dots-per-inch or DPI value.

# Set minimum and maximum values for the y and x-axis. Hint: check out methods like set_xlim().

# Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.

plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
plt.show()

# Challenge
# Plot the search for "unemployment benefits" against the official unemployment rate.

# Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate

# Change the y-axis label to: FRED U/E Rate

# Change the axis limits

# Add a grey grid to the chart to better see the years and the U/E rate values. Use dashed lines for the line style.

# Can you discern any seasonality in the searches? Is there a pattern?

plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
 
# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')
 
# Change the dataset used
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 
         color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 
         color='skyblue', linewidth=3)
 
plt.show()