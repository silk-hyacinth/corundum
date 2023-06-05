# @author Ben W

import requests
import csv

api = "enter api key here"

class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.functions = ["TIME_SERIES_INTRADAY", "TIME_SERIES_DAILY_ADJUSTED", "TIME_SERIES_WEEKLY_ADJUSTED"]
        self.intervals = ["1min", "5min", "15min", "30min", "60min"]

    def get_stock_data(self, function=1, interval=1, output_size="full", exchange=""):
        '''

        :param function: 0 = intraday, 1 = daily
        :param interval: 0=1min 1=5min 2=15min 3=30min 4=60min
        :param output_size: "full" or "compact"
        :param datatype: only csv. this parameter does not exist.
        :return:
        '''



        if function == 0:
            url = "https://www.alphavantage.co/query?function=" + self.functions[function] + "&symbol=" + self.symbol \
                   + "&interval=" + self.intervals[interval] + "&outputsize=" + output_size + "&datatype=" + \
                   "csv" + "&apikey=" + api
        elif function == 1:
            url = "https://www.alphavantage.co/query?function=" + self.functions[function] + "&symbol=" + self.symbol \
                  + "&outputsize=" + output_size + "&datatype=" + \
                  "csv" + "&apikey=" + api
        elif function == 3:
            url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv" # testing url
        else:
            url = "https://www.alphavantage.co/query?function=" + self.functions[function] + "&symbol=" + self.symbol \
                  + "&datatype=" + \
                  "csv" + "&apikey=" + api

        # (testing url) url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo"
        print(url)


        with requests.Session() as s:
            r = s.get(url)
            decoded = r.content.decode('utf-8')
            cr = csv.reader(decoded.splitlines(), delimiter=",")
            stock_list = list(cr)

            for row in stock_list:
                print(row)

            #cache
            with open('a.csv', 'w', newline="") as f:
                f.write(decoded)

        # print("done
        return stock_list



