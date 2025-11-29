# ======================================================
# Module: Statistical Analysis
# Purpose: Compute statistics, correlation, and summaries
# ======================================================

import pandas as pd

def compute_statistics(df: pd.DataFrame):
    """
    Prints descriptive statistics and correlation matrix.

    Returns:
        corr_matrix (pd.DataFrame): Correlation matrix for latest data year.
        latest_year (int): Most recent year with data.
        latest_data (pd.DataFrame): Filtered data for the latest year.
    """
    print("Performing statistical analysis...\n")

    print("Descriptive Statistics:")
    print(df.describe())

    latest_year = df['Year'].max()
    latest_data = df[df['Year'] == latest_year]

    corr_matrix = latest_data[
        ['GDP_per_capita', 'Life_expectancy', 'Health_expenditure', 'Child_mortality']
    ].corr()

    print("\nCorrelation Matrix:")
    print(corr_matrix)

    return corr_matrix, latest_year, latest_data


def summary_interpretation():
    """Prints text-based interpretation for the analysis."""
    print("\n--- Summary Interpretation ---")
    print("""
Countries with higher GDP per capita typically show higher life expectancy 
and lower child mortality rates. This consistent trend highlights the strong 
relationship between economic performance and public health outcomes.
Higher health expenditure is generally linked to better population health.
However, exceptions (such as Cuba) indicate that strong health policies 
can compensate for limited economic resources.
""")
