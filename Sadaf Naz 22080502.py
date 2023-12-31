# -*- coding: utf-8 -*-
"""JOY_41826.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JHmNSHp-07hqmjdnWZB-nD6m4QPIbdyA

# Importing the dataset
"""

import pandas as pd

data = pd.read_csv("D:\Countries GDP 1960-2020.csv")

"""# EDA"""

# Display the first few rows of the dataset
print("Head of the dataset:")
print(data.head())

# Display information about the dataset, including data types and non-null counts
print("\nInformation about the dataset:")
print(data.info())

# Display summary statistics of the numeric columns
print("\nSummary statistics:")
print(data.describe())

"""#  Recent trends in GDP for some specific countries"""

# Filter the dataset to select specific years
years_to_focus = ['2011', '2015', '2020']

# Create a subset of the data with the chosen years
selected_data = data[['Country Name', 'Country Code'] + years_to_focus]

# Filter the data for the selected countries
selected_countries = ['India', 'Australia', 'Japan', 'France', 'Canada', 'China', 'United States']
selected_data = selected_data[selected_data['Country Name'].isin(selected_countries)]

# Display the filtered data
print(selected_data)

"""# First Visualization"""

import matplotlib.pyplot as plt

# Data for selected countries
countries = ['India', 'Australia', 'Japan', 'France', 'Canada', 'China', 'United States']
years = list(map(str, range(1960, 2021)))

# Filter the data for the selected countries
selected_data = data[data['Country Name'].isin(countries)]

# Set the figure size
plt.figure(figsize=(12, 6))

# Plot the GDP trends for selected countries
for country in countries:
    plt.plot(years, selected_data.loc[selected_data['Country Name'] == country, years].values[0], label=country)

# Customize the plot
plt.title('GDP Trends Over Time (1960-2020)')
plt.xlabel('Year')
plt.ylabel('GDP (in Trillions)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

"""# Second Visualization"""

import matplotlib.pyplot as plt

# Data for selected countries
countries = ['India', 'China']
years = list(map(str, range(1960, 2021)))

# Filter the data for the selected countries
selected_data = data[data['Country Name'].isin(countries)]

# Set the figure size
plt.figure(figsize=(12, 6))

# Plot a scatter plot to compare the GDP of India and China
plt.scatter(selected_data.loc[selected_data['Country Name'] == 'India', years].values[0],
            selected_data.loc[selected_data['Country Name'] == 'China', years].values[0])

# Customize the plot
plt.title('GDP Comparison Between India and China (1960-2020)')
plt.xlabel('GDP of India (in Trillions)')
plt.ylabel('GDP of China (in Trillions)')
plt.grid(True)

# Show the plot
plt.show()

"""# Third Visualization"""

import matplotlib.pyplot as plt

# Data for the selected year
year = '2020'

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a histogram to visualize the distribution of GDP values in 2020
plt.hist(selected_data[year], bins=20, edgecolor='k')

# Customize the plot
plt.title(f'Distribution of GDP Values in {year}')
plt.xlabel('GDP (in Trillions)')
plt.ylabel('Number of Countries')
plt.grid(True)

# Show the plot
plt.show()