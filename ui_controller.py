# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controller.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(382, 643)
        Form.setStyleSheet(u"background-color:rgb(168, 167, 167);\n"
"color:rgb(71, 71, 71);\n"
"font: 700 8pt \"Segoe UI\";")
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"font: 700 26pt \"Wingdings\";\n"
"color: rgb(232, 23, 93);")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.title_label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:rgb(204, 82, 122)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.symbol_label = QLabel(Form)
        self.symbol_label.setObjectName(u"symbol_label")
        self.symbol_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.symbol_label)

        self.stock_symbol = QLineEdit(Form)
        self.stock_symbol.setObjectName(u"stock_symbol")
        self.stock_symbol.setStyleSheet(u"border: 2px solid white;")

        self.verticalLayout_5.addWidget(self.stock_symbol)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.exchange_name = QLineEdit(Form)
        self.exchange_name.setObjectName(u"exchange_name")
        self.exchange_name.setStyleSheet(u"border: 2px solid white;")

        self.verticalLayout_5.addWidget(self.exchange_name)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.api_line_edit = QLineEdit(Form)
        self.api_line_edit.setObjectName(u"api_line_edit")
        self.api_line_edit.setStyleSheet(u"border: 2px solid white;")

        self.verticalLayout_5.addWidget(self.api_line_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stock_interval_label = QLabel(Form)
        self.stock_interval_label.setObjectName(u"stock_interval_label")
        self.stock_interval_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stock_interval_label)

        self.intraday_button = QRadioButton(Form)
        self.stock_interval = QButtonGroup(Form)
        self.stock_interval.setObjectName(u"stock_interval")
        self.stock_interval.addButton(self.intraday_button)
        self.intraday_button.setObjectName(u"intraday_button")
        self.intraday_button.setStyleSheet(u"QRadioButton {\n"
"	color:rgb(204, 82, 122);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(204, 82, 122);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_checked.svg);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.intraday_button)

        self.daily_button = QRadioButton(Form)
        self.stock_interval.addButton(self.daily_button)
        self.daily_button.setObjectName(u"daily_button")
        self.daily_button.setLayoutDirection(Qt.LeftToRight)
        self.daily_button.setStyleSheet(u"QRadioButton {\n"
"	color:rgb(204, 82, 122);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(204, 82, 122);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_checked.svg);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.daily_button)

        self.weekly_button = QRadioButton(Form)
        self.stock_interval.addButton(self.weekly_button)
        self.weekly_button.setObjectName(u"weekly_button")
        self.weekly_button.setStyleSheet(u"QRadioButton {\n"
"	color:rgb(204, 82, 122);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(204, 82, 122);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_checked.svg);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.weekly_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.day_interval_label = QLabel(Form)
        self.day_interval_label.setObjectName(u"day_interval_label")
        self.day_interval_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.day_interval_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.one_min_button = QRadioButton(Form)
        self.intraday_interval = QButtonGroup(Form)
        self.intraday_interval.setObjectName(u"intraday_interval")
        self.intraday_interval.addButton(self.one_min_button)
        self.one_min_button.setObjectName(u"one_min_button")
        self.one_min_button.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(160, 112, 255);\n"
"	border-radius:5px;\n"
"	padding: 10px 18px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(160, 112, 255);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_purple.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/checked_radio_purple.svg);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.one_min_button)

        self.five_min_button = QRadioButton(Form)
        self.intraday_interval.addButton(self.five_min_button)
        self.five_min_button.setObjectName(u"five_min_button")
        self.five_min_button.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(160, 112, 255);\n"
"	border-radius:5px;\n"
"	padding: 10px 18px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(160, 112, 255);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_purple.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/checked_radio_purple.svg);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.five_min_button)

        self.fifteen_minute_button = QRadioButton(Form)
        self.intraday_interval.addButton(self.fifteen_minute_button)
        self.fifteen_minute_button.setObjectName(u"fifteen_minute_button")
        self.fifteen_minute_button.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(160, 112, 255);\n"
"	border-radius:5px;\n"
"	padding: 10px 18px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(160, 112, 255);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_purple.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/checked_radio_purple.svg);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.fifteen_minute_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thirty_minute_button = QRadioButton(Form)
        self.intraday_interval.addButton(self.thirty_minute_button)
        self.thirty_minute_button.setObjectName(u"thirty_minute_button")
        self.thirty_minute_button.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(160, 112, 255);\n"
"	border-radius:5px;\n"
"	padding: 10px 18px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(160, 112, 255);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_purple.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/checked_radio_purple.svg);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.thirty_minute_button)

        self.sixty_minute_button = QRadioButton(Form)
        self.intraday_interval.addButton(self.sixty_minute_button)
        self.sixty_minute_button.setObjectName(u"sixty_minute_button")
        self.sixty_minute_button.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(160, 112, 255);\n"
"	border-radius:5px;\n"
"	padding: 10px 18px;\n"
"	font-size:14px;\n"
"	border: 2px solid rgb(160, 112, 255);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_purple.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/checked_radio_purple.svg);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.sixty_minute_button)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.data_amount_label = QLabel(Form)
        self.data_amount_label.setObjectName(u"data_amount_label")
        self.data_amount_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.data_amount_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_full = QRadioButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.output_full)
        self.output_full.setObjectName(u"output_full")
        self.output_full.setStyleSheet(u"QRadioButton {\n"
"	\n"
"	color: rgb(66, 85, 206);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid  rgb(66, 85, 206);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_blue_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_blue.svg);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.output_full)

        self.output_compact = QRadioButton(Form)
        self.buttonGroup.addButton(self.output_compact)
        self.output_compact.setObjectName(u"output_compact")
        self.output_compact.setStyleSheet(u"QRadioButton {\n"
"	\n"
"	color: rgb(66, 85, 206);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid  rgb(66, 85, 206);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_blue_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_blue.svg);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.output_compact)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.one_more_thing = QLabel(Form)
        self.one_more_thing.setObjectName(u"one_more_thing")
        self.one_more_thing.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.one_more_thing)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.show_stock = QRadioButton(Form)
        self.show_stock.setObjectName(u"show_stock")
        self.show_stock.setStyleSheet(u"QRadioButton {\n"
"	\n"
"	color: rgb(66, 85, 206);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid  rgb(66, 85, 206);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_blue_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_blue.svg);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.show_stock)

        self.show_volume = QRadioButton(Form)
        self.show_volume.setObjectName(u"show_volume")
        self.show_volume.setStyleSheet(u"QRadioButton {\n"
"	\n"
"	color: rgb(66, 85, 206);\n"
"	border-radius:5px;\n"
"	padding: 10px 39px;\n"
"	font-size:14px;\n"
"	border: 2px solid  rgb(66, 85, 206);\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio/radio_blue_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio/radio_blue.svg);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.show_volume)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.go_button = QPushButton(Form)
        self.go_button.setObjectName(u"go_button")
        self.go_button.setStyleSheet(u"border: 2px solid;\n"
"padding: 5px 5px;\n"
"rounding:5px")

        self.verticalLayout_5.addWidget(self.go_button)

        self.plot_widget = QWidget(Form)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout_5.addWidget(self.plot_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"corundum.", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"A Stock Viewer", None))
        self.symbol_label.setText(QCoreApplication.translate("Form", u"Ticker Symbol", None))
        self.stock_symbol.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Exchange Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"AlphaVantage API Key (see README file)", None))
        self.stock_interval_label.setText(QCoreApplication.translate("Form", u"Stock Interval", None))
        self.intraday_button.setText(QCoreApplication.translate("Form", u"Intraday", None))
        self.daily_button.setText(QCoreApplication.translate("Form", u"Daily", None))
        self.weekly_button.setText(QCoreApplication.translate("Form", u"Weekly", None))
        self.day_interval_label.setText(QCoreApplication.translate("Form", u"Intraday Interval (Minutes)", None))
        self.one_min_button.setText(QCoreApplication.translate("Form", u"1", None))
        self.five_min_button.setText(QCoreApplication.translate("Form", u"5", None))
        self.fifteen_minute_button.setText(QCoreApplication.translate("Form", u"15", None))
        self.thirty_minute_button.setText(QCoreApplication.translate("Form", u"30", None))
        self.sixty_minute_button.setText(QCoreApplication.translate("Form", u"60", None))
        self.data_amount_label.setText(QCoreApplication.translate("Form", u"Data Amount", None))
        self.output_full.setText(QCoreApplication.translate("Form", u"Full", None))
        self.output_compact.setText(QCoreApplication.translate("Form", u"Compact", None))
        self.one_more_thing.setText(QCoreApplication.translate("Form", u"Show:", None))
        self.show_stock.setText(QCoreApplication.translate("Form", u"Price", None))
        self.show_volume.setText(QCoreApplication.translate("Form", u"Volume", None))
        self.go_button.setText(QCoreApplication.translate("Form", u"Go", None))
    # retranslateUi

