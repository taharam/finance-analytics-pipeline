import yfinance as yf
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "META",
           "NVDA", "JPM", "V", "JNJ", "XOM"]

START_DATE = "2023-01-01"
END_DATE   = "2025-01-01"

def fetch_prices(tickers, start, end):
    all_dfs = []
    for ticker in tickers:
        try:
            logger.info(f"Fetching {ticker}...")
            df = yf.download(ticker, start=start, end=end, auto_adjust=True)

            if isinstance(df.columns, pd.MultiIndex):
                df.columns = [col[0].lower() for col in df.columns]
            else:
                df.columns = [col.lower() for col in df.columns]

            df["ticker"]      = ticker
            df["ingested_at"] = datetime.utcnow()
            all_dfs.append(df)

        except Exception as e:
            logger.error(f"Failed to fetch {ticker}: {e}")

    return pd.concat(all_dfs)


if __name__ == "__main__":
    raw_df = fetch_prices(TICKERS, START_DATE, END_DATE)
    raw_df = raw_df.reset_index()
    raw_df.columns = [col.lower().replace(" ", "_") for col in raw_df.columns]
    print(f"Rows fetched: {len(raw_df)}")
    print(raw_df.head())