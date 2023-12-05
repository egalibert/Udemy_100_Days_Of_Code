import pandas as pd
import matplotlib.pyplot as plt

# Challenge 1,
# You can actually show a line chart for the popularity
# of a programming language using only a single line of code. 
# Can you use the .plot() documentation to figure out how to do this?

df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(plt.plot(reshaped_df.index, reshaped_df['java']))

# Challenge 2
# Now that you've successfully created and styled your chart, can you figure out how to plot
# both Java and Python next to each other?

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)