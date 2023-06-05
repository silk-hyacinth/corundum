from PySide6.QtWidgets import * # QApplication, QMainWindow, QToolBar, QWidget

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from GraphWidget import GraphWidget
from ui_controller import Ui_Form
from Stock import Stock
from get_symbols_list import GetSymbolsList
from PySide6.QtCore import Qt 

class main_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.function = 1
        self.symbol = ""
        self.interval = 1
        self.exchange = ""
        self.data_amount = ""
        self.volume = False
        self.data = []

        self.symbol_getter = GetSymbolsList()
        self.symbol_list = GetSymbolsList.get_final_list(self.symbol_getter)
        self.completer = QCompleter(self.symbol_list)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.stock_symbol.setCompleter(self.completer)

        self.plot_widget = GraphWidget(self.data, self.symbol.upper())
        #self.plot_widget.update_html(v=self.volume)
        #self.plot_widget.show()

        self.setWindowTitle("Corundum")

       #  widget_layout = QHBoxLayout()
        # controller = Ui_Form()

        # widget_layout.addWidget(controller)


        # stock intervals
        self.daily_button.toggled.connect(lambda: self.set_function(1))
        self.intraday_button.toggled.connect(lambda: self.set_function(0))
        self.weekly_button.toggled.connect(lambda: self.set_function(2))
        
        # day intervals
        self.one_min_button.toggled.connect(lambda: self.set_day_interval(0))
        self.five_min_button.toggled.connect(lambda: self.set_day_interval(1))
        self.fifteen_minute_button.toggled.connect(lambda: self.set_day_interval(2))
        self.thirty_minute_button.toggled.connect(lambda: self.set_day_interval(3))
        self.sixty_minute_button.toggled.connect(lambda: self.set_day_interval(4))

        # data amounts 
        self.output_full.toggled.connect(lambda: self.set_data_amount("full"))
        self.output_compact.toggled.connect(lambda: self.set_data_amount("compact"))

        # text fields

        # self.stock_symbol.editingFinished.connect(self.set_symbol)
        # self.exchange_name.editingFinished.connect(self.set_exchange)

        # volume vs stock
        
        self.show_volume.toggled.connect(self.set_volume)


        self.go_button.pressed.connect(self.plot)

        # widget_layout.addWidget(self.plot_widget)

        # self.setLayout(widget_layout)

        

    def plot(self):
        self.symbol = self.clean_symbol(self.stock_symbol.text())
        self.exchange = self.exchange_name.text()

        try:
            self.stock = Stock(self.symbol)
            self.data = self.stock.get_stock_data(function=self.function, interval=self.interval, output_size=self.data_amount)
        except:
            raise AssertionError ("Retrieving Data Failed")
        
        self.plot_widget = GraphWidget(self.data, self.symbol.upper())
        
        if self.function == 0:
            self.plot_widget.parse_intra()
        elif self.function == 1:
            self.plot_widget.parse_daily()
        else:
            self.plot_widget.parse_weekly()


        # self.update()
        self.plot_widget.update_html(v=self.volume)
        self.plot_widget.show()

    def clean_symbol(self, symbol):
        final = ""
        for char in symbol:
            if char != " ":
                final += char
            else:
                break
        return final

    def set_function(self, function):
        self.function = function

    def set_day_interval(self, day_interval):
        self.interval = day_interval

    def set_data_amount(self, data_amount):
        self.data_amount = data_amount

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_exchange(self, exchange):
        self.exchange = exchange

    def set_volume(self, volume):
        self.volume = volume
    
    
    def function(self):
        return self.function
    
    
    def interval(self):
        return self.interval
    
    
    def symbol(self):
        return self.symbol
    
    
    def data_amount(self):
        return self.data_amount
    
    
    def exchange(self):
        return self.exchange

    

