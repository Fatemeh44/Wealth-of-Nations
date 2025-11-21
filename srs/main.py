# ======================================================
# Global Economic and Health Analysis using World Bank Data
# Author: FATEMEH MOAYEDIRAD
# ======================================================

import wbdata
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------
# 1. Download data from World Bank
# ------------------------------------------------------
print("Downloading data from World Bank...")

# Time range (recent decades)
data_date = (datetime.datetime(1990, 1, 1), datetime.datetime(2022, 1, 1))

# Indicators
indicators = {
    'NY.GDP.PCAP.CD': 'GDP_per_capita',        # GDP per capita (current US$)
    'SP.DYN.LE00.IN': 'Life_expectancy',       # Life expectancy at birth
    'SH.XPD.CHEX.PC.CD': 'Health_expenditure', # Health expenditure per capita (US$)
    'SH.DYN.MORT': 'Child_mortality'           # Child mortality (per 1,000 live births)
}

# Fetch data
df = wbdata.get_dataframe(indicators, date=data_date)
df.reset_index(inplace=True)

# ------------------------------------------------------
# 2. Data cleaning
# ------------------------------------------------------
print("Cleaning data...")

# Remove missing values
df.dropna(inplace=True)

# Convert year to integer
df['date'] = df['date'].astype(int)

# Rename columns
df.rename(columns={'country': 'Country', 'date': 'Year'}, inplace=True)

# ------------------------------------------------------
# 3. Statistical analysis
# ------------------------------------------------------
print("Performing statistical analysis...")

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Latest year in dataset
latest_year = df['Year'].max()
latest_data = df[df['Year'] == latest_year]

# Correlation matrix
corr_matrix = latest_data[['GDP_per_capita', 'Life_expectancy', 'Health_expenditure', 'Child_mortality']].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# ------------------------------------------------------
# 4. Visualization
# ------------------------------------------------------
sns.set(style="whitegrid", palette="muted")

# Scatter: GDP vs Life Expectancy
plt.figure(figsize=(8, 6))
sns.scatterplot(data=latest_data, x='GDP_per_capita', y='Life_expectancy')
plt.title(f"GDP per Capita vs Life Expectancy ({latest_year})")
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Life Expectancy (Years)")
plt.xscale("log")
plt.show()

# Scatter: GDP vs Child Mortality
plt.figure(figsize=(8, 6))
sns.scatterplot(data=latest_data, x='GDP_per_capita', y='Child_mortality')
plt.title(f"GDP per Capita vs Child Mortality ({latest_year})")
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Child Mortality (per 1000 births)")
plt.xscale("log")
plt.yscale("log")
plt.show()

# Heatmap of correlations
plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap between Economic and Health Indicators")
plt.show()

# ------------------------------------------------------
# 5. Time trends for selected countries
# ------------------------------------------------------
countries_to_plot = ['United States', 'China', 'Germany', 'India', 'Iran', 'Brazil']
trend = df[df['Country'].isin(countries_to_plot)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=trend, x='Year', y='GDP_per_capita', hue='Country')
plt.title("GDP per Capita Trend (1990–2022)")
plt.ylabel("GDP per Capita (USD)")
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=trend, x='Year', y='Life_expectancy', hue='Country')
plt.title("Life Expectancy Trend (1990–2022)")
plt.ylabel("Years")
plt.show()

# ------------------------------------------------------
# 6. Summary interpretation
# ------------------------------------------------------
print("\n--- Summary Interpretation ---")
print("""
Results indicate that countries with higher GDP per capita generally have higher life expectancy 
and lower child mortality rates. This pattern is consistent across the past decades. 
Increased health expenditure also shows a positive correlation with better health outcomes. 
However, some nations with relatively low GDP but high life expectancy (such as Cuba) demonstrate 
that strong public health policies can significantly influence population well-being.
""")
