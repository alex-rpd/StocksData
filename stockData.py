import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf
import argparse


style.use('ggplot')

parser = argparse.ArgumentParser(description='')

parser.add_argument(
    '-l',
    '--stockList',
    nargs='+',
    help='<Required> Set flag',
    required=True)

args = parser.parse_args()

if args.stockList[-1] == 'True':
    stocks = args.stockList[:-1]
    plot = True
elif args.stockList[-1] == 'False':
    stocks = args.stockList[:-1]
    plot = False
else:
    stocks = args.stockList
    plot = False

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()


df = yf.download(stocks,
                 start=start,
                 end=end,
                 progress=True)

df.to_csv(f"Stocks_{'-'.join(stocks)}_{dt.date.today()}.csv")
print(f'File with {stocks} stock data saved.')

if plot:
    if len(stocks) == 1:
        plt.plot(df.index, df['Adj Close'], label=stocks[0])
        plt.legend(frameon=False)
        plt.xlabel('Date')
        plt.ylabel('Adj Close price ($)')
        plt.show()

    else:
        for stock in stocks:
            plt.plot(df.index, df['Adj Close'][stock], label=stock)

        plt.legend(frameon=False)
        plt.xlabel('Date')
        plt.ylabel('Adj Close price ($)')
        plt.show()
