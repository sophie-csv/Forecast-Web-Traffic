
import pandas as pd
from prophet import Prophet
import numpy as np

!pip install prophet

df = pd.read_csv('/content/web-search-traffic-16mos.csv')
df.head()

df.describe()

df = df.rename(columns={'Date': 'ds', 'Clicks': 'y'})
df['ds'] = pd.to_datetime(df['ds'])df.drop("Impressions", axis=1)

# Calculate the 95th percentile threshold for Clicks (now 'y')
threshold = np.quantile(df['y'], 0.95)

# Detect spikes and create a new column 'IsSpike'
df['IsSpike'] = df['y'] > threshold

# Filter the rows where spikes are detected
spikes = df[df['IsSpike']]

holidays['holiday'] = "Spike"  # Assign a name for the holiday

# Assign custom lower and upper windows
holidays['lower_window'] = 0  # Start from the spike day
holidays['upper_window'] = holidays['ds'].apply(
    lambda x: 2 if x in pd.to_datetime(["2023-11-07", "2024-11-05"]) else 1
)

# Display the top 10 spikes
print("\nTop 10 Spikes:")
print(spikes.nlargest(10, 'y'))

model = Prophet(
    daily_seasonality=False,
    yearly_seasonality=True,
    weekly_seasonality=True,
    holidays=holidays
)

model.fit(df)

# Create future dataframe for forecasting
future = model.make_future_dataframe(periods=365)

# Predict the future values
forecast = model.predict(future)


# Plot the forecast
fig1 = model.plot(forecast)
fig2 = model.plot_components(forecast)
