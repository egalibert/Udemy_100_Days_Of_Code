# Challenge: How many rows and columns does df_apps have?
# What are the column names? What does the data look like?
# Look at a random sample of 5 different rows with .sample()

import pandas as pd
import plotly.express as px

df_apps = pd.read_csv('apps.csv')
df_apps.shape
df_apps.tail()
df_apps.sample()

# Challenge: Remove the columns called Last_Updated and Android_Version from the DataFrame.
# We will not use these columns.

df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)

# Challenge: How many rows have a NaN value (not-a-number) in
# the Rating column? Create DataFrame called df_apps_clean that
# does not include these rows.

nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
nan_rows.head()

df_apps_clean = df_apps.dropna()
df_apps_clean.shape()

# Challenge: Are there any duplicates in data?
# Check for duplicates using the .duplicated() function.
# How many entries can you find for the "Instagram" app?
# Use .drop_duplicates() to remove any duplicates from df_apps_clean.

duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()
df_apps_clean[df_apps_clean.App == 'Instagram']

df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean[df_apps_clean.App == 'Instagram']

# Challenge: Identify which apps are the highest rated.
# What problem might you encounter if you rely exclusively on ratings alone
# to determine the quality of an app?

# Challenge:
# What's the size in megabytes (MB) of the largest
# Android apps in the Google Play Store. Based on the data,
# do you think there could be a limit in place or
# can developers make apps as large as they please?

# Challenge: Which apps have the highest number of reviews?
# Are there any paid apps among the top 50?

df_apps_clean.sort_values('Rating', ascending=False).head()
# Most of them have really few ratings

df_apps_clean.sort_values('Size_MBs', ascending=False).head()

df_apps_clean.sort_values('Reviews', ascending=False).head(50)

# Create with plotly a Create Pie and Donut Chart

ratings = df_apps_clean.Content_Rating.value_counts()
ratings

fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
hole=0.6,
)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
 
fig.show()

# Challenge
# How many apps had over 1 billion (that's right - BILLION) installations?
# How many apps just had a single install?

# Check the datatype of the Installs column.

# Count the number of apps at each level of installations.

# Convert the number of installations (the Installs column) to a numeric data type.
# Hint: this is a 2-step process.
# You'll have to make sure you remove non-numeric characters first.

df_apps_clean.Installs.describe()
df_apps_clean.info()

df_apps_clean[['App', 'Installs']].groupby('Installs').count()
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

# Challenge
# Convert the price column to numeric data.
# Then investigate the top 20 most expensive apps in the dataset.

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
 
df_apps_clean.sort_values('Price', ascending=False).head(20)

df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)