import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('cost_revenue_dirty.csv')

# Challenge: Answer these questions about the dataset:

# How many rows and columns does the dataset contain?
# Are there any NaN values present?
# Are there any duplicate rows?
# What are the data types of the columns?

data.shape
data.isna().values.any()
data.duplicated().values.any()
data.info()

# Challenge 2
# Convert the USD_Production_Budget, USD_Worldwide_Gross,
# and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.

# Note that domestic in this context refers to the United States.

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 
					'USD_Worldwide_Gross',
					'USD_Domestic_Gross']
 
for col in columns_to_clean:
	for char in chars_to_remove:
		data[col] = data[col].astype(str).str.replace(char, "")
	data[col] = pd.to_numeric(data[col])

# Challenge 3
# Convert the Release_Date column to a Pandas Datetime type.

data.Release_Date = pd.to_datetime(data.Release_Date)


# Challenge 1
# What is the average production budget of the films in the data set?

# What is the average worldwide gross revenue of films?

# What were the minimums for worldwide and domestic revenue?

# Are the bottom 25% of films actually profitable or do they lose money?

# What are the highest production budget and highest worldwide gross revenue of any film?

# How much revenue did the lowest and highest budget films make?

data.describe()

# Challenge:
# How many films grossed $0 domestically (i.e., in the United States)?
# What were the highest budget films that grossed nothing?

zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)

# Challenge:
# Same but worldwide

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

# Challenge
# Use the Pandas .query() function to accomplish the same thing.
# Create a subset for international releases that had some worldwide gross revenue,
# but made zero revenue in the United States.

international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()

# Challenge
# Now that you've seen how to create a beautiful bubble chart in Seaborn, it's time to create your own.
# Can you write the code to replicate this chart?
# Notice how we are actually representing THREE dimensions in this chart:
# the budget, the release date, and the worldwide revenue.
# This is what makes bubble charts so awesomely informative.

plt.figure(figsize=(8,4), dpi=200)
 
with sns.axes_style("darkgrid"):
	ax = sns.scatterplot(data=data_clean, 
					x='Release_Date', 
					y='USD_Production_Budget',
					hue='USD_Worldwide_Gross',
					size='USD_Worldwide_Gross',)

	ax.set(ylim=(0, 450000000),
		xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
		xlabel='Year',
		ylabel='Budget in $100 millions')
	

# Challenge
# Can you create a column in data_clean that has the decade of the movie release.
# For example, a film released in 1992 or 1999 should have 1990 in the Decade column.

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
