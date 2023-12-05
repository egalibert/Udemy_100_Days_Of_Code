import pandas as pd

df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)

# Q1 count all the rows
print(df.count())

# Q2 Can you count how many months of posts exist for each programming language?

print(df.groupby('TAG').sum())
print(df.groupby('TAG').count())

# Time usage practice
df.DATE = pd.to_datetime(df.DATE)
print(df.head())

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
						'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
						'Power': [100, 80, 25, 50, 99, 75, 5, 30]})

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

# Challenge
# Can you pivot the df DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called reshaped_df. 

# Examine the dimensions of the reshaped DataFrame. How many rows does it have? How many columns?

# Examine the head and the tail of the DataFrame. What does it look like?

# Print out the column names.

# Count the number of entries per column.

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df.columns)
print(reshaped_df.head())
print(reshaped_df.count())

reshaped_df = reshaped_df.fillna(0)

print(reshaped_df.head())