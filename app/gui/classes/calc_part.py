from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QScrollArea, QWidget, QSplitter
from PyQt5.QtCore import Qt
from app.gui.classes.calc_setup import CalcSetup
from app.gui.classes.calc_display import CalcDisplay
from app.gui.classes.calc_setup_2 import CalcSetup2
from app.gui.classes.calc_display_2 import CalcDisplay2
from app.gui.classes.calc_setup_3 import CalcSetup3
from app.gui.classes.calc_display_3 import CalcDisplay3
from app.gui.classes.calc_setup_4 import CalcSetup4
from app.gui.classes.calc_display_4 import CalcDisplay4


class CalcPart:
    def __init__(self, parent_splitter, calc_name, part_name, n_box):
        # self.calc_module = calc_module
        self.group_box = QGroupBox(parent_splitter)
        # self.group_box.setBaseSize(QSize(800, 800))
        self.group_box.setTitle(part_name)
        self.vertical_layout = QVBoxLayout(self.group_box)
        self.scroll_area = QScrollArea(self.group_box)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_calc_and_disc = QWidget()
        self.vertical_layout_calc_and_disc = QVBoxLayout(self.scroll_area_calc_and_disc)
        self.splitter_calc_and_disc = QSplitter(self.scroll_area_calc_and_disc)
        self.splitter_calc_and_disc.setHandleWidth(20)
        self.splitter_calc_and_disc.setOrientation(Qt.Horizontal)
        self.calc_name = calc_name
        if n_box == 1:
            self.calc_display = CalcDisplay(self.splitter_calc_and_disc, self.calc_name)
            self.calc_setup = CalcSetup(self.splitter_calc_and_disc, self.calc_name, self.calc_display)
        elif n_box == 2:
            self.calc_display = CalcDisplay2(self.splitter_calc_and_disc, self.calc_name)
            self.calc_setup = CalcSetup2(self.splitter_calc_and_disc, self.calc_name, self.calc_display)
        elif n_box == 3:
            self.calc_display = CalcDisplay3(self.splitter_calc_and_disc, self.calc_name)
            self.calc_setup = CalcSetup3(self.splitter_calc_and_disc, self.calc_name, self.calc_display)
        elif n_box == 4:
            self.calc_display = CalcDisplay4(self.splitter_calc_and_disc, self.calc_name)
            self.calc_setup = CalcSetup4(self.splitter_calc_and_disc, self.calc_name, self.calc_display)
        self.vertical_layout_calc_and_disc.addWidget(self.splitter_calc_and_disc)
        self.scroll_area.setWidget(self.scroll_area_calc_and_disc)
        self.vertical_layout.addWidget(self.scroll_area)

    def close_part(self):
        self.calc_setup.delete_data()
