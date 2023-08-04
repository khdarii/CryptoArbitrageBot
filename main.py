import pandas as pd
import matplotlib.pyplot as plt
import asyncio
from dataclasses import dataclass


@dataclass
class Opportunity:
    timestamp: str
    buy_price: float
    sell_price: float
    volume: float
    profit: float


class CryptoArbitrageBot:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.fee_percentage = 0.02
        self.max_volume = 100

    def calculate_profit(self, buy_price: float, sell_price: float, volume: float) -> float:
        return (sell_price - buy_price) * volume * (1 - self.fee_percentage)

    def calculate_volume(self, available_volume_a: float, available_volume_b: float) -> float:
        return min(self.max_volume, available_volume_a, available_volume_b)

    def add_opportunity(self, opportunities: list[Opportunity], row: tuple) -> None:
        timestamp, price_a, price_b, volume_a, volume_b = row
        if price_a > price_b:
            price_a, price_b = price_b, price_a
        volume = self.calculate_volume(volume_a, volume_b)
        if volume > 0:
            profit = self.calculate_profit(price_a, price_b, volume)
            opportunity = Opportunity(
                timestamp=timestamp,
                buy_price=price_a,
                sell_price=price_b,
                volume=volume,
                profit=profit
            )
            opportunities.append(opportunity)

    async def find_arbitrage_opportunities(self) -> list[Opportunity]:
        opportunities = []

        chunk_size = 1000  # Adjust the chunk size as needed
        for chunk in pd.read_csv(self.data_file, chunksize=chunk_size):
            for row in chunk.itertuples(index=False):
                self.add_opportunity(opportunities, row)

        return opportunities

    @staticmethod
    def visualize_opportunities(opportunities: list[Opportunity]) -> None:
        profits = [opportunity.profit for opportunity in opportunities]
        timestamps = [opportunity.timestamp for opportunity in opportunities]

        plt.figure(figsize=(100, 15))
        plt.bar(timestamps, profits, color='blue')
        plt.xlabel('Timestamp')
        plt.ylabel('Profit')
        plt.title('Arbitrage Profits Over Time')
        plt.xticks(rotation=45)
        plt.show()

    @staticmethod
    def display_summary(opportunities: list[Opportunity]) -> None:
        total_profit = sum(opportunity.profit for opportunity in opportunities)
        total_trades = len(opportunities)

        print("\nSummary:")
        print(f"Total Profit: {total_profit:,.2f}")
        print(f"Total Number of Trades: {total_trades}")

    @staticmethod
    def print_opportunities(opportunities: list[Opportunity]) -> None:
        print("Arbitrage Opportunities:")
        for opportunity in opportunities:
            print(f"Timestamp: {opportunity.timestamp}")
            print(f"Buy Price on Exchange A: {opportunity.buy_price:,.2f}")
            print(f"Sell Price on Exchange B: {opportunity.sell_price:,.2f}")
            print(f"Volume Traded: {opportunity.volume:,.2f}")
            print(f"Profit Made: {opportunity.profit:,.2f}")
            print('-' * 40)


async def main() -> None:
    bot = CryptoArbitrageBot('crypto_prices.csv')  # Replace with your data file path
    opportunities = await bot.find_arbitrage_opportunities()

    bot.print_opportunities(opportunities)
    bot.display_summary(opportunities)
    bot.visualize_opportunities(opportunities)


if __name__ == '__main__':
    asyncio.run(main())
