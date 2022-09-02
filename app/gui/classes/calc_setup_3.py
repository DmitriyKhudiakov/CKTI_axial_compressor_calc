from threading import Thread
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QScrollArea, QWidget
####################################
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import app.calc.axial_compressor.setup.get_setup as gs
import app.calc.axial_compressor.setup.get_var_setup as gvs
import app.calc.axial_compressor.calc_3 as clc
import app.calc.axial_compressor.calc_run as clc_run
import app.calc.axial_compressor.elem_dict_3 as eld
import app.calc.axial_compressor.init_calc as clc_init


class CalcSetup3:
    def __init__(self, parent_splitter, calc_name, calc_display):
        self.is_empty = True
        self.f = None
        self.calc_part4 = None
        self.line_edit_calc_list = []
        self.group_box_calc = QGroupBox(parent_splitter)
        self.group_box_calc.setTitle("Параметры")
        self.vertical_layout_calc = QVBoxLayout(self.group_box_calc)
        self.scroll_area_calc = QScrollArea(self.group_box_calc)
        self.scroll_area_calc.setWidgetResizable(True)
        self.scroll_area_calc_inside = QWidget()
        self.vertical_layout_calc_inside = QVBoxLayout(self.scroll_area_calc_inside)
        ######################################
        self.calc_display = calc_display
        self.calc_name = calc_name
        self.get_setup = gs
        self.get_var_setup = gvs
        self.calc = clc
        self.parent_splitter = parent_splitter
        # for data enter
        self.enter_box = QGroupBox(self.parent_splitter)
        self.save_box = QGroupBox(self.parent_splitter)
        self.save_layout = QHBoxLayout()
        self.empty_qw_save = QWidget()
        self.save_btn = QPushButton("Сохранить", self.empty_qw_save)
        self.save_btn.setStyleSheet('''
        background: qradialgradient(cx:0.5, cy:0.5, radius: 0.9, fx:0.5, fy:0.5, stop:0 #FFFFFF, stop:1 #CACACA)
        ''')
        # self.var_enter_box = QGroupBox(self.parent_splitter)
        self.enter_box_v_box = QVBoxLayout()
        self.enter_box_h_box_list = []
        self.calc_run = clc_run
        self.desc_element_dict = eld
        self.init_calc = clc_init
        self.f = self.init_calc.init_calc(self.calc_name)
        self.lbl1 = QLabel("Данные для расчета берутся из предыдущего пункта", self.enter_box)
        self.enter_data_is_ready = False
        self.init_data_enter()
        # self.init_data_var_enter()
        # for run btn
        self.run_h_box = QHBoxLayout()
        self.empty_qw = QWidget()
        self.run_btn = QPushButton("Рассчитать", self.empty_qw)
        self.run_btn.setStyleSheet('''
        background: qradialgradient(cx:0.5, cy:0.5, radius: 0.9, fx:0.5, fy:0.5, stop:0 #FFFFFF, stop:1 #CACACA)
        ''')
        self.init_run()
        self.is_init_vars = False
        ######################################
        self.scroll_area_calc.setWidget(self.scroll_area_calc_inside)
        self.vertical_layout_calc.addWidget(self.scroll_area_calc)

    def init_data_enter(self):
        self.enter_box.setTitle("Входные данные")
        self.enter_box.setMaximumHeight(200)
        self.save_box.setTitle("Сохранение")
        self.save_box.setMaximumHeight(70)
        self.enter_box_h_box_list.append(QHBoxLayout())
        self.lbl1.setFont(QFont("Times", 10))
        self.enter_box_h_box_list[-1].addWidget(self.lbl1)
        self.enter_box_v_box.addLayout(self.enter_box_h_box_list[-1])
        self.enter_box.setMinimumHeight(50)
        self.enter_box.setMinimumHeight(70)
        self.save_layout.addStretch(1)
        self.save_btn.setFixedSize(100, 30)
        self.save_btn.clicked.connect(self.tap_save_btn)
        self.save_layout.addWidget(self.save_btn)
        self.save_box.setLayout(self.save_layout)
        self.save_box.setMinimumHeight(70)
        self.enter_box.setLayout(self.enter_box_v_box)
        self.vertical_layout_calc_inside.addWidget(self.enter_box)
        self.vertical_layout_calc_inside.addWidget(self.save_box)
        self.vertical_layout_calc_inside.setAlignment(self.enter_box, Qt.AlignTop)

    def init_enter_data(self, f):
        self.enter_data_is_ready = True

    def init_run(self):
        self.empty_qw.setFixedHeight(50)
        self.run_h_box.addStretch(1)
        self.run_btn.setFixedSize(100, 30)
        self.run_btn.clicked.connect(self.tap_run_btn)
        self.run_h_box.addWidget(self.run_btn)
        self.empty_qw.setLayout(self.run_h_box)
        self.vertical_layout_calc_inside.addWidget(self.empty_qw)

    def tap_run_btn(self):
        if self.enter_data_is_ready is True:
            def threading_func():
                self.calc.calc(self.f, self.is_init_vars, self.calc_name, 1)
                self.calc_part4.calc_setup.init_enter_data(self.f)
                self.calc_part4.calc_setup.f = self.f
                self.is_empty = False
            th = Thread(target=threading_func)
            th.start()
            th.join()
            self.calc_display.show_res(self.f, self.desc_element_dict.get_dict(self.f, self.calc_name))

    def tap_save_btn(self):
        data = self.calc_display.get_html_data_file(self.f, self.desc_element_dict.get_dict(self.f, self.calc_name,),
                                                    self.is_empty)
        name = QFileDialog.getSaveFileName(self.parent_splitter, "Сохранение", "/", ".html")[0]
        if (name[-5:] == ".html") and (len(name) > 5):
            with open(name, "w+", encoding='utf-8') as file_write:
                file_write.write(data)
            file_write.close()
        else:
            name += ".html"
            with open(name, "w+", encoding='utf-8') as file_write:
                file_write.write(data)
            file_write.close()

    def delete_data(self):
        self.f.delete_data()
