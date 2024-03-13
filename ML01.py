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

# In[1]:


import pandas as pd
bikes = pd.read_csv("bikes.csv")
bikes.head()


# ## 2. Explore the Data

# In[2]:


bikes.info()


# In[3]:


bikes.describe()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
bikes.plot(kind = 'scatter', x = 'temperature', y = 'rentals')


# In[5]:


bikes.plot(kind = 'scatter', x = 'humidity', y = 'rentals')


# In[6]:


bikes.plot(kind = 'scatter', x = 'windspeed', y = 'rentals')


# ## 3. Prepare the Data

# In[7]:


response = 'rentals'
y = bikes[[response]]
y


# In[8]:


predictors = list(bikes.columns)
predictors.remove(response)
x = bikes[predictors]
x


# In[9]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1234) 


# ## 4. Train the Model

# In[10]:


from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x_train, y_train)


# In[11]:


model.intercept_


# In[12]:


model.coef_


# The model coefficients correspond to the order in which the independent variables are listed in the training data. This means that the equation for the fitted regression line can be written as:
# 
# $y = 3800.68 + 80.35 \times temperature - 4665.74 \times humidity - 196.22 \times windspeed$
# 
# With the linear regression equation, we can estimate what our model will predict given any weather condition. For example, given a temperature of $72^{\circ}F$, $22\%$ humidity and windspeed of $5$ miles per hour, our model would predict:
# 
# $7,578 \text{ bikes} \approx 3800.68 + 80.35 \times 72 - 4665.74 \times .22 - 196.22 \times 5$
# 

# ## 5. Evaluate the Model

# In[13]:


model.score(x_test, y_test)


# In[14]:


y_pred = model.predict(x_test)


# In[15]:


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)

