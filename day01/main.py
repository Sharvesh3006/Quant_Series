import pandas as pd
import yfinance as yf
ticker = "SPY"
data = yf.download(ticker,period="1mo",interval="1d",auto_adjust=True)
print(data)
'''print('\nDataset shape')
print(data.shape)
print('\nDataset Information')
print(data.info())
print('\nMissing Values:')
print(data.isna().sum())
print('\nDuplicate Dates')
print(data.index.duplicated().sum())'''
high=data[("High","SPY")]
low=data[("Low","SPY")]
open_price=data[("Open","SPY")]
close = data[("Close","SPY")]

'''print("\nOHLC Validation")

print("High>=Open",(high>=open_price).all())
print("High>=Close",(high>=close).all())
print("Low<=Open:",(low<=open_price).all())
print("Low<=Close",(low<=close).all())'''

'''print("\nNon-Positive values")
print("Prices <= 0:")
print((data[
       [("Open","SPY"),("High","SPY"),("Low","SPY"),("Close","SPY")] 
        ] <=0).sum()
)
print("\nVolume <=0:")
print((data[("Volume","SPY")]<=0).sum())'''

#clean column structure
data.columns = data.columns.get_level_values(0)
data.columns.name = None
#print('\nCleaned Columns:')
#print(data.columns)
#print('\nCleaned Dataset:')
#print(data.head())
""" data = data[["Open","High","Low","Close","Volume"]]
print("\nFinal Columns:")
print(data.columns)
print(data.head()) """

#calculating the simple returns
data["Daily_Return"] = data["Close"].pct_change()
print("\nDaily Returns:\n")
print(data[["Close","Daily_Return"]])

print("Return Summary:\n")
print(data["Daily_Return"].describe())

