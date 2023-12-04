import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

clean_df = df.dropna()


# Q1 What college major has the highest mid-career salary? 
# How much do graduates with this major earn? 
# (Mid-career is defined as having 10+ years of experience).
print(clean_df["Mid-Career Median Salary"].idxmax())
print(clean_df["Undergraduate Major"].loc[8])

# Chemical Engineering

# Q2 Which college major has the lowest starting 
# salary and how much do graduates earn after university?

print(clean_df["Starting Median Salary"].idxmin())
print(clean_df["Undergraduate Major"].loc[49])

# Spanish

# Q3 Which college major has the lowest mid-career salary and 
# how much can people expect to earn with this degree? 

print(clean_df["Mid-Career Median Salary"].idxmin())
print(clean_df["Undergraduate Major"].loc[18])