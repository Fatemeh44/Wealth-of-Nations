# ======================================================
# Module: Data Loader
# Purpose: Download World Bank data
# ======================================================

import wbdata
import pandas as pd
from config import DATA_DATE_RANGE, INDICATORS

def load_worldbank_data():
    """
    Downloads data from the World Bank API.

    Returns:
        pd.DataFrame: Raw dataset including country, year, and indicator values.
    """
    print("Downloading data from World Bank...")
    df = wbdata.get_dataframe(INDICATORS, date=DATA_DATE_RANGE)
    df.reset_index(inplace=True)
    return df
    
print(load_worldbank_data().head(28))