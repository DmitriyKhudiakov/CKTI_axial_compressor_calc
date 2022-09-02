#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon
from app.gui.classes import calc_wcl as cw
import sys
import pathlib


class StartWin(QWidget):
    def __init__(self, calc_list, app):
        super().__init__()
        self.app = app
        self.title = "Calc manager"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 100
        self.calc_list = calc_list
        self.v_box = QVBoxLayout()
        self.combo = QComboBox(self)
        self.init_ui()
        self.calc_wins = []

    def init_ui(self):
        self.setStyleSheet("background-color: qradialgradient(cx:0.5, cy:0.5, radius: 0.9, fx:0.5, fy:0.5, "
                           "stop:0 #FFFFFF, stop:1 #CACACA);")
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("app\\gui\\source\\images\\simple_icon.png"))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.init_box()
        self.init_open_btn()
        # self.init_quit_btn()
        self.setLayout(self.v_box)
        self.show()

    def init_quit_btn(self):
        quit_button = QPushButton("Quit", self)
        # quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.clicked.connect(self.closeEvent)
        quit_button.resize(quit_button.sizeHint())
        self.v_box.addWidget(quit_button)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Также закроются все открытые окна расчетов",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            path = str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\id.csv"
            with open(path, "w+", encoding='utf-8') as file_write:
                file_write.write("")
            file_write.close()
            sys.exit(self.app.exec_())
        else:
            event.ignore()

    def init_open_btn(self):
        open_button = QPushButton("Открыть", self)
        open_button.clicked.connect(self.open_btn_on_click)
        open_button.resize(open_button.sizeHint())
        self.v_box.addWidget(open_button)

    def init_box(self):
        for curr_calc in self.calc_list[0]:
            self.combo.addItem(curr_calc)
        self.v_box.addWidget(self.combo)

    def open_btn_on_click(self):
        self.calc_wins.append(cw.CalcWin(str(self.combo.currentText())))
        self.calc_wins[-1].setGeometry(300, 100, 1000, 800)
        self.calc_wins[-1].showMaximized()
