from threading import Thread
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QScrollArea, QWidget
####################################
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import app.calc.axial_compressor.setup.get_setup as gs
import app.calc.axial_compressor.setup.get_var_setup as gvs
import app.calc.axial_compressor.calc as clc
import app.calc.axial_compressor.calc_run as clc_run
import app.calc.axial_compressor.elem_dict as eld
import app.calc.axial_compressor.init_calc as clc_init


class CalcSetup:
    def __init__(self, parent_splitter, calc_name, calc_display):
        self.is_empty = True
        self.f = None
        self.calc_part2 = None
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
        self.var_enter_box = None
        self.var_setup_combo = None
        self.enter_box_v_box = QVBoxLayout()
        self.enter_box_h_box_list = []
        self.enter_lbl_list = []
        self.enter_lbl_lim_list = []
        self.enter_le_list = []
        self.enter_lbl_msg_list = []
        self.var_enter_box_v_box = QVBoxLayout()
        self.var_enter_box_h_box_1_list = []
        self.var_enter_box_h_box_2_list = []
        self.var_enter_box_h_box_3_list = []
        self.var_enter_lbl_list = []
        self.var_enter_lbl_lim_1_list = []
        self.var_enter_lbl_lim_2_list = []
        self.var_enter_lbl_iter_list = []
        self.var_enter_le_1_list = []
        self.var_enter_le_2_list = []
        self.var_enter_le_3_list = []
        self.var_enter_lbl_msg_1_list = []
        self.var_enter_lbl_msg_2_list = []
        self.var_enter_lbl_msg_3_list = []
        self.get_setup_list = []
        self.get_var_setup_list = []
        self.calc_run = clc_run
        self.desc_element_dict = eld
        self.init_calc = clc_init
        self.f = self.init_calc.init_calc(self.calc_name)
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
        self.set_start_values()
        self.is_init_vars = False
        ######################################
        self.scroll_area_calc.setWidget(self.scroll_area_calc_inside)
        self.vertical_layout_calc.addWidget(self.scroll_area_calc)

    def init_data_enter(self):
        self.enter_box.setTitle("Входные данные")
        self.enter_box.setMaximumHeight(200)
        self.save_box.setTitle("Сохранение")
        self.save_box.setMaximumHeight(70)
        self.get_setup_list = self.get_setup.get_setup(self.calc_name, self.f)
        for curr_var in self.get_setup_list:
            self.enter_box_h_box_list.append(QHBoxLayout())
            self.enter_lbl_list.append(QLabel("", self.enter_box))
            self.enter_lbl_list[-1].setFixedWidth(250)
            h_pix_map = QPixmap(curr_var[0])
            self.enter_lbl_list[-1].setPixmap(h_pix_map)
            self.enter_box_h_box_list[-1].addWidget(self.enter_lbl_list[-1])
            self.enter_lbl_lim_list.append(QLabel(curr_var[1], self.enter_box))
            self.enter_lbl_lim_list[-1].setFixedWidth(200)
            self.enter_box_h_box_list[-1].addWidget(self.enter_lbl_lim_list[-1])
            self.enter_le_list.append(QLineEdit(self.enter_box))
            self.enter_le_list[-1].setFixedWidth(200)
            self.enter_le_list[-1].setStyleSheet('''
        background: qradialgradient(cx:0.5, cy:0.5, radius: 0.9, fx:0.5, fy:0.5, stop:0 #FFFFFF, stop:1 #CACACA)
        ''')
            self.enter_box_h_box_list[-1].addWidget(self.enter_le_list[-1])
            self.enter_lbl_msg_list.append(QLabel(curr_var[2], self.enter_box))
            self.enter_box_h_box_list[-1].addWidget(self.enter_lbl_msg_list[-1])
            self.enter_box_v_box.addLayout(self.enter_box_h_box_list[-1])
        self.enter_box.setMinimumHeight(270)
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

    def init_data_var_enter(self):
        self.var_enter_box.setTitle("var_enter_data")
        self.var_enter_box.setMaximumHeight(200)
        self.get_var_setup_list = self.get_var_setup.get_var_setup(self.calc_name, self.f)
        if len(self.get_var_setup_list) > 0:
            curr_var = self.get_var_setup_list[0]
            self.var_enter_box_h_box_1_list.append(QHBoxLayout())
            self.var_enter_box_h_box_2_list.append(QHBoxLayout())
            self.var_enter_box_h_box_3_list.append(QHBoxLayout())

            self.var_enter_lbl_list.append(QLabel("", self.var_enter_box))
            self.var_enter_lbl_list[-1].setFixedWidth(150)
            h_pix_map = QPixmap(curr_var[0])
            self.var_enter_lbl_list[-1].setPixmap(h_pix_map)
            self.var_enter_box_h_box_2_list[-1].addWidget(self.var_enter_lbl_list[-1])

            self.var_setup_combo = QComboBox()
            self.var_setup_combo.setFixedWidth(150)
            for i in range(len(self.get_var_setup_list)):
                self.var_setup_combo.addItem(self.get_var_setup_list[i][11])
            self.var_setup_combo.activated[str].connect(self.var_setup_on_activated)
            self.var_enter_box_h_box_1_list[-1].addWidget(self.var_setup_combo)

            help_lbl = QLabel("", self.var_enter_box)
            help_lbl.setFixedWidth(150)
            self.var_enter_box_h_box_3_list[-1].addWidget(help_lbl)

            self.var_enter_lbl_lim_1_list.append(QLabel(curr_var[1], self.var_enter_box))
            self.var_enter_lbl_lim_1_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_1_list[-1].addWidget(self.var_enter_lbl_lim_1_list[-1])
            self.var_enter_le_1_list.append(QLineEdit(self.var_enter_box))
            self.var_enter_le_1_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_1_list[-1].addWidget(self.var_enter_le_1_list[-1])
            self.var_enter_lbl_msg_1_list.append(QLabel(curr_var[2], self.var_enter_box))
            self.var_enter_box_h_box_1_list[-1].addWidget(self.var_enter_lbl_msg_1_list[-1])

            self.var_enter_lbl_lim_2_list.append(QLabel(curr_var[3], self.var_enter_box))
            self.var_enter_lbl_lim_2_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_2_list[-1].addWidget(self.var_enter_lbl_lim_2_list[-1])
            self.var_enter_le_2_list.append(QLineEdit(self.var_enter_box))
            self.var_enter_le_2_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_2_list[-1].addWidget(self.var_enter_le_2_list[-1])
            self.var_enter_lbl_msg_2_list.append(QLabel(curr_var[4], self.var_enter_box))
            self.var_enter_box_h_box_2_list[-1].addWidget(self.var_enter_lbl_msg_2_list[-1])

            self.var_enter_lbl_iter_list.append(QLabel(curr_var[5], self.var_enter_box))
            self.var_enter_lbl_iter_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_3_list[-1].addWidget(self.var_enter_lbl_iter_list[-1])
            self.var_enter_le_3_list.append(QLineEdit(self.var_enter_box))
            self.var_enter_le_3_list[-1].setFixedWidth(250)
            self.var_enter_box_h_box_3_list[-1].addWidget(self.var_enter_le_3_list[-1])
            self.var_enter_lbl_msg_3_list.append(QLabel(curr_var[6], self.var_enter_box))
            self.var_enter_box_h_box_3_list[-1].addWidget(self.var_enter_lbl_msg_3_list[-1])

            self.var_enter_box_v_box.addLayout(self.var_enter_box_h_box_1_list[-1])
            self.var_enter_box_v_box.addLayout(self.var_enter_box_h_box_2_list[-1])
            self.var_enter_box_v_box.addLayout(self.var_enter_box_h_box_3_list[-1])
        self.var_enter_box.setLayout(self.var_enter_box_v_box)
        self.vertical_layout_calc_inside.addWidget(self.var_enter_box)
        self.vertical_layout_calc_inside.setAlignment(self.var_enter_box, Qt.AlignTop)
        self.vertical_layout_calc_inside.addStretch(1)

    def set_setup_var_combo(self, text):
        name_list = [self.get_var_setup_list[i][11] for i in range(len(self.get_var_setup_list))]
        curr_n = name_list.index(text)
        curr_var = self.get_var_setup_list[curr_n]
        self.var_enter_lbl_list[-1].setFixedWidth(150)
        h_pix_map = QPixmap(curr_var[0])
        self.var_enter_lbl_list[-1].setPixmap(h_pix_map)

        self.var_enter_lbl_lim_1_list[-1].setText(curr_var[1])
        self.var_enter_lbl_msg_1_list[-1].setText(curr_var[2])

        self.var_enter_lbl_lim_2_list[-1].setText(curr_var[3])
        self.var_enter_lbl_msg_2_list[-1].setText(curr_var[4])

        self.var_enter_lbl_iter_list[-1].setText(curr_var[5])
        self.var_enter_lbl_msg_3_list[-1].setText(curr_var[6])

    def var_setup_on_activated(self, text):
        self.set_setup_var_combo(text)

    def set_start_values(self):
        if self.calc_name == "axial_compressor":
            pass

    def init_run(self):
        self.empty_qw.setFixedHeight(50)
        self.run_h_box.addStretch(1)
        self.run_btn.setFixedSize(100, 30)
        self.run_btn.clicked.connect(self.tap_run_btn)
        self.run_h_box.addWidget(self.run_btn)
        self.empty_qw.setLayout(self.run_h_box)
        self.vertical_layout_calc_inside.addWidget(self.empty_qw)

    def tap_run_btn(self):
        enter_list = [le.text() for le in self.enter_le_list]
        var_enter_list = []
        for le1, le2, le3 in zip(self.var_enter_le_1_list, self.var_enter_le_2_list, self.var_enter_le_3_list):
            var_enter_list.append([le1.text(), le2.text(), le3.text()])
        is_ok, ret_list, var_ret_list, f = self.calc_run.run(self.calc_name, self.get_setup_list, enter_list,
                                                             self.get_var_setup_list, var_enter_list, self.f)
        self.f = f
        for lb_msg, le, rl in zip(self.enter_lbl_msg_list, self.enter_le_list, ret_list):
            lb_msg.setText(rl)
        for lb_msg_1, lb_msg_2, lb_msg_3, rl in zip(self.var_enter_lbl_msg_1_list, self.var_enter_lbl_msg_2_list,
                                                    self.var_enter_lbl_msg_3_list, var_ret_list):
            lb_msg_1.setText(rl[0])
            lb_msg_2.setText(rl[1])
            lb_msg_3.setText(rl[2])
        if is_ok is True:
            def thread_calc_func():
                self.is_init_vars = self.calc.calc(f, self.is_init_vars, self.calc_name)
                self.calc_part2.calc_setup.init_combo(f)
                self.calc_part2.calc_setup.f = f
                self.is_empty = False
            thread_calc_func()
            th = Thread(target=thread_calc_func())
            th.start()
            th.join()
            self.calc_display.show_res(f, self.desc_element_dict.get_dict(f, self.calc_name))

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
