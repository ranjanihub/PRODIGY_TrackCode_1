#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Add the dataset path
file_path = r"C:\Users\TRINITY ELE\Downloads\annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
data = pd.read_csv(file_path)

# Selecting the last 10 rows of the dataset
last_10_data = data.tail(10)

# Creating bar chart for showing the difference between the country and their income level
plt.bar(last_10_data["Variable_name"], last_10_data["Value"])
plt.xlabel("Name")  # Adding x-axis label
plt.ylabel("Value")  # Adding y-axis label
plt.title("Income Level by Country (Last 10 Values)")  # Adding title
plt.xticks(rotation=45) 
plt.show()


# In[ ]:




