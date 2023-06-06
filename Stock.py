# June 4 2023

import requests
import csv, sys, os

class Stock:
    api =""
    def __init__(self, symbol: str, api: str):
        

        self.symbol = symbol.upper()
        self.functions = ["TIME_SERIES_INTRADAY", "TIME_SERIES_DAILY_ADJUSTED", "TIME_SERIES_WEEKLY_ADJUSTED"]
        self.intervals = ["1min", "5min", "15min", "30min", "60min"]
        
        

        try:
            self.api = api.strip().split()[0].upper() # cleans the string a bit.
            if len(self.api) > 5:
                with open(resource_path("api.txt"), 'w') as f:
                    f.write(self.api)
        
        except:
            print("lol")
            pass

        with open(resource_path("api.txt"), 'r') as f:
            Stock.api = f.read()


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
                   "csv" + "&apikey=" + Stock.api
        elif function == 1:
            url = "https://www.alphavantage.co/query?function=" + self.functions[function] + "&symbol=" + self.symbol \
                  + "&outputsize=" + output_size + "&datatype=" + \
                  "csv" + "&apikey=" + Stock.api
        elif function == 3:
            url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv" # testing url
        else:
            url = "https://www.alphavantage.co/query?function=" + self.functions[function] + "&symbol=" + self.symbol \
                  + "&datatype=" + \
                  "csv" + "&apikey=" + Stock.api

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
            with open(resource_path('a.csv'), 'w', newline="") as f:
                f.write(decoded)

        # print("done
        return stock_list



def resource_path(relative):
    #print(os.environ)
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    #print(application_path)
    return os.path.join(application_path, relative)
