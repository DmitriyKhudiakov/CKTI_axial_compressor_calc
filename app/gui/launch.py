#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from app.gui.classes import start_wcl as sw

from PyQt5.QtWidgets import QApplication


def launch(calc_list):
    app = QApplication(sys.argv)
    app.setStyleSheet('''
            QSplitter::handle {background: qradialgradient(cx:0.5, cy:0.5, radius: 0.2, fx:0.5, fy:0.5, stop:0 #64BCAD, 
            stop:1 #F0F0F0)  }
            ''')
    start_win = sw.StartWin(calc_list, app)
    sys.exit(app.exec_())
