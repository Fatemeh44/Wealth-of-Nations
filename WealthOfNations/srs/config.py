# ======================================================
# Configuration File – Global Settings for the Project
# ======================================================

import datetime

# Time range for fetching World Bank data
DATA_DATE_RANGE = (
    datetime.datetime(1990, 1, 1),
    datetime.datetime(2022, 1, 1)
)

# List of World Bank Indicators
INDICATORS = {
    'NY.GDP.PCAP.CD': 'GDP_per_capita',
    'SP.DYN.LE00.IN': 'Life_expectancy',
    'SH.XPD.CHEX.PC.CD': 'Health_expenditure',
    'SH.DYN.MORT': 'Child_mortality'
}

# Countries used in time-series visualizations
COUNTRIES_OF_INTEREST = ['United States', 'China', 'Germany', 'India', 'Brazil']
