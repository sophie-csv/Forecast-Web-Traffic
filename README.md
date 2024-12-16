# Forecast Web Traffic

This project uses Prophet, a forecasting tool developed by Facebook, to implement a basic forecasting model of website traffic. The purpose of this project is to evaluate Meta's Prophet forecasting system. 

# Meta's Prophet
Prophet is a model created by Meta to forecast time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. <br> 

Strengths:
- Automatically takes into account trends, seasonality, and holiday effects.
- User-friendly because of its simplicity.
- Available in many programming languages.

Weaknesses:
- Univariable limitation.
- May oversimplify irregular trends.
- May need to preprocess data to rename columns (see data preparation).

# Setup
Prerequisites:
- Python 3.7+
- Libraries: pandas, numpy, prophet
Installation
Clone this repository or download the script. <br>

Install dependencies: <br>
```pip install pandas numpy prophet```

# Data Preparation

<ins>Columns are renamed for Prophet compatibility (Date → ds, Clicks → y)</ins>.  <br>
- **Date (ds):** The timestamp of traffic data points.
- **Clicks (y):** The number of clicks recorded.
- **Impressions:** (Removed in processing due to the univariable limitation).


# License
This project uses the MIT license. See the LICENSE.md file for more details.


