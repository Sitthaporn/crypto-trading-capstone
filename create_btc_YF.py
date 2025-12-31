import yfinance as yf

df = yf.download(
    tickers='BTC-USD',
    period= '360d',
    interval='4h'
)
print(df.head())
df.to_csv("btc_4h_price.csv")