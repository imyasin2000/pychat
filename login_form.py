from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys



class UI_l(QMainWindow):
    def __init__(self):
        super(UI_l, self).__init__()
        uic.loadUi("Login_F.ui", self)
        self.textedit1 = self.findChild(QTextEdit, "username_t")
        self.textedit_2 = self.findChild(QTextEdit, "password_t")
        self.button_1 = self.findChild(QPushButton, "forget_b")
        self.button_2 = self.findChild(QPushButton, "login_b")
        self.button_1.clicked.connect(self.clickedBtn_1)
        self.button_2.clicked.connect(self.clickedBtn_2)
        self.show()


    def clickedBtn_1(self):#forget
        self.myOtherWindow = UI_r()
        self.myOtherWindow.show()
        self.hide()


    def clickedBtn_2(self):#login
        pass



class UI_r(QMainWindow):
    def __init__(self):
        super(UI_r, self).__init__()
        uic.loadUi("Rigister_F.ui", self)
        # self.textedit1 = self.findChild(QTextEdit, "pushButton")
        # self.textedit_2 = self.findChild(QTextEdit, "password_t")
        # self.button_1 = self.findChild(QPushButton, "forget_b")
        # self.button_2 = self.findChild(QPushButton, "login_b")
        # self.button_1.clicked.connect(self.clickedBtn_1)
        # self.button_2.clicked.connect(self.clickedBtn_2)

        self.show()


    def clickedBtn_1(self):#forget
        pass

    def clickedBtn_2(self):#login
        pass







app = QApplication(sys.argv)
window = UI_l()
app.exec_()