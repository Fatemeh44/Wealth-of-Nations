# ======================================================
# Module: Data Cleaning
# Purpose: Clean and prepare raw data
# ======================================================

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the raw dataset:
    - Removes missing values
    - Converts year column to integer
    - Renames columns for consistency

    Returns:
        pd.DataFrame: Fully cleaned dataset
    """
    print("Cleaning data...")

    df = df.dropna()

    df['date'] = df['date'].astype(int)

    df.rename(columns={'country': 'Country', 'date': 'Year'}, inplace=True)

    return df
