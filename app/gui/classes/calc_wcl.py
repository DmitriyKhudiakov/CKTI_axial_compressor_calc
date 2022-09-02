#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QGridLayout, QScrollArea, QVBoxLayout, QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app.gui.classes.calc_description import CalcDescription
from app.gui.classes.calc_part import CalcPart


class CalcWin(QWidget):
    def __init__(self, calc_name):
        super().__init__()
        self.title = calc_name
        self.main_grid_layout = QGridLayout(self)
        self.main_scroll_area = QScrollArea(self)
        self.main_scroll_area_widget_contents = QWidget()
        self.main_vertical_layout = QVBoxLayout(self.main_scroll_area_widget_contents)
        self.main_splitter = QSplitter(self.main_scroll_area_widget_contents)
        self.main_splitter.setHandleWidth(20)
        self.calc_desc_list = []
        self.calc_part_list = []
        self.calc_name = calc_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("app\\gui\\source\\images\\simple_icon.png"))
        self.main_scroll_area.setWidgetResizable(True)
        self.main_splitter.setOrientation(Qt.Vertical)
        self.main_splitter.setMinimumHeight(4700)
        self.init_start_group_box_model()
        self.init_calc_part_group_box_model()
        self.main_vertical_layout.addWidget(self.main_splitter)
        self.main_scroll_area.setWidget(self.main_scroll_area_widget_contents)
        self.main_grid_layout.addWidget(self.main_scroll_area, 0, 0, 1, 1)
        self.show()

    def init_start_group_box_model(self):
        self.calc_desc_list.append(CalcDescription(self.main_splitter, self.calc_name))

    def init_calc_part_group_box_model(self):
        self.calc_part_list.append((CalcPart(self.main_splitter, self.calc_name,
                                             "Вариантный расчет лопаточного аппарата", 1)))
        self.calc_part_list.append((CalcPart(self.main_splitter, self.calc_name,
                                             "Первый поступенчатый расчет", 2)))
        self.calc_part_list.append((CalcPart(self.main_splitter, self.calc_name,
                                             "Второй поступенчатый расчет", 3)))
        self.calc_part_list.append((CalcPart(self.main_splitter, self.calc_name,
                                             "Определение статических давлений и статических температур в лопаточном "
                                             "аппарате", 4)))
        self.calc_part_list[0].calc_setup.calc_part2 = self.calc_part_list[1]
        self.calc_part_list[1].calc_setup.calc_part3 = self.calc_part_list[2]
        self.calc_part_list[2].calc_setup.calc_part4 = self.calc_part_list[3]

    def close_part(self):
        for curr_part in self.calc_part_list:
            curr_part.close_part()

    def closeEvent(self, event):
        self.close_part()
