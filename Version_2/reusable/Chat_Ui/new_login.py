from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Chat_box.ui", self)    

        # self.labelLis = []
        # self.labelLis_2 = []

        self.show()

    def add_me(self):
        # self.labelLis.append(QLabel("Label1"))
        # self.labelLis_2.append(QLabel("Label2"))
        self.formLayout.addRow(QLabel("You : salam"))
        # self.formLayout.addRow(QLabel("Khobi? : Ali",alignment=Qt.AlignRight))
    
    def add_other(self):
        # self.labelLis.append(QLabel("Label1"))
        # self.labelLis_2.append(QLabel("Label2"))
        # self.formLayout.addRow(QLabel("You : salam"))
        self.formLayout.addRow(QLabel("Khobi? : Ali",alignment=Qt.AlignRight))
    
    def dele(self,size):
        # for i in  range(size):
        #     self.formLayout.removeRow(self.labelLis[-1])
        #     del self.labelLis[-1]
        #     del self.comboList[-1]
        pass


App = QApplication(sys.argv)


window2 = Window()

while (True):
    x=(input("enter 1 : add me, enter 2 : add other \n"))
    if x=='1':
        window2.add_me()
    elif x=='2':
        window2.add_other()
    else:
        break
sys.exit(App.exec())