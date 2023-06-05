import csv

# TODO: add NASDAQ

class GetSymbolsList:
    def __init__(self) -> None:
        self.files = ["symbols/nyse_symbols.csv", "symbols/nasdaq_symbols.csv"]
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





if __name__ == "__main__":
    a = GetSymbolsList()
    print(a.to_strings(a.parse(a.files[0])))
    

