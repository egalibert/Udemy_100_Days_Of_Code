import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv('monthly_deaths.csv', parse_dates=['date'])


# Challenge: Check out these two DataFrames ☝️.

# What is the shape of df_yearly and df_monthly? How many rows and columns?
# What are the column names?
# Which years are included in the dataset?
# Are there any NaN values or duplicates?
# What were the average number of births that took place per month?
# What were the average number of deaths that took place per month?

df_monthly.shape # 98 3, date births deaths 1841-1848
df_monthly.head()

df_yearly.shape # 12 4, date births	deaths 1841-1846
df_yearly.head()

df_monthly.isna().values.any() # False on all
df_yearly.isna().values.any()
df_yearly.duplicated().values.any()
df_monthly.duplicated().values.any()

df_monthly.describe() # 257 births, 23 deaths
df_yearly.describe() # 3,152.75 births , deaths 223.33

# Challenge: How dangerous was childbirth in the 1840s in Vienna?

# Using the annual data, calculate the percentage of women giving birth who died throughout the 1840s at the hospital.
# In comparison, the United States recorded 18.5 maternal deaths per 100,000 or 0.018% in 2013 (source).

prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')

# Challenge: Create a Matplotlib chart with twin y-axes. It should look something like this:

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y') 

plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)
 
# Use Locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.grid(color='grey', linestyle='--')
 
ax1.plot(df_monthly.date, 
         df_monthly.births, 
         color='skyblue', 
         linewidth=3)
 
ax2.plot(df_monthly.date, 
         df_monthly.deaths, 
         color='crimson', 
         linewidth=2, 
         linestyle='--')
 
plt.show()


# Challenge 1: The Yearly Data Split by Clinic
# Let's turn our attention to the annual data.
#  Use plotly to create line charts of the births and deaths of the two different clinics at the Vienna General Hospital.
# Which clinic is bigger or more busy judging by the number of births?
# Has the hospital had more patients over time?
# What was the highest number of deaths recorded in clinic 1 and clinic 2?

line = px.line(df_yearly, 
			x='year', 
			y='births',
			color='clinic',
			title='Total Yearly Births by Clinic')

line.show()


# Challenge 2: Calculate the Proportion of Deaths at Each Clinic
# Calculate the proportion of maternal deaths per clinic. That way we can compare like with like.
# Work out the percentage of deaths for each row in the df_yearly DataFrame by adding a column called "pct_deaths".
# Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the total number of births).
# Create another plotly line chart to see how the percentage varies year over year with the two different clinics.
# Which clinic has a higher proportion of deaths?
# What is the highest monthly death rate in clinic 1 compared to clinic 2?

df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births

clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')

clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')

line = px.line(df_yearly, 
			x='year', 
			y='pct_deaths',
			color='clinic',
			title='Proportion of Yearly Deaths by Clinic')

line.show()

# Challenge 1: The Effect of Handwashing
# Add a column called "pct_deaths" to df_monthly that has the percentage of deaths per birth for each row.
# Create two subsets from the df_monthly data: before and after Dr Semmelweis ordered washing hand.
# Calculate the average death rate prior to June 1846.
# Calculate the average death rate after June 1846.

handwashing_start = pd.to_datetime('1847-06-01')

df_monthly['pct_deaths'] = df_monthly.deaths/df_monthly.births
before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]

bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
print(f'Average death rate before 1847 was {bw_rate:.4}%')
print(f'Average death rate AFTER 1847 was {aw_rate:.3}%')


# Challenge 2: Calculate a Rolling Average of the Death Rate
# Create a DataFrame that has the 6-month rolling average death rate prior to mandatory handwashing.

roll_df = before_washing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()


# Challenge 3: Highlighting Subsections of a Line Chart
# Copy-paste and then modify the Matplotlib chart from before to plot the
# monthly death rates (instead of the total number of births and deaths). The chart should look something like this:

plt.figure(figsize=(14,8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color='grey', linestyle='--')

ma_line, = plt.plot(roll_df.index, 
					roll_df.pct_deaths, 
					color='crimson', 
					linewidth=3, 
					linestyle='--',
					label='6m Moving Average')
bw_line, = plt.plot(before_washing.date, 
					before_washing.pct_deaths,
					color='black', 
					linewidth=1, 
					linestyle='--', 
					label='Before Handwashing')
aw_line, = plt.plot(after_washing.date, 
					after_washing.pct_deaths, 
					color='skyblue', 
					linewidth=3, 
					marker='o',
					label='After Handwashing')

plt.legend(handles=[ma_line, bw_line, aw_line],
		fontsize=18)

plt.show()