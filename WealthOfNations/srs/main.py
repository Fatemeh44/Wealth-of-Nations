# ======================================================
# Main Runner Script
# Purpose: Orchestrates all project modules
# ======================================================


# just a test

from data_loader import load_worldbank_data
from data_cleaning import clean_data
from analysis import compute_statistics, summary_interpretation
from visualization import (
    plot_gdp_vs_life,
    plot_gdp_vs_mortality,
    plot_correlation_heatmap,
    plot_time_trends
)

# ------------------------------------------------------
# Main Execution Sequence
# ------------------------------------------------------

# 1. Load data
df = load_worldbank_data()

# 2. Clean data
df = clean_data(df)

# 3. Compute statistics
corr_matrix, latest_year, latest_data = compute_statistics(df)

# 4. Visualization
plot_gdp_vs_life(latest_data, latest_year)
plot_gdp_vs_mortality(latest_data, latest_year)
plot_correlation_heatmap(corr_matrix)
plot_time_trends(df)

# 5. Summary
summary_interpretation()
