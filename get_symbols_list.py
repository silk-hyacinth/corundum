import csv, sys, os

# TODO: add NASDAQ

class GetSymbolsList:
    def __init__(self) -> None:
        self.files = [resource_path("symbols/nyse_symbols.csv"), resource_path("symbols/nasdaq_symbols.csv")]
        # self.files = [":/symbols/amex_symbols.csv", ":/symbols/nyse_symbols.csv", ":/symbols/amex_symbols.csv"]

    def parse(self, f: str):
        with open(f) as file:
            cr = csv.reader(file, delimiter=",")
            symbol_list = list(cr)

        return symbol_list
    
    def to_strings(self, parsed_list):
        '''
        so it will return the [EXCHANGE, [[AA, ALCOA][AACM, AAC]]]
        '''
        wanted = [l[0] + " (" + l[1] + ")" for l in parsed_list[1:]]
        return wanted
    
    def get_final_list(self):
        temp = []
        for file in self.files:
            temp += self.parse(file)
        return self.to_strings(temp)
    
    

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



if __name__ == "__main__":
    a = GetSymbolsList()
    print(a.to_strings(a.parse(a.files[0])))
    

