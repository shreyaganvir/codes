#!/usr/bin/env python
# coding: utf-8

# # How to Build a Machine Learning Model in Python
# 
# ## Learning Objectives
# In the modeling stage of the machine learning process, our goal is to choose and apply the appropriate machine learning approach that works with the data we have and solves the problem that we intend to solve. If our objective is to build a model that predicts a numeric or continuous value, then our problem is known as a regression problem. One of the most common models used in solving regression problems is **Linear Regression**. By the end of the tutorial, you will have learned:
# 
# + how to collect, explore and prepare data
# + how to build and evaluate a model

# ## 1. Collect the Data

# In[ ]:


import pandas as pd
bikes = pd.read_csv("bikes.csv")
bikes.head()


# ## 2. Explore the Data

# In[ ]:


bikes.info()


# In[ ]:


bikes.describe()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
bikes.plot(kind = 'scatter', x = 'temperature', y = 'rentals')


# In[ ]:


bikes.plot(kind = 'scatter', x = 'humidity', y = 'rentals')


# In[ ]:


bikes.plot(kind = 'scatter', x = 'windspeed', y = 'rentals')


# ## 3. Prepare the Data

# In[ ]:


response = 'rentals'
y = bikes[[response]]
y


# In[ ]:


predictors = list(bikes.columns)
predictors.remove(response)
x = bikes[predictors]
x


# In[ ]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1234) 


# ## 4. Train the Model

# In[ ]:


from sklearn.linear_model import LinearRegression


# In[ ]:





# In[ ]:





# The model coefficients correspond to the order in which the independent variables are listed in the training data. This means that the equation for the fitted regression line can be written as:
# 
# $y = 3800.68 + 80.35 \times temperature - 4665.74 \times humidity - 196.22 \times windspeed$
# 
# With the linear regression equation, we can estimate what our model will predict given any weather condition. For example, given a temperature of $72^{\circ}F$, $22\%$ humidity and windspeed of $5$ miles per hour, our model would predict:
# 
# $7,578 \text{ bikes} \approx 3800.68 + 80.35 \times 72 - 4665.74 \times .22 - 196.22 \times 5$
# 

# ## 5. Evaluate the Model

# In[ ]:





# In[ ]:





# In[ ]:


from sklearn.metrics import mean_absolute_error

