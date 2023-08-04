import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Generate fictional price data for Exchange A and Exchange B
def generate_price_data(start_date, end_date, interval, price_range, volume_range):
    timestamps = pd.date_range(start=start_date, end=end_date, freq=interval)
    prices_a = np.random.uniform(price_range[0], price_range[1], len(timestamps))
    prices_b = np.random.uniform(price_range[0], price_range[1], len(timestamps))
    volumes_a = np.random.randint(volume_range[0], volume_range[1], len(timestamps))
    volumes_b = np.random.randint(volume_range[0], volume_range[1], len(timestamps))

    data = {
        'Timestamp': timestamps,
        'Price_A': prices_a,
        'Price_B': prices_b,
        'Volume_A': volumes_a,
        'Volume_B': volumes_b
    }

    return pd.DataFrame(data)


# Define parameters
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 31)
interval = '1H'  # Hourly interval
price_range = (30000, 35000)  # Price range for BTC
volume_range = (10, 1000)  # Volume range

# Generate price data and save to CSV
price_data = generate_price_data(start_date, end_date, interval, price_range, volume_range)
price_data.to_csv('crypto_prices.csv', index=False)

print("Fictional price data generated and saved to 'crypto_prices.csv'.")
