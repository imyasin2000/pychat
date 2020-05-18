from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
import time
import send_email


class UI_l(QMainWindow):
    def __init__(self):
        super(UI_l, self).__init__()
        uic.loadUi("Login_F.ui", self)
        self.textedit1 = self.findChild(QTextEdit, "username_t")
        self.textedit_2 = self.findChild(QTextEdit, "password_t")
        self.button_1 = self.findChild(QPushButton, "forget_b")
        self.button_2 = self.findChild(QPushButton, "login_b")
        self.button_3 = self.findChild(QPushButton, "rigister_b")
        self.button_1.clicked.connect(self.clickedBtn_1)
        self.button_2.clicked.connect(self.clickedBtn_2)
        self.button_3.clicked.connect(self.clickedBtn_3)
        self.show()



    def clickedBtn_1(self):#forget
        self.myOtherWindow = UI_f()
        self.myOtherWindow.show()
        self.hide()

    def clickedBtn_2(self):#login
        pass

    def clickedBtn_3(self):#rigester
        self.myOtherWindow = UI_r()
        self.myOtherWindow.show()
        self.hide()

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


class UI_f(QMainWindow):
    def __init__(self):
        super(UI_f, self).__init__()
        uic.loadUi("Forget_F.ui", self)
        self.textedit1 = self.findChild(QTextEdit, "textEdit")
        self.label1 = self.findChild(QTextEdit, "label")
        self.button_1 = self.findChild(QPushButton, "pushButton")
        self.button_1.clicked.connect(self.clickedBtn_1)


        self.show()


    def clickedBtn_1(self):#forget
        # self.frame1.setVisible(True)
        # for i in range (2):
        #     time.sleep(.2)
        #     self.resize((self.frameGeometry().width()),self.frameGeometry().height())
        sender=self.textedit1.toPlainText()
        self.textedit1.setPlainText("wait . . .")
        if (send_email.send_email_c(sender)==1):
            self.textedit1.setVisible(False)




    def clickedBtn_2(self):#login
        pass


try:
    f = open("lsc_u.txt")
    app = QApplication(sys.argv)
    window = UI_l()
    app.exec_()
except IOError:
    print("File not accessible")
finally:
    f.close()

