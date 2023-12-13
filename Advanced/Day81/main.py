import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('boston.csv', index_col=0)
data.shape # 506 data points
data.columns # column names
data.head()
data.count() # number of rows
data.info()


print(f'Any NaN values? {data.isna().values.any()}')
print(f'Any duplicates? {data.duplicated().values.any()}')

sns.displot(data['PRICE'], 
			bins=50, 
			aspect=2,
			kde=True, 
			color='#2196f3')

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()

sns.displot(data.DIS, 
			bins=50, 
			aspect=2,
			kde=True, 
			color='darkblue')

plt.title(f'Distance to Employment Centres. Average: {(data.DIS.mean()):.2}')
plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
plt.ylabel('Nr. of Homes')

plt.show()

sns.displot(data.RM, 
			aspect=2,
			kde=True, 
			color='#00796b')

plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Nr. of Homes')

plt.show()

river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
			y=river_access.values,
			color=river_access.values,
			color_continuous_scale=px.colors.sequential.haline,
			title='Next to Charles River?')

bar.update_layout(xaxis_title='Property Located Next to the River?', 
				yaxis_title='Number of Homes',
				coloraxis_showscale=False)
bar.show()

with sns.axes_style('darkgrid'):
sns.jointplot(x=data['DIS'], 
				y=data['NOX'], 
				height=8, 
				kind='scatter',
				color='deeppink', 
				joint_kws={'alpha':0.5})

plt.show()

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, 
													target, 
													test_size=0.2, 
													random_state=10)

regr = LinearRegression()
regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()