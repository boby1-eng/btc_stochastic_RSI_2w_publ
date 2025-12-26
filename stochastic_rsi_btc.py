import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get Bitcoin data for the last 2 years
btc_data = yf.download('BTC-USD', period='2y', interval='1d')

# Calculate Stochastic RSI
def stochastic_rsi(data, window=14):
    # Calculate RSI
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    # Stochastic RSI
    stoch_rsi = (rsi - rsi.rolling(window=window, min_periods=1).min()) / (rsi.rolling(window=window, min_periods=1).max() - rsi.rolling(window=window, min_periods=1).min())
    
    return stoch_rsi

# Compute Stochastic RSI for the data
btc_data['Stochastic RSI'] = stochastic_rsi(btc_data)

# Set plot figure and axes
plt.figure(figsize=(14, 7))

# Plot Stochastic RSI
plt.plot(btc_data.index, btc_data['Stochastic RSI'], label="Stochastic RSI", color='blue', lw=1.5)

# Plot 80 and 20 levels (Overbought and Oversold levels)
plt.axhline(y=0.8, color='red', linestyle='--', label="Overbought (80%)")
plt.axhline(y=0.2, color='red', linestyle='--', label="Oversold (20%)")

# Formatting plot
plt.title("2-Year Stochastic RSI for Bitcoin (BTC-USD)")
plt.xlabel("Date")
plt.ylabel("Stochastic RSI")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

# Display plot
plt.tight_layout()
plt.show()
