# Forecast-Web-Traffic

This project uses Prophet, a forecasting tool developed by Facebook, to implement a basic forecasting model of website traffic. The purpose of this project is to evaluate Meta's Prophet forecasting system.

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
- **Impressions:** (Removed in processing).

# License
This project uses the MIT license. See the LICENSE.md file for more details.


