import face_recognition
import cv2
import numpy as np

####qt
import threading
        
from PyQt5.QtCore import QTimer
from threading import Thread
from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt 
import sys 
from PyQt5.QtGui import QColor
from PyQt5.Qt import QApplication
import os
import time
from threading import Timer
##qt

close_cam =True
counter=0

def face_id_unlock():
    global counter
    global close_cam
    video_capture = cv2.VideoCapture(0)
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("face.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    known_face_encodings = [obama_face_encoding,]
    known_face_names = ["Mohammad Hossein",]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame

        print('\033c')
        print (counter)
        if face_names==known_face_names:
            counter += 1
        else:
            counter = 0
        if counter == 30:
            break
        
       
        
    # Release handle to the webcam
    
    video_capture.release()
    cv2.destroyAllWindows()
    close_cam =False
    



#########################qt###########################

def show_next():
    global window3
    global close_cam
    
    if close_cam == False:
        window3.timer.stop()
        window3.lookingfor_l.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        

        movie = QtGui.QMovie(os.getcwd() + '/after_unlock.gif')
        window3.lookingfor_l.setMovie(movie)
        movie.start()
        window3.welcome_l.setText("Hello "+"mohammad hossein"+" !")
        window3.welcome_l_2.setHidden(True)
        window3.textEdit.setHidden(True)
        window3.welcome_l.setHidden(False)
        window3.timer = QtCore.QTimer()
        window3.timer.timeout.connect(lambda :window3.close())
        window3.timer.start(3000)
        
        
        
  
    
        
    

class face_ui(QMainWindow):
    global close_cam
    def __init__(self):
        
        super(face_ui, self).__init__()
        uic.loadUi("unlock.ui", self)
       
        self.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(247, 247, 247).name())
        
        self.welcome_l.setHidden(True)
        self.offset = None
        radius = 25.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)


        # self.lookingfor_l.setHidden(False)
        self.lookingfor_l.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        movie = QtGui.QMovie(os.getcwd() + '/befor_unlock.gif')
        self.lookingfor_l.setMovie(movie)
        movie.start()

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.move(qr.topLeft())
        self.welcome_l.setStyleSheet('background-color:transparent;color:rgba(9, 120, 239)')
        self.welcome_l_2.setStyleSheet('background-color:transparent;color:rgba(9, 120, 239)')
        threading.Thread(target=face_id_unlock, args=()).start()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(show_next)
        self.timer.start(30)
        self.textEdit.textChanged.connect(self.textChanged_messege_event)
        

        self.show()
    
    def textChanged_messege_event(self):
        global close_cam
        if str(self.textEdit.toPlainText())=='1234' :
            self.welcome_l_2.setHidden(True)
            self.textEdit.setHidden(True)
            close_cam=False
        
       
      
    
    
       


app = QApplication(sys.argv)
window3 = face_ui()
app.exit(app.exec_())
