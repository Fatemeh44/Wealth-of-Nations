# ======================================================
# Module: Visualization
# Purpose: Generate all plots for the study
# ======================================================

import matplotlib.pyplot as plt
import seaborn as sns
from config import COUNTRIES_OF_INTEREST

sns.set(style="whitegrid", palette="muted")

def plot_gdp_vs_life(latest_data, year):
    """Scatter plot: GDP per capita vs Life expectancy."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=latest_data, x='GDP_per_capita', y='Life_expectancy')
    plt.title(f"GDP per Capita vs Life Expectancy ({year})")
    plt.xlabel("GDP per Capita (USD)")
    plt.ylabel("Life Expectancy (Years)")
    plt.xscale("log")
    plt.show()


def plot_gdp_vs_mortality(latest_data, year):
    """Scatter plot: GDP per capita vs Child mortality."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=latest_data, x='GDP_per_capita', y='Child_mortality')
    plt.title(f"GDP per Capita vs Child Mortality ({year})")
    plt.xlabel("GDP per Capita (USD)")
    plt.ylabel("Child Mortality (per 1000 births)")
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


def plot_correlation_heatmap(corr_matrix):
    """Heatmap of correlation matrix."""
    plt.figure(figsize=(7, 5))
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Correlation Heatmap – Economic vs Health Indicators")
    plt.show()


def plot_time_trends(df):
    """Time-series trends for selected countries."""
    trend = df[df['Country'].isin(COUNTRIES_OF_INTEREST)]

    # GDP trend
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend, x='Year', y='GDP_per_capita', hue='Country')
    plt.title("GDP per Capita Trend (1990–2022)")
    plt.ylabel("GDP per Capita (USD)")
    plt.show()

    # Life expectancy trend
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend, x='Year', y='Life_expectancy', hue='Country')
    plt.title("Life Expectancy Trend (1990–2022)")
    plt.ylabel("Years")
    plt.show()
