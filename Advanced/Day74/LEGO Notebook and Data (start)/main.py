import pandas as pd
import matplotlib.pyplot as plt

# Read the colors.csv file 
# from the data folder and find the total number of unique colours.
# Also, figure out how many of the LEGO colours are transparent

colors = pd.read_csv('colors.csv')
colors.head()

colors.groupby('is_trans').count()
colors.is_trans.value_counts()

#In which year were the first LEGO sets released and what were these sets called?
# How many different products did the LEGO company sell in their first year of operation?
# What are the top 5 LEGO sets with the most number of parts? 

sets = pd.read_csv('sets.csv')
sets.head()

sets['year'].min()
sets[sets['year'] == 1949]
sets.sort_values('num_parts', ascending=False).head()

# Challenge, Use groupby() and count() to show the number of LEGO sets released year-on-year

sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()

# Vizualise it with maplotlib

plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# Challenge 3
# Create a line plot of the number of themes released year-on-year.
# Only include the full calendar years in the dataset (1949 to 2019).

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace = True)
themes_by_year.head()

plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# Both of them

ax1 = plt.gca() # get current axes
ax2 = ax1.twinx() # another axis that shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(sets_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# With some styling
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(sets_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')

# Challenge
# Create a Pandas Series called parts_per_set that has the year as
# the index and contains the average number of parts per LEGO set in that year.
# Here's what you're looking to create:

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
parts_per_set.head()

# Challenge
# See if you can use the Matplotlib documentation to generate the scatter plot chart. Do you spot a trend in the chart?
# Again, you'll have to exclude the last two observations.

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])