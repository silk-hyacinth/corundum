
import sys, csv
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from Stock import Stock
from GraphWidget import GraphWidget
from main_window import main_window

app = QApplication(sys.argv)

window = main_window()

window.show()

app.exec()


#window = QMainWindow()

#IBM = Stock("ibm")
#data = IBM.get_stock_data(function=3, output_size="compact")

# print("DATA: "+str(data))

#grapher = GraphWidget(data)
#grapher.parse_intra()
#grapher.plot(show=True)

#plotWidget = GraphWidget(data)
#plotWidget.parse_intra()

#html = '<html><body>'
# html = plotWidget.plot()
#html += '</body></html>'

#plotWidget.update_html()

#plotWidget.update_html()

#window.setCentralWidget(plotWidget)




#controller = main_window()



#try:
#    stock = Stock(controller.symbol)
#    data = stock.get_stock_data(function=controller.function, interval=controller.interval, output_size=controller.data_amount)
#except:
#    raise AssertionError ("Retrieving Data Failed")
#
#plot_widget = GraphWidget(data)
#
#if controller.function == 0:
#    plot_widget.parse_intra()
#elif controller.function == 1:
#    plot_widget.parse_daily()
#else:
#    plot_widget.parse_weekly()
#
#plot_widget.update_html()
#
#layout = QVBoxLayout()
#layout.addWidget(controller)
#layout.addWidget(plot_widget)
#window.setLayout(layout)

#window.show()

# window.show()



#with open('a.csv', 'w', newline='') as f:
#    writer = csv.writer(f, delimiter=",")
#    cr = csv.reader(open("daily_adjusted_IBM.csv"), delimiter=",")
#    writer.writerows(cr)