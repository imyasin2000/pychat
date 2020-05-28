from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("123.ui", self)
        
        
        self.groupBox = self.findChild(QGroupBox, "groupBox")
        self.formLayout = self.findChild(QFormLayout, "formLayout_2")
        
        self.labelLis = []
        self.comboList = []
        # self.groupBox.setLayout(self.formLayout)
        scroll = QScrollArea()
        scroll.setWidget(self.groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()

    def add(self):
        self.labelLis.append(QLabel("Label"))
        self.comboList.append(QPushButton("Click Me"))
        self.formLayout.addRow(self.labelLis[-1], self.comboList[-1])
    
    def dele(self,size):
        for i in  range(size):
            self.formLayout.removeRow(self.labelLis[-1])
            del self.labelLis[-1]
            del self.comboList[-1]



App = QApplication(sys.argv)


window2 = Window()
window2.add()
window2.add()
window2.add()
window2.add()
window2.dele(2)


sys.exit(App.exec())