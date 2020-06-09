# StocksData
Simple python program to be used from the command line directly to download stocks data.

To use the program, either run the jupyter notebook or save the stocksData.py file in a folder on your computer.

Use a command line to run the program:

`python stockData.py -l AAPL TSLA MSFT True`

The `-l` argument is needed, followed by the name of the stocks separated by space.

The above command will download the data for Apple, Tesla and Microsoft, plot them and save them as a CSV file in the same folder, naming the CSV with the stock titles and the current date in reverse order (YYYY-MM-DD).

The data start on 01/01/2015 until today (today = the day the program is run).

![alt text](https://github.com/alex-rpd/StocksData/blob/master/Figure_1.png)

Changing the last argument to False will avoid plotting the data, same if the argument is omitted. The `True`/`False` plotting argument must be last.

The program requires the `yfinance` package. Install using `pip install yfinance` as per the instructions on the [yfinance](https://pypi.org/project/yfinance/) website.
