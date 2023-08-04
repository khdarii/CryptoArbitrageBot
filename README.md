# Crypto Arbitrage Bot Simulation

This project simulates a crypto arbitrage trading strategy between multiple fictional exchanges. It generates a CSV file with price and volume data for different cryptocurrency pairs and exchanges, identifies arbitrage opportunities, and provides a summary of profits made.

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- numpy
- matplotlib

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot
```

2. Generate fictional price data CSV file:

```bash
python generate_data.py
```

3. Run the Crypto Arbitrage Bot simulation:

```bash
python crypto_arbitrage_bot.py
```

## Features

- Generates fictional price data cryptocurrency pairs.
- Identifies arbitrage opportunities based on price differences and trading volume.
- Displays the details of each arbitrage opportunity.
- Provides a summary of total profit made and total number of trades executed.
- Plots cryptocurrency prices over time and highlights arbitrage opportunities.

## Streaming Approach
This project utilizes a streaming approach to efficiently read large CSV files without loading the entire file into memory.
The `find_arbitrage_opportunities` method in the `CryptoArbitrageBot` class reads the CSV file in chunks, processing each chunk to identify arbitrage opportunities.
This allows for processing even very large CSV files without consuming excessive memory.

## Customization

You can customize the following parameters in the `generate_data.py` script:

- `start_date`: The start date for generating price data.
- `end_date`: The end date for generating price data.
- `interval`: The time interval between data points.
- `price_range`: The range of fictional prices for cryptocurrencies.
- `volume_range`: The range of fictional trading volumes.


## Acknowledgments

- This project is for educational purposes and demonstrates a simplified crypto arbitrage trading simulation.
