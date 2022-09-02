from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QSize
import app.calc.axial_compressor.description.get_description as gd

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import pathlib


MIN_WIDTH = 400
MIN_HEIGHT = 200


class CalcDescription:
    def __init__(self, parent_splitter, calc_name):
        global MIN_WIDTH, MIN_HEIGHT
        self.text_list_disc = []
        self.group_box = QGroupBox(parent_splitter)
        self.group_box.setTitle("Описание")
        self.group_box.setMinimumSize(QSize(MIN_WIDTH, MIN_HEIGHT))
        self.vertical_layout = QVBoxLayout(self.group_box)

        self.web1 = QWebEngineView()
        pdfjs = "file:///" + str(pathlib.Path().absolute()).replace("\\", "/") + "/web/viewer.html"
        pdf = "file:///" + str(pathlib.Path().absolute()).replace("\\", "/") + "/source/study_files/file1.pdf"
        self.web1.setFixedHeight(700)
        self.web1.load(QUrl.fromUserInput('%s?file=%s' % (pdfjs, pdf)))
        self.web1.show()
        
        self.web2 = QWebEngineView()
        pdfjs = "file:///" + str(pathlib.Path().absolute()).replace("\\", "/") + "/web/viewer.html"
        pdf = "file:///" + str(pathlib.Path().absolute()).replace("\\", "/") + "/source/study_files/file2.pdf"
        self.web2.setFixedHeight(700)
        self.web2.load(QUrl.fromUserInput('%s?file=%s' % (pdfjs, pdf)))
        self.web2.show()

        self.get_desc = gd
        self.calc_name = calc_name
        self.add_text()

        self.vertical_layout.addWidget(self.web2)
        self.vertical_layout.addWidget(self.web1)
        self.group_box.setFixedHeight(1700)

    def add_text(self):
        self.text_list_disc.append(QTextEdit())
        self.text_list_disc[-1].setMinimumSize(QSize(400, 180))
        self.text_list_disc[-1].setMaximumSize(QSize(4000, 180))
        self.text_list_disc[-1].setReadOnly(True)
        self.text_list_disc[-1].setStyleSheet("background-color: #F0F0F0")
        self.text_list_disc[-1].setHtml(self.get_desc.get_description(self.calc_name))
        self.text_list_disc[-1].toHtml()
        self.vertical_layout.addWidget(self.text_list_disc[-1])
