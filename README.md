# Finance Analytics Pipeline

End-to-end analytics pipeline built on S&P 500 stock data.

## Stack
- **Ingestion:** Python + yfinance API
- **Storage & Transform:** Apache Spark + Delta Lake (Databricks)
- **Modeling:** dbt Core
- **Analysis:** SQL

## Project Structure
- `ingestion/` — Python scripts to pull data from Yahoo Finance API
- `transformation/` — PySpark transformation logic
- `dbt/` — dbt models (staging → intermediate → marts)
- `analysis/` — analytical SQL queries

## Status
🚧 Work in progress
