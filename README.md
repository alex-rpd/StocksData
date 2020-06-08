# StocksData
Simple python program to be used from the command line directly to download stocks data.

To use the program, save the stocksData.py file in a folder on your computer.

Use a command line to run the program:

`python stockData.py -l AAPL TSLA MSFT True`

will download the data for Apple, Tesla, Microsoft, plot them and save them as a CSV file in the same folder, naming the CSV with the stock titles.

Changing the last argument to False will avoid plotting the data, same if it is omitted. The plotting argument must be last.

The program requires the `yfinance` package. Install using `pip install yfinance` as per the instructions on the `yfinance` website.
