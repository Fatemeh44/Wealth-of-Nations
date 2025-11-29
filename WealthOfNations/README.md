# The Wealth of Nations — Economic and Health Analysis

This project analyzes the relationship between national wealth and population health 
using open data from the **World Bank** covering the period 1990–2022. 
The goal is to explore correlations between economic indicators such as GDP per capita 
and health-related metrics like life expectancy, health expenditure, and child mortality rates.

## Dataset
- Source: [World Bank Open Data](https://data.worldbank.org)
- Indicators used in this project:
  - GDP per capita (NY.GDP.PCAP.CD)
  - Life expectancy at birth (SP.DYN.LE00.IN)
  - Health expenditure per capita (SH.XPD.CHEX.PC.CD)
  - Child mortality rate (SH.DYN.MORT)

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt

The required Python packages include:

wbdata for downloading World Bank data

pandas for data manipulation

matplotlib and seaborn for data visualization

Project Structure

WealthOfNations/
├── data/
│   └── worldbank_data.csv          # Raw data downloaded from World Bank
├── srs/
│   └── main.py                     # Main script with analysis and visualizations
├── README.md                       # Project documentation
├── .gitignore                      # Files and folders to ignore in Git
└── requirements.txt                # Python dependencies

How to Run

Clone the repository:

git clone https://github.com/your-username/WealthOfNations.git


Navigate to the project folder:

cd WealthOfNations


Run the main script:

python srs/main.py


The program will download the data, save it in data/worldbank_data.csv,
and generate statistical summaries and visualizations.

Analysis and Visualizations

Descriptive statistics and correlation matrix for economic and health indicators.

Scatter plots showing relationships between GDP per capita, life expectancy, and child mortality.

Heatmap of correlations between variables.

Time series plots for selected countries to show trends in GDP and life expectancy over time.

Interpretation

Results generally show that countries with higher GDP per capita tend to have higher life expectancy
and lower child mortality rates. Increased health expenditure is also associated with better health outcomes.
Some countries with relatively low GDP but high life expectancy demonstrate the impact of effective public health policies.

Author 