#!/usr/bin/env python
# coding: utf-8

# Build a Machine Learning Model 

# Collect the Data

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


bikes = pd.read_csv("bikes.csv")
print(bikes.head())

# Explore the Data

print(bikes.info())
print(bikes.describe())
#get_ipython().run_line_magic('matplotlib', 'inline')
#bikes.plot(kind = 'scatter', x = 'temperature', y = 'rentals')
#bikes.plot(kind = 'scatter', x = 'humidity', y = 'rentals')
#bikes.plot(kind = 'scatter', x = 'windspeed', y = 'rentals')


# Prepare the Data
response = 'rentals'
y = bikes[[response]]
predictors = list(bikes.columns)
predictors.remove(response)
x = bikes[predictors]


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1234)
model = LinearRegression().fit(x_train, y_train)
print(model.intercept_)
print(model.coef_)


# Train the Model

# The model coefficients correspond to the order in which the independent variables are listed in the training data. This means that the equation for the fitted regression line can be written as:
# $y = 3800.68 + 80.35 \times temperature - 4665.74 \times humidity - 196.22 \times windspeed$
# With the linear regression equation, we can estimate what our model will predict given any weather condition. For example, given a temperature of $72^{\circ}F$, $22\%$ humidity and windspeed of $5$ miles per hour, our model would predict:
# $7,578 \text{ bikes} \approx 3800.68 + 80.35 \times 72 - 4665.74 \times .22 - 196.22 \times 5$

# Evaluate the Model

model.score(x_test, y_test)


y_pred = model.predict(x_test)

print(mean_absolute_error(y_test, y_pred))
