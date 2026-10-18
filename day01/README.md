
# Day 01 — Quant Market Data Ingestion

## Objective
Build a Python pipeline to download, validate, and normalize historical market data.

## Dataset
- Asset: SPY
- Source: Yahoo Finance via yfinance
- Frequency: Daily
- Fields: Open, High, Low, Close, Volume

## Implemented
- Download market data
- Inspect dataset shape and information
- Check missing values and duplicate dates
- Validate OHLC consistency
- Check for non-positive prices and volume
- Flatten MultiIndex columns
- Standardize OHLCV column order

## Validation Results
- Missing values: 0 in the inspected dataset
- Duplicate dates: 0 in the inspected dataset
- OHLC checks: Passed
- Non-positive prices: 0
- Non-positive volume observations: 0

## Limitations
- Historical daily data, not a live streaming feed
- Yahoo Finance is the data provider
- Validation does not guarantee source-data accuracy


