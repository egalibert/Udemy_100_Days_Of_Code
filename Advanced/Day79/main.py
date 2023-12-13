import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format
df_data = pd.read_csv('nobel_prize_data.csv')

# Challenge: Preliminary data exploration.

# What is the shape of df_data? How many rows and columns?
# What are the column names?
# In which year was the Nobel prize first awarded?
# Which year is the latest year included in the dataset?

df_data.shape
df_data.head()
df_data.tail()
df_data.info()

# Challange:

# Are there any duplicate values in the dataset?
# Are there NaN values in the dataset?
# Which columns tend to have NaN values?
# How many NaN values are there per column?
# Why do these columns have NaN values?

df_data.isna().values.any() #True
df_data.duplicated().values.any() #False
df_data.isna().sum()

col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
df_data.loc[df_data.organization_name.isna()][col_subset]

col_subset = ['year','category', 'laureate_type', 'birth_date','full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset]

# Challenge 3
# Convert the birth_date column to Pandas Datetime objects

df_data.birth_date = pd.to_datetime(df_data.birth_date)

# Add a Column called share_pct which has the laureates'
# share as a percentage in the form of a floating-point number.

separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

# Challenge 2
# Create a donut chart using plotly which shows how many prizes went to men
# compared to how many prizes went to women.
# What percentage of all the prizes went to women?

biology = df_data.sex.value_counts()
fig = px.pie(labels=biology.index, 
             values=biology.values,
             title="Percentage of Male vs. Female Winners",
             names=biology.index,
             hole=0.4,)
 
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
 
fig.show() # Percentage was 94 men 6 women


# Challenge 3
# What are the names of the first 3 female Nobel laureates?
# What did the win the prize for?
# What do you see in their birth_country? Were they part of an organisation?

df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]


# Challenge 4
# Did some people get a Nobel Prize more than once? If so, who were they?

is_winner = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner]
print(f'There are {multiple_winners.full_name.nunique()}' \
	' winners who were awarded the prize more than once.') # 6 people got twice or more

col_subset = ['year', 'category', 'laureate_type', 'full_name']
multiple_winners[col_subset]


# Challenge 5
# In how many categories are prizes awarded?
# Create a plotly bar chart with the number of prizes awarded by category.
# Use the color scale called Aggrnyl to colour the chart, but don't show a color axis.
# Which category has the most number of prizes awarded?
# Which category has the fewest number of prizes awarded?

df_data.category.nunique()

prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
		x = prizes_per_category.index,
		y = prizes_per_category.values,
		color = prizes_per_category.values,
		color_continuous_scale='Aggrnyl',
		title='Number of Prizes Awarded per Category')

v_bar.update_layout(xaxis_title='Nobel Prize Category', 
					coloraxis_showscale=False,
					yaxis_title='Number of Prizes')
v_bar.show()


# Challenge 6
# When was the first prize in the field of Economics awarded?
# Who did the prize go to?

df_data[df_data.category == 'Economics'].sort_values('year')[:3]


# Challenge 1
# Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually.
# Count the number of prizes awarded every year.
# Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).
# Using Matplotlib superimpose the rolling average on a scatter plot.
# Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

prize_per_year = df_data.groupby(by='year').count().prize 

moving_average = prize_per_year.rolling(window=5).mean()

plt.scatter(x=prize_per_year.index, 
           y=prize_per_year.values, 
           c='dodgerblue',
           alpha=0.7,
           s=100,)
 
plt.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
 
plt.show()


# Challenge 2
# Investigate if more prizes are shared than before.
# Calculate the average prize share of the winners on a year by year basis.
# Calculate the 5 year rolling average of the percentage share.
# Copy-paste the cell from the chart you created above.
# Modify the code to add a secondary axis to your Matplotlib chart.
# Plot the rolling average of the prize share on this chart.
# See if you can invert the secondary y-axis to make the relationship even more clear.

prize_per_year = df_data.groupby(by='year').count().prize 

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
           fontsize=14, 
           rotation=45)
 
ax = plt.gca() # get current axis
ax.set_xlim(1900, 2020)
 
ax.scatter(x=prize_per_year.index, 
           y=prize_per_year.values, 
           c='dodgerblue',
           alpha=0.7,
           s=100,)
 
ax.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
 
plt.show()

# Challenge 1: Top 20 Country Ranking
# Create a Pandas DataFrame called top20_countries that has the two columns.
# The prize column should contain the total number of prizes won.
# Is it best to use birth_country, birth_country_current or organization_country?
# What are some potential problems when using birth_country or any of the others? Which column is the least problematic?
# Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what you're after:

top_countries = df_data.groupby(['birth_country_current'], 
								as_index=False).agg({'prize': pd.Series.count})

top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]


h_bar = px.bar(x=top20_countries.prize,
			y=top20_countries.birth_country_current,
			orientation='h',
			color=top20_countries.prize,
			color_continuous_scale='Viridis',
			title='Top 20 Countries by Number of Prizes')

h_bar.update_layout(xaxis_title='Number of Prizes', 
					yaxis_title='Country',
					coloraxis_showscale=False)
h_bar.show()

# Challenge 2: Choropleth Map
# Create this choropleth map using the plotly documentation:

df_countries = df_data.groupby(['birth_country_current', 'ISO'], 
							as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)

world_map = px.choropleth(df_countries,
						locations='ISO',
						color='prize', 
						hover_name='birth_country_current', 
						color_continuous_scale=px.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True,)

world_map.show()
