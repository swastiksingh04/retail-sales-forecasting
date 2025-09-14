"""
Retail Sales Forecasting - Entry Script

This script demonstrates a quick preview of the processed sales data.
Full analysis, modeling (ARIMA & Prophet), and forecasting can be found
in the Jupyter notebooks inside the /notebooks directory.
"""

import pandas as pd
from pathlib import Path

# Path to processed daily sales data
data_path = Path("data/processed/sales_daily.csv")

def main():
    if data_path.exists():
        sales_daily = pd.read_csv(data_path, parse_dates=["order_date"], index_col="order_date")
        print("Loaded processed daily sales data.")
        print(f"Shape: {sales_daily.shape}")
        print("Preview:")
        print(sales_daily.head())
    else:
        print("Processed sales data not found. Please run preprocessing notebooks first.")

    print("\nFor detailed analysis and forecasting, check the notebooks/ directory.")

if __name__ == "__main__":
    main()
