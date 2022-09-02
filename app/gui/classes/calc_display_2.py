from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QScrollArea, QWidget, QTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
import app.calc.axial_compressor.display.get_display_2 as gd


MIN_WIDTH = 200
MIN_HEIGHT = 100


class CalcDisplay2:
    def __init__(self, parent_splitter, calc_name):
        self.calc_name = calc_name
        self.group_box_disc = QGroupBox(parent_splitter)
        self.group_box_disc.setTitle("Результаты")
        self.vertical_layout_disc = QVBoxLayout(self.group_box_disc)
        self.scroll_area_disc = QScrollArea(self.group_box_disc)
        self.scroll_area_disc.setWidgetResizable(True)
        self.scroll_area_disc_inside = QWidget()
        self.vertical_layout_disc_inside = QVBoxLayout(self.scroll_area_disc_inside)
        # self.add_disc_data(self.add_disc_list_save)
        ########################
        self.get_display = gd
        self.te = QTextEdit()
        self.init_display_data()
        ########################
        self.anim_list = []
        self.c_val_list = []
        self.plots_list = []
        self.cb_list = []
        self.a_list = []
        ##########################
        self.scroll_area_disc.setWidget(self.scroll_area_disc_inside)
        self.vertical_layout_disc.addWidget(self.scroll_area_disc)

    def init_display_data(self):
        self.te.setMinimumSize(QSize(MIN_WIDTH, MIN_HEIGHT))
        self.te.setReadOnly(True)
        self.te.setStyleSheet("background-color: #F0F0F0")
        self.te.setHtml("")
        self.te.toHtml()
        self.vertical_layout_disc_inside.addWidget(self.te)
        #####################

    def change_anim_title(self, state):
        if state == Qt.Checked:
            for i in self.anim_list:
                i.start()
        else:
            for i in self.anim_list:
                i.pause()

    def desc_list_res(self, desc_elem_dict, f):
        for key, value in desc_elem_dict.items():
            if key == "html":
                self.te.setHtml(self.get_display.get_display(self.calc_name, f, value))
                self.te.setMinimumHeight(600)

    def show_res(self, f, desc_elem_dict):
        self.desc_list_res(desc_elem_dict, f)
        self.te.setMinimumHeight(600)
        self.te.setMinimumWidth(1400)

    def get_html_data_file(self, f, desc_elem_dict, is_empty):
        for key, value in desc_elem_dict.items():
            if key == "html":
                return self.get_display.get_data(self.calc_name, f, value, is_empty)
