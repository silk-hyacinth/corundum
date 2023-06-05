from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import pandas as pd
import plotly.express as px
import plotly as pl

class GraphWidget(QWebEngineView):
    def __init__(self, data: list, stock: str):
        print("test2")
        super().__init__()
        self.stock = stock
        self.data = data[1:]
        self.x = []
        self.closes = []
        self.volumes = []
        self.setWindowTitle(stock.upper() + " Data")

    def update_html(self, v=False):
        self.setHtml(self.plot(volume=v))

    def parse_intra(self):
        self.x = [l[0][:10]+"T"+l[0][11:19] for l in self.data]
        self.closes = [float(l[4]) for l in self.data]
        self.volumes = [float(l[5]) for l in self.data]

    def parse_daily(self):
        print(self.data)
        self.x = [l[0] for l in self.data]
        self.closes = [float(l[4]) for l in self.data]
        self.volumes = [float(l[5]) for l in self.data]

    def parse_weekly(self):
        self.x = [l[0] for l in self.data]
        self.closes = [float(l[5]) for l in self.data]
        self.volumes = [float(l[6]) for l in self.data]

    def plot(self, show=False, debug=False, volume=False):
        label = self.stock + " Stock Price"

        d = {
            label: pd   .Series(self.closes, index=self.x),
            # "Volume": pd.Series(self.volumes, index=self.x),
        }
        if volume:
            label = self.stock + "Stock Volume"
            d = {
                label: pd.Series(self.volumes, index=self.x),
                # "Volume": pd.Series(self.volumes, index=self.x),
            }



        df = pd.DataFrame(d, index=tuple(self.x))

        color_discrete_map = {label: 'rgb(255,255,255)'}

        fig = px.line(df, color_discrete_map=color_discrete_map)
        fig.update_layout (
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white',
            title_font_color='white',
        )

        fig.update_xaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='white',
            gridcolor='rgb(127, 127, 127)'
        )
        fig.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='white',
            gridcolor='rgb(127, 127, 127)'
        )

        if debug: print("SBKLSDKGV", self.x, self.closes)

        if show: 
            fig.show()

        #html = fig.write_html('html.html')

        return pl.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        #return html

    # def display()



